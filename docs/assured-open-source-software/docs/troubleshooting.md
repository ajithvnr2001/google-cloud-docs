---
url: https://docs.cloud.google.com/assured-open-source-software/docs/troubleshooting/
title: Troubleshoot Assured OSS issues \u00a0|\u00a0 Assured Open Source Software \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:49.332651+00:00
---

# Troubleshoot Assured OSS issues  |  Assured Open Source Software  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-open-source-software/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Open Source Software ](https://docs.cloud.google.com/assured-open-source-software/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-open-source-software/docs/service-account-creation)



Send feedback 

#  Troubleshoot Assured OSS issues Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with Assured Open Source Software.

## Authentication errors

This section lists some errors that you might encounter with authentication and provides suggestions about fixing them.

### HTTP 403: Permission `artifactregistry.mavenartifacts.list` denied

The following error message is returned when authentication fails:
    
    
    {
      "error": {
        "code": 403,
        "message": "Permission 'artifactregistry.mavenartifacts.list' denied on resource '//artifactregistry.googleapis.com/projects/cloud-aoss/locations/us/repositories/cloud-aoss-java' (or it may not exist).",
        "status": "PERMISSION_DENIED",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "IAM_PERMISSION_DENIED",
            "domain": "artifactregistry.googleapis.com",
            "metadata": {
              "permission": "artifactregistry.mavenartifacts.list",
              "resource": "projects/cloud-aoss/locations/us/repositories/cloud-aoss-java"
            }
          }
        ]
      }
    }
    

One of the following reasons can cause this error:

  * **You haven't enabled the service account or AWS account ID** : Enable the service account or AWS account ID by providing its details in the [customer enablement form](https://developers.google.com/assured-oss#get-started).

  * **You haven't set up Application Default Credentials (ADC)** : To resolve this issue, make sure that you have [set up authentication](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection#set_up_authentication).

For more details, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).

  * **You have set up ADC with incorrect service account** : Make sure that the service account you are using is the same service account that you have enabled using the customer enablement form.




### HTTP 403: Permission `artifactregistry.pythonpackages.list` denied

The resolution for this error is the same as that for the HTTP 403 error you receive for Java.

### Service account key creation is disabled

You might encounter the following error while trying to generate a service account key for authentication:
    
    
    Service account key creation is disabled.
    
    The organization policy constraint 'iam.disableServiceAccountKeyCreation' is
    enforced. This constraint disables the creation of new service account keys.
    

To resolve this issue, contact your organization policy administrator and request an exception to the organization policy constraint that disables the creation of service account keys.

## Can't download packages

If you're experiencing issues downloading packages, complete the following:

  * Check whether the package exists in the repository. For instructions, see [Validate your connection](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection).
  * For the free tier, check whether you're downloading a supported package. For more information, see [List of supported Java and Python packages for the Assured OSS free tier](https://docs.cloud.google.com/assured-open-source-software/docs/supported-packages).
  * Verify that your environment supports the package and version. Build tools such as `pip` only download supported packages.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
