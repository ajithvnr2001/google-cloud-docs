---
url: https://docs.cloud.google.com/docs/get-started/authentication/
title: Authentication basics \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:27.177964+00:00
---

# Authentication basics  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/get-started/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Authentication basics Stay organized with collections  Save and categorize content based on your preferences. 

Before you can interact with Google Cloud APIs and services, you need to prove that you are who you say you are. This process of proving your identity is known as authentication.

To authenticate to Google Cloud, you must provide _credentials_ as evidence of your identity. For example, to use a service, you might authenticate using credentials such as a password and a one-time code.

Google Cloud refers to authenticated users as _principals_. When you attempt to access a resource such as a Google Cloud project or storage bucket, Google Cloud checks what level of access your principal has to the requested resource. This process is called [_authorization_](https://docs.cloud.google.com/docs/get-started/authorization-access-control), and is handled by a system called Identity and Access Management (IAM).

These same concepts apply to code performing automated tasks on your behalf, which are known as _workloads_. A workload must provide credentials to prove its identity and authenticate as a principal, after which Google Cloud can determine what level of access the workload has to the resources it has requested.

## Principal types

There are different types of principals that you can authenticate as. You might even use different principal types at different stages of a task, or across different development environments.

The primary principal types and the credentials they require to authenticate include the following:

  * **User accounts** : These are [Google Accounts](https://docs.cloud.google.com/iam/docs/principals-overview#google-account) that are for humans to do interactive work, such as incidental administrative tasks, non-programmatic configuration of Google Cloud services, testing, experimenting, and observability. 

You authenticate as a user account with user credentials, such as a password and one-time code. 

  * **Service accounts** : These are accounts specific to Google Cloud that workloads can use to access services or resources. You typically don't authenticate as a service account directly. Instead, you attach a service account to a resource such as a Compute Engine VM, or use [service account impersonation](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation). 

  * **Federated principals** : These are identities that reference user or service accounts in an external identity provider. There are two types of federated principals supported by Google Cloud, which have similar names: 

    * **[**Workforce Identity Federation**](https://docs.cloud.google.com/iam/docs/workforce-identity-federation)** : Lets human users sign in to Google Cloud with identities managed by an external identity provider. If your organization already has single sign-on (SSO) set up, you might use this type of identity to authenticate to Google Cloud. 

Your identity provider must support [OpenID Connect (OIDC)](https://openid.net/connect/) or [ SAML 2.0](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html) to use Workforce Identity Federation. 

    * **[Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation)** : Lets workloads running outside of Google Cloud operate on Google Cloud resources. 

You can use Workload Identity Federation with workloads that authenticate using [ X.509 client certificates](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-x509-certificates); that run on [ Amazon Web Services (AWS) or Azure](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds); on-premises [ Active Directory](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-active-directory); deployment services, such as [ GitHub and GitLab](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines); and with any identity provider that supports [ OpenID Connect (OIDC) or Security Assertion Markup Language (SAML) V2.0](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers). 




To learn more about these and other supported principal types in Google Cloud, see [Principal types](https://docs.cloud.google.com/iam/docs/principals-overview#principal-types).

## Configure your Google Cloud organization for authentication

When setting up authentication for your Google Cloud organization, you might need to integrate existing systems and workflows into Google Cloud:

  * If you have an existing identity provider that you want to use, you need to set up [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

  * If you have workloads running outside of Google Cloud that need access to Google Cloud resources, you need to set up [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation).




We recommend that you also do the following to help secure your Google Cloud environment:

  * Make sure [multi-factor authentication is enabled](https://docs.cloud.google.com/docs/authentication/mfa-requirement) for your users.

  * Check if you need to change [reauthentication settings](https://docs.cloud.google.com/docs/authentication/reauthentication).

  * Create policies for [managing API keys](https://docs.cloud.google.com/docs/authentication/api-keys-best-practices).

  * Create policies for [managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).




## Authenticate humans and workloads

How you authenticate to Google Cloud depends on the APIs and services that you're using, and the way in which you interact with those APIs and services.

### Authenticate humans

When performing manual, interactive work such as incidental administrative tasks, setting up resources, changing configurations, experimenting, and browsing logs, you use your user account's credentials to authenticate.

###  Console 

For interactive work in the Google Cloud console, you authenticate by signing in to the web interface with your user credentials.

[Go to the Google Cloud console](https://console.cloud.google.com/)

The same credentials for your Google Cloud console session are used for [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works), where you can access the gcloud CLI.

###  gcloud 

After you [install the gcloud CLI on your local device](https://docs.cloud.google.com/sdk/docs/install-sdk), you can use your user credentials to authenticate to Google Cloud by running the following command in your terminal:
    
    
    gcloud auth login
    

After you authenticate, subsequent `gcloud` commands use the signed-in principal to make their requests.

**Note:** You don't need to run `gcloud auth login` if you're using Cloud Shell.

For authenticating with Workforce Identity Federation credentials, Workload Identity Federation credentials, or service account keys, see [Authentication for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate).

### Authenticate workloads

Whether you're developing and running code on your local device, in Google Cloud, on-premises, or in another cloud, the most flexible and portable way to authenticate your workload is to provide credentials through a mechanism called _Application Default Credentials (ADC)_.

Libraries that implement ADC (such as the [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained)) check known locations in the environment they're run in for credentials. This means that, if you change where your code runs, you don't need to change the code itself—only the credentials that are used for that environment.

For example, when developing locally, you can set your environment so that ADC makes use of your user credentials for authentication. When your code is ready for production, you can deploy it unchanged to a Compute Engine VM instance, and set the environment to use short-lived service account credentials to authenticate instead.

You can't use ADC to authenticate in the following scenarios:

  * When authenticating the gcloud CLI.

  * When using an [API key](https://docs.cloud.google.com/docs/authentication/api-keys-use). API keys can only be used with specific APIs.




To learn how to set up ADC for specific environments, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).

## What's next

  * Learn more about the different [authentication methods for Google Cloud](https://docs.cloud.google.com/docs/authentication).

  * To understand how you control what a principal can access in Google Cloud, see [Authorization and access control](https://docs.cloud.google.com/docs/get-started/authorization-access-control).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
