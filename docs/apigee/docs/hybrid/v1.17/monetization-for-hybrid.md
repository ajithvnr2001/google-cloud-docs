---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid/
title: Enabling monetization for Apigee hybrid \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:49.428821+00:00
---

# Enabling monetization for Apigee hybrid  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Enabling monetization for Apigee hybrid Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/monetization-for-hybrid.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/monetization-for-hybrid.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/monetization-for-hybrid.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/monetization-for-hybrid.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/monetization-for-hybrid.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/monetization-for-hybrid.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/monetization-for-hybrid.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/monetization-for-hybrid.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/monetization-for-hybrid.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/monetization-for-hybrid.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/monetization-for-hybrid.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/monetization-for-hybrid.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/monetization-for-hybrid.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/monetization-for-hybrid.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/monetization-for-hybrid.html)



## Overview

This document describes the procedures to enable recurring, top-up, and setup fees for Apigee's Monetization feature in Hybrid orgs. 

## Prerequisites

  * Apigee hybrid version 1.15.1 or higher. See [Upgrading Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/upgrade) for upgrade instructions.
  * Monetization enabled for your Apigee hybrid project. See [Enabling Apigee monetization](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enable).



## Procedure

Enabling recurring, top-up, and setup fees for Apigee hybrid monetization requires creating and setting up the `apigee-mint-task-scheduler` Google service account and granting it access to the Pub/Sub data pipeline. 

  1. If you have not already downloaded version 1.17.1 of the Helm charts, Pull the Helm charts with the following commands: **Note:** If you are performing a fresh install, you will perform this step in [Step 2: Download the Apigee Helm charts: Pull Apigee Helm charts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-download-charts#pull-apigee-helm-charts). 

In the $APIGEE_HELM_CHARTS_HOME directory, use the `pull` command to copy all of the Apigee hybrid Helm charts to your local storage:
         
         export **CHART_REPO** =oci://us-docker.pkg.dev/apigee-release/apigee-hybrid-helm-charts
         export **CHART_VERSION** =1.17.1
         helm pull **$CHART_REPO** /apigee-operator --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-datastore --version **$CHART_VERSION** --untar
         helm pull **$CHART_REP** O/apigee-env --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-ingress-manager --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-org --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-redis --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-telemetry --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-virtualhost --version **$CHART_VERSION** --untar
         

  2. Create the `apigee-mint-task-scheduler` service account. 

If you haven't already created the `apigee-mint-task-scheduler` service account, create it now with the `create-service-account` tool. See [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-service-accounts#create-the-service-accounts) for information on creating service accounts as part of a fresh hybrid install.

     1. Locate the `create-service-account` tool in the $APIGEE_HELM_CHARTS_HOME directory: 
            
            $APIGEE_HELM_CHARTS_HOME/
                └── apigee-operator/
                    └── etc/
                        └── tools/
                            └── create-service-account

Verify you can execute `create-service-account`. If you have just downloaded the charts the `create-service-account` file might not be in an executable mode. In your APIGEE_HELM_CHARTS_HOME directory run the following command: 
            
            $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/**create-service-account --help**

If your output says `permission denied` you need to make the file executable, for example with `chmod` in Linux, MacOS, or UNIX or in the Windows Explorer or with the `icacls` command in Windows. For example: 
            
            chmod +x $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/**create-service-account**

     2. Create the `apigee-mint-task-scheduler` service account and store the downloaded cert file in the `apigee-org` chart directory with the following command: 
            
            $APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/tools/create-service-account \
              --profile apigee-mint-task-scheduler \
              --env prod \
              --dir $APIGEE_HELM_CHARTS_HOME/apigee-org

  3. Enable control plane access for the `apigee-mart` and `apigee-mint-task-scheduler` service accounts. 

If you have not already enabled control plane access for the `apigee-mart` and `apigee-mint-task-scheduler` service accounts, do so now with the following steps. See [Step 7: Enable control plane access](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-enable-control-plane-access) for information on enabling control plane access as part of a fresh hybrid install.

     1. If you are not the owner of the Google Cloud project that is associated with your Apigee hybrid organization, be sure that your Google Cloud user account has the **roles/apigee.admin** (Apigee Organization Admin) role. You can check the roles assigned to you with this command: 
            
            gcloud projects get-iam-policy ${PROJECT_ID}  \
              --flatten="bindings[].members" \
              --format='table(bindings.role)' \
              --filter="bindings.members:your_account_email"
            

If your output does not include **roles/apigee.admin** , see [Step 7: Enable control plane access](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-enable-control-plane-access) for steps to add the role or have a user who does have the role perform this step. 

     2. Call the [updateControlPlaneAccess](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/updateControlPlaneAccess) API to enable the required permissions using the following command: 

### No data residency
            
            curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
              -H "Content-Type:application/json" \
              "https://apigee.googleapis.com/v1/organizations/$ORG_NAME/controlPlaneAccess?update_mask=analytics_publisher_identities" \
              -d "{\"analytics_publisher_identities\": [\"serviceAccount:apigee-mart@$ORG_NAME.iam.gserviceaccount.com\",\"serviceAccount:apigee-mint-task-scheduler@$ORG_NAME.iam.gserviceaccount.com\",\"serviceAccount:apigee-runtime@$ORG_NAME.iam.gserviceaccount.com\"]}"
            

Where the following are the email addresses of the service accounts:

        * `apigee-mart@${ORG_NAME}.iam.gserviceaccount.com`
        * `apigee-mint-task-scheduler@${ORG_NAME}.iam.gserviceaccount.com`
        * `apigee-runtime@${ORG_NAME}.iam.gserviceaccount.com`

### Data residency
    
    curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type:application/json" \
      "https://$CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/$ORG_NAME/controlPlaneAccess?update_mask=analytics_publisher_identities" \
      -d "{\"analytics_publisher_identities\": [\"serviceAccount:apigee-mart@$ORG_NAME.iam.gserviceaccount.com\",\"serviceAccount:apigee-mint-task-scheduler@$ORG_NAME.iam.gserviceaccount.com\",\"serviceAccount:apigee-runtime@$ORG_NAME.iam.gserviceaccount.com\"]}"
    

Where: 

        * **`CONTROL_PLANE_LOCATION`** is the location for your control plane data if your hybrid installation uses [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts). This is location where customer core content like proxy bundles are stored. For a list see [Available Apigee API control plane regions](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions).
        * The following are the email addresses of the service accounts: 
          * `apigee-mart@${ORG_NAME}.iam.gserviceaccount.com`
          * `apigee-mint-task-scheduler@${ORG_NAME}.iam.gserviceaccount.com`
          * `apigee-runtime@${ORG_NAME}.iam.gserviceaccount.com`
     3. Verify control plane access for the `apigee-mart` and `apigee-mint-task-scheduler` service accounts. 

### No data residency
            
            curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
              -H "Content-Type:application/json" \
              "https://apigee.googleapis.com/v1/organizations/$ORG_NAME/controlPlaneAccess"

### Data residency
            
            curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
              -H "Content-Type:application/json" \
              "https://$CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/$ORG_NAME/controlPlaneAccess"

Your output should include the `apigee-mart`, `apigee-mint-task-scheduler`, and `apigee-runtime` service accounts similar to the following:
            
            {
              "synchronizerIdentities": [
                "serviceAccount:apigee-synchronizer@$ORG_NAME.iam.gserviceaccount.com"
              ],
              "analyticsPublisherIdentities": [
                "serviceAccount:apigee-mart@$ORG_NAME.iam.gserviceaccount.com",
                "serviceAccount:apigee-mint-task-scheduler@$ORG_NAME.iam.gserviceaccount.com",
                "serviceAccount:apigee-runtime@$ORG_NAME.iam.gserviceaccount.com"
              ]
            }

  4. Add the Monetization-specific stanzas to your `overrides.yaml` file. 

Add the following stanzas to your `overrides.yaml` file:
         
         runtime:
           image:
             url: "gcr.io/apigee-release/hybrid/apigee-runtime"
             tag: "1.17.1" #must be 1.15.1 or higher.
         
         mintTaskScheduler:
           # if using stored SA cert files:
           serviceAccountPath: MINT_TASK_SCHEDULER_SA_CERT_FILE.json
           # if using stored Kubernetes secrets:
           serviceAccountRef: MINT_TASK_SCHEDULER_SA_K8S_SECRET
           # if using Workload Identity on GKE:
           gsa: "apigee-mint-task-scheduler@PROJECT_ID.iam.gserviceaccount.com"
         
         # or if using Vault:
         serviceAccountSecretProviderClass: apigee-orgsakeys-spc
         

If you are using Kubernetes secrets, see [Storing data in a Kubernetes secret](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/k8s-secrets). 

If you are using Vault, see [Storing service account keys in Hashicorp Vault](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/storing-sa-keys-in-vault). 

If you are using Vault, make sure you have added `mint` to the organization-specific secret provider class. See [Create `SecretProviderClass` objects](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/storing-sa-keys-in-vault#create-secretproviderclass-objects). 

  5. Apply the changes to the `apigee-operator`, `apigee-org`, and `apigee-env` charts. 

If you have set the $ORG_NAME and APIGEE_NAMESPACE environment variables, you can use them in the following commands:

     1. Install the operator. 

Dry run:
            
            helm upgrade operator apigee-operator/ \
              --install \
              --namespace $APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

Install the chart:
            
            helm upgrade operator apigee-operator/ \
              --install \
              --namespace $APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     2. Install Apigee organization. 

Dry run:
            
            helm upgrade $ORG_NAME apigee-org/ \
              --install \
              --namespace $APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

Install the chart:
            
            helm upgrade $ORG_NAME apigee-org/ \
              --install \
              --namespace $APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Install the environment. Repeat this step for each environment. 

You must install one environment at a time. Specify the environment with `--set env=`ENV_NAME. If you have set the $ENV_NAME environment variable in your shell, you can use that in the following commands:

Dry run:
            
            helm upgrade ENV_RELEASE_NAME apigee-env/ \
              --install \
              --namespace $APIGEE_NAMESPACE \
              --atomic \
              --set env=$ENV_NAME \
              -f overrides.yaml \
              --dry-run=server
            

ENV_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-env` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_NAME`. However, if your environment has the same name as your environment group, you must use different release names for the environment and environment group, for example `dev-env-release` and `dev-envgroup-release`. For more information on releases in Helm, see [Three big concepts](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.

Install the chart:
            
            helm upgrade ENV_RELEASE_NAME apigee-env/ \
              --install \
              --namespace $APIGEE_NAMESPACE \
              --atomic \
              --set env=$ENV_NAME \
              -f overrides.yaml
            

  6. **Workload Identity on GKE only:** Configure Workload Identity for the `apigee-mint-task-scheduler` service account. 

If you are performing a fresh install, perform this step in addition to the steps in [Step 11 (Optional): Configure Workload Identity](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-workload-identity).

When you run the helm upgrade with the `--dry-run` flag for the `apigee-org` chart, the output will include the commands you will need to configure Workload Identity with the correct Google service account and Kubernetes service account names.

     1. Get the commands to set up Workload Identity for `apigee-org` and run the command under `NOTES:` in the output. 
            
            helm upgrade $ORG_NAME apigee-org/ \
              --namespace $NAMESPACE \
              -f overrides.yaml \
              --dry-run=server

The output should contain instructions similar to the following under `NOTES:`:
            
            NOTES:
            ...
            For organization GKE Workload Identity, please make sure to add the below membership to the IAM policy binding using the respective Kubernetes SA (KSA).
            gcloud iam service-accounts add-iam-policy-binding _apigee-mint-task-scheduler_ @PROJECT_ID.iam.gserviceaccount.com \
                  --role roles/iam.workloadIdentityUser \
                  --member "serviceAccount:PROJECT_ID.svc.id.goog[APIGEE_NAMESPACE/apigee-mint-task-scheduler-PROJECT_ID-UNIQUE_ID]" \
                  --project PROJECT_ID
            

The Kubernetes service account name has the format `apigee-mint-task-scheduler-PROJECT_ID-UNIQUE_ID`.

     2. Run the commands to set up Workload Identity for `apigee-mint-task-scheduler`.



### See also

  * [Enabling Apigee monetization](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enable) for more information about monetization in Apigee.
  * [`mintTaskScheduler.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#minttaskscheduler-serviceaccountpath): Sets the path to the service account key file for the `apigee-mint-task-scheduler` service account.
  * [`mintTaskScheduler.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#minttaskscheduler-serviceaccountref): Sets the Kubernetes secret that contains the service account key for the `apigee-mint-task-scheduler` service account.
  * [`mintTaskScheduler.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#minttaskscheduler-gsa): Sets the Google service account for the `apigee-mint-task-scheduler` service account. This must be the service account email address.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
