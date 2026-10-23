---
url: https://docs.cloud.google.com/logging/docs/agent/ops-agent/authorization/
title: Authorize the Ops Agent \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:39.500393+00:00
---

# Authorize the Ops Agent  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/agent/ops-agent/authorization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Authorize the Ops Agent Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Skip this guide and return to [Install the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/installation) unless you are using very old Compute Engine VMs or have to use a [custom service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#newserviceaccounts) instead of the [default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account). Compute Engine instances are pre-authorized to run the agent.

This guide explains how to ensure that the Ops Agent, which you install on your virtual machine (VM) instance, is authorized to send telemetry data to Logging.

## Authorization overview

_Authorization_ refers to the process of determining what permissions an authenticated client has for a set of resources. Google Cloud authorizes the Ops Agent on a Compute Engine VM instance by using [application default credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) (ADC).

The Ops Agent supports ADC that authenticate either a VM's attached service account, or a service account key.

  * An _attached service account_ refers to a service account that's specific to a given resource, such as a VM. The service account has its own unique credentials. ADC uses the VM's [metadata server](https://docs.cloud.google.com/compute/docs/metadata/overview) to obtain credentials for a service.
  * A _service account key_ refers to a private key used to authorize the key pair on a service account in a project, which lets you create an access token. You use the token to provide an identity so that you can interact with Google Cloud APIs on behalf of the service account.


  * The Ops Agent doesn't support authorization using `gcloud auth`. To prevent unwanted behavior, you must [revoke](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/revoke) any credentials created by using `gcloud auth`.



We recommend that you configure ADC to authenticate by using [an attached service account](https://docs.cloud.google.com/docs/authentication/set-up-adc-attached-service-account) whenever possible, as the private key requires local storage, and that storage can be compromised. For more information about service account keys, see [Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

## Verify your access scopes

Compute Engine VM instances are assigned access scopes when you create them. New Compute Engine VMs have adequate access scopes for the Ops Agent, but old VMs or those on which scopes have been modified might not. For more information about access scopes and service accounts, see [Authorization](https://docs.cloud.google.com/compute/docs/access/service-accounts#authorization) in the Compute Engine documentation.

To verify your access scopes, do the following: 

  1. Query the access scopes by running the following command on your Compute Engine instance: 
         
         curl --silent --connect-timeout 1 -f -H "Metadata-Flavor: Google" http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/scopes

  2. In the command output, if the access scope `https://www.googleapis.com/auth/cloud-platform` is listed, then you have sufficient authorization.

If `https://www.googleapis.com/auth/cloud-platform` isn't listed, then you require two access scopes, one from each of the following "logging" and "monitoring" pairs: 

     * `https://www.googleapis.com/auth/logging.write` or  
`https://www.googleapis.com/auth/logging.admin`
     * `https://www.googleapis.com/auth/monitoring.write` or  
`https://www.googleapis.com/auth/monitoring.admin`



To modify your access scopes, do the following: 

  1. In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  2. If necessary, click the drop-down list of Google Cloud projects and select the name of your project.
  3. Select **VM instances** from the navigation menu, select the **Instances** tab, and the select the name of your VM.
  4. Shut down the VM by clicking _stop_ **Stop**.
  5. After the VM stops, click _edit_ **Edit**.
  6. Locate the **Access scopes** in the **Identity and API access** section of the page, and then select **Set access for each API**.
  7. For **Stackdriver Logging API** and **Stackdriver Monitoring API** entries, select the **Write Only**.
  8. Click **Save** , and then restart the VM by clicking _play_arrow_ **Start/Resume**.



## Use a service account

_Authentication_ refers to the process of determining a client's identity. For authentication, we recommend using a _service account_ , a special kind of account that is typically used by an application or a workload, rather than a person. For more information, see [Service accounts overview](https://docs.cloud.google.com/iam/docs/service-account-overview).

You can use service accounts for authentication regardless of where your code runs: on Compute Engine, App Engine, or on-premise. For more information, see [Authentication at Google](https://docs.cloud.google.com/docs/authentication).

This section describes how to create a new service account and grant it the necessary roles, and how to update an existing service account if it doesn't have the necessary roles.

### Create a service account

To create a service account, complete the [Creating a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) procedures with the following information:

  * Select the Google Cloud project in which to create the service account.

    * For Compute Engine instances, choose the project in which you created the instance.
  * In the **Role** drop-down menu, select the following roles:

    * **Monitoring** > **Monitoring Metric Writer**.

    * **Logging** > **Logs Writer**.

  * If you plan to authenticate using a service account key, then select **JSON** as the **Key type** and click **Create**.

When you click **Create** , a file that contains a service account key is downloaded to your local system. For more information, see [Create and delete service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete).

**Note:** After you download a key, you cannot download that key again.



Next, configure your service account and settings based on whether you authorize by using attached service accounts or by using service account private keys.

### Verify and modify roles of an existing service account

You can use the Google Cloud console to determine which roles an existing service account has, and to add any necessary roles that are missing:

  1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

  2. If necessary, click the drop-down list of Google Cloud projects and select the name of your project.

  3. If you don't see a list of IAM principals (users and service accounts), then select the **Permissions** tab.

  4. In the **View by Principals** list, locate the entry for the service account. The **Role** column lists the roles granted to the service account.

  5. If your service account does not have the necessary roles for the Ops Agent, then use the following steps to add the roles described in Create a service account:

     1. Click _edit_ **Edit** in the entry for the service account.
     2. Click **Add Another Role** to add any missing roles.
     3. Click **Save**.



## Authorize with an attached service account

To authorize the Ops Agent installed on a Compute Engine VM instance that has an attached service account, do the following:

  1. Ensure that you verified the access scopes of your VM.

  2. Grant your service account the [least privileged](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) IAM roles possible. For the required roles, see the Create a service account section of this page.

  3. [Attach the service account](https://docs.cloud.google.com/iam/docs/attach-service-accounts#attaching-to-resources) to the VM where the agent is running.

  4. If you haven't already installed the agent, then install it. For information about how to install the agent, see [Installing the agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/installation).




## Authorize with a service account key

To authorize the Ops Agent installed on a VM instance by using service account private keys, do the following:

  1. Transfer the service account key file from your local system to your VM instance:

     1. Create an environment variable to point to the service account key file on your local system. The following example creates a variable called `CREDS`:
            
            CREDS=~/Downloads/PROJECT-NAME-KEY-ID.json
            

     2. In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

Identify the INSTANCE_NAME and INSTANCE_ZONE for your VM.

     3. On your local system, run a [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/quickstarts) command to copy the key file from your local system to your VM instance:
            
            REMOTE_USER="$USER"
            INSTANCE="INSTANCE_NAME"
            ZONE="INSTANCE_ZONE"
            gcloud compute scp "$CREDS" "$REMOTE_USER@$INSTANCE:~/temp.json" --zone "$ZONE"
            

     4. On your Compute Engine instance, move the service account key file from the temporary location to a permanent location, and for Linux, ensure that the service account key file is readable only by `root`.

You must also set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to point to the location of the service account key file, and the variable must be visible to the agent's process. For configuration information, see Set `GOOGLE_APPLICATION_CREDENTIALS`.

**Warning:** If you already have a service account key file, ensure that your new key file doesn't overwrite the key file for your current applications.

For example, on Linux you can run the following script which moves the service account key file to the default location, and then sets the appropriate permissions:
            
            CREDENTIALS_FILE_LOCATION="/etc/google/auth/application_default_credentials.json"
            sudo mkdir -p /etc/google/auth
            sudo mv "$HOME/temp.json" "$CREDENTIALS_FILE_LOCATION"
            sudo chown root:root "$CREDENTIALS_FILE_LOCATION"
            sudo chmod 0400 "$CREDENTIALS_FILE_LOCATION"
            

  2. Your VM instance now has the service account key file that the agent needs. Next, install or restart the agent:

     * For information about how to install the agent, see [Installing the agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/installation).

     * For information about how to restart the agent, see [Restarting the agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/installation#restart).

     * If you would like to double-check the service account key file, see [Verifying private-key credentials](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-credentials#verify-key).




### Set `GOOGLE_APPLICATION_CREDENTIALS`

This section shows how to set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` so that it is visible to the agent's process.

**Note:** The Ops Agent isn't the only service that uses the environment variable `GOOGLE_APPLICATION_CREDENTIALS`. If you change the value of this variable as described in this section, then that change affects all system services that rely on that variable.

### Linux

  1. Edit the following configuration file, or create the file if it doesn't exist:
         
         /etc/systemd/system.conf
         

  2. Add the following to the configuration file:
         
         DefaultEnvironment="GOOGLE_APPLICATION_CREDENTIALS=PATH_TO_CREDENTIAL_FILE"
         

  3. Reload the environment variables:
         
         sudo systemctl daemon-reload
         

  4. Restart the agent by running the following command on your VM instance:
         
         sudo systemctl restart google-cloud-ops-agent
         




### Windows

  1. In PowerShell, run the following commands as administrator to set the `GOOGLE_APPLICATION_CREDENTIALS` system environment variable for the Ops Agent to use:
         
         [Environment]::SetEnvironmentVariable("GOOGLE_APPLICATION_CREDENTIALS", "PATH_TO_CREDENTIAL_FILE", "Machine")
         

  2. Restart the agent by running the following command on your VM instance:
         
         Restart-Service -Name google-cloud-ops-agent -Force
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
