---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/extend-schema/
title: Extend schema \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:06.876034+00:00
---

# Extend schema  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/extend-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Extend schema Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to extend the schema in a Managed Service for Microsoft Active Directory instance.

## Before you begin

Before you begin, do the following:

  1. [Create a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain).
  2. [Create and join a Windows VM to the domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-join-windows).
  3. Make sure that you read [About schema extension](https://docs.cloud.google.com/managed-microsoft-ad/docs/schema-extension) and understand these [considerations](https://docs.cloud.google.com/managed-microsoft-ad/docs/schema-extension#considerations).
  4. Prepare the LDIF file with the schema changes. For more information, see [How to prepare your LDIF file](https://docs.cloud.google.com/managed-microsoft-ad/docs/schema-extension#prepare-ldif).
  5. Make sure that you have any one of the following Identity and Access Management (IAM) user roles:

     * Google Cloud Managed Identities Domain Admin (`roles/managedidentities.domainAdmin`)
     * Google Cloud Managed Identities Admin (`roles/managedidentities.admin`)

For more information, see [Cloud Managed Identities roles](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities).




## Extend the schema

When you initiate schema extension, Managed Microsoft AD creates a [schema extension backup](https://docs.cloud.google.com/managed-microsoft-ad/docs/backup-restore#overview) automatically before applying the schema changes. You can use this backup to [restore the domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/backup-restore#restore-backup) if you encounter any problems after schema extension. To identify the schema extension backup, you can [list the backups](https://docs.cloud.google.com/managed-microsoft-ad/docs/backup-restore#list-backup) created for your domain.

To extend the schema, run the following gcloud CLI command:
    
    
    gcloud active-directory domains extend-schema DOMAIN_NAME  --ldif-file=LDIF_FILE_PATH \
        --description=SCHEMA_EXTENSION_DESCRIPTION --project=DOMAIN_RESOURCE_PROJECT_ID --async
    

Replace the following:

  * DOMAIN_NAME: The name of your Managed Microsoft AD domain. For example, `my-domain.example.com`.
  * LDIF_FILE_PATH: The path of the LDIF file with the schema changes. The maximum file size is limited to 1 MB.
  * SCHEMA_EXTENSION_DESCRIPTION: The description of the schema changes.
  * DOMAIN_RESOURCE_PROJECT_ID: The project ID of the domain resource project. For example, `my-project`.



Managed Microsoft AD initiates schema extension and responds with an operation ID which you can use to track the completion of schema extension.

To check the status of your schema extension, run the following gcloud CLI command:
    
    
    gcloud active-directory operations describe OPERATION_ID
    

Replace OPERATION_ID with the operation ID of your schema extension. For example, `operation-1234567890-98765a1b2c3d4e5-e6f7g8-9h0i1j2`.

## Verify the schema extension

After you extend the schema of your Managed Microsoft AD instance, it's important you verify the schema changes before integrating your applications with Active Directory. You can verify the schema changes using different tools and approaches. In the following sections, we explain how you can verify the schema changes using any one of these approaches:

  1. Active Directory Schema Snap-In
  2. Windows PowerShell



### Active Directory Schema Snap-In

To verify the schema changes using Active Directory Schema Snap-In, do the following:

  1. Login to your domain-joined VM as a delegated administrator.
  2. [Install the **Active Directory Schema Snap-In**](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc732110\(v=ws.11\)?redirectedfrom=MSDN).
  3. Open the **Microsoft Management Console (MMC)**.
  4. Expand the **Active Directory Schema** tree for your directory.
  5. Verify if you can see the changes in classes and attributes of the schema.



### Windows PowerShell

To verify the schema changes using Windows PowerShell, use `Get-ADObject` cmdlet. Run the following command in Windows PowerShell:
    
    
    get-adobject -Identity 'cn=ATTRIBUTE,cn=Schema,cn=Configuration,dc=ROOT_DOMAIN,dc=TOP_LEVEL_DOMAIN' -Properties *
    

Replace the following:

  * ATTRIBUTE: The name of an attribute in your schema. For example, `example-attribute`.
  * ROOT_DOMAIN: The root domain of your domain name. For example, if your domain name is `example.com`, enter `example`.
  * TOP_LEVEL_DOMAIN: The top-level domain of your domain name. For example, if your domain name is `example.com`, enter `com`.



In the response, verify if you can see the changes in classes and attributes of the schema.

## What's next

  * [Back up and restore a domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/backup-restore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
