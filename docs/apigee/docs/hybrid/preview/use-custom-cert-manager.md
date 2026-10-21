---
url: https://docs.cloud.google.com/apigee/docs/hybrid/preview/use-custom-cert-manager/
title: Use a custom cert-manager \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:01:32.171861+00:00
---

# Use a custom cert-manager  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/preview/use-custom-cert-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)



Send feedback 

#  Use a custom cert-manager Stay organized with collections  Save and categorize content based on your preferences. 

| 

### Private GA: Use a custom cert-manager with Apigee hybrid

This feature is offered as a private GA for Apigee hybrid version 1.13.  
---|---  
  
This feature gives you the option to install a custom cert-manager for Apigee hybrid with a modified role based access control (RBAC)-related configuration using restrictive permissions.

**Note:** Apigee only provides a Helm chart for this process to be consistent with Apigee hybrid installation. 

## Before you begin

**Caution** : Due to the restrictive RBAC enforcement, make sure to only install this cert-manager in a namespace where you intend to install hybrid workloads. 

This feature is only available in Private GA when using it with Apigee hybrid versions 1.13 and higher.

Before proceeding with the installation steps, download the Helm chart using the following commands: 
    
    
    export CHART_REPO=oci://us-docker.pkg.dev/apigee-release/apigee-hybrid-helm-charts
    export CERT_MANAGER_VERSION=v1.14.5
    helm pull $CHART_REPO/apigee-cert-manager --version $CERT_MANAGER_VERSION --untar

## Setting up the custom cert-manager

Setting up a custom cert-manager requires the following steps:

  1. Fresh installation of a custom cert-manager
  2. Upgrade to the custom cert-manager



### Fresh installation of a custom cert-manager

To perform a fresh installation of a custom cert-manager for use with Apigee hybrid, complete the following steps: 

  1. Install the CRDs using `kubectl` with the following commands: 
         
         export CERT_MANAGER_VERSION=v1.14.5
         kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/${CERT_MANAGER_VERSION}/cert-manager.crds.yaml
         

  2. Install the cert-manager component using the Helm chart. 
         
         helm install CERT_MANAGER_RELEASE_NAME apigee-cert-manager/ \
           --namespace APIGEE_NAMESPACE

Subsequently, when the new version of chart is available, you can upgrade it with `helm upgrade`:
         
         helm upgrade CERT_MANAGER_RELEASE_NAME apigee-cert-manager/ \
           --namespace APIGEE_NAMESPACE




### Upgrade to the custom cert-manager

To migrate from an existing non-custom cert-manager to a custom version, use the following steps. Only one cert-manager can run in the cluster at a given time. 

  1. Disable existing webhooks and update the deployment to have 0 replicas for a seamless migration: 
         
         kubectl delete validatingwebhookconfiguration cert-manager-webhook
           kubectl delete mutatingwebhookconfiguration cert-manager-webhook
         
             # set the replicas to 0
         
           kubectl scale deployment cert-manager -n cert-manager --replicas=0
           kubectl scale deployment cert-manager-cainjector -n cert-manager --replicas=0
           kubectl scale deployment cert-manager-webhook -n cert-manager --replicas=0

  2. Install the CRDs: 
         
         kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/${CERT_MANAGER_VERION}/cert-manager.crds.yaml

  3. Install the custom cert-manager: 
         
         helm install CERT_MANAGER_RELEASE_NAME apigee-cert-manager/ \
           --namespace APIGEE_NAMESPACE

  4. Once the installation completes, you can delete the previously installed cert-manager. **Note:** Do not delete the CRDs during the clean up step.



## Installing or upgrading Apigee hybrid with a custom cert-manager

Installing or upgrading hybrid with a custom cert-manager requires the following changes to the installation or upgrade procedures.

### Changes to Apigee hybrid installation

When installing Apigee hybrid v1.13 or higher with a custom cert-cert manager, make the following change in your `overrides.yaml` file **before** installing the Apigee hybrid components in [Step 10: Install Apigee hybrid Using Helm](https://docs.cloud.google.com/apigee/docs/hybrid/latest/install-helm-charts).

Update your `overrides.yaml` file to notify the operator where to find the cert-manager related resources and enable the operator to use the custom cert-manager's Issuer. 
    
    
    certManager:
      namespace: APIGEE_NAMESPACE
    
    ao:
      certManagerCAIssuerEnabled: true
    

### Changes to the Apigee hybrid upgrade process

When upgrading Apigee hybrid to v1.13 or higher with a custom cert-cert manager, make the following changes **after** the steps in [Prepare for the Helm charts upgrade](https://docs.cloud.google.com/apigee/docs/hybrid/latest/upgrade#prepare-for-the-helm-charts-upgrade) and **before** [Install the Apigee hybrid Helm charts](https://docs.cloud.google.com/apigee/docs/hybrid/latest/upgrade#install-the-apigee-hybrid-helm-charts):

  1. Make the following changes in your `overrides.yaml` file to notify the operator where to find the cert-manager related resources and enable the operator to use the custom cert-manager's ClusterIssuer. 
         
         certManager:
           namespace: APIGEE_NAMESPACE
         
         ao:
           certManagerCAIssuerEnabled: true
         

  2. Copy the existing apigee-ca secret from cert-manager namespace to your apigee namespace: 
         
         kubectl -n cert-manager get secret apigee-ca -o yaml > apigee-ca.yaml
         

  3. Edit the `apigee-ca.yaml` file to remove the namespace parameter that identifies the namespace as `cert-manager`.
  4. Apply `apigee-ca` secret to your apigee namespace with `kubectl apply`: 
         
         kubectl -n APIGEE_NAMESPACE apply -f apigee-ca.yaml




### Rolling back an Apigee hybrid upgrade

If you need to roll back to a previous version of Apigee hybrid, follow the instructions in [Rolling back to a previous version](https://docs.cloud.google.com/apigee/docs/hybrid/latest/upgrade#rolling-back-to-a-previous-version).

## Rolling back and uninstalling custom cert-manager

### Roll back the custom cert-manager

To roll back the custom cert-manager, use the following steps: 

  1. Uninstall the Helm release using the following command: 
         
         helm uninstall CERT_MANAGER_RELEASE_NAME

  2. Install the regular (non-custom) cert-manager using your preferred method. Make sure to use the corresponding CRDs version. For example, if you are using the [kubectl method](https://cert-manager.io/docs/installation/kubectl/) to install the cert-manager, it will update the CRDs to a corresponding version, as the payload will include CRDs as well. Make sure the installation method you use includes the CRDs. 



### Uninstall the custom cert-manager

To uninstall the custom cert-manager, use the following steps: 

  1. Uninstall the Helm release using the following command: 
         
         helm uninstall CERT_MANAGER_RELEASE_NAME

  2. Delete the CRDs with the following commands: 
         
         export CERT_MANAGER_VERSION=v1.14.5
         kubectl delete -f https://github.com/cert-manager/cert-manager/releases/download/${CERT_MANAGER_VERSION}/cert-manager.crds.yaml




## Infrastructure as Code (overrides.yaml)

Helm chart supports overrides as needed, enabling you to use an overrides file as needed during the installation or upgrade process. To avoid confusion, we recommend using a filename like `cert-manager-overrides.yaml`. 

See the [cert-manager documentation](https://artifacthub.io/packages/helm/cert-manager/cert-manager) for all the supported cert-manager override configurations. 

## Common cert-manager configurations

The following examples show how to accomplish some common cert-manager configurations in Apigee hybrid.

**Note:**

  * We recommend using a dedicated override.yaml file for this custom cert manager. If you're using an override file then add the following flag to the `helm install` command to install or upgrade: 

`--f CERT_MANAGER_OVERRIDES_FILE`

  * We do NOT recommend using Helm to manage the lifecycle of CRDs.
  * Because the modified Helm chart is already preconfigured to a single namespace, you cannot override that behavior in your override file. Namespace changes need RBAC changes from Role to ClusterRole which will defeat the purpose of having this modified configuration.



### Override images

The following is an example of overriding images along with `imagepullsecrets` if you need to host the image privately. 
    
    
    # cert-manager-overrides.yaml
    
    global:
      # Reference to one or more secrets to be used when pulling images
      # ref: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/
      #
      # For example:
      #  imagePullSecrets:
      #    - name: "image-pull-secret"
      imagePullSecrets: []
    
    
    image:
      # Override the image tag to deploy by setting this variable.
      # If no value is set, the chart's appVersion will be used.
      repository: quay.io/jetstack/cert-manager-controller
    
    webhook:
      image:
        # without a tag
        repository: quay.io/jetstack/cert-manager-webhook
    
    cainjector:
      image:
        # without a tag
        repository: quay.io/jetstack/cert-manager-cainjector
    
    startupapicheck:
      image:
        # without a tag
        repository: quay.io/jetstack/cert-manager-startupapicheck
    
    

### NodeSelector and Node Affinity

In Apigee Hybrid installation, you are required to use separate nodes for Cassandra pods and other pods. If you want to run the cert-manager in the node pool not related to Cassandra, you can use node affinity: 
    
    
    # A Kubernetes Affinity, if required; see https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#affinity-v1-core
    #
    # For example:
    #   affinity:
    #     nodeAffinity:
    #      requiredDuringSchedulingIgnoredDuringExecution:
    #        nodeSelectorTerms:
    #        - matchExpressions:
    #          - key: cloud.google.com/gke-nodepool
    #            operator: In
    #            values:
    #            - master
    affinity:
      nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: KEY
              operator: In
              values:
              - value for the non-C* node pool
    
    webhook:
      affinity:
      nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: KEY
              operator: In
              values:
              - value for the non-C* node pool
    
    cainjector:
      affinity:
      nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: KEY
              operator: In
              values:
              - value for the non C* node pool
    

### Tolerations

You can also provide tolerations, as shown in the following example: 
    
    
    # A list of Kubernetes Tolerations, if required; see https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#toleration-v1-core
    #
    # For example:
    #   tolerations:
    #   - key: node.kubernetes.io/not-ready
    #     operator: Equal
    #     value: master
    #     effect: NoSchedule
    tolerations: []
    
    webhook:
      tolerations: []
    
    cainjector:
      tolerations: []
    
    startupapicheck:
      tolerations: []
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
