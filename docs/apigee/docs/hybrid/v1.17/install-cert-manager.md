---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-cert-manager/
title: Step 9: Install cert-manager \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:07.219307+00:00
---

# Step 9: Install cert-manager  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-cert-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 9: Install cert-manager Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

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

**Installations on Google Distributed Cloud**

You do not need to install cert-manager if you are performing a fresh installation on one of the following on-premises platforms: 

  * Google Distributed Cloud (software only) on VMware
  * Google Distributed Cloud (software only) on bare metal



Google Distributed Cloud comes with its own version of cert-manager. Apigee can use this Distributed Cloud version of cert-manager. If it is installed in a namespace other than `cert-manager`, you will need to include the namespace with the [`certManager.namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#certmanager) property in your overrides file. For more information about Google Distributed Cloud and cert-manager, see [Conflicting cert-manager installation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues#conflicting-cert-manager-installation). 

**Installations on OpenShift**

If you are installing Apigee hybrid on OpenShift, install cert-manager by following the instructions in [Installation](https://cert-manager.io/docs/installation/) in the cert-manager documentation.

See a [Known Issue about cert-manager version 1.10 on OpenShift](https://cloud.google.com/apigee/docs/release/known-issues#271689008). 

**Issues with Older Versions**

Some versions of cert-manager have an issue where the webhook TLS server may fail to automatically renew its CA certificate. To avoid this, Apigee recommends using cert-manager versions [1.16.3](https://cert-manager.io/docs/releases/release-notes/release-notes-1.16/#v1163)\+ or [1.17.2](https://cert-manager.io/docs/releases/release-notes/release-notes-1.17/#v1172)+. 

##  Install cert-manager 

  1. Use the following command to install cert-manager v1.19.2 from GitHub. 
         
         kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.19.2/cert-manager.yaml

You should see a response that the cert-manager namespace and several cert-manager resources have been created. For example: 
         
         customresourcedefinition.apiextensions.k8s.io/certificaterequests.cert-manager.io configured
         customresourcedefinition.apiextensions.k8s.io/certificates.cert-manager.io configured
         ...
         mutatingwebhookconfiguration.admissionregistration.k8s.io/cert-manager-webhook configured
         validatingwebhookconfiguration.admissionregistration.k8s.io/cert-manager-webhook configured
         

  2. Use the following command to verify the successful creation of cert-manager namespace and its corresponding components: 
         
         kubectl get all -n cert-manager -o wide

Your output should be similar to the following example. You should see pods for `cert-manager`, `cert-manager-cainjector`, and `cert-manager-webhook`. 
         
         NAME                                          READY   STATUS    RESTARTS   AGE   IP           NODE                                                  NOMINATED NODE   READINESS GATES
             pod/cert-manager-675d667c9-8rrdf              1/1     Running   0          13s   x.x.x.x      gke-test-apigee-apigee-runtime-fbff3412-fsz9          none             none
             pod/cert-manager-cainjector-6674494d8-lfr5r   1/1     Running   0          13s   x.x.x.x      gke-test-apigee-hy-apigee-data-efb302e2-1gqg          none             none
             pod/cert-manager-webhook-8566bcbc98-5krnh     1/1     Running   0          12s   x.x.x.x      gke-test-apigee-hy-apigee-data-0081cb07-2t5v          none             none
         
             NAME                           TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE   SELECTOR
             service/cert-manager           ClusterIP   x.x.x.x            none        9402/TCP   13s   app.kubernetes.io/component=controller,app.kubernetes.io/instance=cert-manager,app.kubernetes.io/name=cert-manager
             service/cert-manager-webhook   ClusterIP   x.x.x.x            none        443/TCP    13s   app.kubernetes.io/component=webhook,app.kubernetes.io/instance=cert-manager,app.kubernetes.io/name=webhook
         
             NAME                                      READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS                IMAGES                                             SELECTOR
             deployment.apps/cert-manager              1/1     1            1           13s   cert-manager-controller   quay.io/jetstack/cert-manager-controller:v1.15.1   app.kubernetes.io/component=controller,app.kubernetes.io/instance=cert-manager,app.kubernetes.io/name=cert-manager
             deployment.apps/cert-manager-cainjector   1/1     1            1           13s   cert-manager-cainjector   quay.io/jetstack/cert-manager-cainjector:v1.15.1   app.kubernetes.io/component=cainjector,app.kubernetes.io/instance=cert-manager,app.kubernetes.io/name=cainjector
             deployment.apps/cert-manager-webhook      1/1     1            1           13s   cert-manager-webhook      quay.io/jetstack/cert-manager-webhook:v1.15.1      app.kubernetes.io/component=webhook,app.kubernetes.io/instance=cert-manager,app.kubernetes.io/name=webhook
         
             NAME                                                DESIRED   CURRENT   READY   AGE   CONTAINERS                IMAGES                                             SELECTOR
             replicaset.apps/cert-manager-675d667c9              1         1         1       13s   cert-manager-controller   quay.io/jetstack/cert-manager-controller:v1.15.1   app.kubernetes.io/component=controller,app.kubernetes.io/instance=cert-manager,app.kubernetes.io/name=cert-manager,pod-template-hash=675d667c9
             replicaset.apps/cert-manager-cainjector-6674494d8   1         1         1       13s   cert-manager-cainjector   quay.io/jetstack/cert-manager-cainjector:v1.15.1   app.kubernetes.io/component=cainjector,app.kubernetes.io/instance=cert-manager,app.kubernetes.io/name=cainjector,pod-template-hash=6674494d8
             replicaset.apps/cert-manager-webhook-8566bcbc98     1         1         1       12s   cert-manager-webhook      quay.io/jetstack/cert-manager-webhook:v1.15.1      app.kubernetes.io/component=webhook,app.kubernetes.io/instance=cert-manager,app.kubernetes.io/name=webhook,pod-template-hash=8566bcbc98




For more information about installing cert-manager, see [kubectl apply](https://cert-manager.io/docs/installation/kubectl/) in the cert-manager installation documentation.

##  Summary 

You now have cert-manager installed, and you are ready to install the Apigee hybrid custom resource definitions (CRDs). 

## Next step

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-download-charts) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-namespace) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-service-accounts) [5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-sa-authentication) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-tls-certificates) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-overrides) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-enable-control-plane-access) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-cert-manager) [(NEXT) Step 10: Install the CRDs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-crds) [11](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-helm-charts)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
