---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/retail-api-tutorials-troubleshooting/
title: Troubleshoot tutorial issues \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:41.232937+00:00
---

# Troubleshoot tutorial issues  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/retail-api-tutorials-troubleshooting/

  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



#  Troubleshoot tutorial issues Stay organized with collections  Save and categorize content based on your preferences. 

If you run into problems configuring your tutorial, this page lists issues that you might encounter and provides suggestions for how to fix each issue.

## The cloudshell_open folder is missing

If you can't see the cloudshell_open folder in your home directory by running `ls ~`, the folder and its files are lost. This issue occurs when you use Cloud Shell in Ephemeral mode and lose your Internet connection or refresh the page. To resolve this issue, rerun the tutorial from the beginning. To avoid the loss of your files in the future, consider switching to Default mode.

## Unable to detect a project ID in the current environment

The following error occurs when you attempt to run a code sample:
    
    
    ERROR Unable to detect a Project Id in the current environment.
    

This issue occurs when your Google Cloud project isn't set. To resolve this issue, set the project by running the following command:
    
    
    gcloud config set project <YOUR-PROJECT-ID>
    

## key.json errors when running code samples

One of the following errors occurs when you run code samples:
    
    
    File /home/user/key.json is not a valid json file
    
    
    
    no JSON input found
    
    
    
    The file at /home/user/key.json does not exist, or it is not a file
    
    
    
    Could not find file '/home/user/key.json'
    
    
    
    Error reading credential file from location /home/user/key.json: Value cannot be null
    

This issue occurs when the key.json file, which is used to authenticate a service account, is empty or missing. You can check if that's the case by running the following command:
    
    
    cat ~/key.json
    

This prints either the file's contents or the `No such file or directory` message. An empty file means that the error occurred during key creation. A missing file means that the error occurred before that. To resolve this issue, follow the "Prepare your work environment" tutorial step.

## AI Commerce Search has not been used in project before or it is disabled

This following error occurs when you attempt to run a tutorial:
    
    
    PERMISSION_DENIED: AI Commerce Search API has not been used in project <YOUR-PROJECT-ID> before or it is disabled
    

To resolve this issue, enable the AI Commerce Search on the [API/Services Details](https://console.cloud.google.com/apis/api/retail.googleapis.com/) page of the Google Cloud console, or run the following command:
    
    
    gcloud services enable \
        retail.googleapis.com \
        --project=<YOUR-PROJECT-ID>
    

## Service account does not have permission to access project instance

The following error occurs when you assign roles to the service account:
    
    
    User [USER@YOUR-PROJECT-ID.] does not have permission to access projects instance [YOUR-PROJECT-ID:setIamPolicy] (or it may not exist): Policy update access denied.
    

To resolve this issue, check that you have the right account active by running the `gcloud auth list` command in the Terminal. Ensure that the active account is the service account. Go to the [IAM](https://console.cloud.google.com/iam-admin/iam) page in the Google Cloud console to check that the service account is an owner of your Google Cloud project.

## Invalid authentication using end user credentials

The following error occurs when you run code samples:
    
    
    PERMISSION_DENIED: Your application has been authenticated using end user credentials from the Google Cloud SDK or Google Cloud Shell which are not supported by the retail.googleapis.com.
    

This issue occurs when end user credentials are used instead of a service account. This issue can also occur when a service account isn't active or the required environment variables aren't set. You might see this error after restarting Cloud Shell or opening a new Terminal window.

To resolve this issue:

  1. Follow the "Prepare your work environment" tutorial steps and make sure you have a service account active by running `gcloud auth list`.
  2. Set the environment variables:

     1. For all languages, run the command:
    
    export GOOGLE_APPLICATION_CREDENTIALS=~/key.json
    

     1. Additionally for .NET, run the command:
    
    export GOOGLE_PROJECT_ID=<YOUR-PROJECT-ID>
    




## Permissions error when service account doesn't have needed roles

The following error occurs when you run code samples:
    
    
    google.api_core.exceptions.PermissionDenied: 403 Permission 'retail.<YOUR-REQUEST>' denied on resource '//retail.googleapis.com/projects/<YOUR-PROJECT-ID>/locations/<YOUR-LOCATION>' (or it may not exist). [reason: "IAM_PERMISSION_DENIED"
    

This issue occurs when your service account doesn't have the required roles: retail.admin and editor. To resolve this issue, set up your work environment by following the "Prepare your work environment" tutorial steps.

## The search operation returned no matching results

This issue occurs when no products in the catalog match your search query or the product catalog is empty. To resolve this issue, check to see if you have products in your catalog on the [Catalog](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/data/catalog) page of the Google Cloud console. If you do not, import catalog data by following the "Import catalog data" tutorial step.

## There are still problems

Try resetting [Cloud Shell](https://cloud.google.com/shell/docs/resetting-cloud-shell) and run tutorials from the beginning.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
