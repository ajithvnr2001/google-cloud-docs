---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-service-accounts/
title: Step 4: Create service accounts \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:56:36.442813+00:00
---

# Step 4: Create service accounts  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 4: Create service accounts Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

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

This procedure uses the following two environment variables defined in [Step 2: Download the Apigee Helm charts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-download-charts). These variables are optional. If you did not define them, substitute the appropriate directory path for each variable in the code samples. 

  * `$APIGEE_HELM_CHARTS_HOME`: The directory where you downloaded the Apigee Helm charts, defined in [Step 2: Download the Apigee Helm charts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-download-charts).
  * `$PROJECT_ID`: Your Google Cloud project ID, defined in [Part 1: Project and Org setup--Step 1: Enable APIs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/precog-enableapi).



### Production vs. non-production environments

This guide refers to _Production_ ("Prod") and _Non-production_ ("Non-prod") installations. A production installation is tuned for greater usage capacity, storage, and scalability. A non-production installation uses fewer resources and is mainly for learning and demonstration purposes. 

When you create and configure service accounts for Apigee hybrid, it is important to be aware of the type of installation you are targeting. 

For _production_ installations, we recommend creating a separate service account for each Apigee hybrid component. For example, runtime, mart, metrics, mint, and so on. Each component has a dedicated service account. 

For _non-prod_ installations, you can create a single service account that applies to all the components. 

To learn more about the service accounts used by Apigee and the roles they are assigned, see [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/sa-about#recommended-sas). 

## Authenticating service accounts

Apigee hybrid supports the following methods of authenticating Google service accounts:

  * Kubernetes secrets
  * Service account JSON key files ("JSON files" in the selection tabs in the following section).
  * Vault
  * Workload Identity Federation for GKE ("WIF for GKE" in the selection tabs in the following section).
  * Workload Identity Federation on other platforms ("WIF on other platforms" in the selection tabs in the following section).



In the following section choose the procedure for the type of authentication you plan to use.

## Create the service accounts

Apigee hybrid uses the following service accounts: 

### Production

Service account | IAM roles | Apigee Helm chart  
---|---|---  
`apigee-cassandra` | [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) | `apigee-datastore`  
`apigee-guardrails` | [Service Usage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageViewer) | `apigee-operator`  
`apigee-logger` | [Logs Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) | `apigee-telemetry`  
`apigee-mart` | [Apigee Connect Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeconnect#apigeeconnect.Agent) | `apigee-org`  
`apigee-metrics` | [Monitoring Metric Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) | `apigee-telemetry`  
`apigee-mint-task-scheduler`  
(Required only if you are using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid)) | No role required | `apigee-org`  
`apigee-runtime` | No role required | `apigee-env`  
`apigee-synchronizer` | [Apigee Synchronizer Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.synchronizerManager)  
[Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) | `apigee-env`  
`apigee-watcher` | [Apigee Runtime Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.runtimeAgent) | `apigee-org`  
  
### Non-prod

Service account | IAM roles | Apigee Helm chart  
---|---|---  
`apigee-non-prod` | [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin)  
[Service Usage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageViewer)  
[Logs Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter)  
[Apigee Connect Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeconnect#apigeeconnect.Agent)  
[Monitoring Metric Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter)  
[Apigee Synchronizer Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.synchronizerManager)  
[Apigee Runtime Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.runtimeAgent) | `apigee-datastore`  
`apigee-operator`  
`apigee-telemetry`  
`apigee-org`  
`apigee-env`  
  
### The `create-service-account` tool

Apigee provides a tool, [ `create-service-account`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/create-service-account), in the `apigee-operator/etc/tools` directory: 
    
    
    $APIGEE_HELM_CHARTS_HOME/
        └── apigee-operator/
            └── etc/
                └── tools/
                    └── create-service-account

This tool creates the service accounts, assigns the IAM roles to each account, and downloads the certificate files in JSON format for each account. 

Use the following flags to control which service accounts `create-service-account` creates and which project and directory it uses: 

  * `--prod` creates all the supported production service accounts. This is the default: if you run `create-service-account` with neither `--prod` nor `--non-prod`, it behaves as if you passed `--prod`. 
  * `--prod SA_NAME` creates a single named production service account, for example `--prod apigee-cassandra`. 
  * `--non-prod` creates a single non-production service account that has all the IAM roles. The account is named `apigee-non-prod`. 
  * `--non-prod SA_NAME` creates the single non-production service account with the name SA_NAME instead of the default `apigee-non-prod`, for example `--non-prod my-non-prod-sa`. 
  * `--name NAME` (or `-n NAME`) names the single created service account NAME. `--name` changes only what the account is called, never which IAM roles it receives. Use `--prod SA_NAME --name NAME` to give a single production service account a name other than SA_NAME. `--name` is not valid with a bare `--prod` (which creates a separate account for each supported production service account name), and with `--non-prod` it takes precedence over a positional SA_NAME. 
  * `--project-id PROJECT_ID` sets the Google Cloud project ID. If both `--project-id` and the `PROJECT_ID` environment variable are set, `--project-id` takes precedence and the tool logs a warning. The tool always logs which project ID source it used and prints the resolved deployment type, project, and output directory before it creates any service accounts. 
  * `--dir DIRECTORY` writes the service account key files to DIRECTORY. 
  * `--skip-key-download` creates the service accounts and assigns their IAM roles but does not download the JSON key files. Use this flag when you do not need the key files, such as with the Workload Identity Federation for GKE authentication methods. 
  * `--help` prints the full usage, including the list of supported production service account names. 



Verify you can execute `create-service-account`. If you have just downloaded the charts the `create-service-account` file might not be in an executable mode. In your APIGEE_HELM_CHARTS_HOME directory run the following command: 
    
    
    $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/**create-service-account --help**

If your output says `permission denied` you need to make the file executable, for example with `chmod` in Linux, MacOS, or UNIX or in the Windows Explorer or with the `icacls` command in Windows. For example: 
    
    
    chmod +x $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/**create-service-account**

### Create the service accounts

Choose the procedure for the service account authentication method you plan to use in your installation. For more information, see [Service account authentication methods in Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/sa-authentication-methods).

### Kubernetes Secrets

To prepare the service account key files to store in Kubernetes Secrets you can use the `create-service-account` tool to create the service account key files with the `--dir` flag to create a directory for the key files. 

### Production

  1. Make sure the `PROJECT_ID` environment variable is defined. 
         
         echo $PROJECT_ID

The `create-service-account tool uses the value of the`PROJECT_ID` environment variable `. If it is not defined, either define it with your ID of your Google Cloud Project ID or add the `--project-id _PROJECT_ID_` flag to the `create-service-account` command. 

  2. Create the service accounts with the following commands, where `$APIGEE_HELM_CHARTS_HOME` is the path where you downloaded the Apigee Helm charts. You may be prompted to create each service account. Respond with `y`. 
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --prod \
           --dir $APIGEE_HELM_CHARTS_HOME/service-accounts

  3. Verify that the service account files were created by checking the contents of the `service-accounts` directory. Your output should look like: 
         
         ls $APIGEE_HELM_CHARTS_HOME/service-accounts/
         my-project-apigee-cassandra.json    my-project-apigee-mint-task-scheduler.json
         my-project-apigee-guardrails.json   my-project-apigee-runtime.json
         my-project-apigee-logger.json       my-project-apigee-synchronizer.json
         my-project-apigee-mart.json         my-project-apigee-watcher.json
         my-project-apigee-metrics.json
         




### Non-prod

  1. Make sure the `PROJECT_ID` environment variable is defined. 
         
         echo $PROJECT_ID

The `create-service-account tool uses the value of the`PROJECT_ID` environment variable `. If it is not defined, either define it with your ID of your Google Cloud Project ID or add the `--project-id _PROJECT_ID_` flag to the `create-service-account` command. 

  2. Create the service accounts with the following command, where `$APIGEE_HELM_CHARTS_HOME` is the path where you downloaded the Apigee Helm charts. You may be prompted to create the service account. Respond with `y`. 
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --non-prod \
           --dir $APIGEE_HELM_CHARTS_HOME/service-accounts

  3. Verify that the service account file was created by checking the contents of the `service-accounts` directory. Your output should look like: 
         
         ls $APIGEE_HELM_CHARTS_HOME/service-accounts/
         my-project-apigee-non-prod.json




### JSON files

Because Helm does not support referencing files outside of the chart directory, you will create each service account certificate file in the chart directory for the corresponding hybrid component. 

For the next steps choose whether you are configuring a Production or Non-production installation.

### Production

  1. Make sure the `PROJECT_ID` environment variable is defined. 
         
         echo $PROJECT_ID

The `create-service-account tool uses the value of the`PROJECT_ID` environment variable `. If it is not defined, either define it with your ID of your Google Cloud Project ID or add the `--project-id _PROJECT_ID_` flag to the `create-service-account` commands. 

  2. Create the service accounts with the following commands, where `$APIGEE_HELM_CHARTS_HOME` is the path where you downloaded the Apigee Helm charts. You may be prompted to create each service account. Respond with `y`. 
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --prod apigee-cassandra \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-datastore
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --prod apigee-guardrails \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-operator
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --prod apigee-logger \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-telemetry
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --prod apigee-mart \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-org
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --prod apigee-metrics \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-telemetry
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --prod apigee-runtime \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-env
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --prod apigee-synchronizer \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-env
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --prod apigee-watcher \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-org

If you are enabling [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid) (Apigee hybrid [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later):
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --prod apigee-mint-task-scheduler \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-org
         

  3. Verify that the service account files were created in the correct directories by checking the contents of each chart's directory. Your output should look like: 
         
         ls ./apigee-operator
         Chart.yaml  **my-project-apigee-guardrails.json**  tests
         etc         templates                          values.yaml
         
         ls ./apigee-datastore
         Chart.yaml  **my-project-apigee-cassandra.json**  templates  values.yaml
         
         ls ./apigee-telemetry
         Chart.yaml                     **my-project-apigee-metrics.json**  values.yaml
         **my-project-apigee-logger.json**  templates
         
         ls ./apigee-org
         Chart.yaml                                  **my-project-apigee-watcher.json**
         **my-project-apigee-mart.json**                 values.yaml
         **my-project-apigee-mint-task-scheduler.json**
         
         ls ./apigee-env
         Chart.yaml                            templates
         **my-project-apigee-runtime.json**      values.yaml
         **my-project-apigee-synchronizer.json**
         

**Tip:** You can also verify the location of the service account files with the following `tree` command: 
         
         tree -P *.json




### Non-prod

  1. Make sure the `PROJECT_ID` environment variable is defined. 
         
         echo $PROJECT_ID

The `create-service-account tool uses the value of the`PROJECT_ID` environment variable `. If it is not defined, either define it with your ID of your Google Cloud Project ID or add the `--project-id _PROJECT_ID_` flag to the `create-service-account` commands. 

  2. Create the service account with the following command, where `$APIGEE_HELM_CHARTS_HOME` is the path where you downloaded the Apigee Helm charts. You may be prompted to create each service account. Respond with `y`. 
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --non-prod \
           --dir $APIGEE_HELM_CHARTS_HOME/apigee-datastore

  3. Verify the name of the service account file created in the `apigee-datastore` directory: 
         
         ls $APIGEE_HELM_CHARTS_HOME/apigee-datastore
         
         Chart.yaml  **_PROJECT_ID_ -apigee-non-prod.json**  templates  values.yaml

  4. Copy the service account file to the other chart directories that will need to refer to it: 
         
         cp $APIGEE_HELM_CHARTS_HOME/apigee-datastore/SA_FILE_NAME $APIGEE_HELM_CHARTS_HOME/apigee-operator/
         
         cp $APIGEE_HELM_CHARTS_HOME/apigee-datastore/SA_FILE_NAME $APIGEE_HELM_CHARTS_HOME/apigee-telemetry/
         
         cp $APIGEE_HELM_CHARTS_HOME/apigee-datastore/SA_FILE_NAME $APIGEE_HELM_CHARTS_HOME/apigee-org/
         
         cp $APIGEE_HELM_CHARTS_HOME/apigee-datastore/SA_FILE_NAME $APIGEE_HELM_CHARTS_HOME/apigee-env/




### Vault

To prepare the service account key files to store in Vault you can use the `create-service-account` tool to create the service account key files with the `--dir` flag to create a directory for the key files. 

### Production

  1. Make sure the `PROJECT_ID` environment variable is defined. 
         
         echo $PROJECT_ID

The `create-service-account tool uses the value of the`PROJECT_ID` environment variable `. If it is not defined, either define it with your ID of your Google Cloud Project ID or add the `--project-id _PROJECT_ID_` flag to the `create-service-account` command. 

  2. Create the service accounts with the following commands, where `$APIGEE_HELM_CHARTS_HOME` is the path where you downloaded the Apigee Helm charts. You may be prompted to create each service account. Respond with `y`. 
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --prod \
           --dir $APIGEE_HELM_CHARTS_HOME/service-accounts

  3. Verify that the service account files were created by checking the contents of the `service-accounts` directory. Your output should look like: 
         
         ls $APIGEE_HELM_CHARTS_HOME/service-accounts/
         my-project-apigee-cassandra.json    my-project-apigee-mint-task-scheduler.json
         my-project-apigee-guardrails.json   my-project-apigee-runtime.json
         my-project-apigee-logger.json       my-project-apigee-synchronizer.json
         my-project-apigee-mart.json         my-project-apigee-watcher.json
         my-project-apigee-metrics.json
         
         




### Non-prod

  1. Make sure the `PROJECT_ID` environment variable is defined. 
         
         echo $PROJECT_ID

The `create-service-account tool uses the value of the`PROJECT_ID` environment variable `. If it is not defined, either define it with your ID of your Google Cloud Project ID or add the `--project-id _PROJECT_ID_` flag to the `create-service-account` command. 

  2. Create the service accounts with the following command, where `$APIGEE_HELM_CHARTS_HOME` is the path where you downloaded the Apigee Helm charts. You may be prompted to create the service account. Respond with `y`. 
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --non-prod \
           --dir $APIGEE_HELM_CHARTS_HOME/service-accounts

  3. Verify that the service account file was created by checking the contents of the `service-accounts` directory. Your output should look like: 
         
         ls $APIGEE_HELM_CHARTS_HOME/service-accounts/
         my-project-apigee-non-prod.json




### WIF for GKE

Create the service accounts for your installation with the following commands: 

### Production

  1. Make sure the `PROJECT_ID` environment variable is defined. 
         
         echo $PROJECT_ID

The `create-service-account tool uses the value of the`PROJECT_ID` environment variable `. If it is not defined, either define it with your ID of your Google Cloud Project ID or add the `--project-id _PROJECT_ID_` flag to the `create-service-account` command. 

  2. Create the service accounts with the following commands, where `$APIGEE_HELM_CHARTS_HOME` is the path where you downloaded the Apigee Helm charts. You may be prompted to create each service account. Respond with `y`. 
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --prod \
           --dir $APIGEE_HELM_CHARTS_HOME/service-accounts

  3. Verify the creation of the Google service accounts" with the following command: 
         
         gcloud iam service-accounts list --project $PROJECT_ID

The output should look similar to the following: 
         
         DISPLAY NAME                EMAIL                                                          DISABLED
         apigee-cassandra            apigee-cassandra@my-project.iam.gserviceaccount.com            False
         apigee-guardrails           apigee-guardrails@my-project.iam.gserviceaccount.com           False
         apigee-mart                 apigee-mart@my-project.iam.gserviceaccount.com                 False
         apigee-metrics              apigee-metrics@my-project.iam.gserviceaccount.com              False
         apigee-mint-task-scheduler  apigee-mint-task-scheduler@my-project.iam.gserviceaccount.com  False
         apigee-runtime              apigee-runtime@my-project.iam.gserviceaccount.com              False
         apigee-synchronizer         apigee-synchronizer@my-project.iam.gserviceaccount.com         False
         apigee-watcher              apigee-watcher@my-project.iam.gserviceaccount.com              False
         




### Non-prod

  1. Make sure the `PROJECT_ID` environment variable is defined. 
         
         echo $PROJECT_ID

The `create-service-account tool uses the value of the`PROJECT_ID` environment variable `. If it is not defined, either define it with your ID of your Google Cloud Project ID or add the `--project-id _PROJECT_ID_` flag to the `create-service-account` command. 

  2. Create the service accounts with the following command, where `$APIGEE_HELM_CHARTS_HOME` is the path where you downloaded the Apigee Helm charts. You may be prompted to create the service account. Respond with `y`. 
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --non-prod \
           --dir $APIGEE_HELM_CHARTS_HOME/service-accounts

  3. Verify the creation of the Google service accounts" with the following command: 
         
         gcloud iam service-accounts list --project $PROJECT_ID

The output should look similar to the following: 
         
         DISPLAY NAME         EMAIL                                                   DISABLED
         apigee-non-prod      apigee-non-prod@my-project.iam.gserviceaccount.com      False
         




**Optional:** You will not need the service account key files for Workload Identity Federation for GKE. You may delete the `service-accounts` directory after you are done.

### WIF on other platforms

Create the service accounts for your installation with the following commands: 

### Production

  1. Make sure the `PROJECT_ID` environment variable is defined. 
         
         echo $PROJECT_ID

The `create-service-account tool uses the value of the`PROJECT_ID` environment variable `. If it is not defined, either define it with your ID of your Google Cloud Project ID or add the `--project-id _PROJECT_ID_` flag to the `create-service-account` command. 

  2. Create the service accounts with the following commands, where `$APIGEE_HELM_CHARTS_HOME` is the path where you downloaded the Apigee Helm charts. You may be prompted to create each service account. Respond with `y`. 
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --prod \
           --dir $APIGEE_HELM_CHARTS_HOME/service-accounts

  3. Verify the creation of the Google service accounts" with the following command: 
         
         gcloud iam service-accounts list --project $PROJECT_ID

The output should look similar to the following: 
         
         DISPLAY NAME                EMAIL                                                          DISABLED
         apigee-cassandra            apigee-cassandra@my-project.iam.gserviceaccount.com            False
         apigee-guardrails           apigee-guardrails@my-project.iam.gserviceaccount.com           False
         apigee-mart                 apigee-mart@my-project.iam.gserviceaccount.com                 False
         apigee-metrics              apigee-metrics@my-project.iam.gserviceaccount.com              False
         apigee-mint-task-scheduler  apigee-mint-task-scheduler@my-project.iam.gserviceaccount.com  False
         apigee-runtime              apigee-runtime@my-project.iam.gserviceaccount.com              False
         apigee-synchronizer         apigee-synchronizer@my-project.iam.gserviceaccount.com         False
         apigee-watcher              apigee-watcher@my-project.iam.gserviceaccount.com              False
         




### Non-prod

  1. Make sure the `PROJECT_ID` environment variable is defined. 
         
         echo $PROJECT_ID

The `create-service-account tool uses the value of the`PROJECT_ID` environment variable `. If it is not defined, either define it with your ID of your Google Cloud Project ID or add the `--project-id _PROJECT_ID_` flag to the `create-service-account` command. 

  2. Create the service accounts with the following command, where `$APIGEE_HELM_CHARTS_HOME` is the path where you downloaded the Apigee Helm charts. You may be prompted to create the service account. Respond with `y`. 
         
         $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
           --non-prod \
           --dir $APIGEE_HELM_CHARTS_HOME/service-accounts

  3. Verify the creation of the Google service accounts" with the following command: 
         
         gcloud iam service-accounts list --project $PROJECT_ID

The output should look similar to the following: 
         
         DISPLAY NAME         EMAIL                                                   DISABLED
         apigee-non-prod      apigee-non-prod@my-project.iam.gserviceaccount.com      False
         




**Optional:** You will not need the service account key files for Workload Identity Federation for GKE. You may delete the `service-accounts` directory after you are done.

For more information about service accounts and the `create-service-account` tool see: 

  * [About service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/sa-about)
  * [`create-service-account`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/create-service-account)



You now have created service accounts and assigned the roles needed by the Apigee hybrid components. Next, create the TLS certificates required by the hybrid ingress gateway. 

## Next step

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-download-charts) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-namespace) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-service-accounts) [(NEXT) Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-sa-authentication) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-tls-certificates) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-overrides) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-enable-control-plane-access) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-cert-manager) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-crds) [11](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-helm-charts)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
