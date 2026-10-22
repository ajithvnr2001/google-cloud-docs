---
url: https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-credentials/
title: Troubleshoot credentials \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:30.339713+00:00
---

# Troubleshoot credentials  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Troubleshoot credentials Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information to help you troubleshoot Ops Agent authorization and credentials problems on your Compute Engine VM instances.

If the Ops Agent is reporting access or authorization errors, or if the agent seems to be running normally but there is no data or your alerting policies aren't working as you expect, then check that your VM instance's credentials are correct, including that they specify the correct project:

  * If you are using a Compute Engine VM instance with standard (not private-key) credentials, then it is unlikely that data is going to the wrong project, but your credentials might still be deficient. For information about credentials, see [Authorize the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/authorization#private_key_authorization). To verify your credentials, see Verifying Compute Engine credentials.

  * If you are using private-key credentials on your Compute Engine instance, then the credentials could be invalid or they could be from the wrong project. For information about credentials, see [Authorize the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/authorization#private_key_authorization). To verify your credentials, see Verifying private-key credentials.




## Verifying Compute Engine credentials

Use the Compute Engine **VM instances** page of the Google Cloud console to verify that your Compute Engine VM instance has adequate credential for the Ops Agent. The credentials are typically added in the default service account of all new Compute Engine VM instances, but it is possible to overwrite those defaults when creating an instance.

In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  1. If necessary, change the current Google Cloud project to be the one associated with your Compute Engine VM instance. For example, if you are prompted to **Enable billing** , then it means the current project doesn't have any Compute Engine VM instances in it.
  2. In the **VM Instances** page, click the name of your VM instance. The detail page for your VM instance appears.
  3. In the **VM instance details** page, look under the **Cloud API access scopes** heading: 
     * If you see "Allow full access to all Cloud APIs," then you have adequate credentials.
     * If you see, next to **Stackdriver Monitoring API** , an older name for the Cloud Monitoring API, that you have **Write Only** or **Full** permission, then you have adequate credentials.
     * Otherwise, your instance's default service account doesn't have the credentials needed by the agent. To use the agent on your instance, you must add private-key service account credentials. For instructions, see [Adding credentials](https://docs.cloud.google.com/monitoring/agent/ops-agent/authorization#private_key_authorization).



If you have the correct default credentials, skip ahead to [Installing on Linux and Windows](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation#joint-install).

## Verifying private-key credentials

To verify that valid private-key credentials are installed on your VM instance, first verify that the credentials file exists in its expected location, and then verify that the information in the credentials file is valid. Previously-valid credentials can be revoked using the **IAM & Admin > Service accounts** section of the Google Cloud console. If valid credentials aren't present, see [Adding credentials](https://docs.cloud.google.com/monitoring/agent/ops-agent/authorization#private_key_authorization) to replace the existing credentials or to add new ones.

**Caution:** Other services besides Cloud Monitoring might use private-key credentials on your instance. Replacing existing credentials might prevent other services from working.

### Are the credentials present?

To see if private-key service account credentials are on your instance, run the following Linux commands on your instance:
    
    
    sudo cat $GOOGLE_APPLICATION_CREDENTIALS
    sudo cat /etc/google/auth/application_default_credentials.json
    

If either command displays a file like the one shown below, then your instance might have valid private-key credentials. If both commands display a file, then the file denoted by `GOOGLE_APPLICATION_CREDENTIALS` is used.
    
    
    {
      "type": "service_account",
      "project_id": "{your-project-id}",
      "private_key_id": "{your-private-key-id}",
      "private_key": "{your-private-key}",
      "client_email": "{your-project-number}-{your-key}@developer.gserviceaccount.com",
      "client_id": "{your-client-id}",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://accounts.google.com/o/oauth2/token",
      "auth_provider_x509_cert_url": "{x509-cert-url}",
      "client_x509_cert_url": "{client-x509-cert-url}"
    }
    

If there are no credential files present, then see [Adding credentials](https://docs.cloud.google.com/monitoring/agent/ops-agent/authorization#private_key_authorization).

### Are the credentials valid?

In the credentials file, the `project_id` field is your Google Cloud project, `client_email` identifies the service account in the project, and `private_key_id` identifies the private key in the service account. Match this information with what is shown in the **IAM & Admin > Service accounts** section of the Google Cloud console.

The credentials file isn't valid if any of the following are true:

  * You are checking a Compute Engine VM instance, but the Google Cloud project in the credentials file isn't the project that contains your instance.
  * The listed service account doesn't exist. It might have been deleted.
  * The listed service account doesn't have the right roles enabled. It should have at least `roles/monitoring.metricWriter` (Monitoring Metric Writer) for metric collection and `roles/logging.logWriter` (Logs Writer) for writing logs.
  * The private key doesn't exist. It might have been revoked.



If the service account is all right but the private key has been revoked, then you can create a new private key and copy it to your instance. Otherwise, you must create a new service account as described in the following section, [Adding credentials](https://docs.cloud.google.com/monitoring/agent/ops-agent/authorization#private_key_authorization).

### Generating new credentials

If the credentials aren't valid, take the following steps:

  1. For each connected project containing instances that need to be authorized with a private key — Compute Engine instances that were created without including the access scope `https://www.googleapis.com/auth/monitoring.write` — create a service account and generate a private key, if they don't already exist. Follow the steps below: 
     1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

     2. Select the **Netric scope** tab.
     3. Identify the project containing the Compute Engine resources in question and navigate to the [Google Cloud console](https://console.cloud.google.com/). 
     4. Go to the **IAM Service Accounts** page of the Google Cloud console, select your Google Cloud project, create a new service account, and then generate a new private key for that service account. 

To perform these steps, do one of the following: 

        * Go to the **IAM Service Accounts** page, select your Google Cloud project, and then follow the steps in [ Create a service account](https://docs.cloud.google.com/monitoring/agent/ops-agent/authorization#create-service-account):

[ Go to IAM Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts/project?project=_)

        * Click the following button and then select your Google Cloud project:

[ Create service account and download key](https://console.cloud.google.com/iam-admin/serviceaccounts/project?project=_&createStackdriverServiceAccount)

The previous button automates the process of creating and downloading a key to your local system for the agent-specific service account. If necessary, the process also creates the required service account and ensures that the service account has the correct permissions. Agent-specific service accounts have a name similar to `stackdriver-1234@PROJECT_ID.iam.gserviceaccount.com`. You are notified of the completion of these actions with a dialog similar to the following:

![A banner notifying the user that a service account and key were created.](https://docs.cloud.google.com/static/monitoring/images/created-service-account-key.png)

**Note:** Service accounts can have a maximum of 10 keys. For more information, see [Limits](https://docs.cloud.google.com/iam/quotas#limits).
  2. Replace the private key on the instances that correspond to the service account in question.

     * On Linux, replace the private key located in `/etc/google/auth/application_default_credentials.json`. 
     * On Windows, replace the private key located in `C:\ProgramData\Google\Auth\application_default_credentials.json`. For more information, see [ Copying the private key to your instance](https://docs.cloud.google.com/monitoring/agent/monitoring/authorization#private_key_authorization). 
  3. Restart the agent

     * On Linux, run `sudo service stackdriver-agent restart`
     * On Windows, go into the service management console and restart the `Cloud Monitoring` service. 



If you have multiple projects that need new private keys, repeat this procedure for each of them.

To verify that the private key is correct, see Are the credentials present?. Specifically:

  * Read the private key JSON file on the instance, for example (on Linux): `sudo cat /etc/google/auth/application_default_credentials.json`
  * Ensure that the value of the `project_id` field matches that of the monitored project for which you just generated credentials.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
