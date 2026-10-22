---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/schema-extension/
title: About schema extension \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:01.103810+00:00
---

# About schema extension  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/schema-extension/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  About schema extension Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how schema extension works in Managed Service for Microsoft Active Directory.

## Overview

Active Directory relies on schema to organize and store the directory data. The AD schema defines the object classes and its attributes that are used to store the directory data.

You can use schema extensions to perform schema changes and enable support for applications which are dependent on specific classes or attributes in Active Directory.

You can extend the default AD schema by defining new classes and attributes or modifying the definitions or properties of existing classes and attributes. Managed Microsoft AD lets you extend the schema using an LDAP Data Interchange Format (LDIF) file that contains commands for schema changes. For more information, see [Extending the Schema](https://docs.microsoft.com/en-us/windows/win32/ad/extending-the-schema?redirectedfrom=MSDN).

For more information about LDIF, see [LDAP Data Interchange Format](https://en.wikipedia.org/wiki/LDAP_Data_Interchange_Format).

## How to prepare your LDIF file

An LDIF file is a standard plain text data interchange format for representing Lightweight Directory Access Protocol (LDAP) directory content and update requests. An LDIF file consists of a series of records that represents a collection of update requests, such as add, modify, rename. Blank lines separate the set of records in the LDIF file representing each entry of update request. We recommend you to understand the format of LDIF files before creating your file with schema changes. For more information, see [LDIF Scripts](https://docs.microsoft.com/en-us/windows/win32/ad/ldif-scripts?redirectedfrom=MSDN).

Before preparing your LDIF file, read the following guidelines.

### Schema elements

Schema elements, such as classes, attributes, objects, are the building blocks of an AD schema. We recommend you to learn the key concepts related to schema elements such as attributes, object classes, object identifiers, and linked attributes. For more information, see [Active Directory Schema (AD DS)](https://docs.microsoft.com/en-us/windows/win32/ad/active-directory-schema).

### LDIF file structure

You need to arrange the entries in an LDIF file by using the [Directory Information Tree (DIT)](https://en.wikipedia.org/wiki/Directory_information_tree) structure. The structure of a valid LDIF file must adhere to the following guidelines:

  * List the parent entries before the child entries.
  * Separate the entries in an LDIF file with a blank line.
  * Any class or attribute that you use in an entry must exist in the schema. Before using a class or attribute, make sure you verify if it is available in the schema. If not, you need to add the class or attribute to the schema. For example, you need to create an attribute before attaching the attribute with a class.



### Distinguished name format

All entries in an LDIF file begin with a distinguished name (DN). It specifies the AD object upon which the records operate on. In case the records update schema cache, DN must be empty. For schema changes, DN must be in the following format:
    
    
    dn: cn=CLASS_OR_ATTRIBUTE,cn=Schema,cn=Configuration,dc=ROOT_DOMAIN,dc=TOP_LEVEL_DOMAIN
    

Replace the following:

  * CLASS_OR_ATTRIBUTE: The name of a class or attribute. For example, `example-attribute`.
  * ROOT_DOMAIN: The root domain of your domain name. For example, if your domain name is `example.com`, enter `example`.
  * TOP_LEVEL_DOMAIN: The top-level domain of your domain name. For example, if your domain name is `example.com`, enter `com`.



For example, the DN of an attribute `example-attribute` for domain name `example.com` must be in the following format:
    
    
    dn: cn=example-attribute,cn=Schema,cn=Configuration,dc=example,dc=com
    

**Note:** For schema extensions, Managed Microsoft AD only supports DNs with the following CN entries: `cn=Schema,cn=Configuration`.

### Supported LDIF changetypes

Managed Microsoft AD supports the following LDIF changetypes for schema extension:

LDIF changetype | Schema extension action  
---|---  
`add` | Creates a new class or attribute in the schema.  
`modify` | Updates the properties of a class or attribute in the schema. The following list describes some of the possible property updates: 
* Attaching an attribute to a class.
* Updating the `ldapDisplayName` property of a class or attribute.
* Disabling a class or attribute.
**Note:** Managed Microsoft AD doesn't support the modification of `defaultSecurityDescriptor` attribute due to security reasons.  
`modrdn` or `moddn` | Renames the relative distinguished name (RDN) for a class or attribute.  
  
### Considerations

Before you extend the schema, make sure you refer to the following considerations.

  * Microsoft provides detailed advisories describing the impact of schema extensions on your Active Directory environment. Make sure you review them carefully before extending the schema. For more information, see [What You Must Know Before Extending the Schema](https://docs.microsoft.com/en-us/windows/win32/ad/what-you-must-know-before-extending-the-schema?redirectedfrom=MSDN).
  * Adding a class or attribute to the schema is permanent. However, you can disable a class or attribute that you no longer require after adding it. For more information, see [Disabling Existing Classes and Attributes](https://docs.microsoft.com/en-us/windows/win32/ad/disabling-existing-classes-and-attributes?redirectedfrom=MSDN).



## How schema extension works

When you initiate schema extension for a domain, Managed Microsoft AD validates the LDIF file for structure, format of schema elements, and supported changetypes or actions.

If the LDIF file is valid, Managed Microsoft AD takes a backup of the domain before applying the schema changes. If you encounter any problems with your application after updating the schema, you can use this backup to restore the domain. Then, Managed Microsoft AD isolates one of your domain controllers from the domain and applies the schema changes using the [Ldifde tool](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc731033\(v=ws.11\)). While schema changes are in progress, other domain controllers in your domain serve the client traffic.

If the schema changes succeed, then the isolated domain controller connects back to the domain and replicates these schema changes to other domain controllers in the domain.

If the schema changes fail, Managed Microsoft AD reverts the domain controller to the backed up state.

Managed Microsoft AD doesn't support partial schema extension on a domain. In other words, if any of the commands in the LDIF file fails to apply on the domain, the schema extension request fails. Managed Microsoft AD also reverts your domain back to the state it was prior to applying the schema changes.

**Note:** If you have your domain deployed in only one region when the schema extension is in progress, then only one domain controller serves your client traffic. For high availability, we recommend that you deploy your domain in at least two regions before you extend the schema.

## What's next

  * Learn how to [extend schema](https://docs.cloud.google.com/managed-microsoft-ad/docs/extend-schema) in Managed Microsoft AD.
  * [Restrictions on Schema Extension](https://docs.microsoft.com/en-us/windows/win32/ad/restrictions-on-schema-extension?redirectedfrom=MSDN)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
