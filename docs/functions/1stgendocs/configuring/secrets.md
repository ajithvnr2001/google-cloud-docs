---
url: https://docs.cloud.google.com/functions/1stgendocs/configuring/secrets/
title: Configure secrets (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:39.190883+00:00
---

# Configure secrets (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/configuring/secrets/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure secrets (1st gen)

You can use [Secret Manager](https://docs.cloud.google.com/secret-manager/docs#docs) to securely store API keys, passwords, and other sensitive information. This guide shows you how to configure Cloud Run functions to access secrets stored in Secret Manager.

This document covers both ways of making a secret available to your function:

  * Mounting the secret as a volume. This makes the secret available to the function as a file. If you reference a secret as a volume, your function accesses the secret value from Secret Manager each time the file is read from disk. This makes mounting as a volume a good strategy if you want to reference the latest version of the secret instead of a pinned version of the secret. This method also works well if you plan to implement [secret rotation](https://docs.cloud.google.com/secret-manager/docs/overview#rotation).

  * Passing the secret as an [environment variable](https://docs.cloud.google.com/functions/1stgendocs/configuring/env-var). Environment variable values are resolved at [instance startup time](https://docs.cloud.google.com/functions/1stgendocs/concepts/execution-environment#cold-starts), so if you use this method, we recommend referencing a pinned version of the secret instead of referencing the latest version of the secret.




For more information on using Secret Manager, see the [Secret Manager overview](https://docs.cloud.google.com/secret-manager/docs/overview). To learn how to create and access secrets, see [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

## Before you begin

  1. Enable the Secret Manager API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=secretmanager.googleapis.com)

  2. If you haven't already, create a secret in Secret Manager, as described in [ Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create).



## Granting access to secrets

Your function can access secrets that reside in the same project as the function as well as secrets that reside in another project. To access a secret, the function's runtime service account must be granted access to the secret.

By default, Cloud Run functions uses the [App Engine default service account](https://docs.cloud.google.com/functions/1stgendocs/securing/function-identity#runtime_service_account) to authenticate with Secret Manager. For production use, Google recommends that you configure your function to authenticate using a [user-managed service account](https://docs.cloud.google.com/iam/docs/service-account-types#user-created) that is assigned the least-permissive set of roles required to accomplish that function's tasks.

To use Secret Manager with Cloud Run functions, assign the `roles/secretmanager.secretAccessor` role to the service account associated with your function:

  1. Go to the Secret Manager page in the Google Cloud console:  
[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager?project=_)

  2. Click the checkbox next to the secret.

  3. If it is not already open, click **Show Info Panel** to open the panel.

  4. In the info panel, click **Add principal**.

  5. In the **New principals** field, enter the service account your function uses for its identity. The function's service account is one of the following:

     * The [user-managed service account](https://docs.cloud.google.com/functions/1stgendocs/securing/function-identity#individual) assigned to the function at deploy time. To learn how to deploy a function with a user-managed service account, see [Using individual service accounts for your function](https://docs.cloud.google.com/functions/1stgendocs/securing/function-identity#individual).

     * The [App Engine default service account](https://docs.cloud.google.com/functions/1stgendocs/concepts/iam#runtime_service_accounts) (not recommended for production use).

  6. In the **Select a role** drop-down, choose **Secret Manager** and then **Secret Manager Secret Accessor**.




## Preparing your function to access secrets

There are two ways of making a secret available to your function:

  * Passing the secret as an environment variable.
  * Mounting the secret as a volume.



### Environment variables

To use environment variables to make secrets available to your function:

  1. Set a runtime [environment variable](https://docs.cloud.google.com/functions/1stgendocs/configuring/env-var#setting_runtime_environment_variables) during function deployment.
  2. Make the secret accessible to your function in an environment variable.
  3. Access the environment variable [programmatically](https://docs.cloud.google.com/functions/1stgendocs/configuring/env-var#setting_and_retrieving_runtime_environment_variables_an_example) at runtime.



### Mounting the secret as a volume

To mount a secret as a volume:

  1. Create a file containing your secret.

  2. Choose an unused, non-system directory such as `/mnt/secrets` as the mount path for your secret. Any pre-existing files or subdirectories in that directory other than your secret and its versions become inaccessible once the secret is mounted.

  3. Make the secret accessible to your function as a mounted volume.

  4. At runtime, programmatically read the file contents to access the secret value.




For example, if the secret has been mounted to `/mnt/secrets/secret1`, then the function has to read this file. Here is an example of how you might read the file synchronously using Node.js:
    
    
    fs.readFileSync('/mnt/secrets/secret1')
    

## Making a secret accessible to a function

In order to reference a secret from a function, you must first make the secret accessible to the function. You can make a secret accessible to new or existing functions using either the Google Cloud console or the Google Cloud CLI:

###  Console 

To make a secret accessible to a function:

  1. Go to the Cloud Run functions page in the Google Cloud console:   
[Go to the Cloud Run functions page](https://console.cloud.google.com/functions)

  2. Click the name of the function you want to be able to access a secret.

  3. Click **Edit**.

  4. Click **Runtime, build ...** to expand the advanced configuration options.

  5. Click **Security and Image Repo** to open the tab.

  6. Click **Add a Secret Reference** to set a secret for the function.

  7. Select the secret to make accessible. If you need to, [create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

     * To reference a secret in the same project as your function:

       1. Select the secret from the drop-down list.
     * To reference a secret from another project:

       1. Verify that your project's service account has been granted access to the secret.

       2. Select **Enter secret manually**.

       3. Enter the secret's resource ID in the following format:

`projects/PROJECT_ID/secrets/SECRET_NAME`

Replace the following:

          * PROJECT_ID: The ID of the project where the secret resides.

          * SECRET_NAME: The name of the secret in Secret Manager.

  8. Select the reference method for the secret. You can mount the secret as a volume or expose the secret as an environment variable.

     * To mount the secret as a volume:

       1. Select **Mounted as volume**.

       2. In the **Mount path** field, enter the mount path for this secret. This is the directory where all versions of your secret are placed.

       3. In the **Path1** field, enter the name of the file to mount. This name is concatenated with the mount path from the previous step to form the full mount path where your secret is mounted.

       4. From the **Version1** drop-down, select the version of the secret to reference.

       5. You can mount additional versions of this secret by clicking **+Add** to define additional paths and the versions of this secret to mount in them.

     * To expose the secret as an environment variable:

       1. Select **Exposed as environment variable**.

       2. In the **Name1** field, enter the name of the environment variable.

       3. From the **Version1** drop-down, select the version of the secret to reference.

       4. You can expose additional versions of this secret to your function by clicking **+Add** to define additional environment variables and the versions of this secret to store in them.

  9. Click **Done**.

  10. Click **Next**.

  11. Click **Deploy**.




Your function's code can now reference the secret.

###  gcloud 

To make a secret accessible to a function, enter one of the following commands.

  * To mount the secret as a volume, enter the following command:
        
        gcloud functions deploy FUNCTION_NAME \
        --no-gen2 \
        --runtime RUNTIME \
        --set-secrets 'SECRET_FILE_PATH=SECRET:VERSION'
        

Replace the following:

    * FUNCTION_NAME: The name of your function.

    * RUNTIME: The [runtime](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) in which to run your function.

    * SECRET_FILE_PATH: The full path of the secret. For example, `/mnt/secrets/primary/latest`, where `/mnt/secrets/primary/` is the mount path and `latest` is the secret path. You can also specify the mount and secret paths separately:

`--set-secrets 'MOUNT_PATH:SECRET_PATH=SECRET:VERSION'`

    * SECRET: The name of the secret in Secret Manager.

    * VERSION: The version of the secret to use. For example, `1` or `latest`.

The `--set-secrets` flag overrides any existing secrets. To keep the function's existing secrets, use the `--update-secrets` flag instead.

  * To expose the secret as an environment variable, enter the following command:
        
        gcloud functions deploy FUNCTION_NAME \
        --no-gen2 \
        --runtime RUNTIME \
        --set-secrets 'ENV_VAR_NAME=SECRET:VERSION'
        

Replace the following:

    * FUNCTION_NAME: The name of your function.

    * RUNTIME: The [runtime](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) in which to run your function.

    * ENV_VAR_NAME: The name of the environment variable.

    * SECRET: The name of the secret in Secret Manager.

    * VERSION: The version of the secret to use. For example, `1` or `latest`.

The `--set-secrets` flag overrides any existing secrets. To keep the function's existing secrets, use the `--update-secrets` flag instead.

  * You can reference a secret from another project if the function's service account has been granted access to the secret. To reference a secret from another project, use the secret's resource path:
        
        gcloud functions deploy FUNCTION_NAME \
        --no-gen2 \
        --runtime RUNTIME \
        --update-secrets 'SECRET_FILE_PATH=SECRET_RESOURCE_PATH:VERSION'
        

Replace the following:

    * FUNCTION_NAME: The name of your function.

    * SECRET_RESOURCE_PATH: The resource path for the secret residing in another project. The resource path uses the following format:

`projects/PROJECT_ID/secrets/SECRET_NAME`

Replace the following:

      * PROJECT_ID: The ID of the project where the secret resides.

      * SECRET_NAME: The name of the secret in Secret Manager.

    * RUNTIME: The [runtime](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) in which to run your function.

    * SECRET_FILE_PATH: The full path of the secret. For example, `/mnt/secrets/primary/latest`, where `/mnt/secrets/primary/` is the mount path and `latest` is the secret path. You can also specify the mount and secret paths separately:

`--set-secrets 'MOUNT_PATH:SECRET_PATH=SECRET:VERSION'`

    * SECRET: The name of the secret in Secret Manager.

    * VERSION: The version of the secret to use. For example, `1` or `latest`.

  * You can update multiple secrets at once. Separate the configuration options for each secret with a comma. The following command updates one secret mounted as a volume and another secret exposed as an environment variable.

To update existing secrets, enter the following command:
        
        gcloud functions deploy FUNCTION_NAME \
        --no-gen2 \
        --runtime RUNTIME \
        --update-secrets 'ENV_VAR_NAME=SECRET:VERSION, \
        SECRET_FILE_PATH=SECRET:VERSION'
        

Replace the following:

    * FUNCTION_NAME: The name of your function.

    * RUNTIME: The [runtime](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) in which to run your function.

    * ENV_VAR_NAME: The name of the environment variable.

    * SECRET: The name of the secret in Secret Manager.

    * VERSION: The version of the secret to use. For example, `1` or `latest`.

    * SECRET_FILE_PATH: The full path of the secret. For example, `/mnt/secrets/primary/latest`, where `/mnt/secrets/primary/` is the mount path and `latest` is the secret path. You can also specify the mount and secret paths separately:

`--set-secrets 'MOUNT_PATH:SECRET_PATH=SECRET:VERSION'`




## Removing secrets from a function

You can remove secrets from a function using either the Google Cloud console or the gcloud CLI:

###  Console 

  1. Go to the Cloud Run functions page in the Google Cloud console:   
[Go to the Cloud Run functions page](https://console.cloud.google.com/functions)

  2. Click the name of the function to remove one of its secrets.

  3. Click **Edit**.

  4. Click **Runtime, build and connections settings** to expand the advanced configuration options.

  5. Click **Security and Image Repo** to open the security tab.

  6. Hold the pointer over the secret you want to remove, then click delete **Delete**.

  7. Click **Next**.

  8. Click **Deploy**.




###  gcloud 

You can remove all secrets from a function or specify one or more secrets to remove:

  * To remove all secrets, run the following command:
        
        gcloud functions deploy FUNCTION_NAME \
        --no-gen2 \
        --runtime RUNTIME \
        --clear-secrets
        

Replace the following:

    * FUNCTION_NAME: The name of your function.

    * RUNTIME: The [runtime](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) in which to run your function.

All secrets are cleared from the function.

  * To specify a list of secrets to remove, use the `--remove-secrets` flag. The following command removes one secret mounted as a volume and another secret exposed as an environment variable:
        
        gcloud functions deploy FUNCTION_NAME \
        --no-gen2 \
        --runtime RUNTIME \
        --remove-secrets='ENV_VAR_NAME,SECRET_FILE_PATH, ...'
        

Replace the following:

    * FUNCTION_NAME: The name of your function.

    * RUNTIME: The [runtime](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) in which to run your function.

    * ENV_VAR_NAME: The name of the environment variable.

    * SECRET_FILE_PATH: The full path of the secret. For example, `/mnt/secrets/primary/latest`, where `/mnt/secrets/primary/` is the mount path and `latest` is the secret path. You can also specify the mount and secret paths separately:

`--set-secrets 'MOUNT_PATH:SECRET_PATH=SECRET:VERSION'`

The specified secrets are removed from the function.




## Viewing your function's accessible secrets

You can see which secrets your function can access using either the Google Cloud console or the gcloud CLI:

###  Console 

  1. Go to the Cloud Run functions page in the Google Cloud console:   
[Go to the Cloud Run functions page](https://console.cloud.google.com/functions)

  2. Click the name of the function to see its available secrets.

  3. Click **Edit**.

  4. Click **Runtime, build and connections settings** to expand the advanced configuration options.

  5. Click **Security** to open the security tab.




The security tab lists the secrets accessible to your function.

###  gcloud 

To see what secrets are available to your function, use the `gcloud functions describe` command:
    
    
    gcloud functions describe FUNCTION_NAME
    

Replace FUNCTION_NAME with the name of your function.

## What's next

  * Consider developing functions that use Secret Manager using the [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
