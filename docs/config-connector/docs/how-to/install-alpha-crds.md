---
url: https://docs.cloud.google.com/config-connector/docs/how-to/install-alpha-crds/
title: Installing Config Connector v1alpha1 CRDs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:37.715237+00:00
---

# Installing Config Connector v1alpha1 CRDs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/how-to/install-alpha-crds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Installing Config Connector v1alpha1 CRDs

This topic explains how to install v1alpha1 Google Cloud resource [Custom Resource Definitions](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) (CRDs) in Config Connector.

**Warning:** Config Connector v1alpha1 Google Cloud resource CRDs should not be used in production. When Config Connector is upgraded, the v1alpha1 CRDs must be manually upgraded to ensure they continue to work. You must manually install, upgrade, and uninstall the v1alpha1 CRDs, as they are not managed by the Config Connector operator or the Config Connector add-on.

## Before you begin

  1. Ensure Config Connector is [installed manually](https://docs.cloud.google.com/config-connector/docs/how-to/install-manually) or through the [GKE add-on](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall).

  2. Check your Config Connector version and ensure it is 1.103.0 and above. You can check the Config Connector version by connecting to the cluster where Config Connector is installed and running the following command:
         
         kubectl get ns cnrm-system -o jsonpath='{.metadata.annotations.cnrm\.cloud\.google\.com/version}'
         




## Installing the v1alpha1 CRDs

  1. Clone the [GitHub repository](https://github.com/GoogleCloudPlatform/k8s-config-connector):
         
         git clone https://github.com/GoogleCloudPlatform/k8s-config-connector
         

You can also browse the CRD manifests in the [`config/crds/resources`](https://github.com/GoogleCloudPlatform/k8s-config-connector/tree/master/config/crds/resources) directory on GitHub.

  2. `git checkout` to your Config Connector version:
         
         cd k8s-config-connector
         echo 'v'$(kubectl get ns cnrm-system -o jsonpath='{.metadata.annotations.cnrm\.cloud\.google\.com/version}') | xargs git checkout
         

  3. Install the v1alpha1 CRDs:
         
         cd config/crds/resources
         

     1. If you want to install a specific v1alpha1 CRD, run the following command:
            
            kubectl apply -f CRD_FILENAME
            

Replace `CRD_FILENAME` with the filename of the v1alpha1 CRD you want to install.

     2. If you want to install all the v1alpha1 CRDs, run the following command:
            
            kubectl apply $(grep -l "cnrm.cloud.google.com/stability-level: alpha" *.yaml | awk ' { print " -f " $1 } ')
            




The v1alpha1 CRDs are successfully installed when the `kubectl apply` command successfully completes.

## Upgrading the v1alpha1 CRDs

**Warning:** The v1alpha1 CRDs need to be upgraded after your Config Connector version is upgraded to ensure the existing CRs of the v1alpha1 CRDs still work.**Warning:** Downgrading the v1alpha1 CRDs is not supported.

  1. Ensure Config Connector version is upgraded before you upgrade the v1alpha1 CRDs.

  2. `git checkout` to your Config Connector version at your local Config Connector repository:
         
         echo 'v'$(kubectl get ns cnrm-system -o jsonpath='{.metadata.annotations.cnrm\.cloud\.google\.com/version}') | xargs git checkout
         

  3. Upgrade the v1alpha1 CRDs:
         
         cd config/crds/resources
         

     1. If you want to upgrade a specific v1alpha1 CRD, run the following command:
            
            kubectl apply -f CRD_FILENAME
            

Replace `CRD_FILENAME` with the filename of the v1alpha1 CRD you want to upgrade.

     2. If you want to upgrade all the v1alpha1 CRDs, run the following command:
            
            kubectl apply $(grep -l "cnrm.cloud.google.com/stability-level: alpha" *.yaml | awk ' { print " -f " $1 } ')
            




The v1alpha1 CRDs are successfully upgraded when the `kubectl apply` command successfully completes.

## Uninstalling the v1alpha1 CRDs

  1. [Delete the CRs](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources) for v1alpha1 CRDs if you no longer need the underlying Google Cloud resources. Otherwise, skip this step.

**Note:** The CRs are [abandoned](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources#keeping_resources_after_deletion) when the v1alpha1 CRDs are uninstalled. The corresponding Google Cloud resources will still exist.
  2. Check out to your Config Connector version at your local Config Connector repository:
         
         echo 'v'$(kubectl get ns cnrm-system -o jsonpath='{.metadata.annotations.cnrm\.cloud\.google\.com/version}') | xargs git checkout
         

  3. Uninstall the v1alpha1 CRDs:
         
         cd config/crds/resources
         kubectl delete $(grep -l "cnrm.cloud.google.com/stability-level: alpha" *.yaml | awk ' { print " -f " $1 } ')
         




The v1alpha1 CRDs are successfully uninstalled if the `kubectl delete` command successfully completes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
