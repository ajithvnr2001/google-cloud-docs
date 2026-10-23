---
url: https://docs.cloud.google.com/sql/docs/sqlserver/ad/
title: Overview of Managed Microsoft AD in Cloud SQL \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:27.238873+00:00
---

# Overview of Managed Microsoft AD in Cloud SQL  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/ad/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Overview of Managed Microsoft AD in Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

You can integrate Cloud SQL for SQL Server with Managed Service for Microsoft Active Directory (also called Managed Microsoft AD).

This page contains information to review before you start an integration. After reviewing the following information, including the limitations, see [Using Cloud SQL with Managed Microsoft AD](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad).

## Advantages of integrating with Managed Microsoft AD

Authentication, authorization, and more are available through [Managed Microsoft AD](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview). For example, joining an instance to a Managed Microsoft AD domain lets you to sign in using Windows Authentication with an AD-based identity.

Integrating Cloud SQL for SQL Server with an AD domain has the additional advantage of Cloud integration with your on-premises AD domains.

## Prerequisites for integration

**Note:** Only instances created after March 12, 2021, are supported. If you try to join an instance to a domain and it fails, check the instance creation date. 

You can integrate with Managed Microsoft AD, [adding support for Windows Authentication](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad) to an instance. However, before integrating, the following are required for your Google Cloud project:

  * A Managed Microsoft AD domain. For information about setting up a domain, see [Create a domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain). 
    * On-premises AD domains require a managed AD trust. See [Creating a one-way trust](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-trust) and [Use an on-premises AD user to create a Windows login to Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad#on-premises-ad-users).
  * A Per-Product, Per-Project Service account, as described in the following sections; see Creating a service account.



## Create and configure a service account

**Note:** To create a service account with the required permissions, you must have the `resourcemanager.projects.setIamPolicy` permission. This permission is included in the Project Owner, Project IAM Admin, and Organization Administrator roles. You also must enable the Cloud SQL Admin API. 

You need a Per-Product, Per-Project Service account for each project that you plan to integrate with Managed Microsoft AD. Use `gcloud` or the Console to create the account at the project level. The Per-Product, Per-Project Service account should be granted the `managedidentities.sqlintegrator` role on the project. For additional information, see [gcloud projects set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/projects/set-iam-policy).

If you are using the Google Cloud console, then Cloud SQL automatically creates a service account for you, and prompts you to grant the `managedidentities.sqlintegrator` role.

To create a service account with `gcloud`, run the following command:
    
    
    gcloud beta services identity create --service=sqladmin.googleapis.com \
        --project=PROJECT_NUMBER

That command returns a service account name in the following format:
    
    
        service-PROJECT_NUMBER@gcp-sa-cloud-sql.iam.gserviceaccount.com

Here is an example of a service account name:
    
    
        service-333445@gcp-sa-cloud-sql.iam.gserviceaccount.com

Granting the necessary permission for integration requires existing permissions. For the required permissions, see [Required permissions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#required-permissions).

To grant the necessary permission for integration, run the following command. If your Managed Microsoft AD is in a different project, `AD_PROJECT_ID` should be the one containing the Managed Service for Microsoft Active Directory instance, while the service account's `SQL_PROJECT_NUMBER` should be the one containing the SQL Server instance:
    
    
    gcloud projects add-iam-policy-binding AD_PROJECT_ID \
    --member=serviceAccount:service-SQL_PROJECT_NUMBER@gcp-sa-cloud-sql.iam.gserviceaccount.com \
    --role=roles/managedidentities.sqlintegrator

Also see [gcloud beta services identity create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/identity/create).

## Best practices for integrating with Managed Microsoft AD

When you plan an integration, review the following:

  * Prerequisites for integration
  * [Integrating with a managed AD domain in a different project](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad#integrating-different-project)
  * [Managed Microsoft AD documentation](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)
  * [Deploy domain controllers in additional regions](https://docs.cloud.google.com/managed-microsoft-ad/docs/add-remove-regions)
  * [Use the AD diagnosis tool](https://docs.cloud.google.com/sql/docs/sqlserver/ad-diagnosis-tool) to troubleshoot AD setup issues with your on-premises domain and Cloud SQL for SQL Server instances in Google Cloud console.



Having a SQL Server instance and a managed AD instance in the same region offers the lowest network latency and the best performance. Thus, when possible, set up a SQL Server instance and an AD instance in the same region. Additionally, whether or not you set them up in the same region, set up a primary and a backup region for higher availability.

### Topologies for integrating with Managed Microsoft AD

Cloud SQL for SQL Server doesn't support domain local groups. However, you can:

  * Add global groups or individual user logins directly in SQL Server
  * Use universal groups when all groups and users belong to the same forest



If domain local groups were supported, individual user accounts, and global and universal groups, could be added as children of a domain local group (that guards access to SQL Server). This would enable you to add a domain local group as a SQL Server login. In Cloud SQL for SQL Server, you can enable similar capabilities, as described in this section.

#### Option 1: Add user accounts and groups as logins to SQL Server

If you have multiple domains, in multiple forests, and you have multiple global groups, you can add all of the individual user accounts, and the global and universal groups, directly as logins to SQL Server. As an example of Option 1, see the following diagram:

![AD topology, Option 1.](https://docs.cloud.google.com/static/sql/images/ad-topology-option-1.png)

#### Option 2: Define a universal group in one of your domains

If your domains are in the same forest, you can define a universal group in one of your domains. Then you can add all of the individual user accounts, and the global and universal groups, as children of that defined universal group, and add the defined universal group as a SQL Server login. As an example of Option 2, see the following diagram:

![AD topology, Option 2.](https://docs.cloud.google.com/static/sql/images/ad-topology-option-2.png)

## Limitations and alternatives

**Note:** For information related to this section, see Unsupported for integration. 

The following limitations apply when integrating with Managed Microsoft AD:

  * Domain local groups are not supported, but you can add global groups or individual user logins directly in SQL Server. Alternatively, you can use universal groups when all groups and users belong to the same forest.
  * In general, new users created through the Google Cloud console are assigned the `CustomerDbRootRole` role, which has this [SQL Server Agent fixed database role](https://docs.microsoft.com/en-us/sql/ssms/agent/sql-server-agent-fixed-database-roles?view=sql-server-ver15): `SQLAgentUserRole`. However, users created through SQL Server directly, such as Managed Microsoft AD users, cannot be granted this role, or use SQL Server Agent, because the MSDB database where this role must be granted is protected.
  * Some restricted operations may result in the following error: "Could not obtain information about Windows NT group/user". One example of this type of restricted operation is creating logins by users from domains that are connected through a trust relationship. Another example is granting privileges to users from domains that are connected through a trust relationship. In these cases, retrying the operation is often successful. If retrying fails, close the connection and open a new connection.
  * Fully qualified domain names (FQDNs) aren't supported by SQL Server on Windows. Therefore, use domain names (short names), rather than FQDNs, when you create SQL Server logins. For example, if your domain name is `ad.mydomain.com`, then create SQL Server logins for `ad\user`, rather than for `ad.mydomain.com\user`.
  * To access SQL Server instances, always use FQDNs. For example, you could use an FQDN similar to `private.myinstance.us-central1.myproject.cloudsql.mydomain.com`. Netbios names aren't supported, nor are any short names if DNS suffixes are omitted.
  * SQL Server logins based on Active Directory users and groups cannot be managed from the Google Cloud console.
  * In Cloud SQL, if a SQL Server instance was created on or before March 12, 2021, it cannot be integrated with Managed Microsoft AD.
  * Windows Authentication won't work with an external trust. The error might be the following: "The target principal name is incorrect. Cannot generate SSPI context." Additionally, as related to [Microsoft's recommendations](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/dd560679\(v=ws.10\)), use a forest trust instead of an external trust for Kerberos authentication.

**Note:** Managed domains with fewer than eight characters (such as the seven-character domain of xyz.com) are unsupported. As a workaround, create a managed domain with a longer name. 

## Active Directory endpoints and TLS connections

If you're using Windows Authentication and you want to establish a TLS connection without trusting the server certificate, you must rotate the certificates after Windows Authentication is enabled on the instance.

If the connection fails and one of your certificates was created before March 15, 2025, you must rotate the [server certificate](https://docs.cloud.google.com/sql/docs/sqlserver/manage-ssl-instance) again and try the connection again.

## Unsupported for integration

**Note:** For alternatives to some unsupported operations, see Limitations and alternatives. 

The following features are unsupported when integrating with Managed Microsoft AD:

  * Domain local groups.
  * Dropping SQL Server logins by users from domains that are connected through a trust relationship. You can do this operation with a user from your managed domain, or through the `sqlserver` login.
  * NTLM authentication.
  * Login with an IP address from domains connected through a trust relationship.
  * Instances with long names (more than 63 characters).



## What's next

  * Review the [ Quickstart for creating a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain).
  * Prepare to [ create an integrated Cloud SQL instance](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad#creating-an-instance-with-windows-authentication).
  * Learn how to [ create a trust relationship](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-trust) between on-premises domains and a Managed Microsoft AD domain.
  * Review how to [ view integrated instances](https://docs.cloud.google.com/managed-microsoft-ad/docs/viewing-sql-server-integrations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
