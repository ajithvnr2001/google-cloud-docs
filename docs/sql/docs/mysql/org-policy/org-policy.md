---
url: https://docs.cloud.google.com/sql/docs/mysql/org-policy/org-policy/
title: Cloud SQL organization policies \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:27.666224+00:00
---

# Cloud SQL organization policies  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/org-policy/org-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Cloud SQL organization policies Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/org-policy/org-policy "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/org-policy/org-policy "View this page for the SQL Server database engine")

This page explain how to use an organization policy with your Cloud SQL project. To get started creating organization policies, see [Add organization policies](https://docs.cloud.google.com/sql/docs/mysql/org-policy/configure-org-policy).

## Overview

Organization policies let organization administrators set restrictions on how users can configure instances under that organization. Organization policies use rules, called constraints, that the organization administrator places on a project, folder, or organization. Constraints enforce the policy across all instances. If, for example, you try to create an instance in an entity that has an organization policy, the constraint runs a check to ensure the instance configuration follows the requirements of the constraint. If the check fails, Cloud SQL doesn't create the instance.

As you add projects to an organization or folder that uses an organization policy, the projects inherit the constraints of that policy.

For more information about organization policies, see [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview), [Constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints), and [ Hierarchy Evaluation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy).

The types of organization policies specific to Cloud SQL are as follows:

  * Predefined organization policies
    * Connection organization policies
    * Customer-managed encryption keys (CMEK) organization policies
  * Custom organization policies



## Predefined organization policies

You can use the predefined constraints to control the public IP settings and Customer Managed Encryption Key (CMEK) settings of Cloud SQL instances. For more granular, customizable control over other supported settings, you can use custom constraints. For more information, see [custom organization policies](https://docs.cloud.google.com/sql/docs/mysql/org-policy/org-policy#custom_constraints).

### Connection organization policies

Connection organization policies provide centralized control of the public IP settings for Cloud SQL, to reduce the security attack surface of Cloud SQL instances from the Internet. An organization policy administrator can use a connection policy to restrict public IP configurations of Cloud SQL at the project, folder, or organization level.

#### Connection organization policy constraints

For the connection organization policy, there are two types of predefined constraints that enforce access to Cloud SQL instances. There are also [custom organization policies](https://docs.cloud.google.com/sql/docs/mysql/org-policy/org-policy#custom_constraints) that can be used to enforce connection organization policies. For more information, see the ipConfiguration examples in [example custom constraints](https://docs.cloud.google.com/sql/docs/mysql/org-policy/custom-org-policy#example_constraints).

Constraint | Description | Default behavior  
---|---|---  
Restrict public IP access on Cloud SQL instances  |  This boolean constraint restricts configuring public IP on Cloud SQL instances where this constraint is set to `True`. This constraint isn't retroactive. Cloud SQL instances with existing public IP access still work even after this constraint is enforced.   
  
By default, public IP access to Cloud SQL instances is allowed.   
  
`constraints/sql.restrictPublicIp` | Allowed  
Restrict Authorized Networks on Cloud SQL instances  |  When set to `True`, this boolean constraint restricts adding Authorized Networks for unproxied database access to Cloud SQL instances. This constraint isn't retroactive. Cloud SQL instances with existing Authorized Networks still work even after this constraint is enforced.   
By default, you can add Authorized Networks to Cloud SQL instances.   
  
`constraints/sql.restrictAuthorizedNetworks` | Allowed  
  
#### Restrictions for connection organization policies

When you set the organization policy for each project, you need to determine if any one of the following apply to your project:

  * Read replicas public IP conflicts
  * Incompatibility using [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) sql connect 
  * Google Cloud hosted services access
  * MySQL failover replica public IP conflicts
  * Non-RFC 1918 private IP addresses



##### Read replicas public IP address conflicts

Cloud SQL read replicas connect to the primary instance over the non-proxied database connection. You use the primary instance **Authorized Networks** setting to either explicitly or implicitly configure the read replica public IP addresses.

If both the primary and replica instances are within the same region and enable private IP, there's no conflict with connection organization policy constraints.

##### Incompatibility using `gcloud sql connect`

The `gcloud sql connect` command uses a public IP address to connect to Cloud SQL instances directly. Therefore, it is incompatible with the `sql.restrictPublicIp` constraint. This is generally a problem for instances that use private IP.

In addition, the `gcloud sql connect` command doesn't use the proxy, making it incompatible with the `sql.restrictAuthorizedNetworks` constraint.

Instead, use the beta version of the command:
    
    
    gcloud beta auth login
    gcloud beta sql connect [INSTANCE_ID]
    

This version uses the Cloud SQL Auth Proxy. See [`gcloud beta sql connect`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/connect) for reference information.

The first time you run this command, you are prompted to install the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) Cloud SQL Auth Proxy component. For that, you need to have write permission to the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) SDK installation directory on your client machine.

##### Google Cloud hosted services access

If your application requires access to Cloud SQL instances from other Google Cloud hosted services, such as App Engine, the application must use public IP addresses. Don't enforce the `sql.restrictPublicIp` constraint on the project. You can, however, enforce `sql.restrictAuthorizedNetworks`, as connections from [App Engine go through the secure (proxied) connection](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine).

##### MySQL failover replica public IP conflicts

A MySQL failover replica acts the same as a read replica for connection organization policies. If both the primary and replica instances are within the same region and enable private IP, there's no conflict with connection organization policy constraints.

##### Non-RFC 1918 private IP addresses

Connections to a Cloud SQL instance using a private IP address are automatically authorized for [RFC 1918 address ranges](https://docs.cloud.google.com/vpc/docs/vpc#valid-ranges). This lets all private clients access the database without going through the proxy. You must configure non-RFC 1918 address ranges as [authorized networks](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks).

To use non-RFC 1918 private IP ranges that are not configured in the authorized networks, you can take one or both of the following actions:

  1. Don't enforce `sql.restrictAuthorizedNetworks`. If the authorized networks also enforce `sql.restrictPublicIp`, you can't configure them in the console. Instead, use the Cloud SQL API or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).
  2. Use proxied connections for private IP instances.



### Customer-managed encryption keys (CMEK) organization policies

Cloud SQL supports two organization policy constraints that help ensure CMEK protection across an organization: `constraints/gcp.restrictNonCmekServices` and `constraints/gcp.restrictCmekCryptoKeyProjects`.

The `constraints/gcp.restrictNonCmekServices` constraint requires CMEK protection for the `sqladmin.googleapis.com`. When you add this constraint and add the `sqladmin.googleapis.com` to the `Deny` policy list of services, Cloud SQL refuses to create new instances unless they are enabled with CMEK.

The `constraints/gcp.restrictCmekCryptoKeyProjects` constraint limits which Cloud KMS CryptoKeys to use for CMEK protection in Cloud SQL for MySQL instances. With this constraint, when Cloud SQL creates a new instance with CMEK, the CryptoKey must come from an allowed project, folder, or organization.

These constraints are only enforced on newly created Cloud SQL for MySQL instances.

For more overview information, see [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy). For information about CMEK organization policy constraints, see [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

## Custom organization policies

For granular, customizable control over the settings, you can create _custom constraints_ and use those custom constraints in a custom organization policy. You can use custom organization policies to improve your security, compliance, and governance.

To learn how to create custom organization policies, see [Add custom organization policies](https://docs.cloud.google.com/sql/docs/mysql/org-policy/custom-org-policy). You can also view a list of [supported fields for custom constraints](https://docs.cloud.google.com/sql/docs/mysql/org-policy/custom-org-policy#supported-fields).

## Organization policy enforcement rules

Cloud SQL enforces the organization policy during the following operations:

  * Instance creation
  * Replica creation
  * Instance restart
  * Instance migration
  * Instance clone



Like all [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints), policy changes don't apply retroactively to existing instances.

  * A new policy has no effect on existing instances.
  * An existing instance configuration remains valid, unless a user changes the instance configuration from a compliance to non-compliance state using the Console, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or RPC.
  * A scheduled maintenance update doesn't cause a policy enforcement, because maintenance doesn't change the configuration of instances.



## What's next

  * [Configuring organization policies](https://docs.cloud.google.com/sql/docs/mysql/org-policy/configure-org-policy).
  * Learn about how [private IP](https://docs.cloud.google.com/sql/docs/mysql/private-ip) works with Cloud SQL.
  * Learn how to [configure private IP](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip) for Cloud SQL.
  * Learn about the [organization policy service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).
  * Learn about [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
