---
url: https://docs.cloud.google.com/iap/docs/sharing-oauth-clients/
title: How to share OAuth clients \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T07:11:47.515135+00:00
---

# How to share OAuth clients  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/sharing-oauth-clients/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  How to share OAuth clients Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to share an OAuth client with another application within your organization.

## Overview

Sharing OAuth clients between projects means using a single, custom OAuth client for multiple Identity-Aware Proxy (IAP)-protected applications instead of creating a new OAuth client for each application. This approach simplifies management, especially for organizations with many applications.

When configuring IAP, you can use one of two OAuth client types:

  * **Google-managed OAuth client** : IAP automatically uses this by default. This built-in option requires no manual client creation but has two key limitations:

    * Only allows access to users within your organization (internal users)
    * Displays Google Cloud branding on the consent screen instead of your organization's branding
  * **Custom OAuth client** : You create and manage this yourself. This option:

    * Can be shared across multiple applications
    * Allows customization of branding on the consent screen
    * Supports access for external users (outside your organization)



When you create a custom OAuth client, you have the flexibility to use it with a single application or share it across multiple applications. Sharing a custom OAuth client provides several benefits:

  * Reduces the administrative overhead of managing multiple clients
  * Simplifies enabling IAP for team members who shouldn't have access to the Credentials page
  * Facilitates programmatic (non-browser) access to applications protected by IAP



For information about creating OAuth clients, see [Creating OAuth clients for IAP](https://docs.cloud.google.com/iap/docs/oauth-client-creation). For details about Google-managed OAuth clients, see [Customize an OAuth configuration to enable IAP](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration).

## Before you begin

Create a new OAuth client by completing the steps in [OAuth client creation](https://docs.cloud.google.com/iap/docs/oauth-client-creation) or use an existing OAuth client.

## Programmatic access

**Configure OAuth clients for programmatic access** to allow non-browser applications to authenticate with your IAP-protected resources. This enables scripts, automated jobs, and backend services to securely access your protected applications without interactive user login.

You can apply these authentication settings at any level in your resource hierarchy: [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations), [folder](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#folders), or [project](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects).

For implementation steps, see the [programmatic authentication guide](https://docs.cloud.google.com/iap/docs/authentication-howto) and [IAP settings management](https://docs.cloud.google.com/iap/docs/managing-access) documentation.

###  gcloud 

  1. Prepare a settings file with your OAuth client IDs:
         
         cat << EOF > SETTINGS_FILENAME
           access_settings:
             oauth_settings:
               programmatic_clients: [clientId1, clientId2, ..]
         EOF
         

  2. Apply settings using the [`gcloud iap settings set`](https://docs.cloud.google.com/sdk/gcloud/reference/iap/settings/set) command:
         
         gcloud iap settings set SETTINGS_FILENAME \
           [--organization=ORGANIZATION | --folder=FOLDER | --project=PROJECT] \
           [--resource-type=RESOURCE_TYPE] \
           [--service=SERVICE] \
           [--version=VERSION]
         

Example commands:
         
         # Organization level
         gcloud iap settings set SETTINGS_FILENAME --organization=ORGANIZATION
         
         # Folder level
         gcloud iap settings set SETTINGS_FILENAME --folder=FOLDER
         
         # Project level (web resources)
         gcloud iap settings set SETTINGS_FILENAME \
           --project=PROJECT \
           --resource-type=iap_web
         
         # App Engine service in a project
         gcloud iap settings set SETTINGS_FILENAME \
           --project=PROJECT \
           --resource-type=app-engine \
           --service=SERVICE
         

Where:

     * SETTINGS_FILENAME: The YAML file you prepared.
     * ORGANIZATION: The organization ID
     * FOLDER: The folder ID
     * PROJECT: The project ID
     * RESOURCE_TYPE: The IAP resource type (`app-engine`, `iap_web`, `compute`, `organization`, or `folder`)
     * SERVICE: The service name (optional for `compute` or `app-engine` resource types)
     * VERSION: The version name (not applicable for `compute`, optional for `app-engine`)



###  API 

  1. Prepare a settings JSON file:
         
         cat << EOF > iap_settings.json
         {
           "access_settings": {
             "oauth_settings": {
               programmatic_clients: [clientId1, clientId2, ..]
             }
           }
         }
         EOF
         

  2. Get the resource name:
         
         gcloud iap settings get \
           [--organization=ORGANIZATION | --folder=FOLDER | --project=PROJECT] \
           [--resource-type=RESOURCE_TYPE] \
           [--service=SERVICE] \
           [--version=VERSION]
         

  3. Update the settings using the resource name:
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         -d @iap_settings.json \
         "https://iap.googleapis.com/v1/RESOURCE_NAME:iapSettings?updateMask=iapSettings.accessSettings.oauthSettings.programmaticClients"
         

Where:

     * ORGANIZATION: The organization ID
     * FOLDER: The folder ID
     * PROJECT: The project ID
     * RESOURCE_TYPE: The IAP resource type (`app-engine`, `iap_web`, `compute`, `organization`, or `folder`)
     * SERVICE: The service name (optional for `compute` or `app-engine` resource types)
     * VERSION: The version name (not applicable for `compute`, optional for `app-engine`)



After configuration, sign in to the application using any one of the OAuth client IDs that you configured. See [Programmatic authentication](https://docs.cloud.google.com/iap/docs/authentication-howto) for details.

## Browser access

To enable IAP to use your client ID and secret through the Google Cloud console, complete the following instructions:

  * [Configure OAuth Client for Compute Engine (Compute Engine)](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration#backend-service)
  * [Configure OAuth Client for Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/iap/docs/enabling-kubernetes-howto)
  * [Configure OAuth Client for App Engine](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration#app-engine)
  * [Configure OAuth Client for Cloud Run](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration#cloud-run)



## Risks

While sharing a client between your applications is convenient, there are risks. This section outlines potential risks when sharing clients and how to mitigate them.

### Single point of failure

Using one OAuth client for many applications creates a single point of dependency. If a client is deleted or modified incorrectly, every application using that client is affected. Deleted OAuth clients can be restored within 30 days.

To manage this operational risk effectively:

  * Implement proper access controls to prevent accidental changes or deletion
  * Restrict access to OAuth clients using [`clientauthconfig.clients.*` permissions](https://docs.cloud.google.com/iap/docs/concepts-overview)
  * Use [Google Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) to track administrative activities involving OAuth clients



This is primarily an operational risk rather than a security risk. With proper access controls and monitoring in place, the convenience and management benefits of shared OAuth clients typically outweigh this consideration.

### Client secret leaks

Sharing a client requires sharing your client secret with people and scripts. This increases the risk of your client secret leaking. IAP can't differentiate between tokens created from your application and tokens created from a leaked client secret.

To mitigate this risk:

  * Protect client secrets like passwords and never store them as plain text
  * Implement secure credential management using [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview)
  * Monitor access to your IAP resources with [Cloud Audit Logging](https://docs.cloud.google.com/logging/docs/audit)
  * A leaked client secret only impacts authentication, not authorization to access resources. If you suspect your secret was leaked, reset it immediately.



For programmatic access to IAP-protected resources, consider using [service account JWT authentication](https://docs.cloud.google.com/iap/docs/authentication-howto) instead of sharing OAuth client secrets with individual users. This approach provides better security isolation while maintaining the benefits of a shared OAuth client for your applications.

### Permission scope considerations

When sharing OAuth clients, all applications use the same permission scopes. For IAP, `openid` and `email` are the only required scopes. This consideration by itself isn't a significant risk, but it's important to understand:

  * OAuth is only used for **authentication** (verifying identity) in IAP; **authorization** (resource access) is handled separately through [IAM policies](https://docs.cloud.google.com/iap/docs/managing-access)
  * Even if authentication credentials are compromised, an attacker would still need appropriate IAM permissions to access protected resources
  * Restricting the client to only the required `openid` and `email` scopes helps limit potential security impact



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
