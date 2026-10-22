---
url: https://docs.cloud.google.com/apigee/docs/api-security/enable-security/
title: Getting started \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:53:12.456883+00:00
---

# Getting started  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-security/enable-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Getting started Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page explains how to get started using Advanced API Security for Subscription and Pay-as-you-go organizations.

## Required roles and permissions

The following sections describe the required roles and permissions to perform tasks using Advanced API Security.

### Required roles for security reports

The table below shows the required roles to perform tasks related to [security reports](https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs).

Security Report Task | Required Role(s)  
---|---  
Enable or disable Advanced API Security | [Apigee Organization Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  
Create reports | [Apigee Organization Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  
[Apigee Security Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityAdmin) (`roles/apigee.securityAdmin`)  
View reports | [Apigee Security Viewer](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityViewer) (`roles/apigee.securityViewer`)  
[Apigee Security Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityAdmin) (`roles/apigee.securityAdmin`)  
  
### Required roles for risk assessment

The table below shows the required roles to perform tasks related to [risk assessment](https://docs.cloud.google.com/apigee/docs/api-security/security-scores).

Risk Assessment Task | Required Role(s)  
---|---  
Create, update, or delete a custom security profile | [Apigee Security Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityAdmin) (`roles/apigee.securityAdmin`)  
[Apigee Organization Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  
Attach or detach a security profile | [Apigee Security Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityAdmin) (`roles/apigee.securityAdmin`)  
[Apigee Organization Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  
View security scores | [Apigee Security Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityAdmin) (`roles/apigee.securityAdmin`)  
[Apigee Security Viewer](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityViewer) (`roles/apigee.securityViewer`)  
[Apigee Organization Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  
List all security profiles or get a profile | [Apigee Security Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityAdmin) (`roles/apigee.securityAdmin`)  
[Apigee Security Viewer](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityViewer) (`roles/apigee.securityViewer`)  
[Apigee Organization Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  
Create, update, or delete a security monitoring condition | [Apigee Security Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityAdmin) (`roles/apigee.securityAdmin`)  
[Apigee Organization Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  
List and view security monitoring conditions | [Apigee Security Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityAdmin) (`roles/apigee.securityAdmin`)  
[Apigee Security Viewer](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityViewer) (`roles/apigee.securityViewer`)  
[Apigee Organization Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  
List and view security monitoring condition metrics |  [Monitoring Admin](https://docs.cloud.google.com/monitoring/access-control#monitoring.admin) (`roles/monitoring.admin`)  
[Monitoring Editor](https://docs.cloud.google.com/monitoring/access-control#monitoring.editor) (`roles/monitoring.editor`)   
Create, update, or delete monitoring alerts | See [Required roles (for security alerts)](https://docs.cloud.google.com/apigee/docs/api-security/security-alerts#required-roles)  
View monitoring alerts | See [ Incidents for metric-based alerting policies: Before you begin](https://docs.cloud.google.com/monitoring/alerts/incidents-events#before-you-begin)  
  
### Required roles and permissions for abuse detection

The table below shows the required roles and permissions to perform tasks related to [abuse detection](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection).

Abuse Detection Task | Required Role(s) and Permission(s)  
---|---  
View incidents in the Abuse detection UI  | [Apigee Security Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityAdmin) (`roles/apigee.securityAdmin`)  
[Apigee Security Viewer](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityViewer) (`roles/apigee.securityViewer`)  
[Apigee Organization Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  
Opt an organization in or out of [machine learning models for abuse detection](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#help-improve-your-machine-learning-models-for-abuse-detection) |  `apigee.securitySettings.update` permission  
[Apigee Security Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityAdmin) (`roles/apigee.securityAdmin`)  
[Apigee Organization Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)   
  
### Required roles for security actions

The table below shows the required roles to perform tasks related to [security actions](https://docs.cloud.google.com/apigee/docs/api-security/security-actions).

Security Action Task | Required Role(s)  
---|---  
Create, edit, or delete security action configurations | [Apigee Security Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityAdmin) (`roles/apigee.securityAdmin`)  
[Apigee Organization Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  
View or list security actions | [Apigee Security Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityAdmin) (`roles/apigee.securityAdmin`)  
[Apigee Security Viewer](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityViewer) (`roles/apigee.securityViewer`)  
[Apigee Organization Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  
Check the state of enforcement | [Apigee Security Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityAdmin) (`roles/apigee.securityAdmin`)  
[Apigee Security Viewer](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityViewer) (`roles/apigee.securityViewer`)  
[Apigee Organization Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  
**Note:** To make the API calls described in the following sections, you need to [obtain an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20), which is passed with the calls.

## Manage Advanced API Security for Subscription organizations

To use Advanced API Security as a Subscription customer, Advanced API Security must be part of your Subscription entitlements. See [Apigee entitlements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements). To add Advanced API Security to your entitlements, contact [Apigee Sales](https://pages.apigee.com/contact-sales-reg.html).

**Note:** Apigee trial organizations can include an Apigee Advanced API Security trial for the trial period. Contact Apigee [Apigee Sales](https://pages.apigee.com/contact-sales-reg.html) for information.

Once Advanced API Security is part of your entitlements, enable it in your organization:

  * Get your Apigee add-ons configuration
  * Enable Advanced API Security for Subscription organizations



If you are unsure whether you are using a Subscription or Pay-as-you-go Apigee organization, contact your Apigee organization administrator.

### Get your Apigee add-ons configuration

In order to enable Advanced API Security for your Subscription organization, you first need to get your current Apigee add-ons configuration, using the following API call. This will also tell you whether Advanced API Security is already enabled.
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG" \
      -X GET \
      -H "Content-type: application/json" \
      -H "Authorization: Bearer $TOKEN"

where

  * ORG is the name of your organization.
  * `$TOKEN` is the environment variable for an [OAuth access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20).



This call returns basic information about your organization, including a section for your Apigee add-ons configuration that begins with the line:
    
    
    "addonsConfig": {

Check to see whether this section contains the following entry:
    
    
    "apiSecurityConfig": {
              "enabled": true
          }

If so, Advanced API Security is already enabled in the organization. Otherwise, you need to enable it, as described next.

### Enable Advanced API Security for Subscription organizations

To enable Advanced API Security in a Subscription organization with the default configuration, issue a `POST` request like the one shown below.

**Caution:** This API call overwrites the current add-ons configuration. You must include the current configuration for all add-ons in the request shown below to prevent them from being overwritten.**Notes:**

  * If you create a new environment after enabling Advanced API Security, you must run the command below again to enable Advanced API Security for the new environment. Note that it is _not_ necessary to disable Advanced API Security before running the command again.
  * If you simply detach an environment in which Advanced API Security is enabled from an instance, and then later reattach it, you do _not_ need to run the command below again.


    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG:setAddons" \
      -X POST \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
        "addonsConfig": {
          "apiSecurityConfig": {
              "enabled": true
          }
          <Other entries of your current add-ons configuration>
        }
      }'

where

  * ORG is the name of your organization.
  * `$TOKEN` is the environment variable for an [OAuth access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20).
  * `<Other entries of your current add-ons configuration>` consists of any other entries of your current Apigee add-ons configuration.

**Note:** The API call above starts a long running operation that may take a while to complete.

For example, if the current add-ons configuration is
    
    
    "addonsConfig": {
      "integrationConfig": {
          "enabled":true
      },
      "monetizationConfig": {
          "enabled":true
      }
    },

the command to enable Advanced API Security would be 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG:setAddons" \
      -X POST \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
        "addonsConfig": {
          "apiSecurityConfig": {
              "enabled": true
          },
          "integrationConfig": {
              "enabled": true
          },
          "monetizationConfig": {
              "enabled": true
          }
        }
      }'

After you send the request, you will see a response like the following:
    
    
    {
      "name": "organizations/apigee-docs-d/operations/0718a945-76e0-4393-a456-f9929603b32c",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
        "operationType": "UPDATE",
        "targetResourceName": "organizations/apigee-docs-d",
        "state": "IN_PROGRESS"
      }
    }

**Note:** When you enable Advanced API Security in an organization, it can take up to a day for the scores for existing proxies and targets to be reflected in an environment. 

### Disable Advanced API Security for Subscription organizations

If for some reason you need to disable Advanced API Security in your Subscription organization, you can do so by issuing a `POST` request, passing the add-ons configuration in your request body, as shown below.

**Caution:** The add-ons configuration that you pass in the request body will **overwrite** the current add-ons configuration. [View the current add-ons configuration](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/get) in the Apigee organization profile and be sure to include it in the request payload. **Note:** The API call below starts a long running operation that may take a while to complete.
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** :setAddons" \
      -X POST \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
        **"addonsConfig": {
          "apiSecurityConfig": {
              "enabled": false
          } <_Include current add-ons configuration_ >**
        }
      }'

The following provides an example of the response showing that the operation is in progress: 
    
    
    {
      "name": "organizations/**$ORG** /operations/06274ffb-8940-41da-836d-781cba190437",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
        "operationType": "UPDATE",
        "targetResourceName": "organizations/**$ORG** ",
        "state": "IN_PROGRESS"
      }
    }

For more information, see the [Configure organization add-ons API](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/setAddons). 

## Manage Advanced API Security for Pay-as-you-go organizations

If you are a [Pay-as-you-go](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview) customer, you can enable Advanced API Security as a paid add-on. For more information on enabling the Advanced API Security add-on for your Intermediate or Comprehensive Apigee environments, see [ Manage the Advanced API Security add-on](https://docs.cloud.google.com/apigee/docs/api-platform/reference/manage-security-add-on). 

If you are unsure whether you are using a Subscription or Pay-as-you-go Apigee organization, contact your Apigee organization administrator.

## Manage Advanced API Security for eval organizations

The Advanced API Security add-on is automatically included with Apigee [trial (evaluation)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/overview-eval) organizations, but you'll need to enable it.

To enable it, follow the instructions in Enable Advanced API Security for Subscription organizations.

If you need to disable it, follow the instructions in Disable Advanced API Security for Subscription organizations.

## Configure Advanced API Security using Terraform

Apigee supports using to manage some Advanced API Security functionality.

For example, you can use Terraform to configure:

  * [ Risk Assessment v2 security profiles](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_security_profile_v2)
  * [ Risk Assessment v2 security monitoring conditions](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_security_monitoring_condition)
  * [ Abuse detection exclusion lists](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_security_feedback)
  * [ Security actions](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_security_action)



For information on the currently supported functionality, see the **Apigee** section of the [ Terraform Registry](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_security_action). Advanced API Security-related resource names start with `google_apigee_security`.

For general information on using Terraform with Apigee, see [Use Terraform with Apigee.](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/terraform-overview)

## Next steps

Once you have enabled Advanced API Security, see:

  * [Security reports](https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs)
  * [Risk assessment](https://docs.cloud.google.com/apigee/docs/api-security/security-scores)
  * [Abuse detection](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection)
  * [Security alerts](https://docs.cloud.google.com/apigee/docs/api-security/security-alerts)
  * [Security actions](https://docs.cloud.google.com/apigee/docs/api-security/security-actions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
