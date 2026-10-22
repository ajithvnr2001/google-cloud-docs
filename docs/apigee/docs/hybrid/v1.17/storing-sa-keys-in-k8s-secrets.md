---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/storing-sa-keys-in-k8s-secrets/
title: Storing service account keys in Kubernetes secrets \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:00.900361+00:00
---

# Storing service account keys in Kubernetes secrets  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/storing-sa-keys-in-k8s-secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Storing service account keys in Kubernetes secrets Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/storing-sa-keys-in-k8s-secrets.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-sa-keys-in-k8s-secrets.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/storing-sa-keys-in-k8s-secrets.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/storing-sa-keys-in-k8s-secrets.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/storing-sa-keys-in-k8s-secrets.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/storing-sa-keys-in-k8s-secrets.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/storing-sa-keys-in-k8s-secrets.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/storing-sa-keys-in-k8s-secrets.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/storing-sa-keys-in-k8s-secrets.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/storing-sa-keys-in-k8s-secrets.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/storing-sa-keys-in-k8s-secrets.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/storing-sa-keys-in-k8s-secrets.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/storing-sa-keys-in-k8s-secrets.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/storing-sa-keys-in-k8s-secrets.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/storing-sa-keys-in-k8s-secrets.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/storing-sa-keys-in-k8s-secrets.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/storing-sa-keys-in-k8s-secrets.html)



##  Storing service account secrets in Kubernetes secrets 

This page describes how to store Apigee hybrid service account keys in Kubernetes secrets. Storing service account keys in Kubernetes secrets enhances security and streamlines management within your Kubernetes environment. With keys stored in secrets, you do not need to store them on the file system.

### Service accounts

Hybrid uses the following service accounts:

### Production

  * `apigee-cassandra` (required for [Cassandra backup and restore in Google Cloud Storage](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/schedule-cassandra-backup-gcs))
  * `apigee-guardrails`
  * `apigee-logger`
  * `apigee-mart`
  * `apigee-metrics`
  * `apigee-mint-task-scheduler` (if you are using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid))
  * `apigee-runtime`
  * `apigee-synchronizer`
  * `apigee-watcher`



### Non-prod

  * `apigee-non-prod`



## Before you begin

This procedure uses two optional environment variables: `$APIGEE_HELM_CHARTS_HOME` and `$PROJECT_ID`. If you do not define these variables, substitute the appropriate value for each variable in the code samples.

  1. Create a directory for the service account keys in the `$APIGEE_HELM_CHARTS_HOME` directory: 
         
         mkdir -p $APIGEE_HELM_CHARTS_HOME/service-accounts

  2. Verify that you can execute the `create-service-account` tool. If you recently downloaded the charts, the `create-service-account` file might not be in an executable mode. In your `$APIGEE_HELM_CHARTS_HOME` directory, run the following command: 
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
         --help

If the output indicates a permission denied error, make the file executable. For example, use `chmod` in Linux, macOS, or UNIX:
         
         chmod +x $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account




## Create service account keys

Create or update the service accounts and download the key files using the `create-service-account` tool. This action downloads one JSON file for each service account. 

The service account key filenames will have the following format: `$PROJECT_ID-apigee-SERVICE_ACCOUNT_NAME.json`

### Production
    
    
    $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
      --env prod \
      --dir $APIGEE_HELM_CHARTS_HOME/service-accounts

### Non-prod
    
    
    $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
      --env non-prod \
      --dir $APIGEE_HELM_CHARTS_HOME/service-accounts

## Create Kubernetes secrets

Create the Kubernetes secrets to store the service account keys.

The `kubectl create secret` command in the following code samples has the structure:
    
    
    kubectl create secret generic SECRET_NAME \
      --from-file="client_secret.json=PATH_TO_SERVICE_ACCOUNT_KEY" \
      -n APIGEE_NAMESPACE

### Production

Create the secrets with the following commands: 

  * `apigee-cassandra` (if [scheduling backups in Cloud Storage](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/schedule-cassandra-backup-gcs)) 
        
        kubectl create secret generic apigee-cassandra-svc-account \
          --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-cassandra.json" \
          -n APIGEE_NAMESPACE

  * `apigee-guardrails`
        
        kubectl create secret generic apigee-guardrails-svc-account \
          --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-guardrails.json" \
          -n APIGEE_NAMESPACE

  * `apigee-logger`
        
        kubectl create secret generic apigee-logger-svc-account \
          --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-logger.json" \
          -n APIGEE_NAMESPACE

  * `apigee-mart`
        
        kubectl create secret generic apigee-mart-svc-account \
          --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-mart.json" \
          -n APIGEE_NAMESPACE

  * `apigee-metrics`
        
        kubectl create secret generic apigee-metrics-svc-account \
          --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-metrics.json" \
          -n APIGEE_NAMESPACE

  * `apigee-mint-task-scheduler` (if you are using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid)) 
        
        kubectl create secret generic apigee-mint-task-scheduler-svc-account \
          --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-mint-task-scheduler.json" \
          -n APIGEE_NAMESPACE

  * `apigee-runtime`
        
        kubectl create secret generic apigee-runtime-svc-account \
          --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-runtime.json" \
          -n APIGEE_NAMESPACE

  * `apigee-synchronizer`
        
        kubectl create secret generic apigee-synchronizer-svc-account \
          --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-synchronizer.json" \
          -n APIGEE_NAMESPACE

  * `apigee-watcher`
        
        kubectl create secret generic apigee-watcher-svc-account \
          --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-watcher.json" \
          -n APIGEE_NAMESPACE




### Non-prod
    
    
    kubectl create secret generic apigee-non-prod-svc-account \
      --from-file="client_secret.json=$APIGEE_HELM_CHARTS_HOME/service-accounts/$PROJECT_ID-apigee-non-prod.json" \
      -n APIGEE_NAMESPACE

## Reference service account keys in configuration

After storing service account keys as Kubernetes secrets, update your Hybrid `overrides.yaml` file to reference these secrets instead of direct file paths. Modify the relevant `serviceAccountPath` properties to use `serviceAccountSecretRef`. 

Use the following `serviceAccountSecretRefs` and `serviceAccountRef` configurations in the appropriate sections your`overrides.yaml`: 

### Production
    
    
    envs:
    - name: test
      serviceAccountSecretRefs:
        synchronizer: apigee-synchronizer-svc-account
        runtime: apigee-runtime-svc-account
    
    guardrails:
      serviceAccountRef: apigee-guardrails-svc-account
    
    mart:
      serviceAccountRef: apigee-mart-svc-account
      # Use the same service account for mart.serviceAccountRef and connectAgent.serviceAccountRef
    
    connectAgent:
      serviceAccountRef: apigee-mart-svc-account
      # Use the same service account for mart.serviceAccountRef and connectAgent.serviceAccountRef
    
    logger:
      serviceAccountRef: apigee-logger-svc-account
    
    metrics:
      serviceAccountRef: apigee-metrics-svc-account
    
    watcher:
      serviceAccountRef: apigee-watcher-svc-account
    
    # If [Scheduling backups in Cloud Storage](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/schedule-cassandra-backup-gcs)
    cassandra:
      backup:
        serviceAccountRef: apigee-cassandra-svc-account
    
    # If using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid)
    mintTaskScheduler:
      serviceAccountRef: apigee-mint-task-scheduler-svc-account
    

### Non-prod
    
    
    envs:
    - name: test-env
      serviceAccountSecretRefs:
        synchronizer: apigee-non-prod-svc-account
        runtime: apigee-non-prod-svc-account
    
    guardrails:
      serviceAccountRef: apigee-non-prod-svc-account
    
    mart:
      serviceAccountRef: apigee-non-prod-svc-account
    
    connectAgent:
      serviceAccountRef: apigee-non-prod-svc-account
    
    logger:
      serviceAccountRef: apigee-non-prod-svc-account
    
    metrics:
      serviceAccountRef: apigee-non-prod-svc-account
    
    watcher:
      serviceAccountRef: apigee-non-prod-svc-account
    
    # If [Scheduling backups in Cloud Storage](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/schedule-cassandra-backup-gcs)
    cassandra:
      backup:
        serviceAccountRef: apigee-non-prod-svc-account
    
    # If using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid)
    mintTaskScheduler:
      serviceAccountRef: apigee-non-prod-svc-account
    

## Apply configuration changes

Apply the changes to the `apigee-operator`, `apigee-telemetry`, `apigee-org`, and `apigee-env` charts with the following commands:

  1. Upgrade the Apigee telemetry: 
         
         helm upgrade telemetry apigee-telemetry/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

  2. Upgrade the Apigee organization: 
         
         helm upgrade ORG_NAME apigee-org/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

  3. Upgrade the environment. 

Specify the environment with `--set env=`ENV_NAME. Repeat this command for each environment.
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --set env=ENV_NAME \
           -f OVERRIDES_FILE
         




## What's next

  * Learn more about [Hybrid service accounts and roles](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/sa-about). 
  * Refer to the [Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-service-account) section of the Hybrid installation guide. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
