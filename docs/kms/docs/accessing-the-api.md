---
url: https://docs.cloud.google.com/kms/docs/accessing-the-api/
title: Accessing the API \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:56.351520+00:00
---

# Accessing the API  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/accessing-the-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Accessing the API Stay organized with collections  Save and categorize content based on your preferences. 

We recommend that you access Cloud Key Management Service via our high performance [Google API Client Libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). These libraries, which connect to the Cloud KMS gRPC API, are provided in several popular programming languages.

You may also access Cloud KMS via our [REST API](https://docs.cloud.google.com/kms/docs/reference/rest). Thus, any language that supports sending HTTP requests can access the API. However, most users will prefer a more idiomatic client library.

There is also a web-based interface for [Cloud KMS on the Google Cloud console](https://console.cloud.google.com/security/kms), which allows for key management operations. Encrypt and decrypt operations cannot be performed from the web interface.

We want to make accessing Cloud KMS a joy from every language and platform, and work on that will be ongoing. If we're falling short in any way, [let us know](https://docs.cloud.google.com/kms/docs/support).

## Platforms

How clients access the API may vary a bit depending on the platform on which the code is running, particularly with respect to authentication. [Google Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) abstract away many of the differences, but there are still some things to keep in mind. For more information about authentication, see the [authentication overview](https://docs.cloud.google.com/docs/authentication).

### Compute Engine and Google Kubernetes Engine

Software running on [Compute Engine](https://docs.cloud.google.com/compute), including Google Kubernetes Engine nodes, typically authenticates using credentials automatically provisioned into the environment using the [attached service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances). The same is true for Cloud KMS. Ensure that when you create an instance, you give it access to the `https://www.googleapis.com/auth/cloudkms` (preferred because it supports the principle of least privilege) or `https://www.googleapis.com/auth/cloud-platform` OAuth scope.

For example:
    
    
    gcloud compute instances create "instance-1" \
        --zone "us-east1-b" \
        **--scopes "https://www.googleapis.com/auth/cloudkms"**
    

For more information, refer to the [Compute Engine documentation](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#using) or the [GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).

### App Engine

To use Cloud KMS with App Engine:

  1. Give your App Engine service account (`PROJECT_ID@appspot.gserviceaccount.com`) [Identity and Access Management permissions](https://docs.cloud.google.com/kms/docs/iam) to manage and/or use your keys.
  2. Use the [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc), and specify the scope `https://www.googleapis.com/auth/cloudkms`. You can also specify the scope `https://www.googleapis.com/auth/cloud-platform`, but it includes broader scopes than just Cloud KMS.



For more information, refer to [Accessing the API](https://docs.cloud.google.com/appengine/docs/admin-api/accessing-the-api) and [Controlling access](https://docs.cloud.google.com/appengine/docs/admin-api/access-control) in the App Engine documentation.

### Client authentication

If your application needs to authenticate your users directly, you can obtain and use credentials on their behalf. To learn more, see [User accounts](https://cloud.google.com/docs/authentication/use-cases#app-users).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
