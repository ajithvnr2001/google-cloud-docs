---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/secure-service-account-keys/
title: Secure service account keys \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:17.021056+00:00
---

# Secure service account keys  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/secure-service-account-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Secure service account keys Stay organized with collections  Save and categorize content based on your preferences. 

Unlike normal users, service accounts don't have passwords. Instead, service accounts use ECDSA key pairs for authentication. Because the private key of the RSA key pair lets you authenticate as the service account, having access to the private key is similar to knowing a user's password. The private key is known as a service account key. Service account keys are a security risk if not managed carefully.

Main threats related to service account keys are as follows:

  * **Credential leakage** : Service account keys might inadvertently end up in places where they are not supposed to be stored. A bad actor can use a leaked service account key to authenticate and gain access to your environment.

  * **Privilege escalation** : If a bad actor gets access to a poorly secured service account key, they might be able to use the key to escalate their privileges.

  * **Information disclosure** : Service account keys might inadvertently disclose confidential data.

  * **Non-repudiation** : By authenticating using a service account key and letting the service account carry out operations on their behalf, a bad actor might conceal their identity and actions.




This page presents best practices for managing, using, and securing service account keys.

## Protect against credential leakage

Like a username and password, service account keys are a form of credential. If a user can access a valid service account key, they can use the key to authenticate and access the resources the respective service account has access to.

Bad actors might find service account keys more valuable than a leaked password. For example, attempting to sign in by using a leaked password is unlikely to succeed if the user account has been configured to use two step verification and login challenges. In contrast, authenticating with a leaked service account key is likely to succeed as service accounts are not subject to any additional sign-in verifications.

Bad actors might look for service account keys in the following ways:

  * Source code repositories of open source projects.
  * Public data dumps of breached services.



In addition to public locations, bad actors might look for service account keys in private locations they've compromised. Examples include:

  * Email inboxes
  * File shares
  * Backup storage
  * Temporary file system directories



An effective way to lower the risk of leaking service account keys is to reduce the number of keys in circulation and to disincentivize the creation of new keys. The following sections describe how you can limit the number of service account keys in circulation, and what other measures can help you limit the risk of leaking service accounts.

### Avoid leaving service account keys in temporary locations

When you create a service account key, immediately move the key to the location where you want to store it. Ensure you're not accidentally leaving a copy in the download folder or the recycle bin of your computer.

### Don't pass service account keys between users

When you deploy an application that requires a service account key, you might not have the permission to create a service account key yourself. Instead, you might have to request a different person to create a service account key for you.

### Don't submit service account keys to source code repositories

Service account keys are credentials, and must be protected from unauthorized access. If you submit a service account key to a source code repository, there is an increased risk that the key becomes accessible to unauthorized users and bad actors:

  * Bad actors might scan the source code of public source repositories for leaked keys.

  * In the future, you might decide to turn a private source repository into a public repository, without checking it for keys first.

  * Other team members might store copies of the source code on their workstation.




When you work on code that uses a service account key, always store the service account key separate from the source code to reduce the risk of accidentally submitting the key to the source repository. In many cases, you can further reduce this risk by not using service account keys at all during development and using your personal credentials instead of service account keys instead.

### Don't embed service account keys in program binaries

Service account keys are strings that match a certain pattern, and they can be identified even if embedded in other files or binaries. If a bad actor has access to the binary, they can extract any service account keys that are embedded in the binary.

Program binaries for server-side applications might be hosted in artifact repositories or they might be copied to developer workstations for debugging purposes. Keeping service account keys separate from the program binaries helps ensure that a user who can access the binary does not implicitly get access to service account credentials.

  * For client-side applications such as tools, desktop programs, or mobile apps, don't use service accounts.
  * For server-side applications, don't embed service account keys into the binary. Instead, keep the keys separate from the application binary.



### Rotate service account keys to reduce security risk caused by leaked keys

Although you can reduce the probability of accidentally leaking a service account key, it can be difficult to eliminate the risk completely.

Key rotation is the process of replacing your existing keys with new keys and then invalidating the replaced keys. We recommend that you routinely rotate all keys that you manage, including your service account keys.

Rotating service account keys can help reduce the risk posed by leaked or stolen keys. If a key is leaked, it might take bad actors days or weeks to discover the key. If you regularly rotate your service account keys, there's a higher chance that the leaked keys will be invalid by the time a bad actor gets them.

To rotate a service account key without downtime, complete the following:

  1. Create a second key pair for the service account:
         
         gdcloud iam service-accounts keys create NEW_KEY_FILE \
             --project=PROJECT \
             --iam-account=NAME \
             --ca-cert-path=CA_CERTIFICATE_PATH
         

**Note:** In air-gapped environments accessed using SOCKS proxies, the gdcloud CLI post-login discovery endpoint does not inherit `HTTPS_PROXY`. Run `keys create` from a host that has direct network reachability to the management API server.
  2. Update your workload or Kubernetes Secret with the new private key file (`NEW_KEY_FILE`).

  3. Trigger a rolling restart of your workload or wait for your application to hot-reload the updated key.

  4. Verify that the workload successfully authenticates with the new credential.

  5. Delete the old public key from the service account using the key ID:
         
         gdcloud iam service-accounts keys delete OLD_KEY_ID \
             --project=PROJECT \
             --iam-account=NAME
         




### Use expiry times to let keys expire automatically

By default, service account keys that you create have an expiry time of one year and stay valid until you delete them. You can also set your own expiry time. Setting an expiry time for service account keys can limit your security risk by reducing the lifetime of the persistent credential. However, there are other risks associated with setting expiry times; for example, setting an expiry time can cause workloads to fail when their keys expire.

Use expiry times when you need temporary access to a system that requires a service account key. For example, use expiry times when you're doing the following:

  * Developing code in a non-production environment for an application that can only authenticate with service account keys.
  * Using a third-party tool that can only authenticate with service account keys.



Avoid using expiry times for these scenarios:

  * Production workloads. In production, an expired service account key could cause an accidental outage. Instead, use keys that don't expire, and manage their lifecycle with key rotation.
  * Non-production workloads that need permanent access, such as a continuous integration (CI) pipeline.
  * Key-rotation systems that prevent a key from being used after a specified amount of time.



To limit the validity of service account keys, you can configure an expiry time for newly created keys in your project or organization. The expiry time does not apply to existing keys.

Having an established process for rotating service account keys also helps you act quickly if you suspect that a service account key has been compromised.

### Use a dedicated key for each machine that runs an application

To help you narrow down the potential sources of suspicious activity, create individual keys for each copy of the application. That way, you can use the `serviceAccountKeyName` field that many services add to audit log records to distinguish which machine an activity originated from.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
