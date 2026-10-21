---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-cert-manager/
title: Step 2: Install cert-manager \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:11:37.773561+00:00
---

# Step 2: Install cert-manager  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-cert-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 2: Install cert-manager Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-cert-manager.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-cert-manager.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-cert-manager.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-cert-manager.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-cert-manager.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-cert-manager.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-cert-manager.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-cert-manager.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-cert-manager.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-cert-manager.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-cert-manager.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-cert-manager.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-cert-manager.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-cert-manager.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-cert-manager.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-cert-manager.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-cert-manager.html)



This step explains how to download and install [cert-manager](https://cert-manager.io/docs/), required for Apigee hybrid to operate. 

**Installations on Anthos**

You do not need to install cert-manager if you are performing a fresh installation on one of the following Anthos platforms: 

  * Anthos on-premises - (VMware)
  * Anthos on Bare Metal



Anthos comes with its own version of cert-manager. Apigee can use this Anthos version of cert-manager. If it is installed in a namespace other than `cert-manager`, you will need to include the namespace with the [`certManager.namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref#certmanager) property in your overrides file. For more information about Anthos and cert-manager, see [Conflicting cert-manager installation](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/known-issues#conflicting-cert-manager-installation). 

**Installations on OpenShift**

If you are installing Apigee hybrid on OpenShift, install cert-manager by following the instructions in [Installation](https://cert-manager.io/docs/installation/) in the cert-manager documentation.

See a [Known Issue about cert-manager version 1.10 on OpenShift](https://cloud.google.com/apigee/docs/release/known-issues#271689008).

##  Install cert-manager 

  1. Use the following command to install cert-manager v1.11.0 from GitHub. 
         
         kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/v1.11.0/cert-manager.yaml

You should see a response that the cert-manager namespace and several cert-manager resources have been created. For example: 
         
         customresourcedefinition.apiextensions.k8s.io/certificaterequests.cert-manager.io configured
         customresourcedefinition.apiextensions.k8s.io/certificates.cert-manager.io configured
         ...
         mutatingwebhookconfiguration.admissionregistration.k8s.io/cert-manager-webhook configured
         validatingwebhookconfiguration.admissionregistration.k8s.io/cert-manager-webhook configured
         

  2. Use the following command to verify the successful creation of cert-manager namespace and its corresponding components: 
         
         kubectl get all -n cert-manager -o wide

Your output should be similar to the following example. You should see pods for `cert-manager`, `cert-manager-cainjector`, and `cert-manager-webhook`. 
         
         NAME                                         READY    STATUS   RESTARTS   AGE     IP           NODE                                    NOMINATED NODE   READINESS GATES
           pod/cert-manager-abcd1234-7hkt9               1/1     Running   0          35s   10.20.x.x    gke-hybrid-on-apigee-data-abcd1234-3d54   
           pod/cert-manager-cainjector-abcd1234-6lb4k    1/1     Running   0          35s   10.20.x.x    gke-hybrid-apigee-runtime-abcd1234-5hmn   
           pod/cert-manager-webhook-abcd1234-c8bg9       1/1     Running   0          35s   10.20.x.x    gke-hybrid-apigee-runtime-abcd1234-fk39   
            
           NAME                           TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE   SELECTOR
           service/cert-manager           ClusterIP   10.24.x.x              9402/TCP   35s   app.kubernetes.io/component=controller,app.kubernetes.io/instance=cert-manager,app.kubernetes.io/name=cert-manager
           service/cert-manager-webhook   ClusterIP   10.24.x.x              443/TCP    35s   app.kubernetes.io/component=webhook,app.kubernetes.io/instance=cert-manager,app.kubernetes.io/name=webhook
             
           NAME                                      READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS                IMAGES                                             SELECTOR
           deployment.apps/cert-manager              1/1     1            1           35s   cert-manager-controller   quay.io/jetstack/cert-manager-controller:v1.11.0   app.kubernetes.io/component=controller,app.kubernetes.io/instance=cert-manager,app.kubernetes.io/name=cert-manager
           deployment.apps/cert-manager-cainjector   1/1     1            1           35s   cert-manager-cainjector   quay.io/jetstack/cert-manager-cainjector:v1.11.0   app.kubernetes.io/component=cainjector,app.kubernetes.io/instance=cert-manager,app.kubernetes.io/name=cainjector
           deployment.apps/cert-manager-webhook      1/1     1            1           35s   cert-manager-webhook      quay.io/jetstack/cert-manager-webhook:v1.11.0      app.kubernetes.io/component=webhook,app.kubernetes.io/instance=cert-manager,app.kubernetes.io/name=webhook
             
           NAME                                                DESIRED   CURRENT   READY   AGE   CONTAINERS                IMAGES                                             SELECTOR
           replicaset.apps/cert-manager-abcd1234                1         1         1       35s   cert-manager-controller   quay.io/jetstack/cert-manager-controller:v1.11.0   app.kubernetes.io/component=controller,app.kubernetes.io/instance=cert-manager,app.kubernetes.io/name=cert-manager,pod-template-hash=abcd1234
           replicaset.apps/cert-manager-cainjector-abcd1234     1         1         1       35s   cert-manager-cainjector   quay.io/jetstack/cert-manager-cainjector:v1.11.0   app.kubernetes.io/component=cainjector,app.kubernetes.io/instance=cert-manager,app.kubernetes.io/name=cainjector,pod-template-hash=abcd1234
           replicaset.apps/cert-manager-webhook-abcd1234        1         1         1       35s   cert-manager-webhook      quay.io/jetstack/cert-manager-webhook:v1.11.0      app.kubernetes.io/component=webhook,app.kubernetes.io/instance=cert-manager,app.kubernetes.io/name=webhook,pod-template-hash=abcd1234




##  Summary 

You now have cert-manager installed, and you are ready to install the Apigee hybrid command-line tool on your local machine. 

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-cert-manager) [(NEXT) Step 3: Install apigeectl](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-apigeectl) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-service-accounts) [5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-create-tls-certificates) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-configure-cluster) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-enable-synchronizer-access) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-check-cluster) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-hybrid-runtime) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-expose-apigee-ingress) [11](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-deploy-proxy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
