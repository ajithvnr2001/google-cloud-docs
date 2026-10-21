---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/upgrade/
title: Upgrading Apigee hybrid to version 1.10 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:14:52.085371+00:00
---

# Upgrading Apigee hybrid to version 1.10  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Upgrading Apigee hybrid to version 1.10 Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

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



This procedure covers upgrading from Apigee hybrid version 1.9.x to Apigee hybrid version 1.10.5 and from previous releases of hybrid 1.10.x to version 1.10.5. 

Use the same procedures for minor version upgrades (for example version 1.9 to 1.10) and for patch release upgrades (for example 1.10.0 to 1.10.5). 

##  Upgrading to version 1.10.5 overview 

Upgrading to Apigee hybrid version 1.10 may require downtime. 

When upgrading the Apigee controller to version 1.10.5, all Apigee deployments undergo a rolling restart. To minimize downtime in production hybrid environments during a rolling restart, make sure you are running at least two clusters (in the same or different region/data center). Divert all production traffic to a single cluster and take the cluster you are about to upgrade offline, and then proceed with the upgrade process. Repeat the process for each cluster.

Apigee recommends that you upgrade all clusters as soon as possible to reduce the chances of production impact. There is no time limit on when all remaining clusters must be upgraded after the first one is upgraded. However, until all remaining clusters are upgraded the following operations will be impacted:

  * Cassandra backup and restore cannot work with mixed versions. For example, a backup from Hybrid 1.9 cannot be used to restore a Hybrid 1.10 instance.
  * Cassandra data streaming will not work between mixed Hybrid versions. Therefore, your Cassandra clusters cannot scale horizontally.
  * Region expansion and decommissioning will be impacted, because these operations depend on Cassandra data streaming.

**Note:** Management plane changes do not need to be suspended during an upgrade. Any required suspension to management plane changes are included in the upgrade instructions.

The procedures for upgrading Apigee hybrid are organized in the following sections: 

  1. Prepare to upgrade.
  2. Install hybrid runtime version 1.10.5.



##  Prerequisites 

These upgrade instructions assume you have Apigee hybrid version 1.9.x installed and wish to upgrade it to version 1.10.5. If you are updating from an earlier version, see the instructions for [Upgrading Apigee hybrid to version 1.9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/upgrade).

##  Prepare to upgrade to version 1.10 

###  Back up your hybrid installation (recommended) 

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

  2. Make a backup copy of your version 1.9 `$APIGEECTL_HOME/` directory. For example: 
         
         tar -czvf **$APIGEECTL_HOME** /../apigeectl-v1.9-backup.tar.gz **$APIGEECTL_HOME**

  3. Back up your Cassandra database following the instructions in [Cassandra backup and recovery](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cassandra-backup-overview).



###  Upgrade your Kubernetes version 

Check your Kubernetes platform version and if needed, upgrade your Kubernetes platform to a version that is supported by both hybrid 1.9 and hybrid 1.10. Follow your platform's documentation if you need help. 

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

##  Install the hybrid 1.10.5 runtime 

**Caution:** Do not create new environments during the upgrade process.

  1. Be sure you are in the hybrid base directory (the parent of the directory where the `apigeectl` executable file is located): 
         
         cd **$APIGEECTL_HOME** /..

  2. Download the release package for your operating system using the following command. Be sure to select your platform in the following table:

###  Linux 

**Linux 64 bit:**
         
         curl -LO \
           https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**1.10.5** /apigeectl_linux_64.tar.gz

###  Mac OS 

**Mac 64 bit:**
         
         curl -LO \
           https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**1.10.5** /apigeectl_mac_64.tar.gz

###  Windows 

**Windows 64 bit:**
         
         curl -LO ^
           https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**1.10.5** /apigeectl_windows_64.zip

  3. Rename your current `apigeectl/` directory to a backup directory name. For example: 

###  Linux 
         
         mv $APIGEECTL_HOME/ $APIGEECTL_HOME-v1.9/

###  Mac OS 
         
         mv $APIGEECTL_HOME/ $APIGEECTL_HOME-v1.9/ 

###  Windows 
         
         rename %APIGEECTL_HOME% %APIGEECTL_HOME%-v1.9 

  4. Extract the downloaded gzip file contents into your hybrid base directory. The hybrid base directory is the directory where the renamed `apigeectl-v1.9` directory is located:

###  Linux 
         
         tar xvzf filename.tar.gz -C ./

###  Mac OS 
         
         tar xvzf filename.tar.gz -C ./

###  Windows 
         
         tar xvzf filename.zip -C ./

  5. The tar contents are, by default, expanded into a directory with the version and platform in its name. For example: `./apigeectl_1.10.5-xxxxxxx_linux_64`. Rename that directory to `apigeectl` using the following command:

###  Linux 
         
         mv apigeectl_1.10.5-xxxxxxx_linux_64 apigeectl

###  Mac OS 
         
         mv apigeectl_1.10.5-xxxxxxx_mac_64 apigeectl

###  Windows 
         
         rename apigeectl_1.10.5-xxxxxxx_windows_64 apigeectl

  6. Change to the `apigeectl` directory: 
         
         cd ./apigeectl

This directory is the `apigeectl` home directory. It is where the `apigeectl` executable command is located. 

  7. These instructions use the environment variable `**$APIGEECTL_HOME**` for the directory in your file system where the `apigeectl` utility is installed. If needed, change directory into your `apigeectl` directory and define the variable with the following command: 

###  Linux 
         
         export APIGEECTL_HOME=$PWD
         
         echo $APIGEECTL_HOME

###  Mac OS 
         
         export APIGEECTL_HOME=$PWD
         
         echo $APIGEECTL_HOME

###  Windows 
         
         set APIGEECTL_HOME=%CD%
         
         echo %APIGEECTL_HOME%

  8. Verify the version of `apigeectl` with the `version` command: 
         
         ./apigeectl version
         
         Version: 1.10.5

  9. Create a `hybrid-base-directory/hybrid-files` directory, and then move into it. The `hybrid-files`directory is where configuration files such as the overrides file, certs, and service accounts are located. For example: 

###  Linux 
         
         mkdir **$APIGEECTL_HOME** /../hybrid-files
         
         cd **$APIGEECTL_HOME** /../hybrid-files

###  Mac OS 
         
         mkdir **$APIGEECTL_HOME** /../hybrid-files
         
         cd **$APIGEECTL_HOME** /../hybrid-files

###  Windows 
         
         mkdir **%APIGEECTL_HOME%** /../hybrid-files
         
         cd **%APIGEECTL_HOME%** /../hybrid-files

  10. Verify that `kubectl` is set to the correct context using the following command. The current context should be set to the cluster in which you are upgrading Apigee hybrid. 
         
         kubectl config get-contexts | grep \*

  11. In the `hybrid-files` directory: 
     1. Update the following symbolic links to `$APIGEECTL_HOME`. These links allow you to run the newly installed `apigeectl` command from inside the `hybrid-files` directory: 
            
            ln -nfs $APIGEECTL_HOME/tools tools
            ln -nfs $APIGEECTL_HOME/config config
            ln -nfs $APIGEECTL_HOME/templates templates
            ln -nfs $APIGEECTL_HOME/plugins plugins

     2. To check that the symlinks were created correctly, execute the following command and make sure the link paths point to the correct locations: 
            
            ls -l | grep ^l

  12. Make the following change to your overrides.yaml file to enable the `apigee-operator` chart ot use the correct tag, `1.10.5-hotfix.1`: 
         
         ao:
             image:
               url: "gcr.io/apigee-release/hybrid/apigee-operators"
               tag: "1.10.5-hotfix.1"
           

  13. Do a dry run initialization to check for errors: 
         
         **${APIGEECTL_HOME}** /apigeectl init -f OVERRIDES_FILE --dry-run=client

Where OVERRIDES_FILE is the name of your overrides file, for example `./overrides/overrides.yaml`. 

**Tip:** You can replace `OVERRIDES_FILE` in the code sample above with the name and path to your overrides file, and every instance on this page will be replaced.
  14. If there are no errors, initialize hybrid 1.10.5: 
         
         $APIGEECTL_HOME/apigeectl init -f OVERRIDES_FILE

**Note:** `apigeectl` installs and configures Apigee ingress gateway when you run `apigeectl init`. 
  15. Check the initialization status: 
         
         $APIGEECTL_HOME/apigeectl check-ready -f OVERRIDES_FILE

On success, the output says: `All containers ready.`
         
         kubectl describe apigeeds -n apigee

In the output, look for `State: running`. 

  16. Check for errors with a dry run of the `apply` command using the `--dry-run` flag: 
         
         $APIGEECTL_HOME/apigeectl apply -f OVERRIDES_FILE --dry-run=client

  17. If there are no errors, apply your overrides. Select and follow the instructions for production environments or non-prod environments, depending on your installation. 

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


**Congratulations!** You have upgraded to Apigee hybrid version 1.10.5. to test your upgrade, call a proxy against the new installation. For an example, see [Step 10: Deploy an API proxy](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-deploy-proxy) in the Apigee hybrid 1.10 installation guide. 

##  Rolling back an upgrade 

Follow these steps to roll back a previous upgrade: 

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

  4. In the root directory of the installation you want to roll back to, run `apigeectl apply`, check the status of your pods, and then run `apigeectl init`. Be sure to use the original overrides file for the version you wish to roll back to: 
     1. In the hybrid-files directory, run `apigeectl apply`: 
            
            $APIGEECTL_HOME/apigeectl apply -f ORIGINAL_OVERRIDES_FILE

Where ORIGINAL_OVERRIDES_FILE is the relative path and filename of the overrides file for your previous version hybrid installation, for example, `./overrides/overrides1.9.yaml`. 

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
