---
url: https://docs.cloud.google.com/compute/docs/access/app-authentication-methods/
title: Choose a workload authentication method \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:26:55.154407+00:00
---

# Choose a workload authentication method  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/access/app-authentication-methods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Choose a workload authentication method Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you authenticate applications or workloads that are either running in a production environment on Compute Engine or being tested locally for future deployment to the production environment. You can do the following:

  * Authenticate your workloads to use Google APIs
  * Authenticate your workloads to other workloads over mTLS



## Authenticate your workloads to use Google APIs

Use the following table to determine which authentication method to use for your workloads.

**Task** | **Method**  
---|---  
Authenticate apps or workloads that are in production | Use the service account that is attached to the VM.   
This is the most common method for authenticating apps and workloads that are running on virtual machine (VM) instances on Google Cloud. For detailed instructions, see [ Authenticate workloads to Google Cloud APIs using service accounts](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads).  
Authenticate apps or workloads that are in development | Use Google Cloud SDK and Application Default Credentials. For more information, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).   
Authorizing apps and workloads that need access to end-user resources | If you are building development or administration tools where users grant you access to their Google Cloud resources, get your application access to user resources by using OAuth 2.0. For detailed instructions, see [ Using OAuth 2.0 for Web Server Applications](https://developers.google.com/identity/protocols/oauth2/web-server).   
In your request, specify an access scope that limits your access to only the methods and user information that your application requires. For a full list of services and required scopes across Google Cloud, see [ OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes).  
  
## Authenticate your workloads to other workloads over mTLS

You can authenticate applications or other workloads by using [managed workload identities](https://docs.cloud.google.com/iam/docs/managed-workload-identity). This authentication method uses a service account, certificate authority (CA) pools, managed workload identities, and a unique instance identifier to identify instances.

Managed workload identities let you bind strongly attested identities to your Compute Engine workloads. Google Cloud provisions X.509 credentials issued from the [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service) that can be used to reliably authenticate your workload with other workloads over [mutual TLS (mTLS)](https://docs.cloud.google.com/chrome-enterprise-premium/docs/understand-mtls) authentication.

Your workload uses the managed workload identity as its identity when it authenticates to other workloads using mutual TLS (mTLS) and uses the service account as its identity when it accesses other Google Cloud services and resources.

For more information, see [Authenticate workloads to other workloads over mTLS](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls).

## What's next

  * Learn more about the following concepts: 
    * [Authenticate to Compute Engine](https://docs.cloud.google.com/compute/docs/authentication)
    * [Authentication methods at Google](https://docs.cloud.google.com/docs/authentication)
    * [Managed workload identities](https://docs.cloud.google.com/iam/docs/managed-workload-identity)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
