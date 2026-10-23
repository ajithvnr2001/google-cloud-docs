---
url: https://docs.cloud.google.com/sql/docs/mysql/use-db-audit/
title: Use MySQL database auditing \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:42.691039+00:00
---

# Use MySQL database auditing  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/use-db-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Use MySQL database auditing Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This topic describes how to enable and use the Cloud SQL for MySQL Audit Plugin. For an overview, see [MySQL database auditing](https://docs.cloud.google.com/sql/docs/mysql/db-audit). For more information about MySQL plugins, see [MySQL plugin loading](https://dev.mysql.com/doc/refman/8.0/en/plugin-loading.html).

**Note:** In this topic, Administrators and Auditors are referred to as audit users. 

## Before you begin

### Data Access audit logs

Enable and configure Data Access audit logs. See [Configure Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

### Privileges required for audit users

You must have `EXECUTE` privileges on the audit stored procedures to run them. If an administrator needs to change an auditor's access privileges to the audit stored procedures, they should use the `GRANT` or `REVOKE` command in the `mysql` client. For details about the user privileges, refer to [MySQL user privileges](https://docs.cloud.google.com/sql/docs/mysql/users#privileges). For example, if an administrator wanted to grant access to an auditor named `user`, to manage the audit rules, they could grant the privileges using the following statement:
    
    
    CREATE USER 'user'@'%' IDENTIFIED BY 'password';
    GRANT EXECUTE ON PROCEDURE mysql.cloudsql_list_audit_rule TO 'user'@'%';

If that administrator later wanted to revoke access to the auditor, they could revoke the privileges using the following statement:
    
    
    REVOKE ALL ON PROCEDURE mysql.cloudql_list_audit_rule FROM 'user'@'%';

By default, [users created using Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#creating) (except IAM users) are administrators who have all privileges except `FILE` and `SUPER`, including all privileges to the audit stored procedures. IAM database users, by default, have no privileges.

## Enable the Cloud SQL for MySQL Audit Plugin

The Cloud SQL for MySQL Audit Plugin (`cloudsql_mysql_audit`) controls the auditing behavior for a given database instance. To use the plugin, you must first enable it on the Cloud SQL instance.

To enable the `cloudsql_mysql_audit` plugin, use one of the following options:

  * `--cloudsql_mysql_audit=ON`

Tells the server to enable the plugin. If the plugin fails to initialize, the server runs with the plugin disabled. 

  * `--cloudsql_mysql_audit=FORCE`

Tells the server to enable the plugin, but if plugin initialization fails, the server does not start. In other words, this option forces the server to run with the plugin enabled or not at all. 

  * `--cloudsql_mysql_audit=FORCE_PLUS_PERMANENT`

Like FORCE, but also prevents the plugin from being unloaded at runtime. If a user tries to unload the plugin with [UNINSTALL PLUGIN](https://dev.mysql.com/doc/refman/8.0/en/uninstall-plugin.html), an error occurs. 




Plugin activation states are visible in the `PLUGIN_STATUS` column of the [INFORMATION_SCHEMA.PLUGINS](https://dev.mysql.com/doc/refman/8.0/en/information-schema-plugins-table.html) table.

**Note:** Changing the value of this audit flag requires a MySQL server **RESTART** each time. **Note:** Enabling logs might result in Cloud Logging charges for the additional logs usage. 

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Open the instance and click **Edit**.
  3. Scroll down to the **Flags** section.
  4. To set a flag that has not been set on the instance before, click **Add flag** , choose `cloudsql_mysql_audit` from the drop-down menu, and set its value to `ON`.
  5. Click **Save** to save your changes.
  6. Confirm your changes under **Flags** on the **Overview** page.



### gcloud

Replace the following: 

  * INSTANCE_NAME: The name of the instance you are setting the flag on.


    
    
    gcloud sql instances patch INSTANCE_NAME \
               --database-flags cloudsql_mysql_audit=ON

This command overwrites all database flags previously set. To keep those and add new ones, include the values for all flags you want set on the instance; any flag not specifically included is set to its default value. For flags that do not take a value, specify the flag name followed by an equals sign (`=`).

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "databaseFlags":
        [
          {
            "name": "cloudsql_mysql_audit",
            "value": "ON"
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "databaseFlags":
        [
          {
            "name": "cloudsql_mysql_audit",
            "value": "ON"
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1/projects/project-id/instances/instance-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### Cloud SQL for MySQL Audit Plugin settings

You can tune the behavior of the Cloud SQL for MySQL Audit Plugin using the flags below. All flags can be altered without restarting the database. To understand how to manage the flags, see [Configuring database flags](https://docs.cloud.google.com/sql/docs/mysql/flags).

  * **`cloudsql_mysql_audit_data_masking_regex`**

A regular expression used for data masking that is compliant with [Perl Compatible Regular Expressions](https://www.pcre.org/) (PCREs).

By default, in the output audit log, user passwords (`<psw>`) are substituted by a password mask of `***`.

Regex is applied only to statements with a command type specified using `cloudsql_mysql_audit_data_masking_cmds`. When using `gcloud` you must use a flag file to set values with complex special characters.

Default values for this flag:
        
        identified(?:/\*.*?\*/|\s)*?by(?:/\*.*?\*/|\s)*?(?:password)?(?:/\*.*?\*/|
        \s)*?['|"](?<psw>.*?)(?<!\\)['|"]|password(?:/\*.*?\*/|\s)*?\((?:/\*.*?\*/|
        \s)*?['|"](?<psw>.*?)(?<!\\)['|"](?:/\*.*?\*/|\s)*?\)|password(?:/\*.*?\*/|
        \s)*?(?:for(?:/\*.*?\*/|\s)*?\S+?)?(?:/\*.*?\*/|\s)*?=(?:/\*.*?\*/|\s)*?[
        '|"](?<psw>.*?)(?<!\\)['|"]|password(?:/\*.*?\*/|\s)*?['|"](?<psw>.*?)
        (?<!\\)['|"]
        
        

See the following examples.

    * Without the `cloudsql_mysql_audit_data_masking_regex`, an audit log entry describing a create user command would appear as follows:
          
          {..."cmd":"create_user","query":"create user user1@'localhost' identified
          by 'pw'"}

    * With the default value of `cloudsql_mysql_audit_data_masking_regex`, the same audit log would be changed to:
          
          {..."cmd":"create_user","query":"create user user1@'localhost' identified by
          '***'"}

    * If you set `cloudsql_mysql_audit_data_masking_regex` to `(?<psw>.*)`, Cloud SQL can filter all the query contents.
          
          {..."cmd":"create_user","query":"***"}

  * **`cloudsql_mysql_audit_data_masking_cmds`**

Comma-separated list of commands that the data masking regex (**cloudsql_mysql_audit_data_masking_regex**) is applied to. Set an empty string (`""`)to stop filtering. When using `gcloud`, you must use a flag file to set a comma-separated list. The default value includes MySQL commands with the following password clause:
        
        create_user,alter_user,grant,update

  * **`cloudsql_mysql_audit_max_query_length`**

Controls the maximum length of the query to record in the audit log. If you don't need to see the details of the query, you can use `0`, which means the query is not recorded in the audit log. This saves storage space for the log, resulting in lower cost. `-1` means no limitation. Default is `-1`.

  * **`cloudsql_mysql_audit_log_write_period`**

The log write period, for which the writer thread writes the contents of the buffer to disk after reaching the number of milliseconds you set for this flag option, or when the buffer is full. If you set this flag option to `0`, the user thread is forced to wait for a notification from the writer thread that the write has been completed. The default is `500` (milliseconds).




### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Open the instance and click **Edit**.
  3. Scroll down to the **Flags** section.
  4. To set a flag that has not been set on the instance before, click **Add flag** , and choose a database flag from the list above from the drop-down menu, and set its value.
  5. Click **Save** to save your changes.
  6. Confirm your changes under **Flags** on the **Overview** page. 



### gcloud

Replace the following: 

  * INSTANCE_NAME: The name of the instance you are setting the flag on.
  * FLAG_NAME: The name of the configuration flag.
  * FLAG_VALUE: The value to use for the flag.


    
    
            gcloud sql instances patch INSTANCE_NAME /
                       --database-flags FLAG_NAME=FLAG_VALUE
        

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "databaseFlags":
        [
          {
            "name": "flag_name",
            "value": "flag_value"
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "databaseFlags":
        [
          {
            "name": "flag_name",
            "value": "flag_value"
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

## Configure database auditing

### Manage audit rules

Cloud SQL uses a set of stored procedures to manage Cloud SQL for MySQL Audit Plugin audit rules. There are four stored procedures that you can use to create, list, update, and delete audit rules.

Each stored procedure returns two variables: `@outval` and `@outmsg`. These variables indicate the status code and the error message of the stored procedure, respectively. You can use an asterisk (`*`) as a wildcard to search for user, host, database, and table names. Use the asterisk as a suffix, a prefix, or both. In addition, you can use the wildcard character `%` only for hosts. You can use the backtick (```) to indicate that a string should be used literally. For example, ``ta*ble`` matches literally.

To make the new changes take effect, you should either run the stored procedures with the input parameter `reload_mode=1` or call `mysql.cloudsql_reload_audit_rule(1)` to make the new changes take effect.

**Note:** Audit rules are changeable, even when the `cloudsql_mysql_audit` plugin is disabled on the primary instance. However, database activity doesn't generate audit logs unless the Cloud SQL for MySQL Audit Plugin is enabled. 

### Create audit rules

You can use `mysql.cloudsql_create_audit_rule` to create a new audit rule.

To create the audit rule and reload it in one call, use the following statement:
    
    
    CALL mysql.cloudsql_create_audit_rule('user@host','db','obj','ops','op_result',1, @outval,@outmsg);
    SELECT @outval, @outmsg;
    

To create the rule and reload it in a separate call, use the following statement:
    
    
    CALL mysql.cloudsql_create_audit_rule('user@host','db','obj','ops','op_result',0, @outval,@outmsg);
    SELECT @outval, @outmsg;
    CALL mysql.cloudsql_reload_audit_rule(1);
    

The previous command lets you create multiple rules and then reload all changes at the same time.

The following tables show the input and output parameters for the previous command.

Input parameters |  |  |   
---|---|---|---  
**Name** | **Type** | **Description** | **Example**  
`user@host` or `user@ip` | string |  The comma-separated list of database users to audit. Use the format `user@host` or `user@ip`.  
  
**Note:** Currently the plugin only supports filters by the host name, not the IP address.  |  `user1@localhost`,  
`user1@*`,  
`user1@%`,  
`user@ip`  
`db` | string | The comma-separated list of databases to audit. | `db1,db2,db3*`  
`obj` | string | The comma-separated list of database objects to audit. | `table1,table2,table3*`  
`ops` | string | The comma-separated list of database actions to audit. | `select,delete,insert`  
`op_result` | string | Audit success (S), unsuccessful (U) or both (B) successful and unsuccessful operations. | `S`,`U`, or `B`  
`reload_mode` | Integer | `0` for not reload the rule and `1` for reload. | `0` or `1`  
Output parameters |  |  |   
---|---|---|---  
**Name** | **Type** | **Description** | **Example**  
`@outval` | int | The status code of the stored procedure. | `0` for success and `1` for failure.  
`@outmsg` | string | The error message of the stored procedure. |   
  
Audit rules have the following limitations:

Limitations |   
---|---  
Length of `user`, `db`, `obj`, and `ops`. | Maximum size is 2048 characters.  
Number of combinations of `user`, `db`, `obj` ,and `ops`. | Maximum of 1000 combinations. For example, an audit rule auditing `user1,user2`, `db1, db2`, `table1,table2`, and `select,delete` generates 2 x 2 x 2 x 2 = 16 combinations.  
  
### List audit rules

Auditors can use `mysql.cloudsql_list_audit_rule` to list existing audit rules.

To list audit rule 1 and 2, use the following commands:
    
    
    CALL mysql.cloudsql_list_audit_rule('1,2',@outval,@outmsg);
    SELECT @outval, @outmsg;
    

To list all audit rules, do the following:
    
    
    CALL mysql.cloudsql_list_audit_rule('*',@outval,@outmsg);
    SELECT @outval, @outmsg;
    

The following tables show the input and output parameters for the previous command.

Input parameters |  |  |   
---|---|---|---  
**Name** | **Type** | **Description** | **Example**  
`rule_id` | string | The comma-separated list of rule IDs to remove. | `1,2,3`  
Output parameters |  |  |   
---|---|---|---  
**Name** | **Type** | **Description** | **Example**  
`@outval` | int | The status code of the stored procedure. | `0` for success and `1` for failure.  
`@outmsg` | string | The error message of the stored procedure. |   
  
### Update audit rules

You can use `mysql.cloudsql_update_audit_rule` to update an existing audit rule.

To update the audit rule and reload it in one call, use the following statement:
    
    
    CALL mysql.cloudsql_update_audit_rule(1,'user@host','db','obj','ops','op_result',1,@outval,@outmsg);
    SELECT @outval, @outmsg;
    

You might want to update multiple audit rules in one session before reloading the rules. You can use the following stored procedure to update rules in one step and then reload those rules in a later step.
    
    
    CALL mysql.cloudsql_update_audit_rule(1,'user@host','db','obj','ops','op_result',0,@outval,@outmsg);
    SELECT @outval, @outmsg;
    CALL mysql.cloudsql_reload_audit_rule(1);
    

The following tables show the input and output parameters for the previous command.

Input parameters |  |  |   
---|---|---|---  
**Name** | **Type** | **Description** | **Example**  
`rule_id` | int | The ID for the rule to update. | `5`  
`user@host` | string |  The comma-separated list of database users to audit. Use the format user@host.  
  
**Note:** Currently the plugin only supports filters by the host name, not the IP address.  |  `user1@localhost,user1@*`  
`user1@%`  
`db` | string | The comma-separated list of databases to audit. | `db1,db2,db3*`  
`obj` | string | The comma-separated list of database objects to audit. | `table1,table2,table3*`  
`ops` | string | The comma-separated list of database actions to audit. | `SELECT,DELETE,INSERT`  
`op_result` | string | Audit success (S), unsuccessful (U), or both (B) successful and unsuccessful operations. | `S`,`U`, or `B`  
`reload_mode` | Integer | `0` for not reload the rule and `1` for reload. | `0` or `1`  
Output parameters |  |  |   
---|---|---|---  
**Name** | **Type** | **Description** | **Example**  
`@outval` | int | The status code of the stored procedure. | `0` for success and `1` for failure.  
`@outmsg` | string | The error message of the stored procedure. |   
  
Audit rules have the following limitations:

Limitations |   
---|---  
Length of `user`, `db`, `obj` and `ops`. | Maximum size 2048 characters.  
Number of combinations of `user`, `db`, `obj` and `ops`. | Maximum of 1000 combinations. For example, an audit rule auditing `user1,user2`, `db1, db2`, `table1,table2`, and `select,delete` generates 2 x 2 x 2 x 2 = 16 combinations.  
  
### Delete audit rules

You can use the `mysql.cloudsql_delete_audit_rule` to delete an existing audit rule.

To delete the audit rule and reload it in one call, use the following statement:
    
    
    CALL mysql.cloudsql_delete_audit_rule('1,2',1,@outval,@outmsg);
    SELECT @outval, @outmsg;
    

To delete the rule and reload it in a separate call, use the following statement:
    
    
    CALL mysql.cloudsql_delete_audit_rule('1,2',0,@outval,@outmsg);
    SELECT @outval, @outmsg;
    CALL cloudsql_reload_audit_rule(1);
    

The previous command lets you delete multiple rules and then reload all changes at the same time.

The following tables show the input and output parameters for the previous command.

Input parameters |  |  |   
---|---|---|---  
**Name** | **Type** | **Description** | **Example**  
`rule_id` | string | The comma-separated list of rule IDs to remove. | `1,2,3`  
`reload_mode` | Integer | `0` for not reload the rule and `1` for reload. | `0` or `1`  
Output parameters |  |  |   
---|---|---|---  
**Name** | **Type** | **Description** | **Example**  
`@outval` | int | The status code of the stored procedure. | `0` for success and `1` for failure.  
`@outmsg` | string | The error message of the stored procedure. |   
  
### Operation groups

The Cloud SQL for MySQL Audit Plugin supports using operation groups in rule definitions to audit collections of activities. You can use the following operation groups to simplify audit rule creation.

Operation groups | Operations included  
---|---  
`dql` | `select`  
`dml` | `delete`,`delete_multi`, `insert`, `insert_select`, `load`, `replace`, `replace_select`, `truncate`, `update`, `update_multi`,  
`ddl` |  `alter_db`, `alter_event`, `alter_function`, `alter_procedure`, `alter_table`, `alter_user`, `create_db`, `create_event`, `create_function`, `create_index`, `create_procedure`, `create_table`, `create_trigger`, `create_user`, `create_udf`, `create_view`, `drop_db`, `drop_event`, `drop_function`, `drop_index`, `drop_procedure`, `drop_table`, `drop_trigger`, `drop_user`, `drop_view`, `rename_table`, `rename_user`  
`dcl` | `grant`, `revoke`, `revoke_all`  
`show` |  `show_binlog_events`, `show_create_func`, `show_create_proc`, `show_procedure_code`, `show_create_event`, `show_create_trigger`, `show_events`, `show_function_code`, `show_grants`, `show_relaylog_events`, `show_triggers`,   
`call` | `call_procedure`  
  
## View Cloud SQL database audit logs

### View database audit log records in Cloud Logging

To view database audit logs, first make sure you've [enabled](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) Data Access audit logs for your project. The generated MySQL audit logs for a given instance are sent to Cloud Logging as [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access). You can view the generated MySQL database audit logs by using the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-summary) page.

In the Logs Explorer, you can view MySQL audit logs by using the following query to show all MySQL database audit logs for a given Cloud SQL project.

Replace the following:

  * PROJECT_ID: The ID of the project you want to find the audit logs for.


    
    
        resource.type="cloudsql_database"
        log_name="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fdata_access"
        protoPayload.request.@type="type.googleapis.com/google.cloud.sql.audit.v1.MysqlAuditEntry"

Alternatively, you can select the **cloudaudit.googleapis.com/data_access** log filter.

#### Audit Log Format

An audit log has the following fields.

Field name | Description  
---|---  
**`msgType`** | A string to represent the audit log message type.The only value for `msgType` is `activity`.  
**`status`** | Status of the operation, either `success` or `unsuccessful`.  
**`date`** | A timestamp indicating when the audit event was generated.  
**`threadId`** | The ID of the MySQL thread.  
**`queryId`** | The ID of the MySQL query.  
**`user`** | A string representing the username sent by the client. This might differ from the privUser value.  
**`privUser`** | A string representing the user that the server authenticated the client as. This is the username that the server uses for privilege checking. It might differ from the user value.  
**`gcpIamAccount`** | A string representing the IAM account or service account.  
**`ip`** | A string representing the client IP address.  
**`host`** | A string representing the client host name.  
**`errCode`** | The MySQL error code for a unsuccessful operation. See the [ MySQL Server Error Message Reference](https://dev.mysql.com/doc/mysql-errors/8.0/en/server-error-reference.html).  
**`cmd`** | A string that indicates the SQL statement (operation type) to use. For example, `INSERT`, `UPDATE`, or `DELETE`.  
**`objects`** |  The audit objects. Normally a table. This field includes the following information about the object:  
  
| `db` | A string representing the default database name.  
---|---  
`name` | A string representing the object name. Normally the table name.  
`objType` | A string representing the type of the object. Normally `TABLE`.  
**`query`** | An SQL statement (executed directly).  
**`chunkCount`** | Total number of chunks if the audit log query size is more than the `cloudsql_mysql_audit_event_split_threshold` (90k).  
**`chunkIndex`** | Index of the chunk. `chunk_index` starts at 1.  
**`@type`** | Type is always `type.googleapis.com/google.cloud.sql.audit.v1.MysqlAuditEntry`.  
  
The following is an example audit log entry.
    
    
    {
    "msgType":"activity",
    "status":"unsuccessful",
    "date":"2021-11-11T06:16:16.163603Z",
    "threadId":"750",
    "queryId":"26763",
    "user":"root",
    "priv_user":"root",
    "ip":"",
    "host":"localhost",
    "errCode":"1146",
    "cmd":"select",
    "objects":[{"db":"test","name":"t4","obj_type":"TABLE"}],
    "query":"select * from test.t4",
    "chunkCount":2,
    "chunkIndex":2,
    "@type":"type.googleapis.com/google.cloud.sql.audit.v1.MysqlAuditEntry"
    }
    

## Disable database auditing

To disable the Cloud SQL for MySQL Audit Plugin, you can set the database flag **cloudsql_mysql_audit** to OFF or remove the flag.

**Note:** This operation requires you to restart the instance. 

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Open the instance and click **Edit**.
  3. Scroll down to the **Flags** section.
  4. To set a flag that has not been set on the instance before, click **Add flag** , choose `cloudsql_mysql_audit` from the drop-down menu, and set its value to `OFF`.
  5. Click **Save** to save your changes.
  6. Confirm your changes under **Flags** on the **Overview** page.



### gcloud

Replace the following: 

  * INSTANCE_NAME: The name of the instance you are setting the flag on.


    
    
        gcloud sql instances patch INSTANCE_NAME \
                   --database-flags cloudsql_mysql_audit=OFF
        

**Note:** This operation requires you to restart the instance. 

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "databaseFlags":
        [
          {
            "name": "cloudsql_mysql_audit",
            "value": "OFF"
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "databaseFlags":
        [
          {
            "name": "cloudsql_mysql_audit",
            "value": "OFF"
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1/projects/project-id/instances/instance-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

## Examples of Audit Rules

  1. Audit all activities for all the users:
         
         CALL mysql.cloudsql_create_audit_rule('*','*','*','*','B',1,@outval,@outmsg);

  2. Audit all activities for a single user `user1`:
         
         CALL mysql.cloudsql_create_audit_rule('user1@*','*','*','*','B',1,@outval,@outmsg);

  3. Audit all activities for all users that start with `user`:
         
         CALL mysql.cloudsql_create_audit_rule('user*@*','*','*','*','B',1, @outval,@outmsg);

  4. Audit all DML operations for all the users:
         
         CALL mysql.cloudsql_create_audit_rule('*','*','*','dml','B',1,@outval,@outmsg);

  5. Audit select operation for a special database `db1`:
         
         CALL mysql.cloudsql_create_audit_rule('*','db1','*','select','B',1,@outval,@outmsg);

  6. Audit all activities for a database with special character `db~1`:
         
         CALL mysql.cloudsql_create_audit_rule('*','`db~1`','*','*','B',1,@outval,@outmsg);

  7. Audit select and delete operations for table `db1.table1`:
         
         CALL mysql.cloudsql_create_audit_rule('*','db1','table1','select,delete','B',1,@outval,@outmsg);

  8. Audit all successful operations:
         
         CALL mysql.cloudsql_create_audit_rule('*','*','*','*','S',1,@outval,@outmsg);

  9. Do not audit all activities for all users that start with `user`:
         
         CALL mysql.cloudsql_create_audit_rule('user*@*','*','*','*','E',1, @outval,@outmsg);




## Troubleshoot

Issue | Troubleshooting  
---|---  
I can't see `cloudsql_mysql_audit` when I invoke the command:   
  
`SHOW (global) variables` |  `cloudsql_mysql_audit` is the name of the plugin. To check if it is active, use the following command:   
  

    
    
    SHOW PLUGINS

  
And check the `status` entry.   
Why can't I see mysql audit logs after enabling `cloudsql_mysql_audit`? |  You must enable Data Access audit logs (as described in [Configure Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)). Also, audit rules are needed for the Cloud SQL for MySQL Audit Plugin to audit wanted audit logs. Use stored procedures with `reload_mode=1` to create audit rules, or run the following command or restart the database to make the newly added audit rules work:   
  

    
    
    CALL mysql.cloudsql_reload_audit_rule(1)

  
Additionally, ensure that you have the required IAM role to view the logs in the Logs Explorer, such as Private Logs Viewer (`roles/logging.privateLogViewer`) for Data Access audit logs in the `_Default` bucket. For more information, see [Required roles](https://docs.cloud.google.com/logging/docs/audit#roles).   
I see the following error when updating the database flag:   
  
Error 1193: Unknown system variable 'cloudsql_mysql_audit_xxx'  |  `cloudsql_mysql_audit_xxx` flags only work when the Audit Plugin is active. Remove any existing `cloudsql_mysql_audit_xxx` flags from the instance, and then turn on the plugin using the following command before updating `cloudsql_mysql_audit_xxx` flags:   
  

    
    
    cloudsql_mysql_audit=ON  
  
I can see audit logs generated even though I didn't set any audit rules. | Changes to the audit rule tables (`mysql.audit_log_rules` and `mysql.audit_log_rules_expanded`) and audit stored procedures (`mysql.cloudsql_xxxx_audit_rule`) are logged by default.  
After I made changes on the primary instance, I can't see the audit logs on my replica instances. | Replication threads and crash recovery threads aren't logged. Cloud SQL audits activities on the primary instance but not on the replica instance.  
I tried to use the following command to set values from a comma-separated list, but it doesn't work.   
  
`gcloud instances patch --database-flags` |  If specifying a comma-separated list of flag values using `gcloud` commands, use the `--flags-file` argument. First, you need to create a file with the following information:   
  

    
    
    --database-flags:
    general_log: OFF
    cloudsql_mysql_audit_max_query_length: '20'
    cloudsql_mysql_audit_data_masking_cmds: select,update
    

  
Then run the following command:   
  

    
    
    gcloud sql instances patch --flags-file=flagfile  
  
The following command returns an error:   
  
`CALL mysql.cloudsql_create_canonical_rules` | This is intended. `mysql.cloudsql_create_canonical_rules` should only be called internally by `mysql.cloudsql_create_audit_rule `and `mysql.cloudsql_update_audit_rule`.  
Which operations can I audit? |  The supported operations are listed in the [Full list of supported operations](https://docs.cloud.google.com/sql/docs/mysql/db-audit-operations). Some operations, such as the following, aren't audited since they're not affecting the database:   
  

    
    
    USE db_name

  
  
or   
  

    
    
    SHOW VARIABLES

  
  
Also, in some cases, the functions can't be audited as an object (non-supported features).   
I want to audit all operations on a specific table, so I created the following audit rule:   
  
`mysql.cloudsql_create_audit_rule("user@*","db", "table","*","B",1,@1,@2);`   
But I can see audit logs that aren't related to this table, such as `disconnect` and `connect`.  | Some operations, such as disconnect or connect, are considered global. They ignore the input `db` and `object` fields.  
When I create, update, or delete an audit rule using stored procedures, I see the following error.   
  
The MySQL server is running with the `read-only` option so it can't execute this statement.  |  Cloud SQL can't change stored procedures on a read-only instance. If the instance is primary, remove the `read_only` flags. If the instance is a replica instance, make the changes on its primary instance. After the changes of the rules are replicated to the replica instance, on the replica instance, run the following command to reload the rules into the replica: 
    
    
    CALL mysql.cloudsql_reload_audit_rule(1)  
  
When I create, update, or delete an audit rule, I see the following error, even though the change was successful.   
  
`0 rows affected` |  The `0 rows affected` response is for the last statement executed in the stored procedure, not the tables. To see if the audit rule is changed, use the following command:   
  

    
    
    mysql.cloudsql_list_audit_rule  
  
I can't set `cloudsql_mysql_audit_data_masking_cmds` and `cloudsql_mysql_audit_data_masking_regexp` with `gcloud`. | `gcloud` requires using the `--flags-file` argument to set complex flag values (the flags that include special characters).  
I created a stored procedure using the `CREATE USER` statement, but the password isn't masked. |  By default, masking only works for `cmds` (operations), such as the following:   
  
`CREATE_USER`, `ALTER_USER`, `GRANT`, `UPDATE`.   
  
To filter the password while creating the stored procedure, add `create_procedure` to the `cloudsql_mysql_audit_data_masking_cmds`.   
I got a lock wait timeout exceeded error when trying to create, update, or delete audit rules. | Normally, this error is caused when two or more sessions try to modify the audit rules at the same time. If this happens frequently, increase the value of the `innodb_lock_wait_timeout` variable. It can be increased either globally (using the database flag) or just for the session, for example, using the following command: 
    
    
    SET innodb_lock_wait_timeout=120

.   
  
## What's next

  * Learn more about [MySQL database auditing](https://docs.cloud.google.com/sql/docs/mysql/db-audit).
  * See the [full list of operations for database auditing](https://docs.cloud.google.com/sql/docs/mysql/db-audit-operations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
