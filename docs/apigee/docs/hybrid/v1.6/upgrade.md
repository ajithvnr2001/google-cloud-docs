---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/upgrade/
title: Upgrading Apigee hybrid to version 1.6 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:57:12.606247+00:00
---

# Upgrading Apigee hybrid to version 1.6  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Upgrading Apigee hybrid to version 1.6 Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.6 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.6 (unsupported)keyboard_arrow_down

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



**Note:** This procedure covers upgrading from Apigee hybrid version 1.5.x to Apigee hybrid version 1.6.9 only. 

If you are upgrading from Apigee hybrid version 1.4 or older, you must first upgrade to hybrid version 1.5 before upgrading to version 1.6.9. See the instructions for [Upgrading Apigee hybrid to version 1.5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/upgrade). 

##  Upgrading to version 1.6.9 overview. 

Upgrading to Apigee hybrid version 1.6 may require downtime: 

  * When upgrading the Apigee controller to version 1.6.9, all Apigee deployments undergo a rolling restart. To minimize downtime in production hybrid environments during a rolling restart, make sure you are running at least two clusters (in the same or different region/data center). Divert all production traffic to a single cluster and take the cluster you are about to upgrade offline, and then proceed with the upgrade process. Repeat the process for each cluster.
  * If you are upgrading Anthos Service Mesh (ASM) to version 1.12.x, from a version prior to ASM version 1.9, you should expect a few seconds of downtime in the cluster you are upgrading when the ingress changes between the two versions.
  * If you change your certificate authority while upgrading ASM, you may experience downtime in your ingress gateway. See [Migrating to Mesh CA](https://docs.cloud.google.com/service-mesh/v1.10/docs/ca-migration) for more information.



The procedures for upgrading Apigee hybrid are organized in the following sections: 

  1. Backup your hybrid installation.
  2. Check your Kubernetes version and upgrade as appropriate.
  3. Install hybrid runtime version 1.6.9.
  4. Upgrade ASM.



##  Prerequisite 

These upgrade instructions assume you have Apigee hybrid 1.5 installed and wish to upgrade it to version 1.6.9. If you are updating from an earlier version see the instructions for [Upgrading Apigee hybrid to version 1.5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/upgrade).

##  Upgrade to version 1.6 

  1. These instructions use the environment variable `**$APIGEECTL_HOME**` for the directory in your file system where the `apigeectl` utility is installed. If needed, `cd` into your `apigeectl` directory and define the variable with the following command: 

###  Linux 
         
         export APIGEECTL_HOME=$PWD
         
         echo $APIGEECTL_HOME

###  Mac OS 
         
         export APIGEECTL_HOME=$PWD
         
         echo $APIGEECTL_HOME

###  Windows 
         
         set APIGEECTL_HOME=%CD%
         
         echo %APIGEECTL_HOME%

  2. (Recommended) Make a backup copy of your version 1.5 `$APIGEECTL_HOME/` directory. For example: 
         
         tar -czvf **$APIGEECTL_HOME** /../apigeectl-v1.5-backup.tar.gz **$APIGEECTL_HOME**

  3. (Recommended) Back up your Cassandra database following the instructions in [Cassandra backup and recovery](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/backup-recovery)
  4. Upgrade your Kubernetes platform to the versions supported by hybrid 1.6. Follow your platform's documentation if you need help. 

### _Click to expand a list of supported platforms_

| Apigee hybrid versions  
---|---  
  
### Platforms

| 1.5 | 1.6  
Anthos(3) (Google Cloud) | 1.18.x  
1.19.x | 1.19.x  
1.20.x  
1.21.x  
Anthos(3) (AWS) | 1.6.x  
1.7.x  
1.8.x(1) | 1.7.x  
1.8.x(1)  
1.9.3+  
1.10.x  
Anthos(3) (Azure) | N/A | 1.8.x  
Anthos(3) (on-premises - VMware) | 1.6.x  
1.7.x  
1.8.x(1) | 1.7.x  
1.8.x(1)  
1.9.3+  
1.10.x  
Anthos(3) (Bare Metal) | 1.6.x  
1.7.x | 1.7.x  
1.8.2+  
1.9.3+  
1.10.x  
Anthos(3) (attached clusters - multi-cloud)  
Kubernetes version (EKS) | 1.18.x  
1.19.x | 1.19.x  
1.20.x  
1.21.x  
Anthos(3) (attached clusters - multi-cloud)  
Kubernetes version (AKS) | 1.18.x  
1.19.x | 1.19.x  
1.20.x  
1.21.x  
Anthos(3) (attached clusters - multi-cloud)  
OpenShift version | 4.5  
4.6  
4.7 | 4.6  
4.7  
4.8  
Anthos(3) (attached clusters - multi-cloud)  
Konvoy version | 1.7.x | 1.7.x  
  
### Components

| 1.5 | 1.6  
Anthos Service Mesh (ASM)(2) | 1.7.x  
1.8.x  
1.9.x  
1.12.x _(for Apigee hybrid 1.5 starting with version 1.5.9)_ | 1.9.x  
1.10.x  
1.12.x _(Apigee hybrid version 1.6.6 and newer)_  
JDK | JDK 11 | JDK 11  
cert-manager | 1.2.0 | 1.2.0  
1.5.4  
Cassandra | 3.11.6 | 3.11.6  
**(1) On version 1.8.2 and above, follow the instructions in this document: [Conflict with cert-manager when upgrading to version 1.8.2 or above](https://cloud.google.com/anthos/clusters/docs/on-prem/1.8/known-issues#conflict_with_cert-manager_when_upgrading_to_version_182_or_above)**. **(2) Install only [ Supported versions](https://cloud.google.com/service-mesh/docs/supported-features#supported_versions) of ASM**. **(3) Install only [ Supported versions](https://cloud.google.com/anthos/docs/version-and-upgrade-support#anthos) of Anthos**.  
  5. If you are running a version of `cert-manager` prior to v1.5.4, you need to upgrade it to v1.5.4. 
     1. Check the current `cert-manager` version using the following command:
            
            kubectl -n cert-manager get deployment -o yaml | grep 'image:'
            

Something similar to the following is returned:
            
            image: quay.io/jetstack/cert-manager-controller:**v1.5.4**
            image: quay.io/jetstack/cert-manager-cainjector:**v1.5.4**
            image: quay.io/jetstack/cert-manager-webhook:**v1.5.4**

     2. Remove the deployments using the following command: 
            
            $ kubectl delete -n cert-manager deployment cert-manager cert-manager-cainjector cert-manager-webhook
            

     3. Upgrade `cert-manager` to v1.5.4 version using the following command: 
            
            $ kubectl apply -f https://github.com/jetstack/cert-manager/releases/download/v1.5.4/cert-manager.yaml
            

  6. Create the `apigee-runtime`service account required for use with Google OAUTH tokens. Use the `create-service-account` tool: 
     1. Create the service account: 
            
            ./tools/create-service-account --env prod --profile apigee-runtime

     2. Add the new service account to your Apigee `overrides.yaml` file: 
            
            envs:
             - name: "environment-name"
               … … …
               serviceAccountPaths:
                 runtime: "path-to-service-account-file"
               … … …

  7. Add the `udca.serviceAccountPath` property at the top level in your overrides file, in addition to the entry under `envs`. `udca` must appear in your overrides twice, once at the environment level and once at the organization level, parallel with `connectAgent`, `logger`, `mart`, `metrics`, and `watcher`. 

For example: 
         
         … … …
         
         metrics:
           serviceAccountPath: "metrics-service-account-file"
         
         **udca:
           serviceAccountPath: " udca-service-account-file"**
         
         watcher:
           serviceAccountPath: "watcher-service-account-file"
         … … …

  8. Optional: If plan to use [Cloud trace](https://docs.cloud.google.com/trace/docs/overview) ensure your `apigee-runtime` service account has the **Cloud Trace Agent** (`roles/cloudtrace.agent`) Google role. You can do so in the [Cloud console > IAM & Admin > Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) UI or with the following commands: 
     1. Get the email address for your `apigee-runtime` service account with the following command: 
            
            gcloud iam service-accounts list --filter "apigee-runtime"

If it matches the pattern `apigee-runtime@**$ORG_NAME**.iam.gserviceaccount.com`, you can use that pattern in the next step. 

     2. Assign the **Cloud Trace Agent** role to the service account: 
            
            gcloud projects add-iam-policy-binding $PROJECT_ID \
                --member="serviceAccount:apigee-runtime@$PROJECT_ID.iam.gserviceaccount.com" \
                --role="**roles/cloudtrace.agent** "

WWhere: $PROJECT_ID is the name of the Google Cloud project where Apigee hybrid is installed. 




##  Install the hybrid 1.6.9 runtime 

**Note:** Do not create new environments during the upgrade process.

  1. Be sure you are in the hybrid base directory (the parent of the directory where the `apigeectl` executable file is located): 
         
         cd **$APIGEECTL_HOME** /..

  2. Download the release package for your operating system using the following command. Be sure to select your platform in the following table:

###  Linux 

**Linux 64 bit:**
         
         curl -LO \
           https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**1.6.9** /apigeectl_linux_64.tar.gz

###  Mac OS 

**Mac 64 bit:**
         
         curl -LO \
           https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**1.6.9** /apigeectl_mac_64.tar.gz

###  Windows 

**Windows 64 bit:**
         
         curl -LO ^
           https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**1.6.9** /apigeectl_windows_64.zip

  3. Rename your current `apigeectl/` directory to a backup directory name. For example: 

###  Linux 
         
         mv **$APIGEECTL_HOME** / **$APIGEECTL_HOME** -v1.5/

###  Mac OS 
         
         mv **$APIGEECTL_HOME** / **$APIGEECTL_HOME** -v1.5/ 

###  Windows 
         
         rename %APIGEECTL_HOME% %APIGEECTL_HOME%-v1.5 

  4. Extract the downloaded gzip file contents into your hybrid base directory. The hybrid base directory is the directory where the renamed `apigeectl-v1.5` directory is located:

###  Linux 
         
         tar xvzf filename.tar.gz -C ./

###  Mac OS 
         
         tar xvzf filename.tar.gz -C ./

###  Windows 
         
         tar xvzf filename.zip -C ./

  5. The tar contents are, by default, expanded into a directory with the version and platform in its name. For example: `./apigeectl_1.6.9-d591b23_linux_64`. Rename that directory to `apigeectl` using the following command:

###  Linux 
         
         mv directory-name-linux apigeectl

###  Mac OS 
         
         mv directory-name-mac apigeectl

###  Windows 
         
         rename directory-name-windows apigeectl

  6. Change to the `apigeectl` directory: 
         
         cd ./apigeectl

The `apigeectl` executable is in this directory. 

  7. These instructions use the environment variable `**$APIGEECTL_HOME**` for the directory in your file system where the `apigeectl` utility is installed. If needed, `cd` into your `apigeectl` directory and define the variable with the following command: 

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
         
         Version: 1.6.9

  9. Move to the `hybrid-base-directory/hybrid-files` directory. The `hybrid-files` directory is where configuration files such as the overrides file, certs, and service accounts are located. For example: 
         
         cd **$APIGEECTL_HOME** /../hybrid-files

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

     3. Do a dry run initialization to check for errors: 
            
            **${APIGEECTL_HOME}** /apigeectl init -f ./overrides/OVERRIDES.yaml --dry-run=client

Where OVERRIDES is the name of your overrides file. 

     4. If there are no errors, initialize hybrid 1.6.9: 
            
            **${APIGEECTL_HOME}** /apigeectl init -f ./overrides/OVERRIDES.yaml

     5. Check the initialization status: 
            
            **${APIGEECTL_HOME}** /apigeectl check-ready -f ./overrides/OVERRIDES.yaml

     6. Check for errors with a dry run of the `apply` command: 
            
            **${APIGEECTL_HOME}** /apigeectl apply -f ./overrides/OVERRIDES.yaml --dry-run=client

     7. If there are no errors, apply your overrides. Select and follow the instructions for production environments or demo/experimental environments, depending on your installation. During the upgrade process each component will perform a rolling restart. Therefore, for production environments, it is best to apply the upgrade to one component at a time.

### Production

For production environments you should upgrade each hybrid component individually, and check the status of the upgraded component before proceeding to the next component. 

        1. Be sure you are in the `hybrid-files` directory.
        2. Apply your overrides to upgrade Cassandra: 
               
               **${APIGEECTL_HOME}** /apigeectl apply -f ./overrides/OVERRIDES.yaml --datastore

        3. Check completion: 
               
               **${APIGEECTL_HOME}** /apigeectl check-ready -f ./overrides/OVERRIDES.yaml

**Tip:** If `check-ready` fails, you can get more information about your pods with: 
               
               kubectl -n NAMESPACE get pods

Where NAMESPACE is your Apigee hybrid namespace. 

Proceed to the next step only when the pods are ready. 

        4. Apply your overrides to upgrade Telemetry components and check completion: 
               
               **${APIGEECTL_HOME}** /apigeectl apply -f ./overrides/OVERRIDES.yaml --telemetry
               
               **${APIGEECTL_HOME}** /apigeectl check-ready -f ./overrides/OVERRIDES.yaml

        5. Bring up Redis components: 
               
               **${APIGEECTL_HOME}** /apigeectl apply -f ./overrides/OVERRIDES.yaml --redis

        6. Apply your overrides to upgrade the org-level components (MART, Watcher and Apigee Connect) and check completion: 
               
               **${APIGEECTL_HOME}** /apigeectl apply -f ./overrides/OVERRIDES.yaml --org
               
               **${APIGEECTL_HOME}** /apigeectl check-ready -f ./overrides/OVERRIDES.yaml

        7. Apply your overrides to upgrade your environments. You have two choices: 
           * **Environment by environment** : Apply your overrides to one environment at a time and check completion. Repeat this step for each environment: 
                 
                 **${APIGEECTL_HOME}** /apigeectl apply -f ./overrides/OVERRIDES.yaml --env ENV_NAME
                 
                 **${APIGEECTL_HOME}** /apigeectl check-ready -f ./overrides/OVERRIDES.yaml

Where ENV_NAME is the name of the environment you are upgrading. 

           * **All environments at one time** : Apply your overrides to all environments at once and check completion: 
                 
                 **${APIGEECTL_HOME}** /apigeectl apply -f ./overrides/OVERRIDES.yaml --all-envs
                 
                 **${APIGEECTL_HOME}** /apigeectl check-ready -f ./overrides/OVERRIDES.yaml

### Demo/Experimental

In most demo or experimental environments, you can apply the overrides to all components at once. If your demo/experimental environment large and complex or closely mimics a production environment, you may want to use the instructions for upgrading production environments

        1. Be sure you are in the `hybrid-files` directory.
        2. **${APIGEECTL_HOME}** /apigeectl apply -f ./overrides/OVERRIDES.yaml

        3. Check the status: 
               
               **${APIGEECTL_HOME}** /apigeectl check-ready -f ./overrides/OVERRIDES.yaml




##  Upgrade ASM to version 1.31 

You may experience a brief interruption of incoming traffic (typically less than two seconds) when you upgrade ASM. If you are running hybrid in two or more clusters, you can avoid this interruption by upgrading one cluster at a time. Divert all production traffic away from the cluster you are about to upgrade, take the cluster offline, and then proceed with the upgrade process. Repeat the process for each cluster.

Perform the upgrade using the ASM documentation appropriate for your platform:

The instructions to install and configure ASM are different depending on your platform. The platforms are divided into the following categories: 

  * **GKE** : Google Kubernetes Engine clusters running on Google Cloud.
  * **Outside Google Cloud** : Anthos clusters running on: 
    * **Anthos clusters on VMware (GKE on-prem)**
    * **Anthos on bare metal**
    * **Anthos clusters on AWS**
    * **Amazon EKS**
  * **Other Kubernetes Platforms** : Conformant clusters created and running on: 
    * **AKS**
    * **EKS**
    * **OpenShift**



###  GKE 

The sequence for upgrading to ASM version 1.31.1 for your hybrid installation is as follows: 

  1. Prepare for the upgrade.
  2. Install the new version of ASM.
  3. Delete the previous ASM version's deployments, services, and webhooks from your current installation.
  4. Upgrade your gateways and configure the new webhooks.



To upgrade to ASM version 1.31.1 for hybrid on GKE: 

**Note:** You can upgrade directly from ASM version 1.10 or higher to ASM version 1.31.1. If you are running a version of ASM older than 1.10, you must first upgrade to version 1.10. Follow the instructions in [Upgrading from earlier versions](https://docs.cloud.google.com/service-mesh/v1.12/docs/upgrade-path-old-versions-gke)

  1. Review the requirements in [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.12/docs/unified-install/upgrade), but do not perform the upgrade yet.
  2. Before installing the new version, determine the current revision. You will need this information to delete the previous ASM version's deployments, services, and webhooks from your current installation. Use the following command to store the current istiod revision to an environment variable: 
         
         export DELETE_REV=$(kubectl get deploy -n istio-system -l app=istiod -o jsonpath={.items[].metadata.labels.'istio\.io\/rev'}'{"\n"}')
         echo ${DELETE_REV}

  3. Create a new `overlay.yaml` file or verify that your existing `overlay.yaml` contains the following contents: 
         
         apiVersion: install.istio.io/v1alpha1
         kind: IstioOperator
         spec:
           revision: asm-1305-8
           components:
             ingressGateways:
               - name: istio-ingressgateway
                 enabled: true
                 k8s:
                   nodeSelector:
                     # default node selector, if different or not using node selectors, change accordingly.
                     cloud.google.com/gke-nodepool: apigee-runtime
                   resources:
                     requests:
                       cpu: 1000m
                   service:
                     type: LoadBalancer
                     loadBalancerIP: STATIC_IP # If you do not have a reserved static IP, leave this out.
                     ports:
                       - name: http-status-port
                         port: 15021
                       - name: http2
                         port: 80
                         targetPort: 8080
                       - name: https
                         port: 443
                         targetPort: 8443
           meshConfig:
             accessLogFormat:
               '{"start_time":"%START_TIME%","remote_address":"%DOWNSTREAM_DIRECT_REMOTE_ADDRESS%","user_agent":"%REQ(USER-AGENT)%","host":"%REQ(:AUTHORITY)%","request":"%REQ(:METHOD)% %REQ(X-ENVOY-ORIGINAL-PATH?:PATH)% %PROTOCOL%","request_time":"%DURATION%","status":"%RESPONSE_CODE%","status_details":"%RESPONSE_CODE_DETAILS%","bytes_received":"%BYTES_RECEIVED%","bytes_sent":"%BYTES_SENT%","upstream_address":"%UPSTREAM_HOST%","upstream_response_flags":"%RESPONSE_FLAGS%","upstream_response_time":"%RESPONSE_DURATION%","upstream_service_time":"%RESP(X-ENVOY-UPSTREAM-SERVICE-TIME)%","upstream_cluster":"%UPSTREAM_CLUSTER%","x_forwarded_for":"%REQ(X-FORWARDED-FOR)%","request_method":"%REQ(:METHOD)%","request_path":"%REQ(X-ENVOY-ORIGINAL-PATH?:PATH)%","request_protocol":"%PROTOCOL%","tls_protocol":"%DOWNSTREAM_TLS_VERSION%","request_id":"%REQ(X-REQUEST-ID)%","sni_host":"%REQUESTED_SERVER_NAME%","apigee_dynamic_data":"%DYNAMIC_METADATA(envoy.lua)%"}'

  4. Follow the instructions in the following sections in the ASM documentation: **Important:** Make sure to follow the instructions to upgrade ASM with optional features, and to include your `overlay.yaml`. 
     1. [Download asmcli](https://docs.cloud.google.com/service-mesh/v1.12/docs/unified-install/install-dependent-tools#download_asmcli)
     2. [Grant cluster admin permissions](https://docs.cloud.google.com/service-mesh/v1.12/docs/unified-install/install-dependent-tools#grant_cluster_admin_permissions)
     3. [Validate project and cluster](https://docs.cloud.google.com/service-mesh/v1.12/docs/unified-install/install-dependent-tools#validate_project_and_cluster)
     4. [Upgrade with optional features](https://docs.cloud.google.com/service-mesh/v1.12/docs/unified-install/upgrade#upgrade_with_optional_features). Stop before starting the "Upgrade Gateways section"
  5. Delete the mutating webhook and validating webhook: 
     1. `cd` into the directory where you installed `asmcli`. 
     2. Store the current new revision in an environment variable to use in the script to delete the webhooks: 
            
            UPGRADE_REV="asm-1305-8"

     3. create a shell script containing the following commands: 
            
            #!/bin/bash
            
            set -ex
            
            PROJECT_ID="YOUR_PROJECT_ID"
            CLUSTER_NAME="YOUR_CLUSTER_NAME"
            CLUSTER_LOCATION="YOUR_CLUSTER_LOCATION"
            
            kubectl label namespace istio-system istio.io/rev=${UPGRADE_REV} istio-injection- --overwrite
            kubectl rollout restart deployment -n istio-system
            kubectl apply -n istio-system -f PATH_TO_INGRESSGATEWAYistio-ingressgateway
            kubectl apply -n istio-system -f PATH_TO_INGRESSGATEWAY/istio-ingressgateway-connectors
            
            if [[ "${DELETE_REV}" != "${UPGRADE_REV}" ]]; then
              kubectl apply -f out/asm/istio/istiod-service.yaml
              kubectl delete deploy -l app=istio-ingressgateway,istio.io/rev=${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete deploy -l app=istio-ingressgateway-connectors,istio.io/rev=${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete ValidatingWebhookConfiguration -l app=istiod,istio.io/rev=${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete MutatingWebhookConfiguration -l app=sidecar-injector,istio.io/rev=${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete Service,Deployment,HorizontalPodAutoscaler,PodDisruptionBudget istiod-${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete IstioOperator installed-state-${DELETE_REV} -n istio-system --ignore-not-found=true
            fi
            

     4. Execute the script to delete the current webhooks.
  6. Follow the steps in [Upgrade gateways](https://docs.cloud.google.com/service-mesh/v1.12/docs/unified-install/upgrade#upgrade_gateways) to create the new webhooks and switch traffic to the new gateways.



###  Outside Google Cloud 

These instructions cover upgrading ASM on: 

  * **Anthos clusters on VMware (GKE on-prem)**
  * **Anthos on bare metal**
  * **Anthos clusters on AWS**
  * **Amazon EKS**

**Note:** You can upgrade directly from ASM version 1.10 or higher to ASM version 1.31.1. If you are running an older version of ASM, you must first upgrade to version 1.10. Follow the instructions in [Upgrading from earlier versions](https://docs.cloud.google.com/service-mesh/v1.12/docs/upgrade-path-old-versions-on-prem)

The sequence for upgrading to ASM version 1.31.1 for your hybrid installation is as follows: 

  1. Prepare for the upgrade.
  2. Install the new version of ASM.
  3. Delete the mutating webhook and validating webhook from your current installation.
  4. Upgrade your gateways and configure the new webhooks.


  1. Review the requirements in [Upgrade Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/v1.12/docs/unified-install/upgrade), but do not perform the upgrade yet.
  2. Before installing the new version, determine the current revision. You will need this information to delete the _validating webhook_ and _mutating webhook_ from your current ASM installation. Use the following command to store the current istiod revision to an environment variable: 
         
         export DELETE_REV=$(kubectl get deploy -n istio-system -l app=istiod -o jsonpath={.items[].metadata.labels.'istio\.io\/rev'}'{"\n"}')
         echo ${DELETE_REV}

  3. Create a new `overlay.yaml` file or verify that your existing `overlay.yaml` contains the following contents: 
         
         apiVersion: install.istio.io/v1alpha1
         kind: IstioOperator
         spec:
           revision: asm-1305-8
           components:
             ingressGateways:
               - name: istio-ingressgateway
                 enabled: true
                 k8s:
                   nodeSelector:
                     # default node selector, if different or not using node selectors, change accordingly.
                     cloud.google.com/gke-nodepool: apigee-runtime
                   resources:
                     requests:
                       cpu: 1000m
                   service:
                     type: LoadBalancer
                     loadBalancerIP: STATIC_IP # If you do not have a reserved static IP, leave this out.
                     ports:
                       - name: http-status-port
                         port: 15021
                       - name: http2
                         port: 80
                         targetPort: 8080
                       - name: https
                         port: 443
                         targetPort: 8443
           values:
             gateways:
               istio-ingressgateway:
                 runAsRoot: true
         
           meshConfig:
             accessLogFormat:
               '{"start_time":"%START_TIME%","remote_address":"%DOWNSTREAM_DIRECT_REMOTE_ADDRESS%","user_agent":"%REQ(USER-AGENT)%","host":"%REQ(:AUTHORITY)%","request":"%REQ(:METHOD)% %REQ(X-ENVOY-ORIGINAL-PATH?:PATH)% %PROTOCOL%","request_time":"%DURATION%","status":"%RESPONSE_CODE%","status_details":"%RESPONSE_CODE_DETAILS%","bytes_received":"%BYTES_RECEIVED%","bytes_sent":"%BYTES_SENT%","upstream_address":"%UPSTREAM_HOST%","upstream_response_flags":"%RESPONSE_FLAGS%","upstream_response_time":"%RESPONSE_DURATION%","upstream_service_time":"%RESP(X-ENVOY-UPSTREAM-SERVICE-TIME)%","upstream_cluster":"%UPSTREAM_CLUSTER%","x_forwarded_for":"%REQ(X-FORWARDED-FOR)%","request_method":"%REQ(:METHOD)%","request_path":"%REQ(X-ENVOY-ORIGINAL-PATH?:PATH)%","request_protocol":"%PROTOCOL%","tls_protocol":"%DOWNSTREAM_TLS_VERSION%","request_id":"%REQ(X-REQUEST-ID)%","sni_host":"%REQUESTED_SERVER_NAME%","apigee_dynamic_data":"%DYNAMIC_METADATA(envoy.lua)%"}'

  4. Follow the instructions in the following sections in the ASM documentation: **Important:** Make sure to follow the instructions to upgrade ASM with optional features, and to include your `overlay.yaml`. 
     1. [Download asmcli](https://docs.cloud.google.com/service-mesh/v1.12/docs/unified-install/install-dependent-tools#download_asmcli)
     2. [Grant cluster admin permissions](https://docs.cloud.google.com/service-mesh/v1.12/docs/unified-install/install-dependent-tools#grant_cluster_admin_permissions)
     3. [Validate project and cluster](https://docs.cloud.google.com/service-mesh/v1.12/docs/unified-install/install-dependent-tools#validate_project_and_cluster)
     4. [Upgrade with optional features](https://docs.cloud.google.com/service-mesh/v1.12/docs/unified-install/upgrade#upgrade_with_optional_features). Stop before starting the "Upgrade Gateways section"
  5. Delete the mutating webhook and validating webhook: 
     1. `cd` into the directory where you installed `asmcli`. 
     2. Store the current new revision in an environment variable to use in the script to delete the webhooks: 
            
            UPGRADE_REV="asm-1305-8"

     3. create a shell script containing the following commands: 
            
            #!/bin/bash
            
            set -ex
            
            PROJECT_ID="YOUR_PROJECT_ID"
            CLUSTER_NAME="YOUR_CLUSTER_NAME"
            CLUSTER_LOCATION="YOUR_CLUSTER_LOCATION"
            
            
            gcloud config configurations activate ${PROJECT_ID}
            gcloud container clusters get-credentials ${CLUSTER_NAME} --region ${CLUSTER_LOCATION} --project ${PROJECT_ID}
            
            
            kubectl label namespace istio-system istio.io/rev=${UPGRADE_REV} istio-injection- --overwrite
            kubectl rollout restart deployment -n istio-system
            kubectl apply -n istio-system -f PATH_TO_INGRESSGATEWAYistio-ingressgateway
            kubectl apply -n istio-system -f PATH_TO_INGRESSGATEWAY/istio-ingressgateway-connectors
            
            if [[ "${DELETE_REV}" != "${UPGRADE_REV}" ]]; then
              kubectl apply -f out/asm/istio/istiod-service.yaml
              kubectl delete deploy -l app=istio-ingressgateway,istio.io/rev=${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete deploy -l app=istio-ingressgateway-connectors,istio.io/rev=${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete ValidatingWebhookConfiguration -l app=istiod,istio.io/rev=${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete MutatingWebhookConfiguration -l app=sidecar-injector,istio.io/rev=${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete Service,Deployment,HorizontalPodAutoscaler,PodDisruptionBudget istiod-${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete IstioOperator installed-state-${DELETE_REV} -n istio-system --ignore-not-found=true
            fi
            

     4. Execute the script to delete the current webhooks.
  6. Follow the steps in [Upgrade gateways](https://docs.cloud.google.com/service-mesh/v1.12/docs/unified-install/upgrade#upgrade_gateways) to create the new webhooks and switch traffic to the new gateways.



###  AKS / EKS 

In these instructions the process of upgrading Anthos Service Mesh (ASM) version istio-1.31.1-asm.16 on Anthos attached clusters is the same as performing a fresh install. 

###  Preparing to install Anthos Service Mesh 

  1. Delete the mutating webhook and validating webhook: 
     1. `cd` into the directory where you installed `asmcli`. 
     2. Store the current new revision in an environment variable to use in the script to delete the webhooks: 
            
            UPGRADE_REV="asm-1305-8"

     3. create a shell script containing the following commands: 
            
            #!/bin/bash
            
            set -ex
            
            kubectl label namespace istio-system istio.io/rev=${UPGRADE_REV} istio-injection- --overwrite
            kubectl rollout restart deployment -n istio-system
            
            if [[ "${DELETE_REV}" != "${UPGRADE_REV}" ]]; then
              kubectl apply -f out/asm/istio/istiod-service.yaml
              kubectl apply -f ASMCLI_OUTPUT_DIR/asm/istio/istiod-service.yaml ASMCLI_OUTPUT_DIR/istioctl tag set default --revision ${UPGRADE_REV}
            
            
              kubectl delete deploy -l app=istio-ingressgateway,istio.io/rev=${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete ValidatingWebhookConfiguration -l app=istiod,istio.io/rev=${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete MutatingWebhookConfiguration -l app=sidecar-injector,istio.io/rev=${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete Service,Deployment,HorizontalPodAutoscaler,PodDisruptionBudget istiod-${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete IstioOperator installed-state-${DELETE_REV} -n istio-system --ignore-not-found=true
            fi
            

     4. Execute the script to delete the current webhooks.

###  Linux 

  2. Download the Anthos Service Mesh installation file to your current working directory: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-linux-amd64.tar.gz

  3. Download the signature file and use openssl to verify the signature: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-linux-amd64.tar.gz.1.sig
         
         openssl dgst -verify /dev/stdin -signature istio-1.31.1-asm.16-linux-amd64.tar.gz.1.sig istio-1.31.1-asm.16.tar.gz <<'EOF'
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF

  4. Extract the contents of the file to any location on your file system. For example, to extract the contents to the current working directory: 
         
         tar xzf istio-1.31.1-asm.16-linux-amd64.tar.gz

The command creates an installation directory in your current working directory named `istio-1.31.1-asm.16` that contains: 

     * Sample applications in the `samples` directory.
     * The `istioctl` command-line tool that you use to install Anthos Service Mesh is in the `bin` directory.
     * The Anthos Service Mesh configuration profiles are in the `manifests/profiles` directory.
  5. Ensure that you're in the Anthos Service Mesh installation's root directory: 
         
         cd istio-1.31.1-asm.16

  6. For convenience, add the tools in the /bin directory to your PATH: 
         
         export PATH=$PWD/bin:$PATH

###  Mac OS 

  7. Download the Anthos Service Mesh installation file to your current working directory: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-osx.tar.gz

  8. Download the signature file and use openssl to verify the signature: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-osx.tar.gz.1.sig
         
         openssl dgst -sha256 -verify /dev/stdin -signature istio-1.31.1-asm.16-osx.tar.gz.1.sig istio-1.31.1-asm.16.tar.gz <<'EOF'
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF

  9. Extract the contents of the file to any location on your file system. For example, to extract the contents to the current working directory: 
         
         tar xzf istio-1.31.1-asm.16-osx.tar.gz

The command creates an installation directory in your current working directory named `istio-1.31.1-asm.16` that contains: 

     * Sample applications in the `samples` directory.
     * The `istioctl` command-line tool that you use to install Anthos Service Mesh is in the `bin` directory.
     * The Anthos Service Mesh configuration profiles are in the `manifests/profiles` directory.
  10. Ensure that you're in the Anthos Service Mesh installation's root directory: 
         
         cd istio-1.31.1-asm.16

  11. For convenience, add the tools in the /bin directory to your PATH: 
         
         export PATH=$PWD/bin:$PATH

###  Windows 

  12. Download the Anthos Service Mesh installation file to your current working directory: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-win.zip

  13. Download the signature file and use openssl to verify the signature: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-win.zip.1.sig
         
         openssl dgst -verify - -signature istio-1.31.1-asm.16-win.zip.1.sig istio-1.31.1-asm.16.win.zip <<'EOF'
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF

  14. Extract the contents of the file to any location on your file system. For example, to extract the contents to the current working directory: 
         
         tar xzf istio-1.31.1-asm.16-win.zip

The command creates an installation directory in your current working directory named `istio-1.31.1-asm.16` that contains: 

     * Sample applications in the `samples` directory.
     * The `istioctl` command-line tool that you use to install Anthos Service Mesh is in the `bin` directory.
     * The Anthos Service Mesh configuration profiles are in the `manifests\profiles` directory.
  15. Ensure that you're in the Anthos Service Mesh installation's root directory: 
         
         cd istio-1.31.1-asm.16

  16. For convenience, add the tools in the \bin directory to your PATH: 
         
         set PATH=%CD%\bin:%PATH%

  17. Now that ASM Istio is installed, check the version of `istioctl`: 
         
         istioctl version

  18. Create a namespace called istio-system for the control plane components: 
         
         kubectl create namespace istio-system




###  Installing Anthos Service Mesh 

  1. Edit your `overlay.yaml` file or create a new one with the following contents: 
         
         apiVersion: install.istio.io/v1alpha1
         kind: IstioOperator
         spec:
           meshConfig:
             accessLogFile: /dev/stdout
             enableTracing: true
             accessLogFormat:
               '{"start_time":"%START_TIME%","remote_address":"%DOWNSTREAM_DIRECT_REMOTE_ADDRESS%","user_agent":"%REQ(USER-AGENT)%","host":"%REQ(:AUTHORITY)%","request":"%REQ(:METHOD)% %REQ(X-ENVOY-ORIGINAL-PATH?:PATH)% %PROTOCOL%","request_time":"%DURATION%","status":"%RESPONSE_CODE%","status_details":"%RESPONSE_CODE_DETAILS%","bytes_received":"%BYTES_RECEIVED%","bytes_sent":"%BYTES_SENT%","upstream_address":"%UPSTREAM_HOST%","upstream_response_flags":"%RESPONSE_FLAGS%","upstream_response_time":"%RESPONSE_DURATION%","upstream_service_time":"%RESP(X-ENVOY-UPSTREAM-SERVICE-TIME)%","upstream_cluster":"%UPSTREAM_CLUSTER%","x_forwarded_for":"%REQ(X-FORWARDED-FOR)%","request_method":"%REQ(:METHOD)%","request_path":"%REQ(X-ENVOY-ORIGINAL-PATH?:PATH)%","request_protocol":"%PROTOCOL%","tls_protocol":"%DOWNSTREAM_TLS_VERSION%","request_id":"%REQ(X-REQUEST-ID)%","sni_host":"%REQUESTED_SERVER_NAME%","apigee_dynamic_data":"%DYNAMIC_METADATA(envoy.lua)%"}'
           components:
           - enabled: true
             name: istio-ingressgateway
             k8s:
               service:
                 type: LoadBalancer
                 ports:
                 - name: status-port
                   port: 15021
                   targetPort: 15021
                 - name: http2
                   port: 80
                   targetPort: 8080
                 - name: https
                   port: 443
                   targetPort: 8443
         

  2. Install Anthos Service Mesh with `istioctl` using the `asm-multicloud` profile: 
         
         istioctl install \
             --set profile=asm-multicloud \
             --set revision="asm-1305-8" \
             --filename overlayfile.yaml

Your output should look something like: 
         
         kubectl get pods -n istio-system
         NAME                                   READY   STATUS    RESTARTS   AGE
         istio-ingressgateway-88b6fd976-flgp2   1/1     Running   0          3m13s
         istio-ingressgateway-88b6fd976-p5dl9   1/1     Running   0          2m57s
         istiod-asm-1305-8-798ffb964-2ls88       1/1     Running   0          3m21s
         istiod-asm-1305-8-798ffb964-fnj8c       1/1     Running   1          3m21s

The `--set revision` argument adds a revision label in the format `istio.io/rev=asm-1305-8` to istiod. The revision label is used by the automatic sidecar injector webhook to associate injected sidecars with a particular istiod revision. To enable sidecar auto-injection for a namespace, you must label it with a revision that matches the label on istiod. 

  3. Verify that your install completed: 
         
         kubectl get svc -n istio-system

Your output should look something like: 
         
         NAME                   TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)                                                                      AGE
         istio-ingressgateway   LoadBalancer   172.200.48.52    34.74.177.168   15021:30479/TCP,80:30030/TCP,443:32200/TCP,15012:32297/TCP,15443:30244/TCP   3m35s
         istiod                 ClusterIP      172.200.18.133   <none>          15010/TCP,15012/TCP,443/TCP,15014/TCP                                        4m46s
         istiod-asm-1305-8       ClusterIP      172.200.63.220   <none>          15010/TCP,15012/TCP,443/TCP,15014/TCP                                        3m43s




###  OpenShift 

In these instructions the process of upgrading Anthos Service Mesh (ASM) version istio-1.31.1-asm.16 on Anthos attached clusters is the same as performing a fresh install. 

###  Preparing to install Anthos Service Mesh 

  1. Delete the mutating webhook and validating webhook: 
     1. `cd` into the directory where you installed `asmcli`. 
     2. Store the current new revision in an environment variable to use in the script to delete the webhooks: 
            
            UPGRADE_REV="asm-1305-8"

     3. create a shell script containing the following commands: 
            
            #!/bin/bash
            
            set -ex
            
            kubectl label namespace istio-system istio.io/rev=${UPGRADE_REV} istio-injection- --overwrite
            kubectl rollout restart deployment -n istio-system
            kubectl apply -n istio-system -f PATH_TO_INGRESSGATEWAYistio-ingressgateway
            
            if [[ "${DELETE_REV}" != "${UPGRADE_REV}" ]]; then
              kubectl apply -f out/asm/istio/istiod-service.yaml
              kubectl delete deploy -l app=istio-ingressgateway,istio.io/rev=${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete deploy -l app=istio-ingressgateway-connectors,istio.io/rev=${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete ValidatingWebhookConfiguration -l app=istiod,istio.io/rev=${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete MutatingWebhookConfiguration -l app=sidecar-injector,istio.io/rev=${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete Service,Deployment,HorizontalPodAutoscaler,PodDisruptionBudget istiod-${DELETE_REV} -n istio-system --ignore-not-found=true
              kubectl delete IstioOperator installed-state-${DELETE_REV} -n istio-system --ignore-not-found=true
            fi
            

     4. Execute the script to delete the current webhooks.

###  Linux 

  2. Grant the `anyuid` security context constraint (SCC) to the istio-system with the following OpenShift CLI (`oc`) command: 
         
         oc adm policy add-scc-to-group anyuid system:serviceaccounts:istio-system

  3. Download the Anthos Service Mesh installation file to your current working directory: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-linux-amd64.tar.gz

  4. Download the signature file and use openssl to verify the signature: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-linux-amd64.tar.gz.1.sig
         
         openssl dgst -verify /dev/stdin -signature istio-1.31.1-asm.16-linux-amd64.tar.gz.1.sig istio-1.31.1-asm.16.tar.gz <<'EOF'
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF

  5. Extract the contents of the file to any location on your file system. For example, to extract the contents to the current working directory: 
         
         tar xzf istio-1.31.1-asm.16-linux-amd64.tar.gz

The command creates an installation directory in your current working directory named `istio-1.31.1-asm.16` that contains: 

     * Sample applications in the `samples` directory.
     * The `istioctl` command-line tool that you use to install Anthos Service Mesh is in the `bin` directory.
     * The Anthos Service Mesh configuration profiles are in the `manifests/profiles` directory.
  6. Ensure that you're in the Anthos Service Mesh installation's root directory: 
         
         cd istio-1.31.1-asm.16

  7. For convenience, add the tools in the /bin directory to your PATH: 
         
         export PATH=$PWD/bin:$PATH

###  Mac OS 

  8. Grant the `anyuid` security context constraint (SCC) to the istio-system with the following OpenShift CLI (`oc`) command: 
         
         oc adm policy add-scc-to-group anyuid system:serviceaccounts:istio-system

  9. Download the Anthos Service Mesh installation file to your current working directory: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-osx.tar.gz

  10. Download the signature file and use openssl to verify the signature: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-osx.tar.gz.1.sig
         
         openssl dgst -sha256 -verify /dev/stdin -signature istio-1.31.1-asm.16-osx.tar.gz.1.sig istio-1.31.1-asm.16.tar.gz <<'EOF'
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF

  11. Extract the contents of the file to any location on your file system. For example, to extract the contents to the current working directory: 
         
         tar xzf istio-1.31.1-asm.16-osx.tar.gz

The command creates an installation directory in your current working directory named `istio-1.31.1-asm.16` that contains: 

     * Sample applications in the `samples` directory.
     * The `istioctl` command-line tool that you use to install Anthos Service Mesh is in the `bin` directory.
     * The Anthos Service Mesh configuration profiles are in the `manifests/profiles` directory.
  12. Ensure that you're in the Anthos Service Mesh installation's root directory: 
         
         cd istio-1.31.1-asm.16

  13. For convenience, add the tools in the /bin directory to your PATH: 
         
         export PATH=$PWD/bin:$PATH

###  Windows 

  14. Grant the `anyuid` security context constraint (SCC) to the istio-system with the following OpenShift CLI (`oc`) command: 
         
         oc adm policy add-scc-to-group anyuid system:serviceaccounts:istio-system

  15. Download the Anthos Service Mesh installation file to your current working directory: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-win.zip

  16. Download the signature file and use openssl to verify the signature: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-win.zip.1.sig
         
         openssl dgst -verify - -signature istio-1.31.1-asm.16-win.zip.1.sig istio-1.31.1-asm.16.win.zip <<'EOF'
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF

  17. Extract the contents of the file to any location on your file system. For example, to extract the contents to the current working directory: 
         
         tar xzf istio-1.31.1-asm.16-win.zip

The command creates an installation directory in your current working directory named `istio-1.31.1-asm.16` that contains: 

     * Sample applications in the `samples` directory.
     * The `istioctl` command-line tool that you use to install Anthos Service Mesh is in the `bin` directory.
     * The Anthos Service Mesh configuration profiles are in the `manifests\profiles` directory.
  18. Ensure that you're in the Anthos Service Mesh installation's root directory: 
         
         cd istio-1.31.1-asm.16

  19. For convenience, add the tools in the \bin directory to your PATH: 
         
         set PATH=%CD%\bin:%PATH%

  20. Now that ASM Istio is installed, check the version of `istioctl`: 
         
         istioctl version

  21. Create a namespace called istio-system for the control plane components: 
         
         kubectl create namespace istio-system




###  Installing Anthos Service Mesh 

  1. Edit your `overlay.yaml` file or create a new one with the following contents: 
         
         apiVersion: install.istio.io/v1alpha1
         kind: IstioOperator
         spec:
           meshConfig:
             accessLogFile: /dev/stdout
             enableTracing: true
             accessLogFormat:
               '{"start_time":"%START_TIME%","remote_address":"%DOWNSTREAM_DIRECT_REMOTE_ADDRESS%","user_agent":"%REQ(USER-AGENT)%","host":"%REQ(:AUTHORITY)%","request":"%REQ(:METHOD)% %REQ(X-ENVOY-ORIGINAL-PATH?:PATH)% %PROTOCOL%","request_time":"%DURATION%","status":"%RESPONSE_CODE%","status_details":"%RESPONSE_CODE_DETAILS%","bytes_received":"%BYTES_RECEIVED%","bytes_sent":"%BYTES_SENT%","upstream_address":"%UPSTREAM_HOST%","upstream_response_flags":"%RESPONSE_FLAGS%","upstream_response_time":"%RESPONSE_DURATION%","upstream_service_time":"%RESP(X-ENVOY-UPSTREAM-SERVICE-TIME)%","upstream_cluster":"%UPSTREAM_CLUSTER%","x_forwarded_for":"%REQ(X-FORWARDED-FOR)%","request_method":"%REQ(:METHOD)%","request_path":"%REQ(X-ENVOY-ORIGINAL-PATH?:PATH)%","request_protocol":"%PROTOCOL%","tls_protocol":"%DOWNSTREAM_TLS_VERSION%","request_id":"%REQ(X-REQUEST-ID)%","sni_host":"%REQUESTED_SERVER_NAME%","apigee_dynamic_data":"%DYNAMIC_METADATA(envoy.lua)%"}'
           components:
           - enabled: true
             name: istio-ingressgateway
             k8s:
               service:
                 type: LoadBalancer
                 ports:
                 - name: status-port
                   port: 15021
                   targetPort: 15021
                 - name: http2
                   port: 80
                   targetPort: 8080
                 - name: https
                   port: 443
                   targetPort: 8443
         

  2. Install Anthos Service Mesh with `istioctl` using the `asm-multicloud` profile: 
         
         istioctl install \
             --set profile=asm-multicloud \
             --set revision="asm-1305-8" \
             --filename overlayfile.yaml

Your output should look something like: 
         
         kubectl get pods -n istio-system
         NAME                                   READY   STATUS    RESTARTS   AGE
         istio-ingressgateway-88b6fd976-flgp2   1/1     Running   0          3m13s
         istio-ingressgateway-88b6fd976-p5dl9   1/1     Running   0          2m57s
         istiod-asm-1305-8-798ffb964-2ls88       1/1     Running   0          3m21s
         istiod-asm-1305-8-798ffb964-fnj8c       1/1     Running   1          3m21s

The `--set revision` argument adds a revision label in the format `istio.io/rev=1.6.11-asm.1` to istiod. The revision label is used by the automatic sidecar injector webhook to associate injected sidecars with a particular istiod revision. To enable sidecar auto-injection for a namespace, you must label it with a revision that matches the label on istiod. 

  3. Verify that your install completed: 
         
         kubectl get svc -n istio-system

Your output should look something like: 
         
         NAME                   TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)                                                                      AGE
         istio-ingressgateway   LoadBalancer   172.200.48.52    34.74.177.168   15021:30479/TCP,80:30030/TCP,443:32200/TCP,15012:32297/TCP,15443:30244/TCP   3m35s
         istiod                 ClusterIP      172.200.18.133   <none>          15010/TCP,15012/TCP,443/TCP,15014/TCP                                        4m46s
         istiod-asm-1305-8       ClusterIP      172.200.63.220   <none>          15010/TCP,15012/TCP,443/TCP,15014/TCP                                        3m43s


**Congratulations!** You have successfully upgraded to Apigee hybrid version 1.6.9. 

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

  4. In the root directory of the installation you want to roll back to, run `**${APIGEECTL_HOME}** /apigeectl apply`, check the status of your pods, and then run `**${APIGEECTL_HOME}** /apigeectl init`. Be sure to use the original overrides file for the version you wish to roll back to: 
     1. In the `hybrid-files` directory, run `**${APIGEECTL_HOME}** /apigeectl apply`: 
            
            **${ APIGEECTL_HOME}**/apigeectl apply -f ./overrides/ORIGINAL_OVERRIDES.yaml

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

Proceed to the next step only when the `apigeeds` ßpod is running. 

     4. Run `apigeectl init`: 
            
            **${ APIGEECTL_HOME}**/apigeectl init -f ./overrides/ORIGINAL_OVERRIDES.yaml




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
