---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/precog-add-environment/
title: Step 3: Create an environment group \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:17:13.683699+00:00
---

# Step 3: Create an environment group  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/precog-add-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 3: Create an environment group Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/precog-add-environment.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/precog-add-environment.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/precog-add-environment.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/precog-add-environment.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/precog-add-environment.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/precog-add-environment.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/precog-add-environment.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/precog-add-environment.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/precog-add-environment.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/precog-add-environment.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/precog-add-environment.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/precog-add-environment.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/precog-add-environment.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/precog-add-environment.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/precog-add-environment.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/precog-add-environment.html)



In this step, you will create an environment and an environment group. 

In Apigee, API proxies are deployed to _environments_ , which provide isolated contexts for your proxies. Environments are organized into _environment groups_ , which provide hostnames for all the proxies deployed to environments within the group. You must have at least one environment and at least one environment group. To learn more, see [About environments and environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview). 

##  Create an environment 

Create the environment first before creating the environment group. You can create an environment using the Apigee UI or using the API. You may want to use the UI for these steps to familiarize yourself with it. 

### Apigee UI

To access the UI and add an environment, perform the following steps:

  1. Open the [Apigee UI](https://apigee.google.com). If this is the first time you are logging in, hybrid displays a consent dialog. If you are prompted to select from more than one account, choose the account that owns the Google Cloud project you are using to install Apigee hybrid. Then click **Allow**.

Your browser navigates to the UI main landing page:

![The landing page in the Apigee
    UI, which consists of left-hand navigation and large images that are links.](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/images/ui-landing.png)

  2. Ensure that your organization is selected from the organization drop-down list. If it is not selected, select it from the drop-down list, as the following example shows: 

![A list of organizations that are hybrid enabled](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/images/ui-project-selector.png)

  3. Click **Admin > Environments > Overview**. 

![The Apigee UI menu showing Admin, Environments, Overview expanded](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/images/hybrid-ui-menu-admin-environments-overview.png)

The **Environments** view is displayed, with no environments (yet):

  4. Click **+Environment**. 

The **New environment** dialog is displayed:

![The new environment dialog](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/images/ui-new-environment.png)

  5. Enter the following information in the **New Environment** dialog: 
     1. **Display name** **(Required)** : A friendly name for the environment that is used in the UI. For example, "My First Environment" or "test". Unlike the **Environment name** , the **Display name** can include uppercase and other special characters. 
     2. **Environment name** **(Required)** : The programmatic name for the environment; also known as the _environment ID_. 

For example, "my-environment" or "test".

**Caution:** An environment name can contain only lowercase letters, numbers, and hyphens. You cannot use uppercase letters or any other special characters. In addition, the **Environment name** can be up to a maximum of 32 characters long. For example: `my-test-env` or `my-test-env-42`. 

The **Display name** and the **Environment name** can be different.

     3. **Description** (_Optional_): Additional information about the environment that you want to add as a reminder of the purpose of the environment. For example, "Created during initial installation".
  6. Keep any other defaults and click **Create**. 

Apigee creates the new environment.

You now need to create an environment group and add your new environment to the group.




### Apigee API

To create an environment with the [Create environments API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments), perform the following steps: 

  1. Open a terminal on the device you are using to manage Apigee.
  2. On the command line, get your `gcloud` authentication credentials using the following command:

###  Linux / MacOS 
         
         export TOKEN=$(gcloud auth print-access-token)

To check that your token was populated, use `echo`, as the following example shows:
         
         echo $TOKEN

This should display your token as an encoded string.

###  Windows 
         
         for /f "tokens=*" %a in ('gcloud auth print-access-token') do set TOKEN=%a

To check that your token was populated, use `echo`, as the following example shows:
         
         echo %TOKEN%

This should display your token as an encoded string.

  3. Create the following environment variable: 

###  Linux / MacOS 
         
         export ENV_NAME="YOUR_ENV_NAME"

###  Windows 
         
         set ENV_NAME="YOUR_ENV_NAME"

Where: 

     * **`ENV_NAME`** **(Required)** The environment name can contain lowercase letters, dashes, and numbers and must start with a lowercase letter. This name will be used as the identifier and cannot be changed after creation of the environment. 
  4. Call the following Apigee API: 
         
         curl -H "Authorization: Bearer **$TOKEN** " -X POST -H "content-type:application/json"   -d '{
             "name": "'"**$ENV_NAME** "'"
           }'   "https://apigee.googleapis.com/v1/organizations/**$ORG_NAME** /environments"

On a successful creation request, the Environments API should respond with a message similar to the following:
         
         {
           "name": "organizations/hybrid-example/operations/c2aee040-7e79-4fd4-b0cf-79ca1b7098a8",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
             "operationType": "INSERT",
             "targetResourceName": "organizations/hybrid-example/environments/example-env",
             "state": "IN_PROGRESS"
           }
         }

As the `state` property in the response indicates, Apigee has started to create the new environment, so its state is `IN_PROGRESS`.

  5. Check to verify the environment was created successfully: 
         
         curl -H "Authorization: Bearer **$TOKEN** " \
                   "https://apigee.googleapis.com/v1/organizations/**$ORG_NAME** /environments"

On a successful creation request, the Environments API responds with a message similar to the following:
         
         [
           "your-environment-name"
         ]




##  Create an environment group 

Now create an environment group and assign the environment you just created to it. 

### Apigee UI

To create an environment group using the Apigee UI, perform the following steps: 

  1. Open the [Apigee UI](https://apigee.google.com). 

Your browser navigates to the Apigee UI main landing page. 

  2. Ensure that your organization is selected from the organization drop-down list. If it is not selected, select it from the drop-down list. 
  3. Click **Admin > Environments > Groups**. 

The **Environment Groups Overview** view is displayed: 

![The Environment groups view](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/images/ui-environment-groups.png)

  4. Click **+Environment Group**. 

The **Add an Environment Group** dialog is displayed. 

![Add Environment Group dialog showing blank Name field](https://docs.cloud.google.com/static/apigee/docs/images/ui-add-environment-group.png)

  5. Enter a name and then click **Add**. 
  6. Hold the pointer over the newly-created environment group and then click **Edit** edit. 

Add a hostname that all proxies deployed to environments within this group will use. This should be a domain you have management access to. The hostname can be the domain itself, like `example.com` or it can include a subdomain like `my-proxies.example.com`.

If you need to register a domain, see a domain registrar like [Google Domains](https://domains.google). 

![Edit Environment Group window showing no environments assigned](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.10/images/ui-edit-environment-group.png)

  7. Click **Add (+)** in the **Environments** box. 
  8. The **Add environment** dialog displays. 

![Add environment dialog listing available environments](https://docs.cloud.google.com/static/apigee/docs/images/ui-add-environment.png)

  9. Select an environment from the list and then click **Add**. 
  10. Click **Save**. 



### Apigee API

To create an environment group using the Apigee API: 

  1. On the command line, get your `gcloud` authentication credentials using the following command:

###  Linux / MacOS 
         
         TOKEN=$(gcloud auth print-access-token)

###  Windows 
         
         for /f "tokens=*" %a in ('gcloud auth print-access-token') do set TOKEN=%a

  2. Create the following environment variables: 

###  Linux / MacOS 
         
         export DOMAIN="YOUR_DOMAIN"
         export ENV_GROUP="YOUR_ENVIRONMENT_GROUP"

###  Windows 
         
         data-terminal-prefix=">">set ENV_GROUP="YOUR_ENVIRONMENT_GROUP"
          data-terminal-prefix=">">set DOMAIN="YOUR_DOMAIN"

Where: 

     * **`DOMAIN`** **(Required)** This is the hostname that all proxies deployed to environments within this group will use. This should be a domain you manage. The address can be the domain itself, like `example.com` or it can include a subdomain like `my-proxies.example.com`. If you don't have a managed domain, you can enter a placeholder for now. You can change the domain address later.
     * **`ENV_GROUP`** **(Required)** The environment name can contain lowercase letters, dashes, and numbers and must start with a lowercase letter. This name will be used as the identifier and cannot be changed after creation. 
  3. Create the environment group: 
         
         curl -H "Authorization: Bearer **$TOKEN** " -X POST -H "content-type:application/json" \
            -d '{
              "name": "'"**$ENV_GROUP** "'",
              "hostnames":["'"**$DOMAIN** "'"]
            }' \
            "https://apigee.googleapis.com/v1/organizations/**$ORG_NAME** /envgroups"
             

  4. Assign the environment to the new group: 
         
         curl -H "Authorization: Bearer **$TOKEN** " -X POST -H "content-type:application/json" \
            -d '{
              "environment": "'"**$ENV_NAME** "'",
            }' \
            "https://apigee.googleapis.com/v1/organizations/**$ORG_NAME** /envgroups/**$ENV_GROUP** /attachments"
             

  5. Verify whether the environment group was created successfully with the following CURL command: 
         
         curl -H "Authorization: Bearer **$TOKEN** " \
           "https://apigee.googleapis.com/v1/organizations/**$ORG_NAME** /envgroups"

On a successful creation request, the Environments Group API responds with a message similar to the following:
         
         {
                 "environmentGroups": [
                   {
                     "name": "your_envgroup_hybrid",
                     "hostnames": [
                       "apigee.hybrid.com"
                     ],
                     "createdAt": "1677826235324",
                     "lastModifiedAt": "1677826235324",
                     "state": "ACTIVE"
                   }
                 ]
               }
             

  6. Fetch the latest attachments for the newly created environment group by using following CURL command: 
         
         curl -H "Authorization: Bearer **$TOKEN** " \
           "https://apigee.googleapis.com/v1/organizations/**$ORG_NAME** /envgroups/**$ENV_GROUP** /attachments"

The environment group creation and attachment were successful if the result shows a unique hash value, as shown in the below sample response output:
         
         {
                   "environmentGroupAttachments": [
                     {
                       "name": "c27046d1-b83e-4cba-xxxx-caaa660b2bd6",
                       "environment": "your_envtest_hybrid",
                       "createdAt": "1677826263567",
                       "environmentGroupId": "your_envgroup_hybrid"
                     }
                   ]
                 }
                 




## Next step

To continue with the installation, go to [Part 2: Hybrid runtime setup](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-before-begin).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
