---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/environment-delete/
title: Delete environments \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:20:18.097667+00:00
---

# Delete environments  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/environment-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Delete environments Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.15 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.15 keyboard_arrow_down

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

##  How to delete an environment 

Assume that you have two environments, **test** and **prod**. In your overrides file, the definitions might look something like this: 
    
    
    ...
    envs:
      - name: test
        serviceAccountPaths:
          synchronizer: "your_keypath/synchronizer-manager-service-account.json
          udca: "your_keypath/analytic-agent-service-account.json
      - name: prod
        serviceAccountPaths:
          synchronizer: "your_keypath/synchronizer-manager-service-account.json
          udca: "your_keypath/analytic-agent-service-account.json
    ...

**Note:** See: 

  * [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/config-prop-ref#envs-name)
  * [`envs[].serviceAccountPaths.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/config-prop-ref#envs-serviceaccountpaths-synchronizer)
  * [`envs[].serviceAccountPaths.udca`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/config-prop-ref#envs-saactpaths-udca)



To delete the **prod** environment, follow these steps: 

  1. Get your gcloud authentication credentials: 
         
         TOKEN=$(gcloud auth print-access-token)

  2. Delete the environment from any associated environment groups, one at a time: 

### No data residency
         
         curl -X DELETE -H "Authorization: Bearer $TOKEN" \
           "https://apigee.googleapis.com/v1/organizations/$ORG_NAME/envgroups/$ENV_GROUP/attachments/prod"

### Data residency
         
         curl -X DELETE -H "Authorization: Bearer $TOKEN" \
           "https://$CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/$ORG_NAME/envgroups/$ENV_GROUP/attachments/prod"

  3. Do a dry run to test removal of the runtime components: 
         
         helm delete $ENV_NAME -n APIGEE_NAMESPACE --dry-run=server
         

The `--dry-run` command will return the same results as the command without the `--dry-run` option. For example:
         
         helm -n apigee delete example-env
         release "example-env" uninstalled

  4. If the dry run is error-free, remove the runtime components: 
         
         helm delete $ENV_NAME -n APIGEE_NAMESPACE
         

  5. Open your overrides file and remove the `prod` environment definition from `envs` and `virtualhosts`, leaving only the **test** definitions. For example: 
         
         ...
         envs:
           - name: test
             serviceAccountPaths:
               synchronizer: "your_keypath/synchronizer-manager-service-account.json
               udca: "your_keypath/analytic-agent-service-account.json
         ...

  6. Save the file.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
