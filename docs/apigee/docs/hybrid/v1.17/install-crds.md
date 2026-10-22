---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-crds/
title: Step 10: Install the Apigee hybrid CRDs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:47.850124+00:00
---

# Step 10: Install the Apigee hybrid CRDs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-crds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 10: Install the Apigee hybrid CRDs Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-crds.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-crds.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-crds.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-crds.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-crds.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-crds.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-crds.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-crds.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-crds.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-crds.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-crds.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-crds.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-crds.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-crds.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-crds.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-crds.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-crds.html)



This step explains how to install the Custom Resource Definitions (CRDs) for Apigee hybrid.

## Install the Apigee CRDs:

**Note:** From this step onwards, all commands should be run from `$APIGEE_HELM_CHARTS_HOME` directory. **Note:** This is the only supported method for installing Apigee CRDs. Do not use `kubectl apply` without `-k`, do not omit `--server-side`. **Note:** This step requires elevated cluster permissions. 

  1. If you are installing Apigee Hybrid into a different namespace than the default (`apigee`), edit `apigee-operator/etc/crds/default/kustomization.yaml` and change the namespace to match: 
         
         namespace: APIGEE_NAMESPACE

For example: 
         
         namespace: my-namespace

  2. Perform a dry-run of the installation by running the following command:
         
         kubectl apply -k  apigee-operator/etc/crds/default/ \
           --server-side \
           --force-conflicts \
           --validate=false \
           --dry-run=server
         

  3. After checking the installation with `--dry-run`, install the Apigee CRDs with the following command:
         
         kubectl apply -k  apigee-operator/etc/crds/default/ \
           --server-side \
           --force-conflicts \
           --validate=false
         

  4. Validate the installation with the `kubectl get crds` command: 
         
         kubectl get crds | grep apigee

Your output should look something like the following:
         
         apigeedatastores.apigee.cloud.google.com            2024-12-16T19:44:48Z
         apigeedeployments.apigee.cloud.google.com           2024-12-16T19:44:49Z
         apigeeenvironments.apigee.cloud.google.com          2024-12-16T19:44:50Z
         apigeeissues.apigee.cloud.google.com                2024-12-16T19:44:52Z
         apigeeorganizations.apigee.cloud.google.com         2024-12-16T19:44:53Z
         apigeeredis.apigee.cloud.google.com                 2024-12-16T19:44:55Z
         apigeerouteconfigs.apigee.cloud.google.com          2024-12-16T19:44:56Z
         apigeeroutes.apigee.cloud.google.com                2024-12-16T19:44:56Z
         apigeetelemetries.apigee.cloud.google.com           2024-12-16T19:44:58Z
         cassandradatareplications.apigee.cloud.google.com   2024-12-16T19:45:00Z
         secretrotations.apigee.cloud.google.com             2024-12-16T19:45:00Z


**Note:** You may see warnings about deprecated terms. This will not impact the installation of the Apigee hybrid CRDs.

You have now installed the structure for Apigee hybrid. Next you will check the readiness of your Kubernetes cluster before installing the Apigee Helm charts. 

## Next step

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-download-charts) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-namespace) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-service-accounts) [5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-sa-authentication) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-tls-certificates) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-overrides) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-enable-control-plane-access) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-cert-manager) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-crds) [(NEXT) Step 11: Install Apigee hybrid using Helm charts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-helm-charts)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
