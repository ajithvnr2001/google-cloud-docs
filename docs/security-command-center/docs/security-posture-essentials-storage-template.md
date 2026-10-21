---
url: https://docs.cloud.google.com/security-command-center/docs/security-posture-essentials-storage-template/
title: Predefined posture template for Cloud Storage, essentials \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:01.512464+00:00
---

# Predefined posture template for Cloud Storage, essentials  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/security-posture-essentials-storage-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Predefined posture template for Cloud Storage, essentials Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes the preventative and detective policies that are included in the v1.0 version of the predefined posture template for Cloud Storage, essentials. This posture template includes two policy sets:

  * A policy set that includes organization policies that apply to Cloud Storage.

  * A policy set that includes Security Health Analytics detectors that apply to Cloud Storage.




You can use this predefined posture template to configure a security posture that helps protect Cloud Storage. You can deploy this predefined posture template without making any changes.

## Organization policy constraints

The following table describes the organization policies that are included in this posture.

Policy | Description | Compliance standard  
---|---|---  
`storage.publicAccessPrevention` | This policy prevents Cloud Storage buckets from being open to unauthenticated public access.The value is `true` to prevent public access to buckets. | NIST SP 800-53 control: AC-3, AC-17, and AC-20  
`storage.uniformBucketLevelAccess` | This policy prevents Cloud Storage buckets from using per-object ACL (a separate system from IAM policies) to provide access, enforcing consistency for access management and auditing. The value is `true` to enforce [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access). | NIST SP 800-53 control: AC-3, AC-17, and AC-20  
  
## Security Health Analytics detectors

The following table describes the Security Health Analytics detectors that are included in the predefined posture template. For more information about these detectors, see [Vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings).

Detector name | Description  
---|---  
`BUCKET_LOGGING_DISABLED` | This detector checks whether there is a storage bucket without logging enabled.  
`LOCKED_RETENTION_POLICY_NOT_SET` | This detector checks whether the locked retention policy is set for logs.  
`OBJECT_VERSIONING_DISABLED` | This detector checks whether object versioning is enabled on storage buckets with sinks.  
`BUCKET_CMEK_DISABLED` | This detector checks whether buckets are encrypted using customer-managed encryption keys (CMEK).  
`BUCKET_POLICY_ONLY_DISABLED` | This detector checks whether uniform bucket-level access is configured.  
`PUBLIC_BUCKET_ACL` | This detector checks whether a bucket is publicly accessible.  
`PUBLIC_LOG_BUCKET` | This detector checks whether a bucket with a log sink is publicly accessible.  
`ORG_POLICY_LOCATION_RESTRICTION` | This detector checks whether a Compute Engine resource is out of compliance with the `constraints/gcp.resourceLocations` constraint.   
  
## View the posture template

To view the posture template for Cloud Storage, essentials, do the following: 

### gcloud

Before using any of the command data below, make the following replacements: 

  * `ORGANIZATION_ID`: the numeric ID of the organization. 



Execute the [`gcloud scc posture-templates describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/posture-templates/describe) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc posture-templates describe \
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/cloud_storage_essential

#### Windows (PowerShell)
    
    
    gcloud scc posture-templates describe `
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/cloud_storage_essential

#### Windows (cmd.exe)
    
    
    gcloud scc posture-templates describe ^
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/cloud_storage_essential

The response contains the posture template.

### REST

Before using any of the request data, make the following replacements: 

  * `ORGANIZATION_ID`: the numeric ID of the organization. 



HTTP method and URL: 
    
    
    GET https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/cloud_storage_essential

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/cloud_storage_essential"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/cloud_storage_essential" | Select-Object -Expand Content

The response contains the posture template.

## What's next

  * [Create a security posture using this predefined posture template](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
