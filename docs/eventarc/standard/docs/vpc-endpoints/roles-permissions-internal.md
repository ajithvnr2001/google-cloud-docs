---
url: https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/roles-permissions-internal/
title: Roles and permissions for an internal HTTP endpoint in a VPC network \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:29.817075+00:00
---

# Roles and permissions for an internal HTTP endpoint in a VPC network  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/roles-permissions-internal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Roles and permissions for an internal HTTP endpoint in a VPC network Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

This document shows you how to grant Identity and Access Management (IAM) roles and permissions to support routing events from Google Cloud to an [internal HTTP endpoint](https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/route-vpc-internal-endpoint-events) in a Virtual Private Cloud (VPC) network using Eventarc.

**Note:** If you want to attach a service account in one project to an Eventarc trigger in another project, you must first complete the steps outlined in [Support a cross-project service account](https://docs.cloud.google.com/eventarc/docs/use-cross-project-service-account). 

  1. Grant project-wide permissions to the principal invoking the Eventarc APIs (for example, the Eventarc trigger creator):

     1. The **Eventarc Admin** role allows you full control over all Eventarc resources, including specifying a service account for the trigger when you create it.
     2. The **Service Account User** role allows a principal to impersonate and use a service account. The service account is associated with an Eventarc trigger and represents the identity of the trigger.
  2. Grant Eventarc trigger permissions to the trigger service account: The **Eventarc Event Receiver** role allows your Eventarc trigger to receive events from event providers. You don't need to grant the role if you are routing direct events from Cloud Pub/Sub.

  3. Grant permissions to Google service agents:

     1. If the URI of the internal HTTP endpoint uses the internal DNS name of a service resolvable by Cloud DNS, grant the **Cloud DNS Peer** role.
     2. If you are creating a trigger for direct events from Cloud Storage, grant the **Pub/Sub Publisher** role.
     3. If you enabled the Cloud Pub/Sub service agent on or before April 8, 2021, grant the **Service Account Token Creator** role.



For more information about granting IAM roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Grant project-wide permissions

If you are the project creator, you are granted the [basic Owner role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`). By default, this role includes the permissions necessary for full access to most Google Cloud resources. Otherwise, required roles must be granted by an administrator on the appropriate resource to the appropriate _principal_ (also known as a member).

For example, a principal can be a Google Account (for end users) or a service account (for applications and compute workloads). Each principal has its own identifier, which is typically an email address.

  1. The [Eventarc Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.admin) (`roles/eventarc.admin`) allows you full control over all Eventarc resources.

Grant the role on the project:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=PRINCIPAL \
             --role=roles/eventarc.admin

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `PRINCIPAL`: an identifier for the trigger creator which usually has the following form: `PRINCIPAL_TYPE:ID`. For example, `user:my-user@example.com`. For a full list of the possible `PRINCIPAL_TYPE` values, see the [Policy Binding reference](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy#Binding).
  2. The [Service Account User role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) allows a principal to run operations as a service account.

For example, you need this role so that you can associate a user-managed service account with an Eventarc trigger. You also need it so that you can act as the [runtime service account](https://docs.cloud.google.com/run/docs/securing/service-identity#runtime_service_account) when deploying a Cloud Run service. For more information, see [Service account impersonation](https://docs.cloud.google.com/iam/docs/service-account-overview#impersonation).

You can either grant the role on the project to allow the principal to impersonate multiple service accounts or grant the role on the service account to allow the principal to impersonate only a specific service account.

Grant the role on the project:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=PRINCIPAL \
             --role=roles/iam.serviceAccountUser

Or, grant the role on the service account:
         
         gcloud iam service-accounts add-iam-policy-binding \
             projects/SERVICE_ACCOUNT_PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_NAME@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com \
             --member=PRINCIPAL \
             --role=roles/iam.serviceAccountUser

Replace the following:

     * `SERVICE_ACCOUNT_PROJECT_ID`: the Google Cloud project ID that contains the service account.
     * `SERVICE_ACCOUNT_NAME`: the name of the service account.



## Grant Eventarc trigger permissions

Every Eventarc trigger is associated with an IAM service account at the time the trigger is created. You can specify a user-managed service account that the trigger uses as its default identity. If you don't specify a service account during the trigger's creation, the trigger uses the [Compute Engine default service account](https://docs.cloud.google.com/iam/docs/service-account-types#default) for its identity.

**Caution:** For production environments, we strongly recommend creating a new service account and granting it one or more IAM roles that contain the [minimum permissions required](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#limit-service-account-privileges). You shouldn't use the default service account since it is automatically granted the highly privileged [basic Editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic).

We recommend that you [create your own user-managed service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) to give you greater control and flexibility when managing your trigger.

  1. Create a service account and note its name:
         
         gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \
             --description="DESCRIPTION" \
             --display-name="DISPLAY_NAME"

Replace the following:

     * `SERVICE_ACCOUNT_NAME`: the name of the service account. This name appears in the email address that identifies the service account.
     * `DESCRIPTION`: an optional description of the service account
     * `DISPLAY_NAME`: a service account name to display in the Google Cloud console
  2. Grant the [Eventarc Event Receiver role](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.eventReceiver) (`roles/eventarc.eventReceiver`) on the project to the service account associated with your Eventarc trigger so that the trigger can receive events from event providers.

Note that you don't need to grant the Eventarc Event Receiver role if you are routing [direct events from Cloud Pub/Sub](https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/receive-vpc-internal-endpoint).
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/eventarc.eventReceiver

Replace `SERVICE_ACCOUNT_NAME` with the name of your service account that you noted in the previous step.




## Grant permissions to service agents

Some Google Cloud services have [_service agents_](https://docs.cloud.google.com/iam/docs/service-agents) that allow the services to access your resources. If an API requires a service agent, then Google creates the service agent after you activate and use the API.

  1. **If the URI of the internal HTTP endpoint in the VPC network uses the[internal DNS name](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names) of a service resolvable by Cloud DNS**, to access target networks with DNS peering zones, grant the [DNS Peer role](https://docs.cloud.google.com/iam/docs/roles-permissions/dns#dns.peer) (`roles/dns.peer`) on the VPC host project to the Eventarc service agent:
         
         gcloud projects add-iam-policy-binding VPC_HOST_PROJECT_ID \
             --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-eventarc.iam.gserviceaccount.com \
             --role=roles/dns.peer

Replace the following:

     * `VPC_HOST_PROJECT_ID`: the Google Cloud project ID for the VPC host project. When you use [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) you attach one or more service projects to the host project, allowing resources from multiple projects to connect to a common VPC network.

Note that depending on how you have configured the VPC network, the VPC host project might also be your Eventarc trigger project.

     * `PROJECT_NUMBER`: the Google Cloud project number for your Eventarc trigger project. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:
           
           gcloud projects describe PROJECT_ID --format='value(projectNumber)'

  2. **If you are creating a trigger for direct events from Cloud Storage** , to support publishing messages to a topic, grant the [Pub/Sub Publisher role](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`) on the project to the Cloud Storage service agent:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:service-PROJECT_NUMBER@gs-project-accounts.iam.gserviceaccount.com \
             --role=roles/pubsub.publisher

Replace `PROJECT_NUMBER` with your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:
         
         gcloud projects describe PROJECT_ID --format='value(projectNumber)'

  3. **If you enabled the Cloud Pub/Sub service agent on or before April 8, 2021** , to support authenticated Pub/Sub push requests, grant the [Service Account Token Creator role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) on the project to the Pub/Sub service agent. Otherwise, this role is granted by default:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com \
             --role=roles/iam.serviceAccountTokenCreator




## What's next

  * Learn about [access control options in Eventarc](https://docs.cloud.google.com/eventarc/docs/access-control).

  * Learn about [best practices for using service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).

  * Learn how to [describe a trigger and verify its associated service account](https://docs.cloud.google.com/eventarc/docs/managing-triggers#trigger-describe).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
