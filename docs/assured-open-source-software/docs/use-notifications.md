---
url: https://docs.cloud.google.com/assured-open-source-software/docs/use-notifications/
title: Subscribe to notifications \u00a0|\u00a0 Assured Open Source Software \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:23.631342+00:00
---

# Subscribe to notifications  |  Assured Open Source Software  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-open-source-software/docs/use-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Open Source Software ](https://docs.cloud.google.com/assured-open-source-software/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-open-source-software/docs/service-account-creation)



Send feedback 

#  Subscribe to notifications Stay organized with collections  Save and categorize content based on your preferences. 

Assured Open Source Software (Assured OSS) publishes two types of notifications:

  * **Package availability:** These notifications contain information about new packages and package versions that are added to Assured OSS and updates regarding the package onboarding status.

  * **Vulnerability notifications:** These notifications contain information about new vulnerabilities detected in the packages that are curated by Assured OSS or updates to existing vulnerabilities.




Programmatic notifications about updates on security metadata and new packages are published on [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) topics. These notifications are available in JSON format. You can create a pull subscription or push subscription to the Assured OSS topic to receive notifications.

To create these subscriptions, use the same service account or workload identity credentials that you use to access artifacts or metadata. When your access to Assured OSS is enabled, the service accounts are granted permission to create subscriptions on these topics.

The following sections describe the Pub/Sub topics.

This document applies to both the premium tier and free tier.

## Before you begin

For the Assured OSS premium tier, if you enabled VPC Service Controls, [configure the egress rule](https://docs.cloud.google.com/security-command-center/docs/aoss-configure-support-for-vpc-sc#pubsub-notifications).

## Package onboarding topic

  * **Topic Name:** `projects/cloud-aoss/topics/package_onboarding`
  * **Message:** this topic contains information about new package versions that are added to Assured OSS and updates regarding its onboarding status.
  * **Message Data Schema:**
        
        {
        "package_name" string
        "package_version" string
        "language" string
        "onboarding_status" string
        "notification_status" string
        }
        

  * **Message Data Attributes:**
        
        "PackageName"     string
        "PackageVersion"  string
        "PackageLanguage" string
        "SchemaVersion"   string
        "GenerateTime"    string
        




## Vulnerability information topic

  * **Topic Name:** `projects/cloud-aoss/topics/vulnerability_information`
  * **Message:** this topic contains information about new vulnerabilities detected in the system or if the metadata of any vulnerability is updated.
  * **Message Data Schema:**
        
        {
        "vulnerabilityId" string
        "notificationStatus" string
        }
        

  * **Message Data Attributes:**
        
        "PackageName"     string
        "PackageVersion"  string
        "PackageLanguage" string
        "SchemaVersion"   string
        "GenerateTime"    string
        




## Consolidated package onboarding and vulnerability information topic for premium tier

You can access all Assured OSS notifications from the following Pub/Sub topic:
    
    
    projects/assuredoss-blue/topics/assuredoss-notifications
    

## Notification attributes

The following notification [attributes](https://docs.cloud.google.com/pubsub/docs/publisher#using-attributes) are part of the published Pub/Sub message. You can use these attributes to filter the message.
    
    
    {
      "Type": "string",             // Indicates the type of notification, can be 'PackageVersion' or 'Vulnerability'
      "PackageName": "string",      // Package ID
      "PackageVersion": "string",   // Version of the package
      "Language": "string",         // Language of the package
      "SchemaVersion": int,         // Schema version of the data in message
      "GenerateTime": "string"      // Time at which the event occurred
    }
    

The `GenerateTime` attribute is in [RFC 3339](https://tools.ietf.org/html/rfc3339) format.

#### Package-related notifications

When the `Type` attribute is `PackageVersion`, the [message data](https://docs.cloud.google.com/pubsub/docs/publisher#message_format) has the following fields:
    
    
    {
      "PackageName": "string",       // Package ID
      "PackageVersion": "string",    // Version of the package
      "Language": "string",          // Language of the package
      "NotificationStatus": "string" // Status of package-version,'New' indicates available to download from Assured OSS
    }
    

#### Vulnerability-related notifications

When the `Type` attribute is `Vulnerability`, the [message data](https://docs.cloud.google.com/pubsub/docs/publisher#message_format) has the following fields:
    
    
    {
      "ID": "string",            // Vulnerability ID affecting the package
      "Severity": "string",      // Severity of the vulnerability
      "Sources": [
        {
          "Name": "string",      // Source of vulnerability information
          "Link": "string"       // URL of vulnerability details
        }
      ],
      "Summary": "string",       // Summary of vulnerability
      "Description": "string",   // Detailed description of vulnerability
      "PackageName": "string",       // Package ID
      "PackageVersion": "string",    // Version of the package
      "Language": "string",          // Language of the package
      "NotificationStatus": "string" // Status of package-version
    }
    

The value of the `NotificationStatus` field indicates the status of the vulnerability. If the vulnerability is new for a package, the value is `New`. If there is an update to an existing vulnerability, the value is `Update`.

## Create a pull subscription

To create a pull subscription, complete the following:

  1. Create a [pull subscription](https://docs.cloud.google.com/pubsub/docs/create-subscription). You can use the Google Cloud console, Google Cloud CLI, or Pub/Sub API.

**Note:** If using the Pub/Sub API, enable the API first for the parent project of the service account you are using for Assured OSS.
  2. After you have created the pull subscription, start polling for messages by using [client libraries](https://docs.cloud.google.com/pubsub/docs/pull) or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions).




## Create a push subscription

**Note:** Push subscriptions cannot be created by premium tier customers.

To create a push subscription, set up an HTTPS server with a certificate that isn't self-signed and that is accessible on the internet. Use the push subscription model in one of the following ways:

  * If you have a Google Cloud project and service account (for example, you integrated Assured OSS with Security Command Center):

Because Assured OSS provides permission to create subscriptions, you can create your own push subscriptions and associate them with the endpoint of your choice. For more information, see [Push subscriptions](https://docs.cloud.google.com/pubsub/docs/push).

  * If you are using the free tier and you don't have a Google Cloud project and service account, enter the HTTPS endpoint in the [Enable Access or Update Notification Preferences form](https://developers.google.com/assured-oss?update_notifications=y#get-started). The Assured OSS team will create a push subscription and attach the endpoint with that subscription.




## What's next

  * [Artifact signature overview](https://docs.cloud.google.com/assured-open-source-software/docs/package-signature-overview)
  * [Verify signatures](https://docs.cloud.google.com/assured-open-source-software/docs/verify-packages)
  * [Verify the build provenance](https://docs.cloud.google.com/assured-open-source-software/docs/verify-build-provenance)
  * [Learn about protecting your software supply chain](https://docs.cloud.google.com/software-supply-chain-security/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
