---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/authenticate-remote-agent-with-workload-identity-federation/
title: Authenticate Remote Agent with Workload Identity Federation \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:56.958519+00:00
---

# Authenticate Remote Agent with Workload Identity Federation  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/authenticate-remote-agent-with-workload-identity-federation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Authenticate Remote Agent with Workload Identity Federation

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document describes how to configure keyless authentication for Google SecOps Remote Agents using Workload Identity Federation (WIF). Workload Identity Federation eliminates the need to download, manage, and store long-lived service account JSON key files on remote agent host environments.

With Workload Identity Federation, Remote Agents running on external cloud providers, on-premises infrastructure, Kubernetes clusters, or CI/CD pipelines use short-lived federated Google Cloud access tokens derived from their external identity provider.

## Before you begin

Before configuring Workload Identity Federation, verify the following prerequisites: 

  * Minimum Remote Agent version **2.6.2** or later.
  * The user configuring Workload Identity Federation must have the required IAM permissions in Google Cloud to create and manage Workload Identity Pools (`roles/iam.workloadIdentityPoolAdmin`) and Service Accounts (`roles/iam.serviceAccountAdmin`).
  * A dedicated Service Account created in Google Cloud with the **Chronicle SOAR Remote Agent** role (`roles/chronicle.soarAgent`). For steps to create a service account, see [Create a service account](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/migrate-remote-agent-to-google#create-a-service-account).
  * Access to your external Identity Provider (AWS, Azure, Active Directory/ADFS, Kubernetes, CI/CD pipeline, X.509 CA, or custom OIDC/SAML provider).



## Step 1: Create a Workload Identity Pool and Provider

In Google Cloud, Workload Identity Pools manage external identities, while Workload Identity Providers define the connection parameters between your external IdP and Google Cloud.

**Provider configuration details:** For provider-specific issuer URLs, allowed audiences, and required attribute mappings, see the documentation for your Identity Provider: 

  * [AWS (EC2 / EKS)](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#aws)
  * [Microsoft Azure (VM / AKS)](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#azure)
  * [Active Directory / ADFS / Microsoft Entra ID](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-active-directory)
  * [Kubernetes (GKE, EKS, AKS, or on-premises)](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-kubernetes)
  * [Deployment Pipelines (GitHub Actions, GitLab, Terraform)](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines)
  * [X.509 Certificates](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-x509-certificates) and [Other Providers](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers)



  1. In Google Cloud console, go to the **Workload Identity Pools** page. [Go to Workload Identity Pools](https://console.cloud.google.com/iam-admin/workload-identity-pools)
  2. Click **Create Pool**.
  3. Enter a **Name** and **Description** for the pool (for example, `soar-remote-agent-pool`).
  4. Click **Continue**.
  5. In the **Add a provider to pool** section, select your provider type and enter the provider connection details (such as AWS Account ID or OIDC Issuer and Audience) from your provider's guide above.
  6. In the **Configure attribute mappings** section, map claims from your external token (such as `google.subject=assertion.sub`) to Google Cloud IAM attributes as specified in your provider's guide.
  7. Click **Save**.



## Step 2: Grant Service Account Impersonation Permissions

Allow external identities in your Workload Identity Pool to impersonate your Remote Agent Service Account.

  1. In Google Cloud console, go to the **Service Accounts** page.
  2. Select your Remote Agent Service Account.
  3. Click the **Principals with access** tab.
  4. Click **Grant access**.
  5. In the **New principals** field, enter the principal identifier corresponding to your Workload Identity Pool: 
         
         principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/*

 **Note:** You can copy the exact **IAM principal** (or **Default principal set**) string directly from your pool's details page on the **Workload Identity Pools** page.**Security best practice:** The wildcard (`/*`) grants impersonation access to all identities in the pool, which is useful for initial testing. For production environments, follow the principle of least privilege by scoping access to a specific identity or mapped attribute: 
     * **Kubernetes:** `principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/system:serviceaccount:NAMESPACE:KSA_NAME`
     * **GitHub Actions:** `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.repository/ORG/REPO`
     * **AWS:** `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.aws_role/arn:aws:sts::AWS_ACCOUNT_ID:assumed-role/ROLE_NAME`
  6. In the **Select a role** list, select **Workload Identity User** (`roles/iam.workloadIdentityUser`).
  7. Click **Save**.



## Step 3: Download or generate External Account Credentials (`agent-key.json`)

On the Remote Agent host machine, obtain an external account credential configuration file named `agent-key.json` using one of the following options.

**Preconfigured credential path:** The Remote Agent runtime environment variable `GOOGLE_APPLICATION_CREDENTIALS` is preconfigured by default to point to `/opt/SiemplifyAgent/agent-key.json`. Save or rename the downloaded credential file to `agent-key.json` so that no changes to the default environment variable path are required. **Important:** When deploying Remote Agents with Workload Identity Federation, obtaining an external identity token alone is not sufficient. The agent must impersonate the designated Google Cloud Service Account to obtain credentials authorized in Google SecOps. Without service account impersonation, API requests to `us-chronicle.googleapis.com` fail with `403 Forbidden`. 

### Option A: Download from Google Cloud console (Recommended)

  1. In Google Cloud console, go to the **Workload Identity Pools** page.
  2. Select your Workload Identity Pool and click **Grant access**.
  3. In the **Grant access** panel, select **Grant access using service account impersonation**.
  4. In the **Select service account** list, select your Remote Agent Service Account.
  5. In the **Select principals (identities that can access the service account)** section, specify which identities can access the service account (such as selecting an attribute name and value).
  6. Click **Save**.
  7. In the **Configure your application** window: 
     * Select your **Workload Identity Provider**.
     * In the **OIDC ID token path** field, enter the exact file path where your external token is mounted or stored (for Kubernetes projected tokens, this must match the `mountPath` \+ `path` defined in your pod manifest, such as `/var/run/secrets/tokens/gcp-kms-token`).
     * Set **Format type** to **Text** (raw JWT string). Do not select JSON for standard token files.
     * Click **Download config** and save the file as `agent-key.json` (or rename the downloaded file to `agent-key.json`).
  8. Transfer the `agent-key.json` file to your Remote Agent host machine.



### Option B: Generate using gcloud CLI

Run the `gcloud iam workload-identity-pools create-cred-config` command to generate the credential configuration file:
    
    
    gcloud iam workload-identity-pools create-cred-config \
        projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID \
        --service-account=SERVICE_ACCOUNT_EMAIL \
        --output-file=agent-key.json \
        --credential-source-file=/var/run/secrets/tokens/gcp-kms-token

**Note:** Adjust credential source flags based on your environment (for example, `--aws` for AWS IMDS, `--azure` for Azure IMDS, or `--credential-source-file` for Kubernetes/OIDC token files). 

### Sample Configuration File Reference

For reference, the generated `agent-key.json` file contains a structure similar to the following:
    
    
    {
      "type": "external_account",
      "audience": "//iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID",
      "subject_token_type": "urn:ietf:params:oauth:token-type:jwt",
      "token_url": "https://sts.googleapis.com/v1/token",
      "credential_source": {
        "file": "/var/run/secrets/tokens/gcp-kms-token"
      },
      "service_account_impersonation_url": "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SERVICE_ACCOUNT_EMAIL:generateAccessToken"
    }

**Mandatory field:** The `service_account_impersonation_url` field is required for Remote Agent authentication to exchange the federated token for service account credentials authorized in Google SecOps. 

## Step 4: Map Service Account in Google SecOps

Before deploying the Remote Agent, authorize the Service Account email address within Google SecOps:

  1. Go to **SOAR Settings** > **Advanced** > **Group Mapping**.
  2. Click add **Add**.
  3. In the **Add Role** dialog, enter the **full service account email address** in the **IAM Role / IdP group** field.
  4. Select the appropriate **Environments** that the remote agent will manage.
  5. Click **Add**.



## Step 5: Deploy or Update Remote Agent Authentication

**Case sensitivity and file permissions:** The Remote Agent installation directory is strictly case-sensitive: `/opt/SiemplifyAgent` (capital `S` and capital `A`). Ensure that the non-root container user (`siemplify_agent`) has read permissions (`chmod 644`) to `/opt/SiemplifyAgent/agent-key.json` and any mounted token files. 

### Podman

To configure Remote Agent authentication on Podman, follow these steps:

  1. List running Podman containers: 
         
         podman ps

  2. Enter your agent's container ID: 
         
         CONTAINER_ID

  3. Use the following command to copy the credential configuration file to the dedicated path in the container:
         
         podman cp PATH_TO_AGENT_KEY/agent-key.json CONTAINER_ID:/opt/SiemplifyAgent/agent-key.json

  4. Use the following command to change the owner of the credential configuration file in the container:
         
         podman exec -u 0 CONTAINER_ID chown siemplify_agent:siemplify_agent /opt/SiemplifyAgent/agent-key.json

  5. Run the following command to apply the changes: 
         
         podman restart CONTAINER_ID




### Docker

To configure Remote Agent authentication on Docker, follow these steps:

  1. List running Docker containers: 
         
         docker ps

  2. Enter your agent's container ID: 
         
         CONTAINER_ID

  3. Use the following command to copy the credential configuration file to the dedicated path in the container:
         
         docker cp PATH_TO_AGENT_KEY/agent-key.json CONTAINER_ID:/opt/SiemplifyAgent/agent-key.json

  4. Use the following command to change the owner of the credential configuration file in the container:
         
         docker exec -u 0 CONTAINER_ID chown siemplify_agent:siemplify_agent /opt/SiemplifyAgent/agent-key.json

  5. Run the following command to apply the changes: 
         
         docker restart CONTAINER_ID




### Installer

To configure Remote Agent authentication on CentOS/RHEL, follow these steps:

  1. Move the credential configuration file to the expected path:
         
         mv PATH_TO_AGENT_KEY/agent-key.json /opt/SiemplifyAgent/agent-key.json

  2. Use the following command to change the owner of the credential configuration file:
         
         chown siemplify_agent:siemplify_agent /opt/SiemplifyAgent/agent-key.json

  3. Run the following command to restart the agent service: 
         
         supervisorctl restart siemplify_agent




## Related documentation

  * [Migrate remote agent authentication infrastructure](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/migrate-remote-agent-to-google)
  * [Remote agent security overview](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/remote-agent-security)
  * [Troubleshoot remote agents](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
