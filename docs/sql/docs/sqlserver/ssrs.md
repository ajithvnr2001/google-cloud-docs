---
url: https://docs.cloud.google.com/sql/docs/sqlserver/ssrs/
title: SQL Server Reporting Services (SSRS) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:30.539239+00:00
---

# SQL Server Reporting Services (SSRS)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/ssrs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  SQL Server Reporting Services (SSRS) Stay organized with collections  Save and categorize content based on your preferences. 

Cloud SQL supports [SQL Server Reporting Services (SSRS)](https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-ver16) which helps you create, deploy, and manage paginated reports.

This page provides the prerequisites, setup procedure, and limitations for using SSRS in Cloud SQL.

## Before you begin

Before using SSRS on Cloud SQL, you must have the following:

  * A Cloud SQL instance to host the report server database
  * A host where you install and run SSRS. It can be either a Compute Engine VM or a host that doesn't use Compute Engine. For installation instructions, see [Install SQL Server Reporting Services](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services?view=sql-server-ver16).
  * A Cloud DNS record to assign a hostname for your Cloud SQL instance. You can create a hostname by using one of the following options:

    * Cloud DNS: Use [Cloud DNS](https://docs.cloud.google.com/dns/docs/overview) to create a hostname that points to your instance.
    * Custom DNS zone: If you manage your own DNS zone, then [create an A record](https://docs.cloud.google.com/dns/docs/records) that maps your preferred hostname to the IP address of your instance.
    * Local hostname mapping: Modify your system's `hosts` file to create a custom alias for your instance.
  * Two existing Cloud SQL logins, a setup login and a service login. To create a login, see [`gcloud sql users create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/create).

**Note:** Cloud SQL doesn't support using Windows logins for SSRS. If you want to use Windows authentication, then you must use Active Directory to join the SQL Server instance and the host running SSRS. For more information, see [Use Managed Service for Microsoft Active Directory with Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad) or [Use customer-managed Active Directory](https://docs.cloud.google.com/sql/docs/sqlserver/configure-cmad).



## Procedure

To set up SSRS in Cloud SQL, perform the following steps:

  1. [Acquire an SSRS lease](https://docs.cloud.google.com/sql/docs/sqlserver/ssrs#acquire).
  2. [Set up SSRS](https://docs.cloud.google.com/sql/docs/sqlserver/ssrs#setup).
  3. [Release an SSRS lease](https://docs.cloud.google.com/sql/docs/sqlserver/ssrs#release).



### Acquire an SSRS lease

SSRS requires elevated permissions during setup. To acquire an SSRS lease for your instance, use the following command:

### gcloud

Use the following command to acquire a lease:
    
    
    gcloud sql instances acquire-ssrs-lease INSTANCE_NAME \
    --project=PROJECT_NAME \
    --setup-login=SETUP_LOGIN \
    --service-login=SERVICE_LOGIN \
    --report-database=REPORT_DATABASE \
    --duration=DURATION \

The following table describes this operation's `gcloud` parameters: 

**Parameter** | **Description** | **Allowed values** | **Default value**  
---|---|---|---  
`--setup-login` |  Required. The login used to connect to the instance during SSRS setup. This is the first login that is requested in Report Server Configuration Manager when setting a report server database.  | This must be a existing SQL Server login, such as `sqlserver` | None  
`--service-login` | Required. The SQL Server login used by report server to connect to the report server database during SSRS setup. This is the second login that is requested in Report Server Configuration Manager when setting a report server database. | This must be an existing SQL Server login and must be different from the setup login. | None.  
`--report-database` | Required. An existing or a new report database name on the instance. | Certain special characters are not allowed in the report database name, such as spaces, brackets, non-English characters. | None  
`--duration` | Optional. The number of hours that the SSRS lease is active during which you can perform the SSRS setup. | Between 1 and 12 hours. For example, `4h` | 5 hours  
  
### REST v1

Using the REST API, you can acquire an SSRS lease on an instance. To acquire an SSRS lease, specify the following: 

  * Two different SQL Server logins, the setup login and service login
  * The report database name
  * The duration for which the lease is active



Only the `DURATION` field is optional. For more information, see [ AcquireSsrsLeaseContext](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances#AcquireSsrsLeaseContext): 

  * PROJECT_ID: the ID of the project.
  * INSTANCE_NAME: the name of the instance.
  * SETUP_LOGIN: the SQL Server login that's used to connect to the SQL Server instance during SSRS setup. This the first login that is requested in Report Server Configuration Manager when setting a report server database.
  * SERVICE_LOGIN: the SQL Server login that's used by report server to connect to the report server database during SSRS setup. This is the second login that is requested in Report Server Configuration Manager when setting a Report Server Database.
  * REPORT_DATABASE: an existing or a new report database name on the instance. Microsoft doesn't allow certain special characters in the report database name, such as spaces, brackets, non-English characters.
  * DURATION: Optional. The number of hours that the SSRS lease is active during which you can perform the SSRS setup. Between 1 and 12 hours, for example, `4h`.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_NAME/acquireSsrsLease

Request JSON body: 
    
    
    {
      "acquireSsrsLeaseContext": {
        "setupLogin": SETUP_LOGIN,
        "serviceLogin": SERVICE_LOGIN,
        "reportDatabase": REPORT_DATABASE,
        "duration": DURATION,
      }
    }

### REST v1beta4

Using the REST API, you can acquire an SSRS lease on an instance. To acquire an SSRS lease, specify the following: 

  * Two different SQL Server logins, the setup login and service login
  * The report database name
  * The duration for which the lease is active



Only the `DURATION` field is optional. For more information, see [ AcquireSsrsLeaseContext](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances#AcquireSsrsLeaseContext): 

  * PROJECT_ID: the ID of the project.
  * INSTANCE_NAME: the name of the instance.
  * SETUP_LOGIN: the SQL Server login that's used to connect to the SQL Server instance during SSRS setup. This the first login that is requested in Report Server Configuration Manager when setting a report server database.
  * SERVICE_LOGIN: the SQL Server login that's used by report server to connect to the report server database during SSRS setup. This is the second login that is requested in Report Server Configuration Manager when setting a Report Server Database.
  * REPORT_DATABASE: an existing or a new report database name on the instance. Microsoft doesn't allow certain special characters in the report database name, such as spaces, brackets, non-English characters.
  * DURATION: Optional. The number of hours that the SSRS lease is active during which you can perform the SSRS setup. Between 1 and 12 hours, for example, `4h`.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME/acquireSsrsLease

Request JSON body: 
    
    
    {
      "acquireSsrsLeaseContext": {
        "setupLogin": SETUP_LOGIN,
        "serviceLogin": SERVICE_LOGIN,
        "reportDatabase": REPORT_DATABASE,
        "duration": DURATION,
      }
    }

### Set up SSRS

**Note:** To automate the setup process described in this section, you can use any scripting solution, such as PowerShell.

To perform the SSRS setup, follow these steps:

  1. Open Reporting Services Configuration Manager on the host where SSRS is installed.
  2. Connect to your local report server instance.
  3. Click **Change Database**. 
     1. Enter the SQL Server hostname created in Cloud DNS and the SQL Server login credentials for the setup login used for the SSRS lease.
     2. Enter the name of a new report server database or existing report database used for the SSRS lease.
     3. Enter the SQL Server login credentials for the service login used for the SSRS lease.
     4. Click **Next** and finish through the last step.
  4. If not already set, then configure the **Web Service URL** and **Web Portal URL**. The Web Portal should load successfully within a few seconds.



### Release an SSRS lease

You can release a lease manually, or you can wait until the lease automatically expires. Releasing the lease is required to revert any elevated permissions needed for setup and to allow the service login to connect to the report database. The service login can't access the report database until the lease expires or is released manually. The following command releases an SSRS lease.

### gcloud

Use the following command to release a lease:
    
    
    gcloud sql instances release-ssrs-lease INSTANCE_NAME \
    --project=PROJECT_NAME

### REST v1

Using the REST API, you can release an SSRS lease for an instance. As shown in the following request example, you only need to provide the instance name and project ID. 

  * PROJECT_ID: the ID of the project.
  * INSTANCE_NAME: the name of the instance.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME/releaseSsrsLease

### REST v1beta4

Using the REST API, you can release an SSRS lease for an instance. As shown in the following request example, you only need to provide the instance name and project ID. 

  * PROJECT_ID: the ID of the project.
  * INSTANCE_NAME: the name of the instance.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME/releaseSsrsLease

## Limitations

  * You can't host SSRS reports on or execute them from Cloud SQL.
  * Active Directory logins are not supported for setting up the report database.
  * The report database name can contain only alphanumeric characters and hyphens.
  * You must acquire a lease for changing the login used to connect to the report database through Report Server Configuration Manager.
  * For a database that is processed by a service login, the import sql files and delete replicated database operations can fail between the completion of the SSRS setup and the release of the lease.
  * You must delete and recreate the database user for the service login on an imported report database. This is because the existing user in the imported database doesn't belong to the new instance.
  * When adding new report servers for a scale-out deployment in SSRS, you must acquire and release the SSRS lease for every new Windows VM hosting a report server. Each Cloud SQL instance requires that you configure the new report database by using the existing report database.
  * You must create a new lease every time you want to change the login credentials for the report server database in Report Server Configuration Manager.



## Frequently asked questions

The following sections help address frequently asked questions related to SSRS.

### Setup and lease mechanism

The following sections help address setup and SSRS lease questions.

#### How do I set up SSRS with Cloud SQL?

You need to install SSRS on a separate Windows host, like a Compute Engine VM. Then, configure SSRS to use your Cloud SQL instance for the ReportServer and ReportServerTempDB databases. The "SSRS lease" is an important part of this process if you are managing setup using Cloud SQL.

#### What is the SSRS lease and why is it needed?

SSRS setup normally requires `sysadmin` permissions, which are not granted to users in Cloud SQL. The lease mechanism temporarily grants the necessary elevated permissions to a specified SQL Server login, for example, `--setup-login`, to complete the database setup.

You acquire a lease using [`gcloud sql instances acquire-ssrs-lease`](https://docs.cloud.google.com/sql/docs/sqlserver/ssrs#gcloud) before configuration and release it afterwards with [`gcloud sql instances release-ssrs-lease`](https://docs.cloud.google.com/sql/docs/sqlserver/ssrs#gcloud_1). The lease has a configurable duration.

### Authentication

The following section helps address authentication questions.

#### Can I use Windows Authentication (Microsoft Active Directory) for setup?

No, you must use SQL Server logins for the `--setup-login` and `--service-login` parameters when acquiring the lease and configuring the report server database. Windows logins are not supported for this initial setup process.

While setup requires SQL logins, you can potentially use Windows Authentication for accessing reports if your Cloud SQL instance and the SSRS host are both joined to one of the following domain types:

  * [Customer-managed Active Directory (CMAD)](https://docs.cloud.google.com/sql/docs/sqlserver/cmad) (recommended)
  * [Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



### Restrictions

The following section helps address questions related to restrictions or limitations.

#### What are the limitations of using SSRS with Cloud SQL?

  * There aren't any Microsoft Active Directory logins for the database setup phase.
  * The report database name can only contain alphanumeric characters and hyphens.
  * You must acquire a new lease if you want to change the service account credentials later.
  * Scale-out deployments require the lease process for each new SSRS host.
  * Importing existing report server databases requires manual steps to remap the service login user.



### Pricing considerations

The following section helps address pricing considerations.

#### What are the costs associated with licensing?

  * A SQL Server license is required for your Cloud SQL instance.
  * Since SSRS runs a separate Windows machine, make sure the Windows OS and any SQL Server components on that machine are properly licensed. According to Microsoft's policies, running SSRS on a separate server might require an additional SQL Server license. As an option, Cloud SQL does offer prebuilt SQL Server images.

For more information, see [SQL Server on Google Cloud](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing-faq#sql-server).




### Automation

The following section helps address questions related to automation.

#### Can you automate the SSRS host installation and configuration process?

You can run operations to acquire and release the SSRS lease within Cloud SQL using [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or REST APIs.

The SSRS installation and configuration within the Windows environment itself typically involves manual steps through the Reporting Services Configuration Manager interface, making full end-to-end automation more challenging.

For more information, see [Install and configure SSRS](https://learn.microsoft.com/en-us/sql/reporting-services/install-windows/install-reporting-services).

### Maintenance

The following section helps address questions related to maintenance.

#### What are the potential management and maintenance activities associated with using SSRS?

Before you begin, consider the ongoing management overhead associated with the separate SSRS server. You are responsible for managing, patching, and securing the Windows VM running the SSRS service. Cloud SQL only manages the database instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
