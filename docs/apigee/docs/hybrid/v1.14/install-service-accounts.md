---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-service-accounts/
title: Step 4: Create service accounts \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:48:42.580345+00:00
---

# Step 4: Create service accounts  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 4: Create service accounts Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.14 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.14 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-service-accounts.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-service-accounts.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-service-accounts.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-service-accounts.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-service-accounts.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-service-accounts.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-service-accounts.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-service-accounts.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-service-accounts.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-service-accounts.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-service-accounts.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-service-accounts.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-service-accounts.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-service-accounts.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-service-accounts.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-service-accounts.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-service-accounts.html)



## Overview

This step explains how to create the Google Cloud service accounts that are required for Apigee hybrid to operate, and assign the appropriate IAM roles to them. 

This procedure uses the following two environment variables defined in [Step 2: Download the Apigee Helm charts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-download-charts). These variables are optional. If you did not define them, substitute the appropriate directory path for each variable in the code samples. 

  * `$APIGEE_HELM_CHARTS_HOME`: The directory where you downloaded the Apigee Helm charts, defined in [Step 2: Download the Apigee Helm charts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-download-charts).
  * `$PROJECT_ID`: Your Google Cloud project ID, defined in [Part 1: Project and Org setup--Step 1: Enable APIs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/precog-enableapi).



### Production vs. non-production environments

This guide refers to _Production_ ("Prod") and _Non-production_ ("Non-prod") installations. A production installation is tuned for greater usage capacity, storage, and scalability. A non-production installation uses fewer resources and is mainly for learning and demonstration purposes. 

When you create and configure service accounts for Apigee hybrid, it is important to be aware of the type of installation you are targeting. 

For _production_ installations, we recommend creating a separate service account for each Apigee hybrid component. For example, runtime, mart, metrics, mint, udca, and so on each get their own service account. 

For _non-prod_ installations, you can create a single service account that applies to all the components. 

To learn more about the service accounts used by Apigee and the roles they are assigned, see [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/sa-about#recommended-sas). 

## Authenticating service accounts

Apigee hybrid supports three methods of authenticating Google service accounts:

### Workload Identity on AKS, EKS, or GKE

For Apigee hybrid installations on GKE, Google Cloud offers an option called Workload Identity to authenticate hybrid runtime components. This option does not use downloaded certificate files to authenticate the service accounts, Instead, it associates the Google Cloud service accounts that you create in this step with Kubernetes service accounts in the Kubernetes cluster. See [Enabling Workload Identity on GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/enable-workload-identity-gke) or [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/enable-workload-identity-federation)

## Create the service accounts

Apigee hybrid uses the following service accounts: 

### Prod

Service account | IAM roles | Apigee Helm chart  
---|---|---  
`apigee-cassandra` | Storage Object Admin | `apigee-datastore`  
`apigee-logger` | Logs Writer | `apigee-telemetry`  
`apigee-mart` | Apigee Connect Agent | `apigee-org`  
`apigee-metrics` | Monitoring Metric Writer | `apigee-telemetry`  
`apigee-mint-task-scheduler`  
([v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143) and later) | No role required | `apigee-org`  
`apigee-runtime` | No role required | `apigee-env`  
`apigee-synchronizer` | Apigee Synchronizer Manager  
Storage Object Admin | `apigee-env`  
`apigee-udca` | Apigee Analytics Agent | `apigee-org`  
`apigee-env`  
`apigee-watcher` | Apigee Runtime Agent | `apigee-org`  
  
### Non-prod

Service account | IAM roles | Apigee Helm chart  
---|---|---  
`apigee-non-prod` | Storage Object Admin  
Logs Writer  
Apigee Connect Agent  
Monitoring Metric Writer  
Apigee Synchronizer Manager  
Apigee Analytics Agent  
Apigee Runtime Agent  | `apigee-datastore`  
`apigee-telemetry`  
`apigee-org`  
`apigee-env`  
  
### The `create-service-account` tool

Apigee provides a tool, [ `create-service-account`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/create-service-account), in the `apigee-operator/etc/tools` directory: 
    
    
    $APIGEE_HELM_CHARTS_HOME/
        └── apigee-operator/
            └── etc/
                └── tools/
                    └── create-service-account

This tool creates the service accounts, assigns the IAM roles to each account, and downloads the certificate files in JSON format for each account. 

Verify you can execute `create-service-account`. If you have just downloaded the charts the `create-service-account` file might not be in an executable mode. In your APIGEE_HELM_CHARTS_HOME directory run the following command: 
    
    
    $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/**create-service-account --help**

If your output says `permission denied` you need to make the file executable, for example with `chmod` in Linux, MacOS, or UNIX or in the Windows Explorer or with the `icacls` command in Windows. For example: 
    
    
    chmod +x $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/**create-service-account**

### Create the service accounts

Because Helm does not support referencing files outside of the chart directory, you will create each service account certificate file in the chart directory for the corresponding hybrid component. 

For the next steps choose whether you are configuring a Production or Non-production installation.

### Prod

  1. Make sure the `PROJECT_ID` environment variable is defined. 
         
         echo $PROJECT_ID

The `create-service-account tool uses the value of the`PROJECT_ID` environment variable `. If it is not defined, either define it with your ID of your Google Cloud Project ID or add the `--project-id _PROJECT_ID_` flag to the `create-service-account` commands. 

  2. Create the service accounts with the following commands, where `$APIGEE_HELM_CHARTS_HOME` is the path where you downloaded the Apigee Helm charts. You may be prompted to create each service account. Respond with `y`. 
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --profile apigee-cassandra \
           --env prod \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-datastore
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --profile apigee-logger \
           --env prod \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-telemetry
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --profile apigee-mart \
           --env prod \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-org
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --profile apigee-metrics \
           --env prod \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-telemetry
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --profile apigee-runtime \
           --env prod \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-env
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --profile apigee-synchronizer \
           --env prod \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-env
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --profile apigee-udca \
           --env prod \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-env
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --profile apigee-udca \
           --env prod \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-org
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --profile apigee-watcher \
           --env prod \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-org

If you are enabling [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/monetization-for-hybrid) (Apigee hybrid [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143) and later):
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --profile apigee-mint-task-scheduler \
           --env prod \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-org
         

  3. Copy the `apigee-udca` JSON file to the `apigee-env` chart directory. It is needed for both org-scope and env-scope operations. 
         
         cp $APIGEE_HELM_CHARTS_HOME/apigee-org/$PROJECT_ID-apigee-udca.json $APIGEE_HELM_CHARTS_HOME/apigee-env/

  4. Verify that the service account files were created in the correct directories by checking the contents of each chart's directory. Your output should look like: 
         
         ls ./apigee-datastore
         Chart.yaml  **_PROJECT_ID_ -apigee-cassandra.json**  templates  values.yaml
         
         ls ./apigee-telemetry
         Chart.yaml  **_PROJECT_ID_ -apigee-logger.json**  **_PROJECT_ID_ -apigee-metrics.json**  templates  values.yaml
         
         ls ./apigee-org
         Chart.yaml                      **_PROJECT_ID_ -apigee-udca.json**     templates
         **_PROJECT_ID_ -apigee-mart.json**  **_PROJECT_ID_ -apigee-mint-task-scheduler.json**  **_PROJECT_ID_ -apigee-watcher.json**  values.yaml
         
         ls ./apigee-env
         Chart.yaml  **_PROJECT_ID_ -apigee-runtime.json**  **_PROJECT_ID_ -apigee-synchronizer.json** **_my_project_id_ -apigee-udca.json**  templates  values.yaml
         

**Tip:** You can also verify the location of the service account files with the following `tree` command: 
         
         tree -P *.json




### Non-prod

  1. Make sure the `PROJECT_ID` environment variable is defined. 
         
         echo $PROJECT_ID

The `create-service-account tool uses the value of the`PROJECT_ID` environment variable `. If it is not defined, either define it with your ID of your Google Cloud Project ID or add the `--project-id _PROJECT_ID_` flag to the `create-service-account` commands. 

  2. Create the service account with the following command, where `$APIGEE_HELM_CHARTS_HOME` is the path where you downloaded the Apigee Helm charts. You may be prompted to create each service account. Respond with `y`. 
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --env non-prod \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-datastore

  3. Verify the name of the service account file created in the `apigee-datastore` directory: 
         
         ls $APIGEE_HELM_CHARTS_HOME/apigee-datastore
         
         Chart.yaml  **_PROJECT_ID_ -apigee-non-prod.json**  templates  values.yaml

  4. Copy the service account file to the other chart directories that will need to refer to it: 
         
         cp $APIGEE_HELM_CHARTS_HOME/apigee-datastore/SA_FILE_NAME $APIGEE_HELM_CHARTS_HOME/apigee-telemetry/
         
         cp $APIGEE_HELM_CHARTS_HOME/apigee-datastore/SA_FILE_NAME $APIGEE_HELM_CHARTS_HOME/apigee-org/
         
         cp $APIGEE_HELM_CHARTS_HOME/apigee-datastore/SA_FILE_NAME $APIGEE_HELM_CHARTS_HOME/apigee-env/




For more information about service accounts and the `create-service-account` tool see: 

  * [About service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/sa-about)
  * [`create-service-account`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/create-service-account)

**Tip:** You can store the service account files in Kubernetes secrets. See [Storing data in a Kubernetes secret](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/k8s-secrets)

You now have created service accounts and assigned the roles needed by the Apigee hybrid components. Next, create the TLS certificates required by the hybrid ingress gateway. 

## Next step

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-download-charts) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-create-namespace) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-service-accounts) [(NEXT) Step 5: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-create-tls-certificates) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-create-overrides) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-enable-control-plane-access) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-cert-manager) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-crds) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-helm-charts) [11](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-workload-identity)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
