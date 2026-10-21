---
url: https://docs.cloud.google.com/functions/1stgendocs/securing/
title: Secure your Cloud Run function \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:40.606928+00:00
---

# Secure your Cloud Run function  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/securing/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Secure your Cloud Run function

This page provides a high-level overview of the ways you can control interactions with your Cloud Run functions resources.

## Access control

There are two approaches to controlling access to Cloud Run functions:

  * Identity-based
  * Network-based



### Securing access with identity

One way to control access to a function is to require that the requesting entity identify itself by using a credential. A credential is a "name" of some sort, secured by a secret that the entity knows or has access to, like a password or a hardware dongle. By default, functions are deployed as _private_ , and require such a credential, although it is possible to deploy a function as _public_ , that is, not requiring one.

The first step in the process is validating the credential to make sure that the requestor is who it says it is, that it presents the right name and secret combination. This step is called ([`Authentication`](https://docs.cloud.google.com/docs/authentication)).

Once the requestor's identity has been authenticated, its level of access, the permissions that the identity has been granted, can be evaluated. This step is called ([`Authorization`](https://en.wikipedia.org/wiki/Authorization)).

#### Authentication

Cloud Run functions supports two different kinds of identities, which are also called _principals_ :

  * [Service accounts](https://docs.cloud.google.com/iam/docs/service-accounts): These are special accounts that serve as the identity of a non-person, like a function or an application or a VM. They give you a way to authenticate these non-persons.
  * User accounts: These accounts represent people - either as individual Google account holders or as part of a Google-controlled entity like a Google Group.



For both service accounts and user accounts, the name portion of the credential is usually an email address associated with the account. The secret for a user account is usually a password, and for a service account, it is usually the private key of the key pair that is created along with the account.

But user passwords and service account keys themselves are very powerful: they can provide wide-ranging access to data and functionality and they remain effective until they are actively revoked or changed. So to limit the potential damage that might occur if the credential leaked, in Google Cloud this core credential is replaced by a short-term credential based on it, a _token_ , one that has a limited lifetime and is created on the fly as part of the request sequence. The token is passed with the request and serves to safely authenticate the account.

There are two kinds of tokens used in Cloud Run functions: access tokens and id tokens. Access tokens are usually used to authenticate API calls and id tokens are used to authenticate calls to developer-created code, for example, if a function calls another function. The tokens themselves are created using the OAuth 2 framework, and its extension, Open Identity Connect, but the sequence is complex and error-prone, and the use of [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) to manage the process is highly recommended.

#### Authorization

Once the identity of the requesting entity has been confirmed, what it is that the requestor is allowed to do must be evaluated. This evaluation is based on what _permissions_ the authenticated account was granted when it was set up. Cloud Run functions uses [Identity and Access Management](https://docs.cloud.google.com/iam/docs) (IAM) to do this. [_Roles_](https://docs.cloud.google.com/iam/docs/understanding-roles), which are sets of individual permissions grouped together for convenience, are assigned to the account, either directly or via a configuration called a [_policy_](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy). Each individual permission in the role set usually corresponds to a single REST API call exposed by the requested service. For more information on this process, see [Authorizing Access via IAM](https://docs.cloud.google.com/functions/1stgendocs/securing/managing-access-iam).

### Network-based access control

You can also limit access by specifying [network settings](https://docs.cloud.google.com/functions/1stgendocs/networking/network-settings) for individual functions. This allows for fine-tuned control over the network ingress and egress to and from your functions.

## Isolation and sandboxing

Internally, function instances are isolated from each other using the [gVisor](https://gvisor.dev/) sandboxing platform. By design, a function cannot access other functions' operating environments.

## Execution environment updates

Google makes security patches and maintenance updates available after a period of stability testing. Cloud Run functions might apply updates to other aspects of the execution environment, such as the operating system or included packages. These updates help keep your function's [execution environment secure](https://docs.cloud.google.com/functions/1stgendocs/securing/execution-environment-security).

### Cloud Run functions security updates

You can choose one of the following security update policies:

  * **Automatic updates** (default): Updates and security patches to the runtime environment are published in new versions of the runtime image. After a period of testing for stability and reliability, the updated runtime is rolled out to all functions resulting in a zero downtime update. Automatic security updates are available with Cloud Run functions (1st gen) and Cloud Run functions. To take on language-level security fixes, you may need to rebuild functions that use compiled languages such as Go or Java.

  * **On deployment updates** : Updates and security patches are applied to runtimes only when functions are deployed or redeployed, unless otherwise noted. Updates on deployment are available on both Cloud Run functions (1st gen) and Cloud Run functions.




The runtime update policy can be changed using the `--runtime-update-policy` [flag](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime-update-policy) in your `gcloud functions deploy` command.

To learn more about execution environment security updates, see [security update policies](https://docs.cloud.google.com/functions/1stgendocs/securing/execution-environment-security#security_update_policy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
