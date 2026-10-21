---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/upgrade/
title: Upgrading Apigee hybrid to version 1.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:57:13.792572+00:00
---

# Upgrading Apigee hybrid to version 1.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Upgrading Apigee hybrid to version 1.5 Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.5 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.5 (unsupported)keyboard_arrow_down

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



**Note:** This procedure covers upgrading from Apigee hybrid version 1.4.x to Apigee hybrid version 1.5.10 only. 

If you are upgrading from Apigee hybrid version 1.3 or older, you must first upgrade to hybrid version 1.4 before upgrading to version 1.5.10. See the instructions for [Upgrading Apigee hybrid to version 1.4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/upgrade). 

##  Upgrading to version 1.5.10 overview. 

Upgrading to Apigee hybrid version 1.5.10 may require downtime: 

  * When upgrading the Apigee controller to version 1.5.10, all Apigee deployments undergo a rolling restart. To minimize downtime in production hybrid environments during a rolling restart, make sure you are running at least two clusters (in the same or different region/data center). Divert all production traffic to a single cluster and take the cluster you are about to upgrade offline, and then proceed with the upgrade process. Repeat the process for each cluster.
  * If you are upgrading Anthos Service Mesh (ASM) to version 1.12.x, from a version prior to ASM version 1.9, you should expect a few seconds of downtime in the cluster you are upgrading when the ingress changes between the two versions.
  * If you change your certificate authority while upgrading ASM, you may experience downtime in your ingress gateway. See [Migrating to Mesh CA](https://docs.cloud.google.com/service-mesh/v1.10/docs/ca-migration) for more information.



The procedures for upgrading Apigee hybrid are organized in the following sections: 

  1. Backup your hybrid installation.
  2. Check your Kubernetes version and upgrade as appropriate.
  3. Upgrade ASM.
  4. Install hybrid runtime version 1.5.



##  Prerequisite 

  * Apigee hybrid version 1.4. If you are updating from an earlier version see the instructions for [Upgrading Apigee hybrid to version 1.4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/upgrade).



##  Upgrade to version 1.5 

  1. These instructions use the environment variable APIGEECTL_HOME for the directory in your file system where you have installed `apigeectl`. If needed, `cd` into your `apigeectl` directory and define the variable with the following command: 

###  Linux 
         
         export APIGEECTL_HOME=$PWD
         
         echo $APIGEECTL_HOME

###  Mac OS 
         
         export APIGEECTL_HOME=$PWD
         
         echo $APIGEECTL_HOME

###  Windows 
         
         set APIGEECTL_HOME=%CD%
         
         echo %APIGEECTL_HOME%

  2. (Recommended) Make a backup copy of your version 1.4 `$APIGEECTL_HOME/` directory. For example: 
         
         tar -czvf $APIGEECTL_HOME/../apigeectl-v1.4-backup.tar.gz $APIGEECTL_HOME

  3. (Recommended) Backup your Cassandra database following the instructions in [Cassandra backup and recovery](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/backup-recovery)
  4. Upgrade your Kubernetes platform to the versions supported by hybrid 1.5. Follow your platform's documentation if you need help. 

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
  5. If you are running a version of `cert-manager` prior to v1.2.0, you need to upgrade it to v1.2.0. 
     1. Check the current `cert-manager` version using the following command:
            
            kubectl -n cert-manager get deployment -o yaml | grep 'image:'
            

Something similar to the following is returned:
            
            image: quay.io/jetstack/cert-manager-controller:**v1.2.0**
            image: quay.io/jetstack/cert-manager-cainjector:**v1.2.0**
            image: quay.io/jetstack/cert-manager-webhook:**v1.2.0**

     2. Remove the deployments using the following command: 
            
            kubectl delete -n cert-manager deployment cert-manager cert-manager-cainjector cert-manager-webhook
            

     3. Upgrade `cert-manager` to v1.2.0 version using the following command: 
            
            kubectl apply -f https://github.com/jetstack/cert-manager/releases/download/v1.2.0/cert-manager.yaml
            




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

The sequence for upgrading to ASM version 1.8._x_ for your hybrid installation is as follows: 

  1. Prepare for the upgrade.
  2. Install the new version of ASM.
  3. Delete the previous ASM version's deployments, services, and webhooks from your current installation.
  4. Upgrade your gateways and configure the new webhooks.



To upgrade to ASM version 1.8._x_ for hybrid on GKE: 

**Note:** You can upgrade directly from ASM version 1.10 or higher to ASM version 1.8._x_. If you are running a version of ASM older than 1.10, you must first upgrade to version 1.10. Follow the instructions in [Upgrading from earlier versions](https://docs.cloud.google.com/service-mesh/v1.12/docs/upgrade-path-old-versions-gke)

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

**Note:** You can upgrade directly from ASM version 1.10 or higher to ASM version 1.8._x_. If you are running an older version of ASM, you must first upgrade to version 1.10. Follow the instructions in [Upgrading from earlier versions](https://docs.cloud.google.com/service-mesh/v1.12/docs/upgrade-path-old-versions-on-prem)

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

###  Linux 

  1. Download the Anthos Service Mesh installation file to your current working directory: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-linux-amd64.tar.gz

  2. Download the signature file and use openssl to verify the signature: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-linux-amd64.tar.gz.1.sig
         
         openssl dgst -verify /dev/stdin -signature istio-1.31.1-asm.16-linux-amd64.tar.gz.1.sig istio-1.31.1-asm.16.tar.gz <<'EOF'
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF

  3. Extract the contents of the file to any location on your file system. For example, to extract the contents to the current working directory: 
         
         tar xzf istio-1.31.1-asm.16-linux-amd64.tar.gz

The command creates an installation directory in your current working directory named `istio-1.31.1-asm.16` that contains: 

     * Sample applications in the `samples` directory.
     * The `istioctl` command-line tool that you use to install Anthos Service Mesh is in the `bin` directory.
     * The Anthos Service Mesh configuration profiles are in the `manifests/profiles` directory.
  4. Ensure that you're in the Anthos Service Mesh installation's root directory: 
         
         cd istio-1.31.1-asm.16

  5. For convenience, add the tools in the /bin directory to your PATH: 
         
         export PATH=$PWD/bin:$PATH

###  Mac OS 

  6. Download the Anthos Service Mesh installation file to your current working directory: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-osx.tar.gz

  7. Download the signature file and use openssl to verify the signature: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-osx.tar.gz.1.sig
         
         openssl dgst -sha256 -verify /dev/stdin -signature istio-1.31.1-asm.16-osx.tar.gz.1.sig istio-1.31.1-asm.16.tar.gz <<'EOF'
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF

  8. Extract the contents of the file to any location on your file system. For example, to extract the contents to the current working directory: 
         
         tar xzf istio-1.31.1-asm.16-osx.tar.gz

The command creates an installation directory in your current working directory named `istio-1.31.1-asm.16` that contains: 

     * Sample applications in the `samples` directory.
     * The `istioctl` command-line tool that you use to install Anthos Service Mesh is in the `bin` directory.
     * The Anthos Service Mesh configuration profiles are in the `manifests/profiles` directory.
  9. Ensure that you're in the Anthos Service Mesh installation's root directory: 
         
         cd istio-1.31.1-asm.16

  10. For convenience, add the tools in the /bin directory to your PATH: 
         
         export PATH=$PWD/bin:$PATH

###  Windows 

  11. Download the Anthos Service Mesh installation file to your current working directory: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-win.zip

  12. Download the signature file and use openssl to verify the signature: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-win.zip.1.sig
         
         openssl dgst -verify - -signature istio-1.31.1-asm.16-win.zip.1.sig istio-1.31.1-asm.16.win.zip <<'EOF'
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF

  13. Extract the contents of the file to any location on your file system. For example, to extract the contents to the current working directory: 
         
         tar xzf istio-1.31.1-asm.16-win.zip

The command creates an installation directory in your current working directory named `istio-1.31.1-asm.16` that contains: 

     * Sample applications in the `samples` directory.
     * The `istioctl` command-line tool that you use to install Anthos Service Mesh is in the `bin` directory.
     * The Anthos Service Mesh configuration profiles are in the `manifests\profiles` directory.
  14. Ensure that you're in the Anthos Service Mesh installation's root directory: 
         
         cd istio-1.31.1-asm.16

  15. For convenience, add the tools in the \bin directory to your PATH: 
         
         set PATH=%CD%\bin:%PATH%

  16. Now that ASM Istio is installed, check the version of `istioctl`: 
         
         istioctl version

  17. Create a namespace called istio-system for the control plane components: 
         
         kubectl create namespace istio-system




###  Configure the validating webhook 

When you install Anthos Service Mesh, you set a revision label on istiod. You need to set the same revision on the validating webhook. 

  1. Create a file called `istiod-service.yaml` with the following contents: 
         
         apiVersion: v1
         kind: Service
         metadata:
           name: istiod
           namespace: istio-system
           labels:
             istio.io/rev: asm-1305-8
             app: istiod
             istio: pilot
             release: istio
         spec:
           ports:
             - port: 15010
               name: grpc-xds # plaintext
               protocol: TCP
             - port: 15012
               name: https-dns # mTLS with k8s-signed cert
               protocol: TCP
             - port: 443
               name: https-webhook # validation and injection
               targetPort: 15017
               protocol: TCP
             - port: 15014
               name: http-monitoring # prometheus stats
               protocol: TCP
           selector:
             app: istiod
             istio.io/rev: asm-1305-8
           meshConfig:
             accessLogFormat:
               '{"start_time":"%START_TIME%","remote_address":"%DOWNSTREAM_DIRECT_REMOTE_ADDRESS%","user_agent":"%REQ(USER-AGENT)%","host":"%REQ(:AUTHORITY)%","request":"%REQ(:METHOD)% %REQ(X-ENVOY-ORIGINAL-PATH?:PATH)% %PROTOCOL%","request_time":"%DURATION%","status":"%RESPONSE_CODE%","status_details":"%RESPONSE_CODE_DETAILS%","bytes_received":"%BYTES_RECEIVED%","bytes_sent":"%BYTES_SENT%","upstream_address":"%UPSTREAM_HOST%","upstream_response_flags":"%RESPONSE_FLAGS%","upstream_response_time":"%RESPONSE_DURATION%","upstream_service_time":"%RESP(X-ENVOY-UPSTREAM-SERVICE-TIME)%","upstream_cluster":"%UPSTREAM_CLUSTER%","x_forwarded_for":"%REQ(X-FORWARDED-FOR)%","request_method":"%REQ(:METHOD)%","request_path":"%REQ(X-ENVOY-ORIGINAL-PATH?:PATH)%","request_protocol":"%PROTOCOL%","tls_protocol":"%DOWNSTREAM_TLS_VERSION%","request_id":"%REQ(X-REQUEST-ID)%","sni_host":"%REQUESTED_SERVER_NAME%","apigee_dynamic_data":"%DYNAMIC_METADATA(envoy.lua)%"}'

  2. Use `kubectl` to apply the validating webhook configuration: 
         
         kubectl apply -f istiod-service.yaml

  3. Verify that the configuration was applied: 
         
         kubectl get svc -n istio-system

The response should look similar to: 
         
         NAME     TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                                 AGE
         istiod   ClusterIP   172.200.18.133   <none>        15010/TCP,15012/TCP,443/TCP,15014/TCP   22s




###  Installing Anthos Service Mesh 

  1. Install Anthos Service Mesh with `istioctl` using the `asm-multicloud` profile: 
         
         istioctl install \
             --set profile=asm-multicloud \
             --set revision="asm-1305-8"

Your output should look something like: 
         
         kubectl get pods -n istio-system
         NAME                                   READY   STATUS    RESTARTS   AGE
         istio-ingressgateway-88b6fd976-flgp2   1/1     Running   0          3m13s
         istio-ingressgateway-88b6fd976-p5dl9   1/1     Running   0          2m57s
         istiod-asm-1305-8-798ffb964-2ls88       1/1     Running   0          3m21s
         istiod-asm-1305-8-798ffb964-fnj8c       1/1     Running   1          3m21s

The `--set revision` argument adds a revision label in the format `istio.io/rev=asm-1305-8` to istiod. The revision label is used by the automatic sidecar injector webhook to associate injected sidecars with a particular istiod revision. To enable sidecar auto-injection for a namespace, you must label it with a revision that matches the label on istiod. 

  2. Verify that your install completed: 
         
         kubectl get svc -n istio-system

Your output should look something like: 
         
         NAME                   TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)                                                                      AGE
         istio-ingressgateway   LoadBalancer   172.200.48.52    34.74.177.168   15021:30479/TCP,80:30030/TCP,443:32200/TCP,15012:32297/TCP,15443:30244/TCP   3m35s
         istiod                 ClusterIP      172.200.18.133   <none>          15010/TCP,15012/TCP,443/TCP,15014/TCP                                        4m46s
         istiod-asm-1305-8       ClusterIP      172.200.63.220   <none>          15010/TCP,15012/TCP,443/TCP,15014/TCP                                        3m43s




###  OpenShift 

In these instructions the process of upgrading Anthos Service Mesh (ASM) version istio-1.31.1-asm.16 on Anthos attached clusters is the same as performing a fresh install. 

###  Preparing to install Anthos Service Mesh 

###  Linux 

  1. Grant the `anyuid` security context constraint (SCC) to the istio-system with the following OpenShift CLI (`oc`) command: 
         
         oc adm policy add-scc-to-group anyuid system:serviceaccounts:istio-system

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

  7. Grant the `anyuid` security context constraint (SCC) to the istio-system with the following OpenShift CLI (`oc`) command: 
         
         oc adm policy add-scc-to-group anyuid system:serviceaccounts:istio-system

  8. Download the Anthos Service Mesh installation file to your current working directory: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-osx.tar.gz

  9. Download the signature file and use openssl to verify the signature: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-osx.tar.gz.1.sig
         
         openssl dgst -sha256 -verify /dev/stdin -signature istio-1.31.1-asm.16-osx.tar.gz.1.sig istio-1.31.1-asm.16.tar.gz <<'EOF'
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF

  10. Extract the contents of the file to any location on your file system. For example, to extract the contents to the current working directory: 
         
         tar xzf istio-1.31.1-asm.16-osx.tar.gz

The command creates an installation directory in your current working directory named `istio-1.31.1-asm.16` that contains: 

     * Sample applications in the `samples` directory.
     * The `istioctl` command-line tool that you use to install Anthos Service Mesh is in the `bin` directory.
     * The Anthos Service Mesh configuration profiles are in the `manifests/profiles` directory.
  11. Ensure that you're in the Anthos Service Mesh installation's root directory: 
         
         cd istio-1.31.1-asm.16

  12. For convenience, add the tools in the /bin directory to your PATH: 
         
         export PATH=$PWD/bin:$PATH

###  Windows 

  13. Grant the `anyuid` security context constraint (SCC) to the istio-system with the following OpenShift CLI (`oc`) command: 
         
         oc adm policy add-scc-to-group anyuid system:serviceaccounts:istio-system

  14. Download the Anthos Service Mesh installation file to your current working directory: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-win.zip

  15. Download the signature file and use openssl to verify the signature: 
         
         curl -LO https://storage.googleapis.com/gke-release/asm/istio-1.31.1-asm.16-win.zip.1.sig
         
         openssl dgst -verify - -signature istio-1.31.1-asm.16-win.zip.1.sig istio-1.31.1-asm.16.win.zip <<'EOF'
         -----BEGIN PUBLIC KEY-----
         MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWZrGCUaJJr1H8a36sG4UUoXvlXvZ
         wQfk16sxprI2gOJ2vFFggdq3ixF2h4qNBt0kI7ciDhgpwS8t+/960IsIgw==
         -----END PUBLIC KEY-----
         EOF

  16. Extract the contents of the file to any location on your file system. For example, to extract the contents to the current working directory: 
         
         tar xzf istio-1.31.1-asm.16-win.zip

The command creates an installation directory in your current working directory named `istio-1.31.1-asm.16` that contains: 

     * Sample applications in the `samples` directory.
     * The `istioctl` command-line tool that you use to install Anthos Service Mesh is in the `bin` directory.
     * The Anthos Service Mesh configuration profiles are in the `manifests\profiles` directory.
  17. Ensure that you're in the Anthos Service Mesh installation's root directory: 
         
         cd istio-1.31.1-asm.16

  18. For convenience, add the tools in the \bin directory to your PATH: 
         
         set PATH=%CD%\bin:%PATH%

  19. Now that ASM Istio is installed, check the version of `istioctl`: 
         
         istioctl version

  20. Create a namespace called istio-system for the control plane components: 
         
         kubectl create namespace istio-system




###  Configure the validating webhook 

When you install Anthos Service Mesh, you set a revision label on istiod. You need to set the same revision on the validating webhook. 

  1. Create a file called `istiod-service.yaml` with the following contents: 
         
         apiVersion: v1
         kind: Service
         metadata:
           name: istiod
           namespace: istio-system
           labels:
             istio.io/rev: asm-1305-8
             app: istiod
             istio: pilot
             release: istio
         spec:
           ports:
             - port: 15010
               name: grpc-xds # plaintext
               protocol: TCP
             - port: 15012
               name: https-dns # mTLS with k8s-signed cert
               protocol: TCP
             - port: 443
               name: https-webhook # validation and injection
               targetPort: 15017
               protocol: TCP
             - port: 15014
               name: http-monitoring # prometheus stats
               protocol: TCP
           selector:
             app: istiod
             istio.io/rev: asm-1305-8
           meshConfig:
             accessLogFormat:
               '{"start_time":"%START_TIME%","remote_address":"%DOWNSTREAM_DIRECT_REMOTE_ADDRESS%","user_agent":"%REQ(USER-AGENT)%","host":"%REQ(:AUTHORITY)%","request":"%REQ(:METHOD)% %REQ(X-ENVOY-ORIGINAL-PATH?:PATH)% %PROTOCOL%","request_time":"%DURATION%","status":"%RESPONSE_CODE%","status_details":"%RESPONSE_CODE_DETAILS%","bytes_received":"%BYTES_RECEIVED%","bytes_sent":"%BYTES_SENT%","upstream_address":"%UPSTREAM_HOST%","upstream_response_flags":"%RESPONSE_FLAGS%","upstream_response_time":"%RESPONSE_DURATION%","upstream_service_time":"%RESP(X-ENVOY-UPSTREAM-SERVICE-TIME)%","upstream_cluster":"%UPSTREAM_CLUSTER%","x_forwarded_for":"%REQ(X-FORWARDED-FOR)%","request_method":"%REQ(:METHOD)%","request_path":"%REQ(X-ENVOY-ORIGINAL-PATH?:PATH)%","request_protocol":"%PROTOCOL%","tls_protocol":"%DOWNSTREAM_TLS_VERSION%","request_id":"%REQ(X-REQUEST-ID)%","sni_host":"%REQUESTED_SERVER_NAME%","apigee_dynamic_data":"%DYNAMIC_METADATA(envoy.lua)%"}'

  2. Use `kubectl` to apply the validating webhook configuration: 
         
         kubectl apply -f istiod-service.yaml

  3. Verify that the configuration was applied: 
         
         kubectl get svc -n istio-system

The response should look similar to: 
         
         NAME     TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                                 AGE
         istiod   ClusterIP   172.200.18.133   <none>        15010/TCP,15012/TCP,443/TCP,15014/TCP   22s




###  Installing Anthos Service Mesh 

  1. Install Anthos Service Mesh with `istioctl` using the `asm-multicloud` profile: 
         
         istioctl install \
             --set profile=asm-multicloud \
             --set revision=istio-1.31.1-asm.16

Your output should look something like: 
         
         kubectl get pods -n istio-system
         NAME                                   READY   STATUS    RESTARTS   AGE
         istio-ingressgateway-88b6fd976-flgp2   1/1     Running   0          3m13s
         istio-ingressgateway-88b6fd976-p5dl9   1/1     Running   0          2m57s
         istiod-asm-1305-8-798ffb964-2ls88       1/1     Running   0          3m21s
         istiod-asm-1305-8-798ffb964-fnj8c       1/1     Running   1          3m21s

The `--set revision` argument adds a revision label in the format `istio.io/rev=1.8.6-asm.1` to istiod. The revision label is used by the automatic sidecar injector webhook to associate injected sidecars with a particular istiod revision. To enable sidecar auto-injection for a namespace, you must label it with a revision that matches the label on istiod. 

  2. Verify that your install completed: 
         
         kubectl get svc -n istio-system

Your output should look something like: 
         
         NAME                   TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)                                                                      AGE
         istio-ingressgateway   LoadBalancer   172.200.48.52    34.74.177.168   15021:30479/TCP,80:30030/TCP,443:32200/TCP,15012:32297/TCP,15443:30244/TCP   3m35s
         istiod                 ClusterIP      172.200.18.133   <none>          15010/TCP,15012/TCP,443/TCP,15014/TCP                                        4m46s
         istiod-asm-1305-8       ClusterIP      172.200.63.220   <none>          15010/TCP,15012/TCP,443/TCP,15014/TCP                                        3m43s




##  Install the hybrid 1.5.10 runtime 

**Note:** Do not create new environments during the upgrade process. This can lead to an error state that is difficult to diagnose.

  1. Download the release package for your operating system:

**Mac 64 bit:**
         
         curl -LO \
             https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**1.5.10** /apigeectl_mac_64.tar.gz

**Linux 64 bit:**
         
         curl -LO \
             https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**1.5.10** /apigeectl_linux_64.tar.gz

**Mac 32 bit:**
         
         curl -LO \
             https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**1.5.10** /apigeectl_mac_32.tar.gz

**Linux 32 bit:**
         
         curl -LO \
             https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**1.5.10** /apigeectl_linux_32.tar.gz

  2. Rename your current `apigeectl/` directory to a backup directory name. For example: 
         
         mv $APIGEECTL_HOME/ $APIGEECTL_HOME-v1.2/ 

  3. Extract the downloaded gzip file contents into your hybrid base directory. For example: 
         
         tar xvzf FILENAME.tar.gz -C HYBRID_BASE_DIRECTORY

  4. `cd` to the base directory.
  5. The tar contents are, by default, expanded into a directory with the version and platform in its name. For example: `./apigeectl_1.5.0-d591b23_linux_64`. Rename that directory to `apigeectl`:
         
         mv apigeectl_1.5.0-d591b23_linux_64 apigeectl

  6. In the **new** `apigeectl/` directory, run `apigeectl init`, `apigeectl apply`, and `apigeectl check-ready`: 
     1. Initialize hybrid 1.5.10: 
            
            apigeectl init -f OVERRIDES.yaml

Where OVERRIDES`.yaml` is your edited `overrides.yaml` file. 

     2. Check that it initialized correctly with the following commands: 
            
            apigeectl check-ready -f OVERRIDES.yaml
            
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
            

     3. The syntax of the `apigeectl` `--dry-run` flag depends on the version of `kubectl` you are running. Check the version of `kubectl`: 
            
            gcloud version

     4. Check for errors with a dry run with the command appropriate to your version of `kubectl`: 

`kubectl` version 1.17 and older: 
            
            apigeectl apply -f OVERRIDES.yaml --dry-run=true

`kubectl` version 1.18 and newer: 
            
            apigeectl apply -f OVERRIDES.yaml --dry-run=client

     5. Apply your overrides. Select and follow the instructions for production environments or demo/experimental environments, depending on your installation. During the upgrade process each component will perform a rolling restart. Therefore, for production environments, it is best to apply the upgrade to one component at a time.

### Production

For production environments you should upgrade each hybrid component individually, and check the status of the upgraded component before proceeding to the next component. 

        1. Apply your overrides to upgrade Cassandra: 
               
               apigeectl apply -f OVERRIDES.yaml --datastore

        2. Check completion: 
               
               apigeectl check-ready -f OVERRIDES.yaml

**Tip:** If `check-ready` fails, you can get more information about your pods with: 
               
               kubectl -n NAMESPACE get pods

Where NAMESPACE is your Apigee hybrid namespace. 

Proceed to the next step only when the pods are ready. 

        3. Apply your overrides to upgrade Telemetry components and check completion: 
               
               apigeectl apply -f OVERRIDES.yaml --telemetry
               
               apigeectl check-ready -f OVERRIDES.yaml

        4. Bring up Redis components: **Note:** Redis support is new with hybrid v1.5. 
               
               apigeectl apply -f OVERRIDES.yaml --redis

        5. Apply your overrides to upgrade the org-level components (MART, Watcher and Apigee Connect) and check completion: 
               
               apigeectl apply -f OVERRIDES.yaml --org
               
               apigeectl check-ready -f OVERRIDES.yaml

        6. Apply your overrides to upgrade your environments. You have two choices: 
           * **Environment by environment** : Apply your overrides to one environment at a time and check completion. Repeat this step for each environment: 
                 
                 apigeectl apply -f OVERRIDES.yaml --env ENV_NAME
                 
                 apigeectl check-ready -f OVERRIDES.yaml

Where ENV_NAME is the name of the environment you are upgrading. 

           * **All environments at one time** : Apply your overrides to all environments at once and check completion: 
                 
                 apigeectl apply -f OVERRIDES.yaml --all-envs
                 
                 apigeectl check-ready -f OVERRIDES.yaml

### Demo/Experimental

In most demo or experimental environments, you can apply the overrides to all components at once. If your demo/experimental environment large and complex or closely mimics a production environment, you may want to use the instructions for upgrading production environments

        1. apigeectl apply -f OVERRIDES.yaml

        2. Check the status: 
               
               apigeectl check-ready -f OVERRIDES.yaml


**Congratulations!** You have successfully upgraded to Apigee hybrid version 1.5.10. 

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

  4. In the root directory of the installation you want to roll back to, run `apigeectl apply`, check the status of your pods, delete the Redis component (new in hybrid v1.5.0), and then run `apigeectl init`. Be sure to use the original overrides file for the version you wish to roll back to: 
     * Run `apigeectl apply`: 
           
           $APIGEECTL_HOME/apigeectl apply -f overrides/ORIGINAL_OVERRIDES.yaml

     * Check the status of your pods: 
           
           kubectl -n NAMESPACE get pods

Where NAMESPACE is your Apigee hybrid namespace. 

Proceed to the next step only when the `apigeeds`pod is running. 

     * Since Redis is a new component in hybrid v1.5, run the following command to delete it:
           
           apigeectl_1.5.0 delete --redis -f ORIGINAL_OVERRIDES.yaml

     * Run `apigeectl init`: 
           
           $APIGEECTL_HOME/apigeectl init -f overrides/ORIGINAL_OVERRIDES.yaml
           




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
