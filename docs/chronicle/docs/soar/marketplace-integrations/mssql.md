---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mssql/
title: MSSQL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:45.919290+00:00
---

# MSSQL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mssql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# MSSQL

This document provides guidance on how to integrate Microsoft SQL Server with Google SecOps.

**Important:** In the Google SecOps platform, the MSSQL integration refers to _Microsoft SQL Server_.

## Before you begin

This section helps you configure a Google SecOps remote agent (RHEL, CentOS, or Docker) to work with SQL Server using Kerberos authentication.

### Configure a Google SecOps remote agent (RHEL or CentOS)

To configure a Google SecOps remote agent (RHEL or CentOS) to work with SQL Server, complete the following steps in the remote agent Linux shell:

  1. Add your DNS servers to the `/etc/resol.conf` file: `#vi /etc/resolv.conf`

  2. Install the krb5 package for CentOS 7: `#yum install krb5-workstation`

  3. Open the `/etc/krb5.conf` file and add your domain as `default_realm`: `#vi etc/krb5.conf`.

**Note:** The domain must be in full FQDN syntax and uppercase.
  4. Test connection with Active Directory. Use a user that has access to the SQL Server database: `#kinit sql_user`

  5. Input your user password.

  6. Show the obtained ticket: `#klist`

  7. Optional: Remove the kerberos ticket: `#kdestroy -A`




For more information about creating a remote agent on CentOS using the Microsoft SQL integration, see [Create agent with installer for CentOS](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/create-agent-with-installer-on-centos#using-microsoft-sql-integration-optional).

### Configure a Google SecOps remote agent (Docker)

To configure a Google SecOps remote agent (Docker) to work with SQL Server, complete the following steps in the remote agent Linux shell:

  1. Run a shell in a docker container: `docker exec -it siemplify /bin/bash`

  2. Add your domain DNS servers to the `/etc/resol.conf` file: `#vi /etc/resolv.conf`

  3. Install the krb5 package for CentOS 7: `#yum install krb5-workstation`

  4. Open the `/etc/krb5.conf` file and add your domain as `default_realm` with uppercase: `#vi etc/krb5.conf`
         
         Note: The domain must be in full FQDN syntax and in upper case.
         

  5. Obtain a kerberos ticket. Use a user that has access to the SQL Server database: `#kinit sql_user`

  6. Enter your user password.

  7. Show the obtained ticket: `#klist`

  8. Optional: Remove the kerberos ticket: `#kdestroy -A`




For more information about creating a remote agent on Docker, see [Create agent with Docker](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-agent-with-docker).

### Optional: Install SQL Server tools for debugging

To install the SQL Server tools for debugging, complete the following steps in the remote agent Linux shell:

  1. Add the Microsoft repository: `# curl https://packages.microsoft.com/config/rhel/7/prod.repo > /etc/yum.repos.d/msprod.repo`

  2. Install SQL Server tools: `# yum install mssql-tools unixODBC-devel`

Binaries are installed in the following directory: `/opt/mssql-tools/bin`.

  3. Test the connection to SQL Server: `#kinit sql_user`

  4. Run the following command: `/opt/mssql-tools/bin/sqlcmd -S sqlserver.yourdomain.com -E`
         
         Note: The domain must be in full FQDN syntax and in upper case.
         




## Integrate MSSQL with Google SecOps

The integration requires the following parameters:

Parameters | Description  
---|---  
`Server Address` | _Required_ An address of the SQL Server instance. The default value is `sqlserver.DOMAIN.com`. The domain must be in full FQDN syntax and uppercase.  
`Username` | _Optional_ The username of the SQL Server instance.  
`Password` | _Optional_ The user password.  
`Port` | _Optional_ The port to use in the integration.  
`Windows Authentication` | _Optional_ If selected, the integration authenticates using the Windows authentication. Not selected by default.  
`Use Kerberos Authentication` | _Optional_ If selected, the integration authenticates using the Kerberos authentication. Not selected by default.  
`Kerberos Realm` | _Optional_ The Kerberos realm value.  
`Kerberos Username` | _Optional_ The username for the Kerberos authentication.  
`Kerberos Password` | _Optional_ The password for the Kerberos authentication.  
`Verify SSL` | _Optional_ If selected, the integration verifies that the SSL certificate for the connection to the SQL Server is valid. Selected by default.This parameter applies only for the Microsoft ODBC driver for SQL Server version 18. If the Google SecOps server host runs earlier ODBC driver versions, the integration ignores this parameter.  
  
For instructions about configuring an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if necessary. After you configure an integration instance, you can use it in playbooks. For more information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

The SQL Server integration includes the following actions:

  * Ping
  * Run SQL Query



### Ping

Use the **Ping** action to test connectivity to the SQL Server.

This action runs on all entities.

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Not available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Run SQL Query

Use the **Run SQL Query** action to run SQL queries.

This action runs on all entities.

#### Action inputs

The **Run SQL Query** action requires the following parameters:

Parameters | Description  
---|---  
`Database Name` | _Required_ The database name to run the query on.  
`` | _Required_ The query to run.The default value is `SELECT * FROM <>`.  
  
#### Action outputs

The **Run SQL Query** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Not available  
Script result | Available  
  
##### JSON result

The following shows an example of the JSON result output received when using the **Run SQL Query** action:
    
    
    [
        {
            "Name": "Actions Monitor System",
            "Creator": "System",
            "Integration": "Example",
            "VersionId": "VERSION_ID",
            "ModificationTimenixTimeInMs": 1558278307098,
            "Description": "Notifies of all the actions, that have individually failed at least 3 times, in the last 3 hours"
        },{
            "Name": "Jobs Monitor System",
            "Creator": "System",
            "Integration": "Example",
            "VersionId": "VERSION_ID",
            "ModificationTimenixTimeInMs": 1558278307098,
            "Description": "Notifies of all the jobs, that have individually failed at least 3 times, in the last 3 hours"
        }
    ]
    

##### Script result

The following table describes the values for the script result output when using the **Run SQL Query** action:

Script result name | Value  
---|---  
`is_blocked` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
