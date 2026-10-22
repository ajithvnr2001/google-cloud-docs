---
url: https://docs.cloud.google.com/alloydb/docs/pgaudit/configure-log-behavior/
title: Configure logging behavior \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:55.526979+00:00
---

# Configure logging behavior  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/pgaudit/configure-log-behavior/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Configure logging behavior Stay organized with collections  Save and categorize content based on your preferences. 

To configure pgAudit logging behavior, you set the `pgaudit.log` flag or the `pgaudit.role` flag:

  * Set `pgaudit.log` to enable and configure session logging. You can set this flag on an instance, a database, or a role to define the scope of operations that the pgAudit logs. You set the flag to a value that defines the type of operations that the pgAudit logs.

  * Set `pgaudit.role` to enable and configure object logging, which logs statements that affect particular relations. You set this flag to the name of a role, and then grant statement access to specific objects that you want to be logged. The statement access includes `SELECT, INSERT, UPDATE, and DELETE`. pgAudit logs all operations that match the combination of access and object run by any user.




The following sections provide examples that show the options for setting pgAudit logging behavior.

**Note:** Database users created through `CREATE ROLE` commands do not have the privilege to modify audit settings. Only database users created through the Google Cloud console and the gcloud command can modify audit settings. 

For additional capabilities of the extension, review the [pgAudit documentation](https://github.com/pgaudit/pgaudit/blob/master/README.md/).

## Configure session audit logging for all databases in an instance

To configure auditing for all databases in an instance, set the `pgaudit.log` flag at the instance level.

For example:

  * To enable auditing for all operations on all databases in an instance: 
        
        gcloud alloydb instances update my-instance \
            --database-flags pgaudit.log=all[,flag2=value2...] \
            --region=us-central1 \
            --cluster=my-cluster \
            --project=my-project
        

  * To enable auditing for only read and write operations on all databases in an instance: 
        
        gcloud alloydb instances update my-instance \
            --database-flags=^:^pgaudit.log=read,write[:flag2=value2...] \
            --region=us-central1 \
            --cluster=my-cluster \
            --project=my-project
        




Note the use of [alternate delimiter syntax](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping), which lets you use comma characters within a flag value.

For information about configuring database flags, see [Configure database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

## Configure session audit logging for a specific database

You can configure auditing for a specific database by setting the `pgaudit.log` flag at the database-level.

For example, to enable read/write auditing for a database, finance:

`finance=> ALTER DATABASE finance SET pgaudit.log = 'read,write';`

## Configure session audit logging for a single user

You can enable auditing for a specific user by setting the `pgaudit.log` on a per role level.

For example, to set auditing for all database operations executed by the user, Alice:

`finance=> ALTER ROLE alice SET pgaudit.log = 'all';`

## Configure object audit logging

Auditing for a relation is narrower than auditing for a specific database. When you audit for a relation, the system assigns a unique auditor role to the `pgaudit.role` parameter. This operation logs any object or relation that is granted to this role.

For example:

  * To configure auditing for all `SELECT` queries on the salary relation within the employee database: 
        
        employee=> CREATE ROLE auditor WITH NOLOGIN;
        employee=> ALTER DATABASE employee SET pgaudit.role = 'auditor';
        employee=> GRANT SELECT ON salary TO auditor;
        




You also can audit a subset of columns for a given relation.

For example:

  * To configure audit logging that occurs only when the `income` and `tax_status` columns are accessed from the salary relation: 
        
        employee=> GRANT SELECT(income, tax_status) ON salary TO auditor;
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
