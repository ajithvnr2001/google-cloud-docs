---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/precog-add-environment/
title: Step 3: Create an environment group \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:26:02.372329+00:00
---

# Step 3: Create an environment group  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/precog-add-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 3: Create an environment group Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.15 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.15 keyboard_arrow_down

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

To create a new environment in the Apigee UI:

  1. In the Apigee UI, go to **Management > Environments**. 

[Go to Environments](https://console.cloud.google.com/apigee/environments)

  2. In the **Environments** pane, click **\+ Create Environment**.
  3. In the **Create an environment** pane, enter the following: 
     * **Name** : The programmatic environment name. The **Name** can't be changed after it is created.

The name must contain between 2 and 32 characters which can be lower-case letters, numbers, or hyphens. The name must begin with a letter and cannot end with a hyphen. The name must be different from any other environment name in your organization.

     * **Display Name** : The name for the environment that is displayed in the UI.
     * **Description** : Optional. A description of the environment.
     * **Instance** : Leave the **Instance** field blank. Instances do not apply to Apigee hybrid installations.
     * **Environment group** : Leave the **Environment group** field blank for now. You will create an environment group in the next procedure.
     * **Deployment type** : For most Apigee hybrid installations, select the option to deploy individual API proxies. You can optionally deploy an archive of your API proxy configuration environment. For more information, see [Supported deployment types](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#deployment-types). **Note** : The deployment type used with this environment cannot be changed after the environment is created.
  4. Click **Create**.

**Note:** This operation to create the environment may take up to five minutes.

Once complete, the new environment is displayed in the table in the **Environments** pane.

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

### No data residency
         
         curl -H "Authorization: Bearer **$TOKEN** " -X POST -H "content-type:application/json"   -d '{
             "name": "'"**$ENV_NAME** "'"
           }'   "https://apigee.googleapis.com/v1/organizations/**$ORG_NAME** /environments"

### Data residency
         
         curl -H "Authorization: Bearer **$TOKEN** " -X POST -H "content-type:application/json"   -d '{
             "name": "'"**$ENV_NAME** "'"
           }'   "https://**$CONTROL_PLANE_LOCATION** -apigee.googleapis.com/v1/organizations/**$ORG_NAME** /environments"

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

### No data residency
         
         curl -H "Authorization: Bearer **$TOKEN** " \
                   "https://apigee.googleapis.com/v1/organizations/**$ORG_NAME** /environments"

### Data residency
         
         curl -H "Authorization: Bearer **$TOKEN** " \
                   "https://**$CONTROL_PLANE_LOCATION** -apigee.googleapis.com/v1/organizations/**$ORG_NAME** /environments"

On a successful creation request, the Environments API responds with a message similar to the following:
         
         [
           "your-environment-name"
         ]




##  Create an environment group 

Now create an environment group and assign the environment you just created to it. 

### Apigee UI

To create a new environment group in the Apigee UI:

  1. In the Apigee UI, go to **Management > Environments > Environment Groups**. 

[Go to Environment Groups](https://console.cloud.google.com/apigee/environments/groups)

  2. In the **Environments** pane, select **Environment Groups**.
  3. Click **\+ Create Environment Group**.
  4. Enter the following: 
     * **Environment group name** : A name for the environment group. The name must start and end with an alphanumeric character. It can have up to 63 characters consisting of alphanumeric characters and hyphens. The name must be different from any existing environment group name in your organization.
  5. **Hostames** : A list of host names that can be used to call proxies. Each host name must be on a separate line.

**Note:** The names assigned to an environment group must be unique to that group: they can't be used by other environment groups.

You also have the option to click **Configure Google Load Balancer with these domains**. This opens the **Load balancing** page in the Cloud console, where you can configure load balancing for the host names.

  6. **Environments** : An optional list of environments to include in the environment group.
  7. Click **Create**.

**Note:** This operation may take up to five minutes.

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

### No data residency
         
         curl -H "Authorization: Bearer **$TOKEN** " -X POST -H "content-type:application/json" \
            -d '{
              "name": "'"**$ENV_GROUP** "'",
              "hostnames":["'"**$DOMAIN** "'"]
            }' \
            "https://apigee.googleapis.com/v1/organizations/**$ORG_NAME** /envgroups"
             

### Data residency
         
         curl -H "Authorization: Bearer **$TOKEN** " -X POST -H "content-type:application/json" \
            -d '{
              "name": "'"**$ENV_GROUP** "'",
              "hostnames":["'"**$DOMAIN** "'"]
            }' \
            "https://**$CONTROL_PLANE_LOCATION** -apigee.googleapis.com/v1/organizations/**$ORG_NAME** /envgroups"
             

  4. Assign the environment to the new group: 

### No data residency
         
         curl -H "Authorization: Bearer **$TOKEN** " -X POST -H "content-type:application/json" \
            -d '{
              "environment": "'"**$ENV_NAME** "'",
            }' \
            "https://apigee.googleapis.com/v1/organizations/**$ORG_NAME** /envgroups/**$ENV_GROUP** /attachments"
             

### Data residency
         
         curl -H "Authorization: Bearer **$TOKEN** " -X POST -H "content-type:application/json" \
            -d '{
              "environment": "'"**$ENV_NAME** "'",
            }' \
            "https://**$CONTROL_PLANE_LOCATION** -apigee.googleapis.com/v1/organizations/**$ORG_NAME** /envgroups/**$ENV_GROUP** /attachments"
             

  5. Verify whether the environment group was created successfully with the following CURL command: 

### No data residency
         
         curl -H "Authorization: Bearer **$TOKEN** " \
           "https://apigee.googleapis.com/v1/organizations/**$ORG_NAME** /envgroups"

### Data residency
         
         curl -H "Authorization: Bearer **$TOKEN** " \
           "https://**$CONTROL_PLANE_LOCATION** -apigee.googleapis.com/v1/organizations/**$ORG_NAME** /envgroups"

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

### No data residency
         
         curl -H "Authorization: Bearer **$TOKEN** " \
           "https://apigee.googleapis.com/v1/organizations/**$ORG_NAME** /envgroups/**$ENV_GROUP** /attachments"

### Data residency
         
         curl -H "Authorization: Bearer **$TOKEN** " \
           "https://**$CONTROL_PLANE_LOCATION** -apigee.googleapis.com/v1/organizations/**$ORG_NAME** /envgroups/**$ENV_GROUP** /attachments"

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

To continue with the installation, go to [Part 2: Hybrid runtime setup](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-before-begin).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
