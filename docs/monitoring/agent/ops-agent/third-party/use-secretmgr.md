---
url: https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/use-secretmgr/
title: Manage secrets in Ops Agent configuration \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:02.889125+00:00
---

# Manage secrets in Ops Agent configuration  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/use-secretmgr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Manage secrets in Ops Agent configuration Stay organized with collections  Save and categorize content based on your preferences. 

Configuring some of the third-party integrations requires you to provide secrets, such as passwords, for the Ops Agent metric receivers. By default, these secrets are stored as plaintext in the agent's `config.yaml` file. These secrets are included in system logs written by the agent and transmitted to Cloud Logging, exposing the secrets beyond the virtual machine (VM) where the Ops Agent is running.

Starting with Ops Agent version 2.57.0, you can use an OpenTelemetry provider integrated [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to eliminate plaintext secrets in your configuration files.

A _provider_ is an OpenTelemetry configuration component, analogous to the receiver and processor components. Each provider has a type, and each type of provider maps a specific identifier in the configuration to a value.

The `googlesecretmanager` provider maps Secret Manager identifiers to the secrets, like passwords, tokens, and API keys, that you've stored in Secret Manager. Using the `googlesecretmanager` provider offers the following benefits:

  * **Enhanced security** : Your configuration files don't contain sensitive information like passwords. The actual secrets are stored in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview), a service designed specifically for securely storing, accessing, and managing sensitive data.
  * **Reduced risk of exposure** : Secret Manager fetches secrets during initialization of the Ops Agent, which prevents plaintext secrets from accidentally being recorded in logs.



You can use the `googlesecretmanager` only in the configuration of metric collection in custom Ops Agent configurations. Don't use the provider to replace secrets in the configuration of log collection.

## Before you begin

To use the `googlesecretmanager` provider, you must enable the Secret Manager API and permit access to the API, as described in the following steps:

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. Set the default project for Google Cloud CLI:
         
         gcloud config set project PROJECT_ID
         

Before you run the previous command, replace the PROJECT_ID variable with the identifier of your Google Cloud project.

  3. Enable the Secret Manager API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable secretmanager.googleapis.com

  4. Update the OAuth access scopes for your instance to include the required scope for Secret Manager, `https://www.googleapis.com/auth/cloud-platform`: 
         
         gcloud compute instances set-service-account "INSTANCE_ID" \
           --service-account "SERVICE_ACCT_EMAIL" \
           --scopes "https://www.googleapis.com/auth/cloud-platform"
         

Before you run the previous command, replace the following variables:

     * INSTANCE_ID: the identifier of your VM.
     * SERVICE_ACCT_EMAIL: the address of the service account associated with the VM.

For more information, see [ Access the Secret Manager API](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api).

  5. Grant the user who manages the Ops Agent configurations the permissions needed to create and manage secrets. The Identity and Access Management role `roles/secretManager.secretAdmin` includes the necessary permissions: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="user:USER_EMAIL" \
           --role=roles/secretManager.secretAdmin
         

Before you run the previous command, replace the following variables:

     * PROJECT_ID: the identifier of your Google Cloud project.
     * USER_EMAIL: the address of the user being granted the role.
  6. Grant the service account associated with the VM the permissions it needs to access the secrets. The Identity and Access Management role `roles/secretManager.secretAccessor` includes the necessary permissions: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:SERVICE_ACCT_EMAIL" \
           --role=roles/secretManager.secretAccessor
         

Before you run the previous command, replace the following variables:

     * PROJECT_ID: the identifier of your Google Cloud project.
     * SERVICE_ACCT_EMAIL: the address of the service account associated with the VM.



## Replace plaintext secrets with managed secrets

To eliminate the use of plaintext secrets in your configuration files by using Secret Manager and the `googlesecretmanager` provider, do the following:

  1. Create a secret in Secret Manager for each plaintext secret in your configuration files.
  2. Replace each plaintext secret in your configuration files with a reference to the corresponding secret in Secret Manager.



For example, if you are using a `mysql` metric receiver, then your configuration file might include an entry like the following:
    
    
    receivers:
      mysql:
        type: mysql
        username: root
        password: plaintext-secret
    

In this example, you want to place the `plaintext-secret` string into Secret Manager and then replace the plaintext secret with a reference to the managed secret.

### Create Secret Manager secrets for plaintext secrets

To create a Secret Manager secret containing the plaintext secret `plaintext-secret`, run the following command: 
    
    
    echo -n "plaintext-secret" | gcloud secrets create SECRET_NAME \
        --replication-policy="automatic" \
        --data-file=-
    

Before you run the previous command, replace the following variables:

  * plaintext-secret: Replace with your plaintext secret.
  * SECRET_NAME: Replace with a meaningful name for your secret. 



The fully qualified resource name of your new secret has the following format, with a VERSION of `1`:
    
    
    projects/PROJECT_ID/secrets/SECRET_NAME/versions/VERSION

For more information about storing, versioning, and accessing secrets in Secret Manager, see [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets). 

### Replace plaintext secrets

To update your configuration files, replace each plaintext secret with a reference to the `googlesecretmanager` provider and the resource name of the managed secret, as shown in the following example:
    
    
    receivers:
      mysql:
        type: mysql
        username: root
        password: ${googlesecretmanager:projects/PROJECT_ID/secrets/SECRET_NAME/versions/VERSION}
    

### Restart the Ops Agent

### Linux

  1. To restart the agent, run the following command on your instance: 
         
         sudo systemctl restart google-cloud-ops-agent
         

  2. To confirm that the agent restarted, run the following command and verify that the components "Metrics Agent" and "Logging Agent" started: 
         
         sudo systemctl status "google-cloud-ops-agent*"
         




### Windows

  1. Connect to your instance using RDP or a similar tool and login to Windows. 
  2. Open a PowerShell terminal with administrator privileges by right-clicking the PowerShell icon and selecting **Run as Administrator**
  3. To restart the agent, run the following PowerShell command: 
         
         Restart-Service google-cloud-ops-agent -Force
         

  4. To confirm that the agent restarted, run the following command and verify that the components "Metrics Agent" and "Logging Agent" started: 
         
         Get-Service google-cloud-ops-agent*
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
