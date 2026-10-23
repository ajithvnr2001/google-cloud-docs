---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/environment-delete/
title: Delete environments \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:31.050180+00:00
---

# Delete environments  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/environment-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Delete environments Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/environment-delete.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/environment-delete.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/environment-delete.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/environment-delete.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/environment-delete.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/environment-delete.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/environment-delete.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/environment-delete.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/environment-delete.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/environment-delete.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/environment-delete.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/environment-delete.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/environment-delete.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/environment-delete.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/environment-delete.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/environment-delete.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/environment-delete.html)



This topic explains how to delete environments in Apigee hybrid. See also [About environments and environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview). 

## About environment deletion

Environment deletion is the reverse of [environment creation](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/environment-create) and includes the following tasks: 

  * Remove the environment's runtime components from your cluster and remove the environment from your overrides file.
  * Delete the environment from the management plane using either the [Apigee UI](https://apigee.google.com) or the [Delete environments API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/delete).

**Caution:** If you delete only the runtime components and don't delete the environment in the management plane, the environment still appears in the [Apigee UI](https://apigee.google.com) and in API responses. If you delete the environment in the management plane but don't remove its runtime components, those components stay in your cluster but are no longer usable.

##  How to delete an environment 

Assume that you have two environments, **test** and **prod**. In your overrides file, the definitions might look something like this:
    
    
    ...
    envs:
      - name: test
        serviceAccountPaths:
          synchronizer: "your_keypath/PROJECT_ID-apigee-synchronizer.json"
          runtime: "your_keypath/PROJECT_ID-apigee-runtime.json"
      - name: prod
        serviceAccountPaths:
          synchronizer: "your_keypath/PROJECT_ID-apigee-synchronizer.json"
          runtime: "your_keypath/PROJECT_ID-apigee-runtime.json"
    ...

**Note:** See: 

  * [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#envs-name)
  * [`envs[].serviceAccountPaths.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#envs-serviceaccountpaths-synchronizer)
  * [`envs[].serviceAccountPaths.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#envs-serviceaccountpaths-runtime)



To delete the **prod** environment, follow these steps:

  1. Get your gcloud authentication credentials: 
         
         TOKEN=$(gcloud auth print-access-token)

  2. As a precaution, detach the environment from each environment group that it is attached to. This stops traffic from being routed to the environment before you remove its runtime components. 
     1. List the attachments of the environment group and note the `name` (attachment ID) of the attachment whose `environment` is `prod`: 

### No data residency
            
            curl -H "Authorization: Bearer $TOKEN" \
              "https://apigee.googleapis.com/v1/organizations/ORG_NAME/envgroups/ENV_GROUP/attachments"

### Data residency
            
            curl -H "Authorization: Bearer $TOKEN" \
              "https://CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/ORG_NAME/envgroups/ENV_GROUP/attachments"

The output is similar to the following:
            
            {
              "environmentGroupAttachments": [
                {
                  "name": "**f6f2958f-a0a1-4260-b9e9-80eead82ff1d** ",
                  "environment": "prod",
                  "createdAt": "1789700385118",
                  "environmentGroupId": "ENV_GROUP"
                }
              ]
            }

     2. Delete the attachment: 

### No data residency
            
            curl -X DELETE -H "Authorization: Bearer $TOKEN" \
              "https://apigee.googleapis.com/v1/organizations/ORG_NAME/envgroups/ENV_GROUP/attachments/ATTACHMENT_ID"

### Data residency
            
            curl -X DELETE -H "Authorization: Bearer $TOKEN" \
              "https://CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/ORG_NAME/envgroups/ENV_GROUP/attachments/ATTACHMENT_ID"

Where:

     * ORG_NAME is the name of your Apigee organization.
     * ENV_GROUP is the name of the environment group.
     * ATTACHMENT_ID is the attachment `name` returned in the previous step. This is a generated ID, not the environment name.
     * CONTROL_PLANE_LOCATION is the control plane location of your organization if you use [data residency](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/using-data-residency-with-apigee-hybrid).

Repeat these steps for each environment group that the environment is attached to.

  3. Do a dry run to test removal of the runtime components: 
         
         helm delete ENV_RELEASE_NAME -n APIGEE_NAMESPACE --dry-run
         

     * ENV_RELEASE_NAME is the name with which you previously installed the `apigee-env` chart for this environment. This is often the same as the environment name. To list the release names in your namespace, run `helm list -n APIGEE_NAMESPACE`.
     * APIGEE_NAMESPACE is the namespace where you installed Apigee hybrid, `apigee` by default.

The `--dry-run` option simulates the uninstall without removing anything, and its output is the same as the output of the actual uninstall. Unlike `helm upgrade`, `helm delete` doesn't accept a value for `--dry-run` such as `--dry-run=server`. For example:
    
    helm delete prod -n apigee --dry-run
    release "prod" uninstalled

  4. If the dry run is error-free, remove the runtime components: 
         
         helm delete ENV_RELEASE_NAME -n APIGEE_NAMESPACE
         

  5. Open your overrides file and remove the `prod` environment definition from `envs`, leaving only the **test** definition. For example: 
         
         ...
         envs:
           - name: test
             serviceAccountPaths:
               synchronizer: "your_keypath/PROJECT_ID-apigee-synchronizer.json"
               runtime: "your_keypath/PROJECT_ID-apigee-runtime.json"
         ...

**Note:** Entries in `virtualhosts` are defined per environment group, not per environment, so you don't need to change them. Only remove a `virtualhosts` entry (and uninstall its `apigee-virtualhost` release) if you also delete the environment group.
  6. Save the file.
  7. Delete the environment from the management plane. You can use either the [Apigee UI](https://apigee.google.com) or the [Delete environments API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/delete). 

### [Apigee UI](https://apigee.google.com)

     1. In the Google Cloud console, go to the **Apigee > Management > Environments** page.

[Go to Environments](https://console.cloud.google.com/apigee/environments)

     2. Select the project of your Apigee organization.
     3. In the row of the `prod` environment, click more_vert **Actions > Delete**.

### API

No data residency:
    
    curl -X DELETE -H "Authorization: Bearer $TOKEN" \
      "https://apigee.googleapis.com/v1/organizations/ORG_NAME/environments/prod"

Data residency:
    
    curl -X DELETE -H "Authorization: Bearer $TOKEN" \
      "https://CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/ORG_NAME/environments/prod"

The call returns a long-running operation. Deletion can take a few minutes to complete.

**Note:** Deleting the environment in the management plane also removes any remaining environment group attachments for that environment.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
