---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/update-environment-types/
title: Update Pay-as-you-go environment types \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:39:15.198809+00:00
---

# Update Pay-as-you-go environment types  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/update-environment-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Update Pay-as-you-go environment types Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee's Pay-as-you-go pricing attributes are based in part upon the [environment types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-environment-types) you attach to your [ Apigee instance](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with#environments-and-instances). You can choose to add [ Base,](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-environment-types#base-env) [Intermediate](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-environment-types#int-env), or [Comprehensive](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-environment-types#comp-env) environments to your Pay-as-you-go organization at any time, tailoring a pricing scheme based on your feature and capacity needs. This topic explains how to upgrade or downgrade the _type_ of an _existing_ environment to add or remove feature capabilities and manage your Apigee Pay-as-you-go billing and resource usage.

## Required roles and permissions

To get the permissions that you need to update a Pay-as-you-go environment type, ask your administrator to grant you the following IAM roles on the project: 

  * Apigee Organization Admin (`apigee.organization.admin`) 
  * Apigee Environment Admin (`apigee.environment.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Update your environment type

You can update the type of an existing Pay-as-you-go environment using the Apigee UI in the Google Cloud console or using the API, as described in the following sections.

### Apigee in Cloud console

To update the type of an existing Pay-as-you-go environment using the Apigee UI in the Google Cloud console: 

  1. Open the **Apigee** page in the console. 

[Go to Apigee](https://cloud.google.com/console/apigee)

  2. Select the project with the Pay-as-you-go organization and environments you want to update.
  3. Select **Management > Environments** to open the **Environments** list page.
  4. In the row for the environment you want to edit, click **Actions** more_vert  and select **Edit**.
  5. In the **Edit environment** dialog, choose an option under **Select environment type**.
  6. Click **Update** to save your changes.
  7. To confirm the change in environment type, refresh the **Environments** list page.



### Apigee API

To update the type of an existing Pay-as-you-go environment using the Apigee API, use the following command: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG_NAME/environments/ENV_NAME?updateMask=type" \
              -H "Authorization: Bearer $token" \
              -X PATCH \
              -H 'Content-Type: application/json' \
              -d '{"type":"ENV_TYPE"}'
            

Where: 

  * ORG_NAME is the name of your Apigee Pay-as-you-go organization.
  * ENV_NAME is the name of the Apigee environment to update.
  * ENV_TYPE is the updated environment type. Options are `BASE`, `INTERMEDIATE`, or `COMPREHENSIVE`.



For example, to upgrade a _Base_ environment named `test-env` to _Comprehensive_ , use the following command: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**my-org** /environments/**test-env**?updateMask=type" \
              -H "Authorization: Bearer $token" \
              -X PATCH \
              -H 'Content-Type: application/json' \
              -d '{"type":"**COMPREHENSIVE** "}'
            

After the operation completes, use the following command to confirm the change in environment type: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG_NAME/environments/ENV_NAME" -H "Authorization: Bearer $token"

This command returns the [environment resource object](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments#resource:-environment), which includes the selected environment type. 

## Error reference

When upgrading or downgrading environment type, the operation will fail if the existing environment contains resources that are incompatible with the newly selected environment type. For more information on available features and limitations by environment type, see [Comparison of environment types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-environment-types#compare-env-table).

If the operation fails, you will see an error with the following format: 
    
    
      {
        "error": {
          "code": "FAILED_PRECONDITION",
          "message": "environment type update invalid: ...<detailed message here >... :failed precondition",
          "status": "FAILED_PRECONDITION"
          }
      }

The following table summarizes possible error messages and potential steps you can take to resolve the issue and upgrade or downgrade the environment type: 

**Failure condition** | **Error message** | **Steps to resolve**  
---|---|---  
Maximum number of environments per organization exceeded | `cannot transfer active environments to INTERMEDIATE, will exceed limit` `cannot transfer active environments to BASE, will exceed limit` | [Delete one or more environments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/delete) from your organization.  
Extensible proxy deployed in the environment | `existing environment has an extensible API` | [ Undeploy the extensible proxy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/undeploy) from the environment.  
Shared flow deployed in the environment | `existing environment has a shared flow` | [ Undeploy the shared flow](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.sharedflows.revisions.deployments/undeploy) from the environment.  
Maximum number of proxy deployment units per environment per region | `pdu count, 50, cannot exceed 20` `pdu count, 425, cannot exceed 50` | Undeploy and delete [ shared flows](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows.revisions/delete) or [ proxies](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis/delete) from the environment.  
Add-ons enabled in the environment | `Existing environment has an addon enabled` | [ Disable the add-ons](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.addonsConfig/setAddonEnablement) in the environment.  
Multi-region support enabled in the environment | `instance attachment count, 2, cannot exceed 1 for BASE environment` `instance attachment count, 2, cannot exceed 1 for INTERMEDIATE environment` | [ Delete the second instance attachment](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.attachments/delete) for the environment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
