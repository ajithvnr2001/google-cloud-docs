---
url: https://docs.cloud.google.com/endpoints/docs/grpc/control-api-access/
title: Granting and revoking access to the API \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:46:09.161224+00:00
---

# Granting and revoking access to the API  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/control-api-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Granting and revoking access to the API Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/control-api-access "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

Controlling who has access to an API is an integral part of development. For example, as you test your API, you might want to automate redeploying updated Cloud Endpoints configurations by using a service account that has the permission to do so. By default, only the project owner can manage access to an API. This page shows you how to grant and revoke access to your API by using the Google Cloud console or the Google Cloud CLI.

Endpoints uses [Identity and Access Management](https://docs.cloud.google.com/iam/docs/overview) roles to grant and revoke access at the API level. You can grant and revoke access to a user, service account, or to a [Google Group](https://support.google.com/groups/answer/2464926).

Google Groups are a convenient way to grant or revoke access to a collection of users. You can grant or revoke access for a whole group at once, instead of granting or revoking access one at a time for individual users or service accounts. You can also easily add members to and remove members from a Google Group instead of granting or revoking the IAM role for each member.

## Granting access

### Google Cloud console

  1. In the Google Cloud console, go to the **Endpoints > Services** page for your project. 

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

  2. If you have more than one API, click the name of the API. 
  3. If the **Permissions** side panel isn't open, click **add Permissions**. 
  4. In the **Add members** box, enter the email address of a user, service account, or Google Group. 
  5. In the **Select a role** drop-down, click **Service Management** , and select one of the following roles: 
     * **Service Consumer:** This role contains the permissions for a non-project member to view and enable the API in their own project. If you have created a [portal](https://docs.cloud.google.com/endpoints/docs/openapi/dev-portal-overview) for your API, this role lets your API users access the portal. 
     * **Service Controller:** This role contains the permissions to make calls to the `check` and ` report` methods in the [Service Infrastructure](https://docs.cloud.google.com/service-infrastructure/docs/checking-status) API during runtime. 
     * **Service Config Editor:** This role contains the minimum permissions that Service Management requires to deploy an Endpoints configuration to an existing service. 
     * **Service Management Administrator:** This role contains the permissions in the Service Config Editor, Service Consumer, and Service Controller roles, plus the permissions required to grant access to this API by using `gcloud` or the programmatic methods described in [ Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

See the [Service Management API access control](https://docs.cloud.google.com/service-infrastructure/docs/service-management/access-control#roles) topic for information about this role. Although the Google Cloud console allows you to select other roles, those roles aren't useful for managing your API. 

  6. To add the member to the specified IAM role, click **Add**. 
  7. Repeat adding members and selecting the role, as needed. 
  8. The Service Management roles don't allow users to access the **Endpoints** > **Services** page in the Google Cloud console. If you want users to be able access the **Endpoints** > **Services** page, you must grant them the **Project Viewer** role or a higher role on the project. See [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) for details. 



### gcloud

  1. Open Cloud Shell, or if you have the Google Cloud CLI installed, open a terminal window. 
  2. Enter the applicable `gcloud` command: 
     * If you are granting access to a user, run the following:  

           
           gcloud endpoints services add-iam-policy-binding [SERVICE-NAME] \
             --member='user:[EMAIL-ADDRESS]' \
             --role='[ROLE]'

For the role, specify one of the following IAM roles: 

       * `roles/servicemanagement.configEditor`: This role contains the minimum permissions that Service Management requires to deploy an Endpoints configuration to an existing service. 
       * `roles/servicemanagement.admin`: This role contains the permissions in `roles/servicemanagement.configEditor`, `roles/servicemanagement.serviceConsumer`, and `roles/servicemanagement.serviceController`, plus the permissions required to grant access to this API by using `gcloud` or the programmatic methods described in [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

For example: 
    
    gcloud endpoints services add-iam-policy-binding example-service-name \
      --member='user:example-user@gmail.com' \
      --role='roles/servicemanagement.admin'

     * If you are granting access to a service account, run the following:  

           
           gcloud endpoints services add-iam-policy-binding [SERVICE-NAME] \
             --member='serviceAccount:[EMAIL-ADDRESS]' \
             --role='[ROLE]'

For example: 
           
           gcloud endpoints services add-iam-policy-binding example-service-name \
             --member='serviceAccount:example-service-account@example-project.iam.gserviceaccount.com' \
             --role='roles/servicemanagement.configEditor'

     * If you are granting access to a Google Group, run the following:  

           
           gcloud endpoints services add-iam-policy-binding [SERVICE-NAME] \
             --member='group:[GROUP-NAME]@googlegroups.com' \
             --role='[ROLE]'

For example: 
           
           gcloud endpoints services add-iam-policy-binding example-service-name \
             --member='group:example-group@googlegroups.com' \
             --role='roles/servicemanagement.configEditor'

  3. The Service Management roles don't allow users to access the **Endpoints** > **Services** page in the Google Cloud console. If you want users to be able access the **Endpoints** > **Services** page, you must grant them the **Project Viewer** role or a higher role on the project. See [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) for details. 



## Revoking access

To revoke access to your API, remove the IAM role from the member who previously had the role.

### Google Cloud console

  1. In the Google Cloud console, go to the **Endpoints** > **Services** page for your project. 

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

  2. If you have more than one API, click the name of the API. 
  3. If the **Permissions** side panel isn't open, click **add Permissions**. 
  4. Locate the member for whom you want to revoke access. You can either click the applicable **Role** card to see a list of members, or you can enter a name or role in the **Search members** box. 
  5. Click **Delete** delete. 
  6. If you also want to revoke a user's access to your Google Cloud project, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) for details. 



### gcloud

  1. Open Cloud Shell, or, if you have the gcloud CLI installed, open a terminal window. 
  2. Enter the applicable `gcloud` command: 
     * If you are revoking access for a user, run the following: 
           
           gcloud endpoints services remove-iam-policy-binding [SERVICE-NAME] \
             --member='user:[EMAIL-ADDRESS]' \
             --role='[ROLE-NAME]'

For example:
           
           gcloud endpoints services remove-iam-policy-binding example-service-name \
             --member='user:example-user@gmail.com' \
             --role='roles/editor'

     * If you are revoking access for a service account, run the following: 
           
           gcloud endpoints services remove-iam-policy-binding [SERVICE-NAME] \
             --member='serviceAccount:[EMAIL-ADDRESS]' \
             --role='[ROLE-NAME]'

For example:
           
           gcloud endpoints services remove-iam-policy-binding example-service-name \
             --member='serviceAccount:example-service-account@example-project.iam.gserviceaccount.com' \
             --role='roles/servicemanagement.configEditor'

     * If you are revoking access for a Google Group, run the following: 
           
           gcloud endpoints services remove-iam-policy-binding [SERVICE-NAME] \
                 --member='group:[GROUP-NAME]@googlegroups.com' \
                 --role='[ROLE-NAME]'

For example:
           
           gcloud endpoints services remove-iam-policy-binding example-service-name \
                 --member='group:example-group@googlegroups.com' \
                 --role='roles/viewer'

  3. If you also want to revoke a user's access to your Google Cloud project, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) for details. 



## What's next

Learn about:

  * [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating_a_service_account)
  * [`gcloud` commands](https://docs.cloud.google.com/sdk/gcloud/reference) referenced on this page.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
