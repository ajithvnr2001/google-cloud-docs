---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/upgrade/
title: Upgrading Apigee hybrid to version 1.13 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:01:53.819589+00:00
---

# Upgrading Apigee hybrid to version 1.13  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Upgrading Apigee hybrid to version 1.13 Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.13 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.13 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/upgrade.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/upgrade.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/upgrade.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/upgrade.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/upgrade.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/upgrade.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/upgrade.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/upgrade.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/upgrade.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/upgrade.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/upgrade.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/upgrade.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/upgrade.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/upgrade.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/upgrade.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/upgrade.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/upgrade.html)



This procedure covers upgrading from Apigee hybrid version 1.12.x to Apigee hybrid version 1.13.4 and from previous releases of hybrid 1.13.x to version 1.13.4. 

Use the same procedures for minor version upgrades (for example version 1.12 to 1.13) and for patch release upgrades (for example 1.13.0 to 1.13.4). 

If you are upgrading from Apigee hybrid version 1.11 or older, you must first upgrade to hybrid version 1.12 before upgrading to version 1.13.4. See the instructions for [Upgrading Apigee hybrid to version 1.12](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/upgrade). 

## Changes from Apigee hybrid v1.12

Please note the following changes: 

  * **`apigee-operator` in the Apigee namespace**: Starting in version 1.13, `apigee-operator` runs in the same Kubernetes namespace as the other Apigee hybrid components, `apigee` by default. You can supply any name for the namespace. In previous versions, the `apigee-operator` was required to run in its own namespace, `apigee-system`.
  * **Anthos (on bare metal or VMware) is now Google Distributed Cloud (for bare metal or VMware)** : For more information see the product overviews for [Google Distributed Cloud for bare metal](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal) and [Google Distributed Cloud for VMware](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview). 
  * **Stricter class instantiation checks** : Starting in version 1.13.3, Apigee hybrid, the [JavaCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy) now includes additional security during Java class instantiation. The enhanced security measure prevents the deployment of policies that directly or indirectly attempt actions that require permissions that are not allowed. 

In the most cases, existing policies will continue to function as expected without any issues. However, there is a possibility that policies relying on third-party libraries, or those with custom code that indirectly triggers operations requiring elevated permissions, could be affected. 

**Important:** To test your installation, follow the procedure in Validate policies after upgrade to 1.13.3 or later to validate policy behavior. 



## Prerequisites

Before upgrading to hybrid version 1.13, make sure your installation meets the following requirements: 

  * If your hybrid installation is running a version older than v1.12, you must upgrade to version 1.12 before upgrading to v1.13. See [Upgrading Apigee hybrid to version 1.12](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/upgrade). 
  * Helm version v3.14.2+.
  * `kubectl`: A supported version of `kubectl` appropriate for your Kubernetes platform version. see [Supported platforms and versions: `kubectl`](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#kubectl).
  * cert-manager: A supported version of cert-manager. See [Supported platforms and versions: cert-manager](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#cert-manager). If needed, you will upgrade cert-manager in the Prepare to upgrade to version 1.13 section below.



##  Upgrading to version 1.13.4 overview 

Upgrading to Apigee hybrid version 1.13 may require downtime. 

When upgrading the Apigee controller to version 1.13.4, all Apigee deployments undergo a rolling restart. To minimize downtime in production hybrid environments during a rolling restart, make sure you are running at least two clusters (in the same or different region/data center). Divert all production traffic to a single cluster and take the cluster you are about to upgrade offline, and then proceed with the upgrade process. Repeat the process for each cluster.

Apigee recommends upgrading all clusters as soon as possible to reduce the chances of production impact. There is no time limit on when all remaining clusters must be upgraded after the first one is upgraded. However, until all remaining clusters are upgraded Cassandra backup and restore cannot work with mixed versions. For example, a backup from Hybrid 1.12 cannot be used to restore a Hybrid 1.13 instance.

**Note:** Management plane changes do not need to be suspended during an upgrade. Any required suspension to management plane changes are included in the upgrade instructions.

The procedures for upgrading Apigee hybrid are organized in the following sections: 

  1. Prepare to upgrade. 
  2. Install hybrid runtime version 1.13.4.



##  Prepare to upgrade to version 1.13 

###  Back up your hybrid installation 

  1. These instructions use the environment variable APIGEE_HELM_CHARTS_HOME for the directory in your file system where you have installed the Helm charts. If needed, change directory into this directory and define the variable with the following command: 

###  Linux 
         
         export APIGEE_HELM_CHARTS_HOME=$PWD
         echo **$APIGEE_HELM_CHARTS_HOME**

###  Mac OS 
         
         export APIGEE_HELM_CHARTS_HOME=$PWD
         echo **$APIGEE_HELM_CHARTS_HOME**

###  Windows 
         
         set APIGEE_HELM_CHARTS_HOME=%CD%
         echo %APIGEE_HELM_CHARTS_HOME%

  2. Make a backup copy of your version 1.12 `$APIGEE_HELM_CHARTS_HOME/` directory. You can use any backup process. For example, you can create a `tar` file of your entire directory with: 
         
         tar -czvf **$APIGEE_HELM_CHARTS_HOME** /../apigee-helm-charts-v1.12-backup.tar.gz **$APIGEE_HELM_CHARTS_HOME**

  3. Back up your Cassandra database following the instructions in [Cassandra backup and recovery](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-backup-overview).
  4. If you are using service cert files (`.json`) in your overrides to authenticate service accounts, make sure your service account cert files reside in the correct Helm chart directory. Helm charts cannot read files outside of each chart directory. 

This step is not required if you are using Kubernetes secrets or Workload Identity to authenticate service accounts.

The following table shows the destination for each service account file, depending on your type of installation:

### Prod

Service account | Default filename | Helm chart directory  
---|---|---  
`apigee-cassandra` | `PROJECT_ID-apigee-cassandra.json` | `$APIGEE_HELM_CHARTS_HOME/apigee-datastore/`  
`apigee-logger` | `PROJECT_ID-apigee-logger.json` | `$APIGEE_HELM_CHARTS_HOME/apigee-telemetry/`  
`apigee-mart` | `PROJECT_ID-apigee-mart.json` | `$APIGEE_HELM_CHARTS_HOME/apigee-org/`  
`apigee-metrics` | `PROJECT_ID-apigee-metrics.json` | `$APIGEE_HELM_CHARTS_HOME/apigee-telemetry/`  
`apigee-runtime` | `PROJECT_ID-apigee-runtime.json` | `$APIGEE_HELM_CHARTS_HOME/apigee-env`  
`apigee-synchronizer` | `PROJECT_ID-apigee-synchronizer.json` | `$APIGEE_HELM_CHARTS_HOME/apigee-env/`  
`apigee-udca` | `PROJECT_ID-apigee-udca.json` | `$APIGEE_HELM_CHARTS_HOME/apigee-org/`  
`apigee-watcher` | `PROJECT_ID-apigee-watcher.json` | `$APIGEE_HELM_CHARTS_HOME/apigee-org/`  
  
### Non-prod

Make a copy of the `apigee-non-prod` service account file in each of the following directories:

Service account | Default filename | Helm chart directories  
---|---|---  
`apigee-non-prod` | `PROJECT_ID-apigee-non-prod.json` | `$APIGEE_HELM_CHARTS_HOME/apigee-datastore/`  
`$APIGEE_HELM_CHARTS_HOME/apigee-telemetry/`  
`$APIGEE_HELM_CHARTS_HOME/apigee-org/`  
`$APIGEE_HELM_CHARTS_HOME/apigee-env/`  
  5. Make sure that your TLS certificate and key files (`.crt`, `.key`, and/or `.pem`) reside in the `$APIGEE_HELM_CHARTS_HOME/apigee-virtualhost/` directory. 



###  Upgrade your Kubernetes version 

Check your Kubernetes platform version and if needed, upgrade your Kubernetes platform to a version that is supported by both hybrid 1.12 and hybrid 1.13. Follow your platform's documentation if you need help. 

### _Click to expand a list of supported platforms_

| 1.10 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(2) | 1.11 | 1.12 | 1.13  
---|---|---|---|---  
GKE on Google Cloud | 1.24.x   
1.25.x   
1.26.x   
1.27.x(≥ 1.10.5)   
1.28.x(≥ 1.10.5) | 1.25.x   
1.26.x   
1.27.x   
1.28.x(≥ 1.11.2)   
1.29.x(≥ 1.11.2) | 1.26.x   
1.27.x   
1.28.x   
1.29.x(≥ 1.12.1) | 1.27.x   
1.28.x   
1.29.x   
1.30.x   
GKE on AWS | 1.13.x (K8s v1.24.x)   
1.14.x (K8s v1.25.x)   
1.26.x(4)   
1.27.x(≥ 1.10.5)   
1.28.x(≥ 1.10.5) | 1.14.x (K8s v1.25.x)   
1.26.x(4)   
1.27.x   
1.28.x(≥ 1.11.2)   
1.29.x(≥ 1.11.2) |  1.26.x(4)   
1.27.x   
1.28.x   
1.29.x(≥ 1.12.1) |  1.27.x   
1.28.x   
1.29.x(≥ 1.12.1)   
1.30.x   
GKE on Azure | 1.13.x   
1.14.x   
1.26.x(4)   
1.27.x(≥ 1.10.5)   
1.28.x(≥ 1.10.5) | 1.14.x   
1.26.x(4)   
1.27.x   
1.28.x(≥ 1.11.2)   
1.29.x(≥ 1.11.2) | 1.26.x(4)   
1.27.x   
1.28.x   
1.29.x(≥ 1.12.1) | 1.27.x   
1.28.x   
1.29.x(≥ 1.12.1)   
1.30.x   
Google Distributed Cloud (software only) on VMware (5) | 1.13.x (1)   
1.14.x   
1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.27.x(≥ 1.10.5)   
1.28.x(≥ 1.10.5) | 1.14.x   
1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.28.x(≥ 1.11.2)   
1.29.x(≥ 1.11.2) | 1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.28.x(4)   
1.29.x(≥ 1.12.1) | 1.16.x (K8s v1.27.x)   
1.28.x(4)   
1.29.x   
1.30.x   
Google Distributed Cloud (software only) on bare metal | 1.13.x (1)   
1.14.x (K8s v1.25.x)   
1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.27.x(4)(≥ 1.10.5)   
1.28.x(≥ 1.10.5) | 1.14.x   
1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.28.x(4)(≥ 1.11.2)   
1.29.x(≥ 1.11.2) | 1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.28.x(4)   
1.29.x(≥ 1.12.1) | 1.16.x (K8s v1.27.x)   
1.28.x(4)   
1.29.x   
1.30.x   
EKS | 1.24.x   
1.25.x   
1.26.x   
1.27.x(≥ 1.10.5)   
1.28.x(≥ 1.10.5) | 1.25.x   
1.26.x   
1.27.x   
1.28.x(≥ 1.11.2)   
1.29.x(≥ 1.11.2) | 1.26.x   
1.27.x   
1.28.x   
1.29.x(≥ 1.12.1) | 1.26.x   
1.27.x   
1.28.x   
1.29.x   
AKS | 1.24.x   
1.25.x   
1.26.x   
1.27.x(≥ 1.10.5)   
1.28.x(≥ 1.10.5) | 1.25.x   
1.26.x   
1.27.x   
1.28.x(≥ 1.11.2)   
1.29.x(≥ 1.11.2) | 1.26.x   
1.27.x   
1.28.x   
1.29.x(≥ 1.12.1) | 1.26.x   
1.27.x   
1.28.x   
1.29.x   
OpenShift | 4.11   
4.12   
4.14(≥ 1.10.5)   
4.15(≥ 1.10.5) | 4.12   
4.13   
4.14   
4.15(≥ 1.11.2)   
4.16(≥ 1.11.2) | 4.12   
4.13   
4.14   
4.15   
4.16(≥ 1.12.1) | 4.12   
4.13   
4.14   
4.15   
4.16   
Rancher Kubernetes Engine (RKE) |  v1.26.2+rke2r1   
1.27.x(≥ 1.10.5)   
1.28.x(≥ 1.10.5) |  v1.26.2+rke2r1   
v1.27.x   
1.28.x(≥ 1.11.2)   
1.29.x(≥ 1.11.2) | v1.26.2+rke2r1  
v1.27.x  
  
1.28.x   
1.29.x(≥ 1.12.1) | v1.26.2+rke2r1  
v1.27.x  
  
1.28.x   
1.29.x   
1.30.x   
VMware Tanzu |  N/A |  N/A | v1.26.x  | v1.26.x   
  
### Components

| 1.10 | 1.11 | 1.12 | 1.13  
Cloud Service Mesh |  1.17.x(3) |  1.17.x(v1.11.0 - v1.11.1)(3)   
1.18.x(≥ 1.11.2)(3) |  1.18.x(3) |  1.19.x(3)  
JDK |  JDK 11 |  JDK 11 |  JDK 11 |  JDK 11  
cert-manager |  1.10.x  
1.11.x  
1.12.x  |  1.11.x  
1.12.x  
1.13.x  |  1.11.x  
1.12.x  
1.13.x  |  1.13.x  
1.14.x  
1.15.x   
Cassandra |  3.11 |  3.11 |  4.0 |  4.0  
Kubernetes | 1.24.x  
1.25.x  
1.26.x  
| 1.25.x  
1.26.x  
1.27.x  
| 1.26.x  
1.27.x  
1.28.x  
1.29.x | 1.27.x  
1.28.x  
1.29.x  
1.30.x  
kubectl | 1.24.x  
1.25.x  
1.26.x | 1.25.x  
1.26.x  
1.27.x | 1.26.x  
1.27.x  
1.28.x  
1.29.x | 1.27.x  
1.28.x  
1.29.x  
1.30.x  
Helm | 3.10+ | 3.10+ | 3.14.2+ | 3.14.2+  
Secret Store CSI driver |  | 1.3.4 | 1.4.1 | 1.4.1  
Vault |  | 1.13.x | 1.15.2 | 1.15.2  
**(1) On Anthos on-premises (Google Distributed Cloud) version 1.13, follow these instructions to avoid conflict with `cert-manager`: [Conflicting cert-manager installation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues#conflicting-cert-manager-installation)** **(2) The official EOL dates for Apigee hybrid versions 1.10 and older have been reached. Regular monthly patches are no longer available. These releases are no longer officially supported except for customers with explicit and official exceptions for continued support. Other customers must upgrade**.  **(3) Cloud Service Mesh is automatically installed with Apigee hybrid 1.9 and newer**.  **(4) GKE on AWS version numbers now reflect the Kubernetes versions. See [GKE Enterprise version and upgrade support](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support#gke_multi_cloud) for version details and recommended patches**.  **(5) Vault is not certified on Google Distributed Cloud for VMware. ** **(6) Support available with Apigee hybrid version 1.10.5 and newer**.  **(7) Support available with Apigee hybrid version 1.11.2 and newer**.  **(8) Support available with Apigee hybrid version 1.12.1 and newer**.   
**Note:** Hybrid installations are not currently supported on Autopilot clusters. 

##  Install the hybrid 1.13.4 runtime 

**Caution:** Do not create new environments during the upgrade process.

### Prepare for the Helm charts upgrade

This upgrade procedure assumes you are using the same namespace and service accounts for the upgraded installation. If you are making any configuration changes, be sure to reflect those changes in your overrides file before installing the Helm charts.

  1. Pull the Apigee Helm charts. 

Apigee hybrid charts are hosted in [Google Artifact Registry](https://docs.cloud.google.com/artifact-registry):

`oci://us-docker.pkg.dev/apigee-release/apigee-hybrid-helm-charts`

Using the `pull` command, copy all of the Apigee hybrid Helm charts to your local storage with the following command: 
         
         export **CHART_REPO** =oci://us-docker.pkg.dev/apigee-release/apigee-hybrid-helm-charts
         export **CHART_VERSION** =1.13.4
         helm pull **$CHART_REPO** /apigee-operator --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-datastore --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-env --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-ingress-manager --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-org --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-redis --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-telemetry --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-virtualhost --version **$CHART_VERSION** --untar
         

  2. Upgrade cert-manager if needed. 

If you need to upgrade your cert-manager version, install the new version with the following command:
         
         kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.15.5/cert-manager.yaml
         

See [Supported platforms and versions: cert-manager](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#cert-manager) for a list of supported versions.

**Note:** Some versions of cert-manager have an issue where the webhook TLS server may fail to automatically renew its CA certificate. To avoid this, Apigee recommends using cert-manager version [1.15.5](https://cert-manager.io/docs/releases/release-notes/release-notes-1.15/#v1155) or higher. 
  3. If your Apigee namespace is not `apigee`, edit the `apigee-operator/etc/crds/default/kustomization.yaml` file and replace the `namespace` value with your Apigee namespace. 
         
         apiVersion: kustomize.config.k8s.io/v1beta1
         kind: Kustomization
         
         namespace: APIGEE_NAMESPACE
         

If you are using `apigee` as your namespace you do not need to edit the file. 

  4. Install the updated Apigee CRDs: **Note:** From this step onwards, all commands should be run under the chart repo root directory. **Note:** This is the only supported method for installing Apigee CRDs. Do not use `kubectl apply` without `-k`, do not omit `--server-side`. **Note:** This step requires elevated cluster permissions. 
     1. Use the `kubectl` dry-run feature by running the following command:
            
            kubectl apply -k  apigee-operator/etc/crds/default/ \
              --server-side \
              --force-conflicts \
              --validate=false \
              --dry-run=server
            

     2. After validating with the dry-run command, run the following command:
            
            kubectl apply -k  apigee-operator/etc/crds/default/ \
              --server-side \
              --force-conflicts \
              --validate=false
            

     3. Validate the installation with the `kubectl get crds` command: 
            
            kubectl get crds | grep apigee

Your output should look something like the following:
            
            apigeedatastores.apigee.cloud.google.com                    2024-08-21T14:48:30Z
            apigeedeployments.apigee.cloud.google.com                   2024-08-21T14:48:30Z
            apigeeenvironments.apigee.cloud.google.com                  2024-08-21T14:48:31Z
            apigeeissues.apigee.cloud.google.com                        2024-08-21T14:48:31Z
            apigeeorganizations.apigee.cloud.google.com                 2024-08-21T14:48:32Z
            apigeeredis.apigee.cloud.google.com                         2024-08-21T14:48:33Z
            apigeerouteconfigs.apigee.cloud.google.com                  2024-08-21T14:48:33Z
            apigeeroutes.apigee.cloud.google.com                        2024-08-21T14:48:33Z
            apigeetelemetries.apigee.cloud.google.com                   2024-08-21T14:48:34Z
            cassandradatareplications.apigee.cloud.google.com           2024-08-21T14:48:35Z
            

  5. Migrate `apigee-operator` from the `apigee-system` namespace to APIGEE_NAMESPACE. **Note:** This step is only required for upgrades from 1.12.x. If you are upgrading from an earlier version of 1.13, you can skip this step. 
     1. Annotate the `clusterIssuer` with the new namespace 
            
            kubectl annotate --overwrite clusterIssuer apigee-ca-issuer meta.helm.sh/release-namespace='APIGEE_NAMESPACE'
            

     2. If you are changing the release name for ` apigee-operator`, annotate the `clusterIssuer` with the new release name. 
            
            kubectl annotate --overwrite clusterIssuer apigee-ca-issuer meta.helm.sh/release-name='APIGEE_OPERATOR_RELEASE_NAME'
            

     3. Update the replicas of your existing Apigee Operator deployment in the `apigee-system` namespace to 0 (zero) to avoid the two controllers reconciling. 
            
            kubectl scale deployment apigee-controller-manager -n apigee-system --replicas=0
            

     4. Delete the `apigee-mutating-webhook-configuration` and `apigee-validating-webhook-configuration`. 
            
            kubectl delete mutatingwebhookconfiguration apigee-mutating-webhook-configuration
            kubectl delete validatingwebhookconfiguration apigee-validating-webhook-configuration
            

  6. Check the labels on the cluster nodes. By default, Apigee schedules data pods on nodes with the label `cloud.google.com/gke-nodepool=apigee-data` and runtime pods are scheduled on nodes with the label `cloud.google.com/gke-nodepool=apigee-runtime`. You can customize your node pool labels in the `overrides.yaml` file. 

For more information, see [Configuring dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/configure-dedicated-nodes). 




### Install the Apigee hybrid Helm charts

**Note:** Before executing any of the Helm upgrade/install commands, use the Helm dry-run feature by adding `--dry-run` at the end of the command. See `helm -h` to list supported commands, options, and usage. 

  1. If you have not, navigate into your `APIGEE_HELM_CHARTS_HOME` directory. Run the following commands from that directory.
  2. Upgrade the Apigee Operator/Controller: **Note:** This step requires elevated cluster permissions. Run `helm -h` or `helm upgrade -h` for details.

Dry run:
         
         helm upgrade operator apigee-operator/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run=server
         

Upgrade the chart:
         
         helm upgrade operator apigee-operator/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

Verify Apigee Operator installation:
         
         helm ls -n APIGEE_NAMESPACE
         
         
         NAME       NAMESPACE       REVISION   UPDATED                                STATUS     CHART                   APP VERSION
         operator   apigee   3          2024-08-21 00:42:44.492009 -0800 PST   deployed   apigee-operator-1.13.4   1.13.4
         

Verify it is up and running by checking its availability:
         
         kubectl -n APIGEE_NAMESPACE get deploy apigee-controller-manager
         
         
         NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
         apigee-controller-manager   1/1     1            1           7d20h
         

  3. Upgrade the Apigee datastore: 

Dry run:
         
         helm upgrade datastore apigee-datastore/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run=server
         

Upgrade the chart:
         
         helm upgrade datastore apigee-datastore/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

Verify `apigeedatastore` is up and running by checking its state:
         
         kubectl -n APIGEE_NAMESPACE get apigeedatastore default
         
         
         NAME      STATE       AGE
         default   running    2d

  4. Upgrade Apigee telemetry: 

Dry run:
         
         helm upgrade telemetry apigee-telemetry/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run=server
         

Upgrade the chart:
         
         helm upgrade telemetry apigee-telemetry/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

Verify it is up and running by checking its state:
         
         kubectl -n APIGEE_NAMESPACE get apigeetelemetry apigee-telemetry
         
         
         NAME               STATE     AGE
         apigee-telemetry   running   2d

  5. Upgrade Apigee Redis: 

Dry run:
         
         helm upgrade redis apigee-redis/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run=server
         

Upgrade the chart:
         
         helm upgrade redis apigee-redis/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

Verify it is up and running by checking its state:
         
         kubectl -n APIGEE_NAMESPACE get apigeeredis default
         
         
         NAME      STATE     AGE
         default   running   2d

  6. Upgrade Apigee ingress manager: 

Dry run:
         
         helm upgrade ingress-manager apigee-ingress-manager/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run=server
         

Upgrade the chart:
         
         helm upgrade ingress-manager apigee-ingress-manager/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

Verify it is up and running by checking its availability:
         
         kubectl -n APIGEE_NAMESPACE get deployment apigee-ingressgateway-manager
         
         
         NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
         apigee-ingressgateway-manager   2/2     2            2           2d

  7. Upgrade the Apigee organization: 

Dry run:
         
         helm upgrade ORG_NAME apigee-org/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run=server
         

Upgrade the chart:
         
         helm upgrade ORG_NAME apigee-org/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

Verify it is up and running by checking the state of the respective org:
         
         kubectl -n APIGEE_NAMESPACE get apigeeorg
         
         
         NAME                      STATE     AGE
         apigee-org1-xxxxx          running   2d

**Note** : If the upgrade command fails with the error `Forbidden: state: releasing`, the existing components are still in releasing status. You can wait for the current update to complete and then retry. Check release status with the following command: 
         
         kubectl get org -n APIGEE_NAMESPACE

  8. Upgrade the environment. 

You must install one environment at a time. Specify the environment with `--set env=`ENV_NAME.

Dry run:
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --set env=ENV_NAME \
           -f OVERRIDES_FILE \
           --dry-run=server
         

     * ENV_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-env` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_NAME`. However, if your environment has the same name as your environment group, you must use different release names for the environment and environment group, for example `dev-env-release` and `dev-envgroup-release`. For more information on releases in Helm, see [Three big concepts](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.
     * ENV_NAME is the name of the environment you are upgrading.
     * OVERRIDES_FILE is your new overrides file for v.1.13.4

Upgrade the chart:
    
    helm upgrade ENV_RELEASE_NAME apigee-env/ \
      --install \
      --namespace APIGEE_NAMESPACE \
      --set env=ENV_NAME \
      -f OVERRIDES_FILE
    

Verify it is up and running by checking the state of the respective env:
    
    kubectl -n APIGEE_NAMESPACE get apigeeenv
    
    
    NAME                          STATE       AGE   GATEWAYTYPE
    apigee-org1-dev-xxx            running     2d

**Note** : If the upgrade command fails with the error `Forbidden: state: releasing`, the existing components are still in releasing status. You can wait for the current update to complete and then retry. Check release status with the following command: 
    
    kubectl get env -n APIGEE_NAMESPACE

  9. Upgrade the environment groups (`virtualhosts`). 
     1. You must upgrade one environment group (virtualhost) at a time. Specify the environment group with `--set envgroup=`ENV_GROUP_NAME. Repeat the following commands for each environment group mentioned in the overrides.yaml file: 

Dry run:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --set envgroup=ENV_GROUP_NAME \
              -f OVERRIDES_FILE \
              --dry-run=server
            

ENV_GROUP_RELEASE_NAME is the name with which you previously installed the `apigee-virtualhost` chart. It is usually ENV_GROUP_NAME.

Upgrade the chart:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --set envgroup=ENV_GROUP_NAME \
              -f OVERRIDES_FILE
            

**Note:** ENV_GROUP_RELEASE_NAME must be unique within the `apigee` namespace. 

For example, if you have an _environment_ named `prod` and an _environment group_ named `prod`, set the value of ENV_GROUP_RELEASE_NAME to something unique, like `prod-envgroup`. 

     2. Check the state of the ApigeeRoute (AR). 

Installing the `virtualhosts` creates ApigeeRouteConfig (ARC) which internally creates ApigeeRoute (AR) once the Apigee watcher pulls environment group-related details from the control plane. Therefore, check that the corresponding AR's state is running: 
            
            kubectl -n APIGEE_NAMESPACE get arc
            
            
            NAME                                STATE   AGE
            apigee-org1-dev-egroup                       2d
            
            kubectl -n APIGEE_NAMESPACE get ar
            
            
            NAME                                        STATE     AGE
            apigee-org1-dev-egroup-xxxxxx                running   2d

  10. After you have verified all the installations are upgraded successfully, delete the older `apigee-operator` release from the `apigee-system` namespace. **Note:** This step is only required for upgrades from 1.12.x. If you are upgrading from an earlier version of 1.13, you can skip this step. 
     1. Uninstall the old `operator` release: 
            
            helm delete operator -n apigee-system
            

     2. Delete the `apigee-system` namespace: 
            
            kubectl delete namespace apigee-system
            

  11. Upgrade `operator` again in your Apigee namespace to re-install the deleted cluster-scoped resources: **Note:** This step is only required for upgrades from 1.12.x. If you are upgrading from an earlier version of 1.13, you can skip this step. 
         
         helm upgrade operator apigee-operator/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f overrides.yaml
         




## Validate policies after upgrade to 1.13.3 or later

Use this procedure to validate the behavior of the [JavaCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy) after upgrading from 1.13.2 or earlier to 1.13.3 or later.

  1. **Check whether the Java JAR files request unnecessary permissions**. 

After the policy is deployed, check the runtime logs to see if the following log message is present: `"Failed to load and initialize class ..."`. If you observe this message, it suggests that the deployed JAR requested unnecessary permissions. To resolve this issue, investigate the Java code and update the JAR file.

  2. **Investigate and update the Java code**. 

Review any Java code (including dependencies) to identify the cause of potentially unallowed operations. When found, modify the source code as required.

  3. **Test policies with the security check enabled**. 

In a _non-production environment_ , enable the security check flag and redeploy your policies with an updated JAR. To set the flag: 

     * In the `apigee-env/values.yaml` file, set `conf_security-secure.constructor.only` to `true` under `runtime:cwcAppend:`. For example: 
           
           # Apigee Runtime
           runtime:
             cwcAppend:
               conf_security-secure.constructor.only: true

     * Update the `apigee-env` chart for the environment to apply the change. For example: 
           
           helm upgrade ENV_RELEASE_NAME apigee-env/ \
             --install \
             --namespace APIGEE_NAMESPACE \
             --set env=ENV_NAME \
             -f OVERRIDES_FILE

ENV_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-env` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_NAME`. However, if your environment has the same name as your environment group, you must use different release names for the environment and environment group, for example `dev-env-release` and `dev-envgroup-release`. For more information on releases in Helm, see [Three big concepts](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.

If the log message `"Failed to load and initialize class ..."` is still present, continue modifying and testing the JAR until the log message no longer appears.

  4. **Enable the security check in the production environment**. 

After you have thoroughly tested and verified the JAR file in the non-production environment, enable the security check in your production environment by setting the flag `conf_security-secure.constructor.only` to `true` and updating the `apigee-env` chart for the production environment to apply the change. 


**Congratulations!** You have upgraded to Apigee hybrid version 1.13.4. To test your upgrade, call a proxy against the new installation. For an example, see [Step 10: Deploy an API proxy](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-deploy-proxy) in the Apigee hybrid 1.13 installation guide. 

##  Rolling back to a previous version 

To roll back to the previous version, use the older chart version to roll back the upgrade process in the reverse order. Start with `apigee-virtualhost` and work your way back to `apigee-operator`, and then revert the CRDs. 

Because of the change in the namespace for `apigee-operator`, you need to perform extra steps to delete the Validating and Mutating admission hooks. That way, when you install the `apigee-operator` back in the `apigee-system` namespace, they will be recreated to point to the correct Apigee Operator endpoint.

**Tip:** If you know the last release version, you can use the `helm rollback` command rather than the `helm upgrade` command described below.

  1. Update the replicas of the existing Apigee Operator deployment in Apigee to 0 (zero) to avoid the two controllers reconciling the Custom Resources to avoid conflicts when rolling it back in the `apigee-system` namespace. 
         
         kubectl scale deployment apigee-controller-manager -n APIGEE_NAMESPACE --replicas=0
         
         kubectl delete mutatingwebhookconfiguration \
           apigee-mutating-webhook-configuration-APIGEE_NAMESPACE
         
         kubectl delete validatingwebhookconfiguration \
           apigee-validating-webhook-configuration-APIGEE_NAMESPACE
         

  2. Revert all the charts from `apigee-virtualhost` to `apigee-datastore`. The following commands assume you are using the charts from the previous version (v1.12.x). 

Run the following command for each environment group:
         
         helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
           --install \
           --namespace apigee \
           --atomic \
           --set envgroup=ENV_GROUP_NAME \
           -f 1.12_OVERRIDES_FILE
         

Run the following command for each environment:
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --install \
           --namespace apigee \
           --atomic \
           --set env=ENV_NAME \
           -f 1.12_OVERRIDES_FILE
         

Revert the remaining charts except for `apigee-operator`.
         
         helm upgrade ORG_NAME apigee-org/ \
           --install \
           --namespace apigee \
           --atomic \
           -f 1.12_OVERRIDES_FILE
         
         
         helm upgrade ingress-manager apigee-ingress-manager/ \
           --install \
           --namespace apigee \
           --atomic \
           -f 1.12_OVERRIDES_FILE
         
         
         helm upgrade redis apigee-redis/ \
           --install \
           --namespace apigee \
           --atomic \
           -f 1.12_OVERRIDES_FILE
         
         
         helm upgrade telemetry apigee-telemetry/ \
           --install \
           --namespace apigee \
           --atomic \
           -f 1.12_OVERRIDES_FILE
         
         
         helm upgrade datastore apigee-datastore/ \
           --install \
           --namespace apigee \
           --atomic \
           -f 1.12_OVERRIDES_FILE
         

  3. Create the `apigee-system` namespace. 
         
         kubectl create namespace apigee-system
         

  4. Patch the resource annotation back to the `apigee-system` namespace. 
         
         kubectl annotate --overwrite clusterIssuer apigee-ca-issuer meta.helm.sh/release-namespace='apigee-system'
         

  5. If you have changed the release name as well, update the annotation with the `operator` release name. 
         
         kubectl annotate --overwrite clusterIssuer apigee-ca-issuer meta.helm.sh/release-name='operator'
         

  6. Install `apigee-operator` back into the `apigee-system` namespace. 
         
         helm upgrade operator apigee-operator/ \
           --install \
           --namespace apigee-system \
           --atomic \
           -f 1.12_OVERRIDES_FILE
         

  7. Revert the CRDs by reinstalling the older CRDs. 
         
         kubectl apply -k apigee-operator/etc/crds/default/ \
           --server-side \
           --force-conflicts \
           --validate=false
         

  8. Clean up the `apigee-operator` release from the APIGEE_NAMESPACE namespace to complete the rollback process. 
         
         helm uninstall operator -n APIGEE_NAMESPACE
         

  9. Some cluster-scoped resources, such as `clusterIssuer`, are deleted when `operator` is uninstalled. Reinstall them with the following command: 
         
         helm upgrade operator apigee-operator/ \
           --install \
           --namespace apigee-system \
           --atomic \
           -f 1.12_OVERRIDES_FILE
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
