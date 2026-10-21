---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/upgrade/
title: Upgrading Apigee hybrid to version 1.11 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:52:23.365727+00:00
---

# Upgrading Apigee hybrid to version 1.11  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Upgrading Apigee hybrid to version 1.11 Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.11 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.11 keyboard_arrow_down

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



This procedure covers upgrading from Apigee hybrid version 1.10.x to Apigee hybrid version 1.11.2 and from previous releases of hybrid 1.11.x to version 1.11.2. 

Use the same procedures for minor version upgrades (for example version 1.10 to 1.11) and for patch release upgrades (for example 1.11.0 to 1.11.2). 

If you are upgrading from Apigee hybrid version 1.9 or older, you must first upgrade to hybrid version 1.10 before upgrading to version 1.11.2. See the instructions for [Upgrading Apigee hybrid to version 1.10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/upgrade). 

##  Upgrading to version 1.11.2 overview 

Upgrading to Apigee hybrid version 1.11 may require downtime. 

When upgrading the Apigee controller to version 1.11.2, all Apigee deployments undergo a rolling restart. To minimize downtime in production hybrid environments during a rolling restart, make sure you are running at least two clusters (in the same or different region/data center). Divert all production traffic to a single cluster and take the cluster you are about to upgrade offline, and then proceed with the upgrade process. Repeat the process for each cluster.

Apigee recommends upgrading all clusters as soon as possible to reduce the chances of production impact. There is no time limit on when all remaining clusters must be upgraded after the first one is upgraded. However, until all remaining clusters are upgraded the following operations will be impacted:

  * Cassandra backup and restore cannot work with mixed versions. For example, a backup from Hybrid 1.10 cannot be used to restore a Hybrid 1.11 instance.
  * Cassandra data streaming will not work between mixed Hybrid versions. Therefore, your Cassandra clusters cannot scale horizontally.
  * Region expansion and decommissioning will be impacted, because these operations depend on Cassandra data streaming.

**Note:** Management plane changes do not need to be suspended during an upgrade. Any required suspension to management plane changes are included in the upgrade instructions.

### Stricter class instantiation checks in Hyrid 1.11.2-Hotfix.3

Starting with Apigee hybrid 1.11.2-Hotfix.3, the [JavaCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy) now includes additional security during Java class instantiation. The enhanced security measure prevents the deployment of policies that directly or indirectly attempt actions that require permissions that are not allowed. 

In the most cases, existing policies will continue to function as expected without any issues. However, there is a possibility that policies relying on third-party libraries, or those with custom code that indirectly triggers operations requiring elevated permissions, could be affected. 

**Important:** To test your installation, follow the procedure in Validate policies after installing 1.11.2-Hotfix.3 to validate policy behavior. 

The procedures for upgrading Apigee hybrid are organized in the following sections: 

  1. Prepare to upgrade.
  2. Install hybrid runtime version 1.11.2.



##  Prerequisites 

These upgrade instructions assume you have Apigee hybrid version 1.10.x installed and wish to upgrade it to version 1.11.2. If you are updating from an earlier version, see the instructions for [Upgrading Apigee hybrid to version 1.10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/upgrade).

## Helm charts and `apigeectl`

In version 1.11 you can choose to install and manage Apigee hybrid with either Helm charts or `apigeectl`. Apigee recommends using Helm to manage your installation. 

### Migrating to v1.11 with Helm from v1.10 with `apigeectl`

To upgrade to Apigee hybrid v1.11 managed by Helm from a hybrid v1.10 installation managed with `apigeectl`: 

  1. First, migrate your v1.10 installation Helm by following the instructions in [Migrate Apigee hybrid to Helm charts from `apigeectl`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-migration). 
  2. Follow the instructions for Helm charts below to upgrade your installation. **Note:** When upgrading a migrated installation, you will need to insert a `--force` flag in the `helm upgrade` commands. 



##  Prepare to upgrade to version 1.11 

**Note:** When migrating from Apigee hybrid v1.10 to v1.11, after transitioning from `apigeectl` to Helm charts in the previous step, you must follow the instructions under the helm tab. After transitioning to Helm you must continue with Helm in further upgrades. 

###  Back up your hybrid installation (recommended) 

### Helm

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

  2. Make a backup copy of your version 1.10 `$APIGEE_HELM_CHARTS_HOME/` directory. You can use any backup process. For example, you can create a `tar` file of your entire directory with: 
         
         tar -czvf **$APIGEE_HELM_CHARTS_HOME** /../apigee-helm-charts-v1.10-backup.tar.gz **$APIGEE_HELM_CHARTS_HOME**

  3. Back up your Cassandra database following the instructions in [Cassandra backup and recovery](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cassandra-backup-overview).
  4. If you are using service cert files (`.json`) in your overrides to authenticate service accounts, make sure your service account cert files reside in the correct Helm chart directory. Helm charts cannot read files outside of each chart directory. 

This step is not needed if you are using Kubernetes secrets or Workload Identity to authenticate service accounts.

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



### `apigeectl`

The examples in these instructions use the following directory structure. Your installation may be different. Adjust the instructions to the structure of your installation. 
    
    
    hybrid-v1.11-root-directory/
    └── apigeectl/
        └── config/
        └── plugins/
        └── templates/
        └── tools/
    └── hybrid-files/
        └── overrides/
        └── service-accounts/
        └── certs/
    hybrid-v1.10-root-directory/

  1. These instructions use the environment variable APIGEECTL_HOME for the directory in your file system where you have installed `apigeectl`. If needed, change directory into your `apigeectl` directory and define the variable with the following command: 

###  Linux 
         
         export APIGEECTL_HOME=$PWD
         echo **$APIGEECTL_HOME**

###  Mac OS 
         
         export APIGEECTL_HOME=$PWD
         echo **$APIGEECTL_HOME**

###  Windows 
         
         set APIGEECTL_HOME=%CD%
         echo %APIGEECTL_HOME%

  2. Make a backup copy of your version 1.10 `$APIGEECTL_HOME/` directory. For example: 
         
         tar -czvf **$APIGEECTL_HOME** /../apigeectl-v1.10-backup.tar.gz **$APIGEECTL_HOME**

  3. Back up your Cassandra database following the instructions in [Cassandra backup and recovery](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cassandra-backup-overview).



###  Upgrade your Kubernetes version 

Check your Kubernetes platform version and if needed, upgrade your Kubernetes platform to a version that is supported by both hybrid 1.10 and hybrid 1.11. Follow your platform's documentation if you need help. 

### _Click to expand a list of supported platforms_

| 1.10 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(3) | 1.11 | 1.12  
---|---|---|---  
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
1.29.x(≥ 1.12.1)  
GKE on AWS | 1.13.x (K8s v1.24.x)   
1.14.x (K8s v1.25.x)   
1.26.x(12)   
1.27.x(≥ 1.10.5)   
1.28.x(≥ 1.10.5) | 1.14.x (K8s v1.25.x)   
1.26.x(12)   
1.27.x   
1.28.x(≥ 1.11.2)   
1.29.x(≥ 1.11.2) |  1.26.x(12)   
1.27.x   
1.28.x   
1.29.x(≥ 1.12.1)  
GKE on Azure | 1.13.x   
1.14.x   
1.26.x(12)   
1.27.x(≥ 1.10.5)   
1.28.x(≥ 1.10.5) | 1.14.x   
1.26.x(12)   
1.27.x   
1.28.x(≥ 1.11.2)   
1.29.x(≥ 1.11.2) | 1.26.x(12)   
1.27.x   
1.28.x   
1.29.x(≥ 1.12.1)  
Google Distributed Cloud (software only) on VMware (1) (13) | 1.13.x   
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
1.28.x(12)   
1.29.x(≥ 1.12.1)  
Google Distributed Cloud (software only) on bare metal (1) | 1.13.x   
1.14.x (K8s v1.25.x)   
1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.27.x(12)(≥ 1.10.5)   
1.28.x(≥ 1.10.5) | 1.14.x   
1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.28.x(12)(≥ 1.11.2)   
1.29.x(≥ 1.11.2) | 1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.28.x(12)   
1.29.x(≥ 1.12.1)  
EKS(7) | 1.24.x   
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
1.29.x(≥ 1.12.1)  
AKS(7) | 1.24.x   
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
1.29.x(≥ 1.12.1)  
OpenShift(7) | 4.11   
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
4.16(≥ 1.12.1)  
Rancher Kubernetes Engine (RKE) |  v1.26.2+rke2r1   
1.27.x(≥ 1.10.5)   
1.28.x(≥ 1.10.5) |  v1.26.2+rke2r1   
v1.27.x   
1.28.x(≥ 1.11.2)   
1.29.x(≥ 1.11.2) | v1.26.2+rke2r1  
v1.27.x  
  
1.28.x   
1.29.x(≥ 1.12.1)  
VMware Tanzu |  N/A |  N/A | v1.26.x   
  
### Components

| 1.10 | 1.11 | 1.12  
Anthos Service Mesh |  1.17.x(10) |  1.18.x(10) |  1.19.x(10)  
JDK |  JDK 11 |  JDK 11 |  JDK 11  
cert-manager |  1.10.x  
1.11.x  
1.12.x  |  1.11.x  
1.12.x  
1.13.x  |  1.11.x  
1.12.x  
1.13.x   
Cassandra |  3.11 |  3.11 |  4.0  
Kubernetes | 1.24.x  
1.25.x  
1.26.x  
| 1.25.x  
1.26.x  
1.27.x  
| 1.26.x  
1.27.x  
1.28.x  
  
kubectl |  |  | 1.27.x  
1.28.x  
1.29.x  
  
Helm | 3.10+ | 3.10+ | 3.14.2+  
Secret Store CSI driver |  | 1.3.4 | 1.4.1  
Vault |  | 1.13.x | 1.15.2  
**(1) On Anthos on-premises (Google Distributed Cloud) version 1.13, follow these instructions to avoid conflict with `cert-manager`: [Conflicting cert-manager installation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues#conflicting-cert-manager-installation)** **(2) Support available with Apigee hybrid version 1.7.2 and newer**.  **(3) The official EOL dates for Apigee hybrid versions 1.10 and older have been reached. Regular monthly patches are no longer available. These releases are no longer officially supported except for customers with explicit and official exceptions for continued support. Other customers must upgrade**.  **(4) Anthos on-premises (Google Distributed Cloud) versions 1.12 and earlier are out of support. See the Distributed Cloud on bare metal [Version Support Policy](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/getting-support#version-support) and the Distributed Cloud on VMware [supported versions list](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#supported-versions).** **(5) Google Distributed Cloud on bare metal or VMware [ requires Anthos Service Mesh 1.14](https://docs.cloud.google.com/anthos/docs/version-and-upgrade-support#112) or later. We recommend that you upgrade to hybrid v1.8 and switch to Apigee ingress gateway which no longer requires you to install Anthos Service Mesh on your hybrid cluster.** **(6) Support available with Apigee hybrid version 1.8.4 and newer**.  **(7) Not supported with Apigee hybrid version 1.8.4 and newer**.  **(8) Support available with Apigee hybrid version 1.7.6 and newer**.  **(9) Not supported with Apigee hybrid version 1.8.5 and newer**.  **(10) Anthos Service Mesh is automatically installed with Apigee hybrid 1.9 and newer**.  **(11) Support available with Apigee hybrid version 1.9.2 and newer**.  **(12) GKE on AWS version numbers now reflect the Kubernetes versions. See [GKE Enterprise version and upgrade support](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support#gke_multi_cloud) for version details and recommended patches**.  **(13) Vault is not certified on Google Distributed Cloud for VMware. ** **(14) Support available with Apigee hybrid version 1.10.5 and newer**.  **(15) Support available with Apigee hybrid version 1.11.2 and newer**.  **(16) Support available with Apigee hybrid version 1.12.1 and newer**.   
  
###  About attached clusters 

For Apigee hybrid versions 1.7.x and older, you must use [GKE attached clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached) if you want to run Apigee hybrid in a multi-cloud context on Elastic Kubernetes Service (EKS), Azure Kubernetes Service (AKS), or another supported third-party Kubernetes service provider. Cluster attachment allows Google to measure the usage of Anthos Service Mesh. 

For Apigee hybrid version 1.8.x, GKE attached clusters are required if you are using Anthos Service Mesh for your ingress gateway. If you are using Apigee ingress gateway, attached clusters are optional. 

**Note:** Hybrid installations are not currently supported on Autopilot clusters. 

##  Install the hybrid 1.11.2 runtime 

**Caution:** Do not create new environments during the upgrade process.

### Helm

### Prepare for the Helm charts upgrade

This upgrade procedure assumes you are using the same namespace and service accounts for the upgraded installation. If you are making any configuration changes, be sure to reflect those changes in your overrides file before installing the Helm charts.

  1. Make the following change to your overrides.yaml file to enable the `apigee-operator` and `apigee-env` charts ot use the correct tag, `1.11.2-hotfix.3`: 
         
         ao:
           image:
             url: "gcr.io/apigee-release/hybrid/apigee-operators"
             tag: "1.11.2-hotfix.3"
         runtime:
           image:
             url: "gcr.io/apigee-release/hybrid/apigee-runtime"
             tag: "1.11.2-hotfix.3"
         

See [Apigee 1.11.2-hotfix.3 release notes](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_1112-hotfix2).

  2. Pull the Apigee Helm charts. 

Apigee hybrid charts are hosted in [Google Artifact Registry](https://docs.cloud.google.com/artifact-registry):

`oci://us-docker.pkg.dev/apigee-release/apigee-hybrid-helm-charts`

Using the `pull` command, copy all of the Apigee hybrid Helm charts to your local storage with the following command: 
         
         export **CHART_REPO** =oci://us-docker.pkg.dev/apigee-release/apigee-hybrid-helm-charts
         export **CHART_VERSION** =1.11.2
         helm pull **$CHART_REPO** /apigee-operator --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-datastore --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-env --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-ingress-manager --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-org --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-redis --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-telemetry --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-virtualhost --version **$CHART_VERSION** --untar
         

  3. Install cert-manager if needed. 

If you need to upgrade your cert-manager version, install the new version with the following command:
         
         kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.11.1/cert-manager.yaml
         

  4. Install the updated Apigee CRDs: **Note:** From this step onwards, all commands should be run under the chart repo root directory. **Note:** This is the only supported method for installing Apigee CRDs. Do not use `kubectl apply` without `-k`, do not omit `--server-side`. **Note:** This step requires elevated cluster permissions. 
     1. Use the `kubectl` dry-run feature by running the following command:
            
            kubectl apply -k  apigee-operator/etc/crds/default/ --server-side --force-conflicts --validate=false --dry-run
            

     2. After validating with the dry-run command, run the following command:
            
            kubectl apply -k  apigee-operator/etc/crds/default/ --server-side --force-conflicts --validate=false
            

     3. Validate the installation with the `kubectl get crds` command: 
            
            kubectl get crds | grep apigee

Your output should look something like the following:
            
            apigeedatastores.apigee.cloud.google.com                    2023-10-09T14:48:30Z
            apigeedeployments.apigee.cloud.google.com                   2023-10-09T14:48:30Z
            apigeeenvironments.apigee.cloud.google.com                  2023-10-09T14:48:31Z
            apigeeissues.apigee.cloud.google.com                        2023-10-09T14:48:31Z
            apigeeorganizations.apigee.cloud.google.com                 2023-10-09T14:48:32Z
            apigeeredis.apigee.cloud.google.com                         2023-10-09T14:48:33Z
            apigeerouteconfigs.apigee.cloud.google.com                  2023-10-09T14:48:33Z
            apigeeroutes.apigee.cloud.google.com                        2023-10-09T14:48:33Z
            apigeetelemetries.apigee.cloud.google.com                   2023-10-09T14:48:34Z
            cassandradatareplications.apigee.cloud.google.com           2023-10-09T14:48:35Z
            

  5. Check the labels on the cluster nodes. By default, Apigee schedules data pods on nodes with the label `cloud.google.com/gke-nodepool=apigee-data` and runtime pods are scheduled on nodes with the label `cloud.google.com/gke-nodepool=apigee-runtime`. You can customize your node pool labels in the `overrides.yaml` file. 

For more information, see [ Configuring dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/configure-dedicated-nodes). 




### Install the Apigee hybrid Helm charts

**Note:** Before executing any of the Helm upgrade/install commands, use the Helm dry-run feature by adding `--dry-run` at the end of the command. See `helm -h` to list supported commands, options, and usage. 

  1. If you have not, navigate into your `APIGEE_HELM_CHARTS_HOME` directory. Run the following commands from that directory.
  2. Upgrade the Apigee Operator/Controller: **Note:** This step requires elevated cluster permissions. Run `helm -h` or `helm upgrade -h` for details 

Dry run:
         
         helm upgrade operator apigee-operator/ \
           --install \
           --create-namespace \
           --namespace apigee-system \
           -f OVERRIDES_FILE \
           --dry-run
         

Upgrade the chart:
         
         helm upgrade operator apigee-operator/ \
           --install \
           --create-namespace \
           --namespace apigee-system \
           -f OVERRIDES_FILE
         

**Note:** For installations migrated from `apigeectl`to Helm, use: 
         
         helm upgrade operator apigee-operator/ \
           --install \
           --create-namespace \
           --namespace apigee-system \
           --force \
           -f OVERRIDES_FILE
         

Verify Apigee Operator installation:
         
         helm ls -n apigee-system
         
         
         NAME           NAMESPACE       REVISION        UPDATED                                 STATUS          CHART                   APP VERSION
         operator    apigee-system   3               2023-06-26 00:42:44.492009 -0800 PST    deployed        apigee-operator-1.11.2   1.11.2

Verify it is up and running by checking its availability:
         
         kubectl -n apigee-system get deploy apigee-controller-manager
         
         
         NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
         apigee-controller-manager   1/1     1            1           7d20h

  3. Upgrade the Apigee datastore: 

Dry run:
         
         helm upgrade datastore apigee-datastore/ \
           --install \
           --namespace apigee \
           -f OVERRIDES_FILE \
           --dry-run
         

Upgrade the chart:
         
         helm upgrade datastore apigee-datastore/ \
           --install \
           --namespace apigee \
           -f OVERRIDES_FILE
         

**Note:** For installations migrated from `apigeectl` to Helm, use: 
         
         helm upgrade datastore apigee-datastore/ \
           --install \
           --namespace apigee \
           --force \
           -f OVERRIDES_FILE
         

Verify `apigeedatastore` is up and running by checking its state:
         
         kubectl -n apigee get apigeedatastore default
         
         
         NAME      STATE       AGE
         default   running    2d

  4. Upgrade Apigee telemetry: 

Dry run:
         
         helm upgrade telemetry apigee-telemetry/ \
           --install \
           --namespace apigee \
           -f OVERRIDES_FILE \
           --dry-run
         

Upgrade the chart:
         
         helm upgrade telemetry apigee-telemetry/ \
           --install \
           --namespace apigee \
           -f OVERRIDES_FILE
         

**Note:** For installations migrated from `apigeectl` to Helm, use: 
         
         helm upgrade telemetry apigee-telemetry/ \
           --install \
           --namespace apigee \
           --force \
           -f OVERRIDES_FILE
         

Verify it is up and running by checking its state:
         
         kubectl -n apigee get apigeetelemetry apigee-telemetry
         
         
         NAME               STATE     AGE
         apigee-telemetry   running   2d

  5. Upgrade Apigee Redis: 

Dry run:
         
         helm upgrade redis apigee-redis/ \
           --install \
           --namespace apigee \
           -f OVERRIDES_FILE \
           --dry-run
         

Upgrade the chart:
         
         helm upgrade redis apigee-redis/ \
           --install \
           --namespace apigee \
           -f OVERRIDES_FILE
         

**Note:** For installations migrated from `apigeectl` to Helm, use: 
         
         helm upgrade redis apigee-redis/ \
           --install \
           --namespace apigee \
           --force \
           -f OVERRIDES_FILE
         

Verify it is up and running by checking its state:
         
         kubectl -n apigee get apigeeredis default
         
         
         NAME      STATE     AGE
         default   running   2d

  6. Upgrade Apigee ingress manager: 

Dry run:
         
         helm upgrade ingress-manager apigee-ingress-manager/ \
           --install \
           --namespace apigee \
           -f OVERRIDES_FILE \
           --dry-run
         

Upgrade the chart:
         
         helm upgrade ingress-manager apigee-ingress-manager/ \
           --install \
           --namespace apigee \
           -f OVERRIDES_FILE
         

**Note:** For installations migrated from `apigeectl` to Helm, use: 
         
         helm upgrade ingress-manager apigee-ingress-manager/ \
           --install \
           --namespace apigee \
           --force \
           -f OVERRIDES_FILE
         

Verify it is up and running by checking its availability:
         
         kubectl -n apigee get deployment apigee-ingressgateway-manager
         
         
         NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
         apigee-ingressgateway-manager   2/2     2            2           2d

  7. Upgrade the Apigee organization: 

Dry run:
         
         helm upgrade ORG_NAME apigee-org/ \
           --install \
           --namespace apigee \
           -f OVERRIDES_FILE \
           --dry-run
         

Upgrade the chart:
         
         helm upgrade ORG_NAME apigee-org/ \
           --install \
           --namespace apigee \
           -f OVERRIDES_FILE
         

**Note:** For installations migrated from `apigeectl` to Helm, use: 
         
         helm upgrade ORG_NAME apigee-org/ \
           --install \
           --namespace apigee \
           --force \
           -f OVERRIDES_FILE
         

Verify it is up and running by checking the state of the respective org:
         
         kubectl -n apigee get apigeeorg
         
         
         NAME                      STATE     AGE
         apigee-org1-xxxxx          running   2d

  8. Upgrade the environment. 

You must install one environment at a time. Specify the environment with `--set env=`ENV_NAME:

Dry run:
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --install \
           --namespace apigee \
           --set env=ENV_NAME \
           -f OVERRIDES_FILE \
           --dry-run
         

     * ENV_RELEASE_NAME is the name with which you previously installed the `apigee-env` chart. In hybrid v1.10, it is usually `apigee-env-ENV_NAME`. In Hybrid v1.11 and newer it is usually ENV_NAME.
     * ENV_NAME is the name of the environment you are upgrading.
     * OVERRIDES_FILE is your new overrides file for v.1.11.2

Upgrade the chart:
    
    helm upgrade ENV_RELEASE_NAME apigee-env/ \
      --install \
      --namespace apigee \
      --set env=ENV_NAME \
      -f OVERRIDES_FILE
    

**Note:** For installations migrated from `apigeectl` to Helm, use: 
    
    helm upgrade ENV_RELEASE_NAME apigee-env/ \
      --install \
      --namespace apigee \
      --set env=ENV_NAME \
      --force \
      -f OVERRIDES_FILE
    

Verify it is up and running by checking the state of the respective env:
    
    kubectl -n apigee get apigeeenv
    
    
    NAME                          STATE       AGE   GATEWAYTYPE
    apigee-org1-dev-xxx            running     2d

  9. Upgrade the environment groups (`virtualhosts`). 
     1. You must upgrade one environment group (virtualhost) at a time. Specify the environment group with `--set envgroup=`ENV_GROUP_NAME. Repeat the following commands for each env group mentioned in the overrides.yaml file: 

Dry run:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace apigee \
              --set envgroup=ENV_GROUP_NAME \
              -f OVERRIDES_FILE \
              --dry-run
            

ENV_GROUP_RELEASE_NAME is the name with which you previously installed the `apigee-virtualhost` chart. In hybrid v1.10, it is usually `apigee-virtualhost-ENV_GROUP_NAME`. In Hybrid v1.11 and newer it is usually ENV_GROUP_NAME.

Upgrade the chart:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace apigee \
              --set envgroup=ENV_GROUP_NAME \
              -f OVERRIDES_FILE
            

**Note:** For installations migrated from `apigeectl` to Helm, use: 
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace apigee \
              --set envgroup=ENV_GROUP_NAME \
              --force \
              -f OVERRIDES_FILE
            

**Note:** ENV_GROUP_RELEASE_NAME must be unique within the `apigee` namespace. 

For example, if you have a an _environment_ named `prod` and an _environment group_ named `prod`, set the value of ENV_GROUP_RELEASE_NAME to something unique, like `prod-envgroup`. 

     2. Check the state of the ApigeeRoute (AR). 

Installing the `virtualhosts` creates ApigeeRouteConfig (ARC) which internally creates ApigeeRoute (AR) once the Apigee watcher pulls env group related details from the control plane. Therefore, check that the corresponding AR's state is running: 
            
            kubectl -n apigee get arc
            
            
            NAME                                STATE   AGE
            apigee-org1-dev-egroup                       2d
            
            kubectl -n apigee get ar
            
            
            NAME                                        STATE     AGE
            apigee-org1-dev-egroup-xxxxxx                running   2d




### Install 1.11.2-hotfix.3

  1. Make the following change to your overrides.yaml file to enable `runtime` to use the correct tag, `1.11.2-hotfix.3`: 
         
         runtime:
           image:
             url: "gcr.io/apigee-release/hybrid/apigee-runtime"
             tag: "1.11.2-hotfix.3"
         

See [Apigee 1.11.2-hotfix.3 release notes](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_1112-hotfix3).

  2. Update the `apigee-env` chart with the `helm upgrade` command and your current overrides file. 

Repeat this for every environment.
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --namespace APIGEE_NAMESPACE \
           --set env ENV_NAME \
           --atomic \
           -f OVERRIDES_FILE 




### `apigeectl`

  1. Store the latest version number in a variable using the following command: 

###  Linux 
         
         export VERSION=$(curl -s \
           https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/current-version.txt?ignoreCache=1)

###  Mac OS 
         
         export VERSION=$(curl -s \
           https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/current-version.txt)

###  Windows 
         
         for /f "tokens=*" %a in ('curl -s ^
           https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/current-version.txt') ^
         do set VERSION=%a

  2. Check that the variable was populated with a version number using the following command. If you want to use a different version, you can save that in an environment variable instead. 
         
         echo $VERSION

You should see the latest Apigee hybrid version: 
         
         1.11.2

  3. Be sure you are in the hybrid base directory (the parent of the directory where the `apigeectl` executable file is located): 
         
         cd **$APIGEECTL_HOME** /..

  4. Download the release package for your operating system using the following command. Be sure to select your platform in the following table:

###  Linux 

**Linux 64 bit:**
         
         curl -LO \
           https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**$VERSION** /apigeectl_linux_64.tar.gz

###  Mac OS 

**Mac 64 bit:**
         
         curl -LO \
           https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**$VERSION** /apigeectl_mac_64.tar.gz

###  Windows 

**Windows 64 bit:**
         
         curl -LO ^
           https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**%VERSION%** /apigeectl_windows_64.zip

  5. Rename your current `apigeectl/` directory to a backup directory name. For example: 

###  Linux 
         
         mv $APIGEECTL_HOME/ $APIGEECTL_HOME-v1.10/

###  Mac OS 
         
         mv $APIGEECTL_HOME/ $APIGEECTL_HOME-v1.10/ 

###  Windows 
         
         rename %APIGEECTL_HOME% %APIGEECTL_HOME%-v1.10 

  6. Extract the downloaded gzip file contents into your hybrid base directory. The hybrid base directory is the directory where the renamed `apigeectl-v1.10` directory is located:

###  Linux 
         
         tar xvzf filename.tar.gz -C ./

###  Mac OS 
         
         tar xvzf filename.tar.gz -C ./

###  Windows 
         
         tar xvzf filename.zip -C ./

  7. The tar contents are, by default, expanded into a directory with the version and platform in its name. For example: `./apigeectl_1.11.2-xxxxxxx_linux_64`. Rename that directory to `apigeectl` using the following command:

###  Linux 
         
         mv apigeectl_1.11.2-xxxxxxx_linux_64 apigeectl

###  Mac OS 
         
         mv apigeectl_1.11.2-xxxxxxx_mac_64 apigeectl

###  Windows 
         
         rename apigeectl_1.11.2-xxxxxxx_windows_64 apigeectl

  8. Change to the `apigeectl` directory: 
         
         cd ./apigeectl

This directory is the `apigeectl` home directory. It is where the `apigeectl` executable command is located. 

  9. These instructions use the environment variable `**$APIGEECTL_HOME**` for the directory in your file system where the `apigeectl` utility is installed. If needed, change directory into your `apigeectl` directory and define the variable with the following command: 

###  Linux 
         
         export APIGEECTL_HOME=$PWD
         
         echo $APIGEECTL_HOME

###  Mac OS 
         
         export APIGEECTL_HOME=$PWD
         
         echo $APIGEECTL_HOME

###  Windows 
         
         set APIGEECTL_HOME=%CD%
         
         echo %APIGEECTL_HOME%

  10. Verify the version of `apigeectl` with the `version` command: 
         
         ./apigeectl version
         
         Version: 1.11.2

  11. Create a `hybrid-base-directory/hybrid-files` directory, and then move into it. The `hybrid-files`directory is where configuration files such as the overrides file, certs, and service accounts are located. For example: 

###  Linux 
         
         mkdir **$APIGEECTL_HOME** /../hybrid-files
         
         cd **$APIGEECTL_HOME** /../hybrid-files

###  Mac OS 
         
         mkdir **$APIGEECTL_HOME** /../hybrid-files
         
         cd **$APIGEECTL_HOME** /../hybrid-files

###  Windows 
         
         mkdir **%APIGEECTL_HOME%** /../hybrid-files
         
         cd **%APIGEECTL_HOME%** /../hybrid-files

  12. Verify that `kubectl` is set to the correct context using the following command. The current context should be set to the cluster in which you are upgrading Apigee hybrid. 
         
         kubectl config get-contexts | grep \*

  13. In the `hybrid-files` directory: 
     1. Update the following symbolic links to `$APIGEECTL_HOME`. These links allow you to run the newly installed `apigeectl` command from inside the `hybrid-files` directory: 
            
            ln -nfs $APIGEECTL_HOME/tools tools
            ln -nfs $APIGEECTL_HOME/config config
            ln -nfs $APIGEECTL_HOME/templates templates
            ln -nfs $APIGEECTL_HOME/plugins plugins

     2. To check that the symlinks were created correctly, execute the following command and make sure the link paths point to the correct locations: 
            
            ls -l | grep ^l

  14. Do a dry run initialization to check for errors: 
         
         **${APIGEECTL_HOME}** /apigeectl init -f OVERRIDES_FILE --dry-run=client

Where OVERRIDES_FILE is the name of your overrides file, for example `./overrides/overrides.yaml`. 

**Tip:** You can replace `OVERRIDES_FILE` in the code sample above with the name and path to your overrides file, and every instance on this page will be replaced.
  15. If there are no errors, initialize hybrid 1.11.2: 
         
         $APIGEECTL_HOME/apigeectl init -f OVERRIDES_FILE

**Note:** `apigeectl` installs and configures Apigee ingress gateway when you run `apigeectl init`. 
  16. Check the initialization status: 
         
         $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE

On success, the output says: `All containers ready.`
         
         kubectl describe apigeeds -n apigee

In the output, look for `State: running`. 

  17. Check for errors with a dry run of the `apply` command using the `--dry-run` flag: 
         
         $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE --dry-run=client

  18. If there are no errors, apply your overrides. Select and follow the instructions for production environments or non-prod environments, depending on your installation. 

### Production

For production environments, upgrade each hybrid component individually, and check the status of the upgraded component before proceeding to the next component. 

     1. Be sure you are in the `hybrid-files` directory.
     2. Apply your overrides to upgrade Cassandra: 
            
            $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE --datastore

     3. Check completion: 
            
            $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE

**Tip:** If `check-ready` fails, you can get more information about your pods with: 
            
            kubectl -n NAMESPACE get pods

Where NAMESPACE is your Apigee hybrid namespace. 

Proceed to the next step only when the pods are ready. 

     4. Apply your overrides to upgrade Telemetry components and check completion: 
            
            $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE --telemetry
            
            $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE

     5. Bring up Redis components: 
            
            $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE --redis

     6. Apply your overrides to upgrade the org-level components (MART, Watcher and Apigee Connect) and check completion: 
            
            $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE --org
            
            $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE

     7. Apply your overrides to upgrade your environments. You have two choices: 
        * **Environment by environment** : Apply your overrides to one environment at a time and check completion. Repeat this step for each environment: 
              
              $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE --env ENV_NAME
              
              $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE

Where ENV_NAME is the name of the environment you are upgrading. 

        * **All environments at one time** : Apply your overrides to all environments at once and check completion: 
              
              $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE --all-envs
              
              $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE

     8. Apply your overrides to upgrade the `virtualhosts` components and check completion: 
            
            $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE --settings virtualhosts
            
            $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE

### Non-prod

In most non-production, demo, or experimental environments, you can apply the overrides to all components at once. If your non-production environment is large and complex or closely mimics a production environment, you may want to use the instructions for upgrading production environments. 

     1. Be sure you are in the `hybrid-files` directory.
     2. $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE

     3. Check the status: 
            
            $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE




### Install 1.11.2-hotfix.3

  1. Make the following change to your overrides.yaml file to enable `runtime` to use the correct tag, `1.11.2-hotfix.3`: 
         
         runtime:
           image:
             url: "gcr.io/apigee-release/hybrid/apigee-runtime"
             tag: "1.11.2-hotfix.3"
         

See [Apigee 1.11.2-hotfix.3 release notes](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_1112-hotfix3).

  2. Install the hotfix with `apigeectl init` using your updated overrides file. 

Dry run:
         
         ${APIGEECTL_HOME}/apigeectl init -f OVERRIDES_FILE --dry-run=client
         

Initialize:
         
         ${APIGEECTL_HOME}/apigeectl init -f OVERRIDES_FILE
         

  3. Apply the hotfix with `apigeectl apply`. 

Dry run:
         
         ${APIGEECTL_HOME}/apigeectl apply -f OVERRIDES_FILE --all-envs --dry-run=client
         

Apply:
         
         ${APIGEECTL_HOME}/apigeectl apply -f OVERRIDES_FILE --all-envs
         




## Validate policies after upgrade to 1.11.2-hotfix.3

Use this procedure to validate the behavior of the [JavaCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy) after upgrading to Hybrid 1.11.2-hotfix.3.

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

ENV_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-env` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_NAME`. However, if your environment has the same name as your environment group, you must use different release names for the environment and environment group, for example `dev-env-release` and `dev-envgroup-release`. For more information on releases in Helm, see [Three big concepts class="external"](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.

If the log message `"Failed to load and initialize class ..."` is still present, continue modifying and testing the JAR until the log message no longer appears.

  4. **Enable the security check in the production environment**. 

After you have thoroughly tested and verified the JAR file in the non-production environment, enable the security check in your production environment by setting the flag `conf_security-secure.constructor.only` to `true` and updating the `apigee-env` chart for the production environment to apply the change. 


**Congratulations!** You have upgraded to Apigee hybrid version 1.11.2. to test your upgrade, call a proxy against the new installation. For an example, see [Step 10: Deploy an API proxy](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-deploy-proxy) in the Apigee hybrid 1.11 installation guide. 

##  Rolling back an upgrade 

Follow these steps to roll back a previous upgrade: 

### Helm

To rollback to the previous version, use the charts charts and the overrides file from the previous installation.

  1. Create the following environment variable: 
     * PREVIOUS_HELM_CHARTS_HOME: The directory where the previous Apigee hybrid Helm charts are installed. This is the version you are rolling back to.
  2. Roll back the virtualhosts. Repeat the following command for each environment group mentioned in the overrides file. 
         
         helm upgrade ENV_GROUP_RELEASE_NAME $PREVIOUS_HELM_CHARTS_HOME/apigee-virtualhost/ \
           --namespace apigee \
           --atomic \
           --set envgroup=ENV_GROUP_NAME \
           -f PREVIOUS_OVERRIDES_FILE
         

ENV_GROUP_RELEASE_NAME is the name with which you previously installed the `apigee-virtualhost` chart. In hybrid v1.10, it is usually `apigee-virtualhost-ENV_GROUP_NAME`. In Hybrid v1.11 and newer it is usually ENV_GROUP_NAME.

  3. Roll back Envs. Repeat the following command for each environment mentioned in the overrides file. 
         
         helm upgrade apigee-env-ENV_NAME $PREVIOUS_HELM_CHARTS_HOME/apigee-env/ \
           --install \
           --namespace apigee \
           --atomic \
           --set env=ENV_NAME \
           -f PREVIOUS_OVERRIDES_FILE
         

ENV_RELEASE_NAME is the name with which you previously installed the `apigee-env` chart. In hybrid v1.10, it is usually `apigee-env-ENV_NAME`. In Hybrid v1.11 and newer it is usually ENV_NAME.

  4. Roll back Org: 
         
         helm upgrade ORG_NAME $PREVIOUS_HELM_CHARTS_HOME/apigee-org/ \
           --install \
           --namespace apigee \
           --atomic \
           -f PREVIOUS_OVERRIDES_FILE
         

  5. Roll back the Ingress Manager: 
         
         helm upgrade ingress-manager $PREVIOUS_HELM_CHARTS_HOME/apigee-ingress-manager/ \
           --install \
           --namespace apigee \
           --atomic \
           -f PREVIOUS_OVERRIDES_FILE
         

  6. Roll back Redis: 
         
         helm upgrade redis $PREVIOUS_HELM_CHARTS_HOME/apigee-redis/ \
           --install \
           --namespace apigee \
           --atomic \
           -f PREVIOUS_OVERRIDES_FILE
         

  7. Roll back Apigee Telemetry: 
         
         helm upgrade telemetry $PREVIOUS_HELM_CHARTS_HOME/apigee-telemetry/ \
           --install \
           --namespace apigee \
           --atomic \
           -f PREVIOUS_OVERRIDES_FILE
         

  8. Roll back Apigee Datastore (the Cassandra database component): 
         
         helm upgrade datastore $PREVIOUS_HELM_CHARTS_HOME/apigee-datastore/ \
           --install \
           --namespace apigee \
           --atomic \
           -f PREVIOUS_OVERRIDES_FILE
         

  9. Roll back the Apigee Controller: 
         
         helm upgrade operator $PREVIOUS_HELM_CHARTS_HOME/apigee-operator/ \
           --install \
           --namespace apigee-system \
           --atomic \
           -f PREVIOUS_OVERRIDES_FILE
         

  10. Roll back the Apigee hybrid CRDs: 
         
         kubectl apply -k  $PREVIOUS_HELM_CHARTS_HOME/apigee-operator/etc/crds/default/ --server-side --force-conflicts --validate=false
         




### `apigeectl`

  1. Clean up completed jobs for the hybrid runtime namespace, where NAMESPACE is the namespace specified in your overrides file, if you specified a namespace. If not, the default namespace is `apigee`: 
         
         kubectl delete job -n NAMESPACE \
           $(kubectl get job -n NAMESPACE \
           -o=jsonpath='{.items[?(@.status.succeeded==1)].metadata.name}')

  2. Clean up completed jobs for the `apigee-system` namespace: 
         
         kubectl delete job -n apigee-system \
           $(kubectl get job -n apigee-system \
           -o=jsonpath='{.items[?(@.status.succeeded==1)].metadata.name}')

  3. Change the `APIGEECTL_HOME` variable to point to the directory that contains the previous version of `apigeectl`. For example: 
         
         export APIGEECTL_HOME=PATH_TO_PREVIOUS_APIGEECTL_DIRECTORY

  4. Run the following commands in the root directory of the installation you want to roll back to. Be sure to use the original overrides file for the version you wish to roll back to: 
     1. In the hybrid-files directory, run `apigeectl apply`: 
            
            $APIGEECTL_HOME/apigeectl apply -f ORIGINAL_OVERRIDES_FILE

Where ORIGINAL_OVERRIDES_FILE is the relative path and filename of the overrides file for your previous version hybrid installation, for example, `./overrides/overrides1.10.yaml`. 

     2. Check the status of your pods: 
            
            kubectl -n NAMESPACE get pods

Where NAMESPACE is your Apigee hybrid namespace. 

     3. Check the status of `apigeeds`: 
            
            kubectl describe apigeeds -n apigee

Your output should look something like: 
            
            Status:
              Cassandra Data Replication:
              Cassandra Pod Ips:
                10.8.2.204
              Cassandra Ready Replicas:  1
              Components:
                Cassandra:
                  Last Successfully Released Version:
                    Revision:  v1-f8aa9a82b9f69613
                    Version:   v1
                  Replicas:
                    Available:  1
                    Ready:      1
                    Total:      1
                    Updated:    1
                  State:        running
              Scaling:
                In Progress:         false
                Operation:
                Requested Replicas:  0
              State:                 running

Proceed to the next step only when the `apigeeds` pod is running. 

     4. Run the following command to make note of what your new replica count values will be for the message processor after the upgrade. If these values do not match what you have set previously, change the values in your overrides file to match your previous configuration. 
            
            apigeectl apply -f ORIGINAL_OVERRIDES_FILE --dry-run=client --print-yaml --env ENV_NAME 2>/dev/null |grep "runtime:" -A 25 -B 1| grep "autoScaler" -A 2

Your output should look something like: 
            
            autoScaler:
                    minReplicas: 2
                    maxReplicas: 10

     5. Run `apigeectl init`: 
            
            $APIGEECTL_HOME/apigeectl init -f ORIGINAL_OVERRIDES_FILE




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
