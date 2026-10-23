---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/control-api-callers/
title: Controlling who can enable your API \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:23.285617+00:00
---

# Controlling who can enable your API  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/control-api-callers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Controlling who can enable your API Stay organized with collections  Save and categorize content based on your preferences. 

API keys are associated with the Google Cloud project in which they have been created. If your API requires an API key, you either have to give your API users a key from the project that you created the Cloud Endpoints service in, or you can let users enable your API in their own Google Cloud project and create an API key. This page shows you how to grant the permission that users need to enable your API.

## Granting access

Endpoints uses the [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) **Service Consumer** role to allow someone who isn't a member of your Google Cloud project to enable your API in their own Google Cloud project. This section shows you how to grant access using the Google Cloud console or the Google Cloud CLI.

### Google Cloud console

  1. In the Google Cloud console, go to the **Endpoints** > **Services** page for your project. 

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

  2. If you have more than one API, click the name of the API that you want to grant access to. 
  3. If the **Permissions** side panel isn't open, click **Show Permissions Panel**. 
  4. In the **Add Principal** field, enter the email address of the person or [Google Group](https://support.google.com/groups/answer/2464926) that you want to grant access to. 
  5. In the **Select a role** drop-down menu, select **Service Management** > **Service Consumer**.
  6. Click **Save**.
  7. Repeat adding members and selecting the role, as needed.
  8. Contact the users or groups that you added and let them know they can enable the API in their Google Cloud projects. See [Enable an API in your Google Cloud project](https://docs.cloud.google.com/endpoints/docs/frameworks/enable-api) for information on how to enable a service in APIs & services. 



### gcloud

  1. Open Cloud Shell, or if you have the Google Cloud CLI installed, open a terminal window. 
     * If you are granting access to an individual user: 
           
           gcloud endpoints services add-iam-policy-binding [SERVICE-NAME] \
                 --member='user:EMAIL-NAME@gmail.com' \
                 --role='roles/servicemanagement.serviceConsumer'  
  
---  
     * If you are granting access to a Google Group: 
           
           gcloud endpoints services add-iam-policy-binding [SERVICE-NAME] \
                 --member='group:GROUP-NAME@googlegroups.com' \
                 --role='roles/servicemanagement.serviceConsumer'  
  
---  
  2. Contact the users or groups that you added and let them know they can enable the API in their Google Cloud projects. See [Enable an API in your Google Cloud project](https://docs.cloud.google.com/endpoints/docs/frameworks/enable-api) for information on how to enable a service in APIs & services. 



## Revoking access

You revoke access to your API by removing the **Service Consumer** role from a user or group that previously had the role. After you revoke someone's access, they won't be able to enable your API.

**Note:** If someone has already enabled your API, revoking access doesn't prevent them from calling your API. Although there is no easy way to to prevent these calls, you can add logic to your code that disallows calls from a specific caller's API key.

This section shows you how to revoke access using the Google Cloud console or the Google Cloud CLI.

### Google Cloud console

  1. In the Google Cloud console, go to the **Endpoints** > **Services** page for your Google Cloud project. 

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

  2. If you have more than one API, click the name of the API that you want to revoke access to. 
  3. If the **Permissions** side panel isn't open, click **add Permissions**. 
  4. Click the **Role** card that the member belongs to. 
  5. Click **Delete** delete.



### gcloud

  * If you are revoking access for an individual user: 
        
        gcloud endpoints services remove-iam-policy-binding [SERVICE-NAME] \
              --member='user:'EMAIL-NAME@gmail.com' --role='roles/servicemanagement.serviceConsumer'  
  
---  
  * If you are revoking access for a Google Group: 
        
        gcloud endpoints services remove-iam-policy-binding [SERVICE-NAME] \
              --member='group:GROUP-NAME@googlegroups.com' \
              --role='roles/servicemanagement.serviceConsumer'  
  
---  



## What's next

  * Tell users how to [enable your API in their Google Cloud project](https://docs.cloud.google.com/endpoints/docs/frameworks/enable-api).


  * Learn more about sharing APIs protected by API keys.

    * [Java: Sharing APIs protected by API key](https://docs.cloud.google.com/endpoints/docs/frameworks/java/restricting-api-access-with-api-keys-frameworks#sharing_apis_protected_by_api_key)
    * [Python: Sharing APIs protected by API key](https://docs.cloud.google.com/endpoints/docs/frameworks/java/restricting-api-access-with-api-keys-frameworks#sharing_apis_protected_by_api_key)


  * Create a [Cloud Endpoints Portal](https://docs.cloud.google.com/endpoints/docs/frameworks/dev-portal-overview) for your users.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
