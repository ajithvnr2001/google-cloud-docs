---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/migrate-remote-agent-to-google/
title: Migrate remote agent authentication infrastructure \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:57.324696+00:00
---

# Migrate remote agent authentication infrastructure  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/migrate-remote-agent-to-google/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate remote agent authentication infrastructure

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document describes how to migrate your Remote Agents Infrastructure using Google Cloud Service Accounts. This migration is only for the authentication infrastructure. You are not required to migrate or replace your Remote Agent instances or hosts.

**Keyless authentication:** To configure keyless authentication for Remote Agents without storing service account JSON key files on host machines, see [Authenticate Remote Agent with Workload Identity Federation](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/authenticate-remote-agent-with-workload-identity-federation). 

## Before you begin

Make sure you have the following: 

  * Necessary permissions to create service accounts in Google Cloud.
  * Required roles to create service account keys.
  * Minimum required Remote Agent version 2.6.2 and later.



## Create a service account

A service account is a special type of Google Account that is used by an application to make authorized API calls.

**Important:** Assign a unique service account to each Remote Agent. Because service accounts are subject to individual API rate limits and quotas, sharing a service account across multiple agents can exhaust quotas and cause communication failures. 

To create a service account, follow these steps:

  1. In Google Cloud console, go to the **Service Accounts** page. 
[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
  2. Click **Create Service Account**.
  3. In the **Service account details** section, do the following: 
     1. Enter a name for the service account.
     2. Enter a description for the service account.
     3. Click **Create and Continue**.
  4. In the **Permissions** section, do the following: 
     1. In the **Select a role** list, select the **Chronicle SOAR Remote Agent** role.
     2. Click **Continue**.
  5. In the **Grant users access to this service account** section, click **Done**. 



## Create a service account key

The service account key is required to authenticate the remote agent. To create this key, follow these steps: 

  1. In Google Cloud console, go to the **Service Accounts** page. 
[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
  2. Click the name of the service account that you created.
  3. Click the **Keys** tab.
  4. Click **Add Key > Create new key**.
  5. Select **JSON** as the key type and click **Create**. 
         
         A JSON file containing the key is downloaded to your computer.
         

  6. Click **Close**.



## Securely store the key file

After downloading the service account key, you must move it to the host machine where the remote agent will run. **Warning:** Don't commit this key file to your source code repository. Treat it as a confidential password. 

### Podman

  1. Locate the downloaded JSON file on your computer.
  2. Store the file in a secure location on the host machine where the agent process can access it.
  3. Enter your agent's service account key full path on the host machine. 
         
         AGENT_SERVICE_ACCOUNT_PATH




### Docker

  1. Locate the downloaded JSON file on your computer.
  2. Store the file in a secure location on the host machine where the agent process can access it.
  3. Enter your agent's service account key full path on the host machine. 
         
         AGENT_SERVICE_ACCOUNT_PATH




### Installer

  1. Locate the downloaded JSON file on your computer.
  2. Store the file in the following location: 
         
         AGENT_SERVICE_ACCOUNT_PATH

  3. Make a note of the full path to this file, as it will be required when you configure the remote agent.



## Map the remote agent service account

After creating the service account for your remote agent, you must authorize it within the platform to ensure it can successfully communicate with Google SecOps.

To grant a _service account access_ or _workload identity federation access_ to Google SecOps, you must map the identity to the platform's access control parameters. This mapping is a mandatory step to provide the identity with the necessary access to **SOC Roles** , and **Environments** required to perform automated tasks or API operations.

  1. Go to **SOAR Settings > Advanced > Group Mapping**.
  2. Click add **Add**.
  3. Complete the fields in the **Add Mapping** dialog to map the identity to the platform's access control parameters.

     1. In the **IdP / User group** field, enter one of the following: 
        * The full email address of your service account, if identity was set up using Cloud Identity.
        * The Workload Identity principal string, if identity was set up using Workforce Identity Federation.
     2. Configure the following access control fields:

Field | Description  
---|---  
**Permission groups** | Select the permission groups to define which modules and submodules the identity can access.  
**SOC roles** | Select the SOC roles to define the identity's role (such as Tier 1).  
**Environments** | Select the environments or environment groups the identity can access (such as **All Environments**).  
**Group members** | Enter the required user emails if applicable. Press **Enter** after adding each email.  
**Restricted actions** | Select the restricted actions to limit specific operations within modules.  
  4. Click **Add**.




## Configure Remote Agent Authentication to Google Cloud

### Podman

If you're deploying a new agent, read [Deploy an agent with Podman.](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-agent-with-podman)

If you're upgrading an agent, read [Upgrade an agent with Podman.](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image)

### Docker

If you're deploying a new agent, read [Deploy an agent with Docker.](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-agent-with-docker)

If you're upgrading an agent, read [Upgrade an agent with Docker.](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-docker-image)

### Installer

If you're deploying a new agent, read either [Deploy an agent with CentOS ](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/create-agent-with-installer-on-centos) or [Deploy an agent with RHEL.](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/create-agent-with-installer-for-rhel)

If you're upgrading an agent, read either [Upgrade an agent with CentOS](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-requirements-for-centos) or [Upgrade an agent with RHEL ](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-requirements-for-rhel)

### Migrate environment variables for existing agent

**Note:** This step can be skipped for Remote Agents installed after **May 10th 2026** because the environment variables are present in the container command/.env file.

Go to **SOAR Settings > Advanced > Remote Agents ** and click **View More** on the required remote agent.

Copy the following values from the **Docker Command** field and paste them in the following commands.  
You will be using them in the migration procedure:

  * `ONE PLATFORM URL DOMAIN`. 
        
        ONE_PLATFORM_URL_DOMAIN

  * `ONE PLATFORM URL PROJECT`. 
        
        ONE_PLATFORM_URL_PROJECT

  * `ONE PLATFORM URL LOCATION`. 
        
        ONE_PLATFORM_URL_LOCATION

  * `ONE PLATFORM URL INSTANCE`. 
        
        ONE_PLATFORM_URL_INSTANCE




### Podman

To migrate the remote agent environment variables, follow these steps:

  1. List running Podman containers. 
         
         podman ps

  2. Enter your agent's container ID: 
         
         CONTAINER_ID

  3. Paste the following environment variables from the earlier procedures and run this command:
         
         podman exec CONTAINER_ID sh -c 'printf "export ONE_PLATFORM_URL_DOMAIN=ONE_PLATFORM_URL_DOMAIN\nexport ONE_PLATFORM_URL_PROJECT=ONE_PLATFORM_URL_PROJECT\nexport ONE_PLATFORM_URL_LOCATION=ONE_PLATFORM_URL_LOCATION\nexport ONE_PLATFORM_URL_INSTANCE=ONE_PLATFORM_URL_INSTANCE\nexport GOOGLE_APPLICATION_CREDENTIALS=/opt/SiemplifyAgent/agent-key.json" >> /home/siemplify_agent/.bash_profile'




### Docker

To migrate the remote agent environment variables, follow these steps:

  1. List running Docker containers. 
         
         docker ps

  2. Enter your agent's container ID: 
         
         CONTAINER_ID

  3. Paste the following environment variables from the earlier procedures and run this command:
         
         docker exec CONTAINER_ID sh -c 'printf "export ONE_PLATFORM_URL_DOMAIN=ONE_PLATFORM_URL_DOMAIN\nexport ONE_PLATFORM_URL_PROJECT=ONE_PLATFORM_URL_PROJECT\nexport ONE_PLATFORM_URL_LOCATION=ONE_PLATFORM_URL_LOCATION\nexport ONE_PLATFORM_URL_INSTANCE=ONE_PLATFORM_URL_INSTANCE\nexport GOOGLE_APPLICATION_CREDENTIALS=/opt/SiemplifyAgent/agent-key.json" >> /home/siemplify_agent/.bash_profile'




### Installer

To migrate the remote agent environment variables, follow these steps:

Paste the following environment variables from the earlier procedures and run this command:
    
    
    cat << EOF >> /home/siemplify_agent/.bash_profile
    export ONE_PLATFORM_URL_DOMAIN=ONE_PLATFORM_URL_DOMAIN
    export ONE_PLATFORM_URL_PROJECT=ONE_PLATFORM_URL_PROJECT
    export ONE_PLATFORM_URL_LOCATION=ONE_PLATFORM_URL_LOCATION
    export ONE_PLATFORM_URL_INSTANCE=ONE_PLATFORM_URL_INSTANCE
    export GOOGLE_APPLICATION_CREDENTIALS=/opt/SiemplifyAgent/agent-key.json
    EOF

### Migrate the service account into the Remote Agent

Once this step is completed, and all the environment variables are present in the remote agent, the migration is completed and the remote agent will communicate through Google Cloud 

### Podman

To migrate the remote agent authentication infrastructure, follow these steps:

  1. List running Podman containers. 
         
         podman ps

  2. Enter your agent's container ID: 
         
         CONTAINER_ID

  3. Use the following command to copy the service account key to a dedicated path in the container.
         
         podman cp AGENT_SERVICE_ACCOUNT_PATH CONTAINER_ID:/opt/SiemplifyAgent/agent-key.json

  4. Use the following command to change the owner of the service account key in the container:
         
         podman exec -u 0 CONTAINER_ID chown siemplify_agent:siemplify_agent /opt/SiemplifyAgent/agent-key.json

  5. Run the following command to apply the changes: 
         
         podman restart CONTAINER_ID




### Docker

To migrate the remote agent authentication infrastructure, follow these steps:

  1. List running Docker containers. 
         
         docker ps

  2. Enter your agent's container ID: 
         
         CONTAINER_ID

  3. Use the following command to copy the service account key to a dedicated path in the container.
         
         docker cp AGENT_SERVICE_ACCOUNT_PATH CONTAINER_ID:/opt/SiemplifyAgent/agent-key.json

  4. Use the following command to change the owner of the service account key in the container:
         
         docker exec -u 0 CONTAINER_ID chown siemplify_agent:siemplify_agent /opt/SiemplifyAgent/agent-key.json

  5. Run the following command to apply the changes: 
         
         docker restart CONTAINER_ID




### Installer

To migrate the remote agent authentication infrastructure, follow these steps:

  1. Move the Service Account to the expected path
         
         mv AGENT_SERVICE_ACCOUNT_PATH /opt/SiemplifyAgent/agent-key.json

  2. Use the following command to change the owner of the service account key in the container:
         
         chown siemplify_agent:siemplify_agent /opt/SiemplifyAgent/agent-key.json

  3. Run the following command to restart the agent service: 
         
         supervisorctl restart siemplify_agent




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
