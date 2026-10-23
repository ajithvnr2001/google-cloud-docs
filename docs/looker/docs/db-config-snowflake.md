---
url: https://docs.cloud.google.com/looker/docs/db-config-snowflake/
title: Snowflake \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:31.080137+00:00
---

# Snowflake  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-snowflake/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Snowflake Stay organized with collections  Save and categorize content based on your preferences. 

**Warning:** Starting in November 2025, Snowflake will no longer allow single-factor authentication. To avoid future connection interruptions, choose the **Key Pair** (not available if the **Use Legacy Connections Page** [legacy feature](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule) is enabled) or the **OAuth** authentication option.

To connect Looker to Snowflake, follow these steps:

  1. Create a Looker user on Snowflake and provision access.
  2. Set up a database connection in Looker.



## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Creating a Looker user on Snowflake

We recommend the following commands for creating the Looker user. Make sure to run each line individually, or select the **All Queries** option in the Snowflake connection panel to ensure that all lines are run (by default, Snowflake runs only the lines that are selected):

![The Snowflake console with the All Queries checkbox selected.](https://docs.cloud.google.com/static/looker/docs/images/setup-snowflake-console-524.png)

We recommend adding the [`ON FUTURE`](https://docs.snowflake.net/manuals/sql-reference/sql/grant-privilege.html#future-grants-on-schema-objects) keyword to each `GRANT` statement so that newly created objects will have the same permissions without further action being required.
    
    
    -- change role to ACCOUNTADMIN
    use role ACCOUNTADMIN;
    
    -- create role for looker
    create role if not exists looker_role;
    grant role looker_role to role SYSADMIN;
        -- Note that we are not making the looker_role a SYSADMIN,
        -- but rather granting users with the SYSADMIN role to modify the looker_role
    
    -- create a user for looker
    create user if not exists looker_user
    password = <enter password here>;
    grant role looker_role to user looker_user;
    alter user looker_user
    set default_role = looker_role
    default_warehouse = looker_wh;
    
    -- change role
    use role SYSADMIN;
    
    -- create a warehouse for looker (optional)
    create warehouse if not exists looker_wh
    
    -- set the size based on your dataset
    warehouse_size = medium
    warehouse_type = standard
    auto_suspend = 1800
    auto_resume = true
    initially_suspended = true;
    grant all privileges
    on warehouse looker_wh
    to role looker_role;
    
    -- grant read only database access (repeat for all database/schemas)
    grant usage on database <database> to role looker_role;
    grant usage on schema <database>.<schema> to role looker_role;
    
    -- rerun the following any time a table is added to the schema
    grant select on all tables in schema <database>.<schema> to role looker_role;
    -- or
    grant select on future tables in schema <database>.<schema> to role looker_role;
    
    -- create schema for looker to write back to
    use database <database>;
    create schema if not exists looker_scratch;
    use role ACCOUNTADMIN;
    grant ownership on schema looker_scratch to role SYSADMIN revoke current grants;
    grant all on schema looker_scratch to role looker_role;
    

If you want to enable [self-service Explores](https://docs.cloud.google.com/looker/docs/exploring-self-service) on your connection, you must also grant `CREATE STAGE` to the Looker role:
    
    
    GRANT CREATE STAGE ON SCHEMA looker_scratch TO ROLE looker_role;
    

## Creating the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information. The following setting descriptions contain notes that are specific to Snowflake:

  * **Database Settings - Host** : Enter the Snowflake hostname. It will look like `<account_name>.snowflakecomputing.com`. Check [Snowflake account name examples by region](https://docs.snowflake.com/en/user-guide/jdbc-configure.html#connection-parameters) to make sure you use the right value for your deployment.

  * **Database Settings - Authentication Method** : Select one of the following authentication methods:

    * **Database Account** should be used only by existing customers who need time to transition to a multi-factor authentication method before [Snowflake's November 2025 deadline](https://www.snowflake.com/en/blog/blocking-single-factor-password-authentification/). Specify the **Username** and **Password** of the Snowflake user account that will be used to connect to Looker.

    * **Key Pair** should be used by customers who want to implement [Snowflake's key-pair authentication](https://docs.snowflake.com/en/user-guide/key-pair-auth) to connect with their database. Specify the user account that will be used to connect to Snowflake in the **Username** field. Upload an encrypted or unencrypted p8 formatted key file in the **Key Pair File** field. Snowflake's documentation [describes how to create a private key file](https://docs.snowflake.com/en/user-guide/key-pair-auth#generate-the-private-key). If you are uploading an encrypted p8 file, do the following:

      * Enable the **Key Pair is Encrypted** toggle.
      * Specify the password for the p8 file in the **Key Pair File Decryption Password** field.
    * **OAuth** should be used by customers who don't need [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables) and want to configure OAuth for the connection.

  * **Optional Settings - Additional JDBC parameters** : Add additional JDBC parameters from the [Snowflake JDBC driver](https://docs.snowflake.com/en/user-guide/jdbc-configure.html). See the Supported JDBC parameters section on this page for a list of supported parameters.

    * Add `warehouse=<YOUR WAREHOUSE NAME>`.
    * Additionally, by default, Looker will set the following [Snowflake parameters](https://docs.snowflake.com/en/sql-reference/parameters.html) on each session:

      * `TIMESTAMP_TYPE_MAPPING=TIMESTAMP_LTZ`
      * `JDBC_TREAT_DECIMAL_AS_INT=FALSE`
      * `TIMESTAMP_INPUT_FORMAT=AUTO`
      * `AUTOCOMMIT=TRUE`

You can override each of these parameters by setting an alternative value in the **Additional JDBC parameters** field, for example: `&AUTOCOMMIT=FALSE`

  * **Optional Settings - Enable PDTs** : PDTs are not supported for Snowflake connections that use OAuth authentication. If PDTs are needed, use the **Key Pair** authentication option instead.

  * **Optional Settings - Enable PDT Overrides** : [PDT overrides](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#enable_pdt_overrides) are supported for Snowflake connections so that you can enter separate JDBC parameters that are specific to PDT processes, such as host, port, database, username, password, schema, additional parameters, and values for the **PDT Override After Connect Statements** field. You can use key-pair authentication in the PDT overrides by doing the following:

    * Upload an encrypted or unencrypted p8 formatted key file in the **PDT Override Key Pair file** field. Snowflake's documentation [describes how to create a private key file](https://docs.snowflake.com/en/user-guide/key-pair-auth#generate-the-private-key). 
    * If you are uploading an encrypted p8 file, specify the password for the p8 file in the **PDT Override Password** field.



To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

If Looker displays **Can Connect** , press **Connect** to create the connection. 

Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Designating Snowflake warehouses on a per-group or per-user basis

You can use Looker [user attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) to assign separate Snowflake [warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses.html) to individual Looker users or groups. This is useful, for example, if you have users who require different levels of computing power. You can assign a warehouse with greater computing resources to just those users who need it, while assigning a warehouse with lesser resources to users with lesser needs.

To designate warehouses on a per-group or per-user basis, follow these steps:

  1. Add the [groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups) or [users](https://docs.cloud.google.com/looker/docs/admin-panel-users-users) in Looker.
  2. Define a [user attribute](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) in Looker where the Snowflake warehouse names will be stored. You can give this attribute any name, such as `snowflake_wh`.

![The User Attributes page in Looker, showing the Snowflake warehouse user attribute.](https://docs.cloud.google.com/static/looker/docs/images/setup-snowflake-user-attribute-2504.png)

  3. In the user attribute that you just defined, assign the warehouse name values to the [groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes#assigning_values_to_user_groups) or [users](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes#assigning_values_to_individual_users) that will need different warehouse access.

![The User Attributes page in Looker, showing the Snowflake warehouse user attribute with values assigned to a group.](https://docs.cloud.google.com/static/looker/docs/images/setup-snowflake-group-values-2504.png)

  4. In the **Additional JDBC parameters** field on the **Connection Settings** page, add the following, replacing `snowflake_warehouse` with the name of the user attribute that you defined:
         
         warehouse={{ _user_attributes['snowflake_warehouse'] }}
         

  5. To test the individual connection settings, you can [sudo](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#impersonating_\(sudoing\)_users) as a user to whom you assigned a warehouse name value.




## Managing Snowflake's autosuspend feature

Snowflake warehouses have an autosuspend feature that is enabled by default. After a specified period, the warehouse will autosuspend. If the warehouse is suspended, all queries produce an error. This error is not visible on dashboards (normally these errors result in no data being shown), but it is visible to any user who queries with the Explore page.

Two methods are typically used to manage this:

  1. Snowflake has an auto-resume feature that will resume the warehouse when it is queried. However, resuming the warehouse can take up to five minutes, causing queries to stop responding for five minutes before being returned. Auto-resume cannot be configured in Looker. Enable this features on the **Warehouses** tab in the Snowflake UI:

![The Warehouses tab in the Snowflake UI, showing the autosuspend and auto-resume checkboxes.](https://docs.cloud.google.com/static/looker/docs/images/setup-snowflake-warehouses-tab-524.png)

  2. If persistent derived tables (PDTs) have been enabled, Looker's default setting is to check for derived table regeneration every 5 minutes. This check will keep Snowflake warehouses active. However, you may want Snowflake to suspend warehouses during non-work hours in order to reduce cost. This can be achieved by modifying the PDT regeneration schedule, as described in the [maintenance schedule documentation](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#pdt_and_datagroup_maintenance_schedule).




## PDT support

> PDTs are not supported for Snowflake connections that use OAuth.

For [persistent derived table](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables) support, create a Snowflake user account for PDTs that has write access to your database and the temp schema that Looker will use to create PDTs. On the Looker **Connections Settings** page, on the **Optional Settings** tab under the **Persistent Derived Table (PDT) Settings** section, turn on the **Enable PDTs** toggle. Then, in the **Temp database** field, enter the name of the temp schema that Looker will use to create PDTs.

For Snowflake connections, Looker sets the value for Snowflake's [`AUTOCOMMIT`](https://docs.snowflake.com/en/sql-reference/parameters.html#autocommit) parameter to `TRUE`, which is Snowflake's default value. `AUTOCOMMIT` is required for SQL commands that Looker runs to maintain its PDT registration system.

## Configuring OAuth for Snowflake connections

Looker supports OAuth for Snowflake connections, meaning that each Looker user authenticates to the database with their own OAuth user account.

OAuth lets database administrators perform the following tasks:

  * Audit which Looker users are running queries against the database
  * Enforce role-based access controls using database-level permissions
  * Use OAuth tokens for all processes and actions that access the database, instead of embedding database IDs and passwords in multiple places
  * Revoke authorization for a given user through the database directly



With Snowflake connections that use OAuth, users must sign in again periodically when their OAuth tokens expire. The maximum age of Snowflake OAuth tokens is set through Snowflake itself.

Note the following for database-level OAuth connections:

  * [Persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table) are not supported for Snowflake connections with OAuth.
  * If a user lets their OAuth token expire, any Looker schedules or alerts that they own will be affected. To guard against this, Looker will send a notification email to the owner of each schedule and each alert 14 days, 7 days, and 1 day before the token expires. The user can go to their Looker user page to reauthorize Looker to the database and avoid any interruption to their schedules and alerts. See the [Personalizing user account settings](https://docs.cloud.google.com/looker/docs/user-account#configuring_oauth_connection_credentials) documentation page for details.
  * Because database connections that use OAuth are "per user," caching policies are also per user and not just per query. This means that Looker will use cached results only if the _same user has run the same query_ within the caching period. For further information on caching, see the [Caching queries](https://docs.cloud.google.com/looker/docs/caching-and-datagroups) documentation page.
  * When using OAuth, you cannot switch to different roles in the Snowflake user account. As described in the [Snowflake documentation](https://docs.snowflake.com/en/user-guide/oauth-custom.html#scope), Snowflake uses the default role of the Snowflake user's account, unless the default role is ACCOUNTADMIN or SECURITYADMIN. Because these roles are blocked for OAuth, Snowflake will instead use the PUBLIC role. See the [Snowflake documentation](https://docs.snowflake.com/en/user-guide/oauth-partner.html#blocking-specific-roles-from-using-the-integration) for information.
  * When a Looker administrator sudos as another user, the administrator uses that user's OAuth access token. When users authorize an OAuth connection in Looker, an **Authorize OAuth Connection** dialog notifies them that privileged Looker users, such as administrators or developers, might have visibility into their data. If the user's access token is expired, the administrator can't create a new token on behalf of the sudoed user. See the [Users](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#impersonating_users) documentation page for information about using the `sudo` command.



### Configuring a Snowflake database for OAuth with Looker

To create a Snowflake connection to Looker using OAuth, you must set up the OAuth integration in Snowflake. This requires a Snowflake user account with ACCOUNTADMIN permission.

  1. Run the following command in Snowflake, where `<looker_hostname>` is the hostname of your Looker instance:
         
         CREATE SECURITY INTEGRATION LOOKER
           TYPE = OAUTH
           ENABLED = TRUE
           OAUTH_CLIENT = LOOKER
           OAUTH_REDIRECT_URI = 'https://<looker_hostname>/external_oauth/redirect';
         

  2. Get the OAuth client ID and secret by running the following command:
         
         SELECT SYSTEM$SHOW_OAUTH_CLIENT_SECRETS('LOOKER');
         

The response will have an `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET` that you will need later in this procedure.

  3. In Looker, create a new connection to your Snowflake warehouse, as described in the Creating the Looker connection to your database section of this page. When you create the new connection, select the **OAuth** option in the **Authentication** field. When you select the **OAuth** option, Looker displays the **OAuth Client ID** and **OAuth Client Secret** fields.

  4. Paste in the `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET` values that you got from your database earlier in this procedure.

  5. Complete the rest of the procedure for [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#creating_a_new_database_connection).




### Testing the OAuth connection

Once you configure the Looker connection to your database, you can test the connection itself by doing either of the following:

  * Select the **Test** button at the bottom of the **Connections Settings** page, as described on the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#testing_your_connection_settings) documentation page.
  * Select the **Test** button by the connection's listing on the **Connections** admin page, as described on the [Connections](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections#testing_connections) documentation page.



Additionally, you can test the connection and deploy it on a model by following these steps:

  1. In Looker, go into [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode).
  2. [Navigate to the project files](https://docs.cloud.google.com/looker/docs/accessing-project-files) for a Looker project that uses your Snowflake connection.
  3. Open a [model file](https://docs.cloud.google.com/looker/docs/model-and-view-files#model_files) and replace the model's [`connection`](https://docs.cloud.google.com/looker/docs/reference/param-model-connection) value with the name of the new Snowflake connection, and then save the model file.
  4. Open one of the model's Explores or dashboards, and run a query. When you try to run a query, Looker will prompt you to [sign in to Snowflake](https://docs.cloud.google.com/looker/docs/db-config-snowflake#signing_into_snowflake_to_run_queries).
  5. Follow the sign in prompts for Snowflake and enter your Snowflake credentials.



Once you successfully sign in to Snowflake, Looker will return you back to your query. If your query runs correctly, you can [commit the new connection value](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#committing_changes) and [deploy your changes to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#deploying_to_production).

### Signing in to Snowflake to run queries

Once the Snowflake connection is set up for OAuth, users will be prompted to sign in to Snowflake before running queries. This includes queries from Explores, dashboards, Looks, and SQL Runner.

![The Looker UI, showing the OAuth login prompt.](https://docs.cloud.google.com/static/looker/docs/images/admin-oauth-login-624.png)

Users can also sign in to Snowflake from the **OAuth Connection Credentials** section on their **Account** page.

To sign in to your Snowflake account using Looker, follow these steps:

![The Account page in Looker, showing the OAuth Connection Credentials section.](https://docs.cloud.google.com/static/looker/docs/images/admin-oauth-credentials-2304.png)

  1. Click the Looker user menu.
  2. Select **Account**.
  3. In the **Account** page, go to the **OAuth Connection Credentials** section, and select the **Log In** button for the appropriate Snowflake database.



Selecting **Log In** displays an **Authorize OAuth Connection** dialog in Looker notifying you that authorizing the connection lets the Looker instance access data on your behalf, and that privileged Looker users, such as administrators or developers, might have visibility into your data. Select **Authorize** to continue to the Snowflake login dialog. (Looker stores this consent in your browser's local storage; if you clear local storage, the dialog appears again when you next start an OAuth authorization flow.) Enter your Snowflake credentials and select **Log In** , and then select **Allow** to give Looker access to your Snowflake account.

Once you sign in to Snowflake through Looker, you can sign out or reauthorize your credentials at any time through your **Account** page, as described on the [Personalizing your user account](https://docs.cloud.google.com/looker/docs/user-account#oauth) documentation page.

## Context comments for Snowflake connections

For most database dialects, Looker adds [SQL context comments](https://docs.cloud.google.com/looker/docs/admin-panel-server-usage#sql_comments) to the beginning of each outgoing SQL query. For Snowflake connections, Looker appends context comments to the end of each SQL query rather than the beginning because Snowflake removes leading comments.

For more information about context comments and the fields that they include, see [Context comments for SQL queries](https://docs.cloud.google.com/looker/docs/admin-panel-server-usage#sql_comments).

## Supported JDBC parameters

For Snowflake, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `account`
  * `allowUnderscoresInHost`
  * `application`
  * `authenticator`
  * `AUTOCOMMIT`
  * `CLEAR_BATCH_ONLY_AFTER_SUCCESSFUL_EXECUTION`
  * `CLIENT_SESSION_KEEP_ALIVE`
  * `db`
  * `disableGcsDefaultCredentials`
  * `disableOCSPChecks`
  * `disableSamlURLCheck`
  * `disableSocksProxy`
  * `ENABLE_WILDCARDS_IN_SHOW_METADATA_COMMANDS`
  * `enablePatternSearch`
  * `HTTP_CLIENT_CONNECTION_TIMEOUT`
  * `HTTP_CLIENT_SOCKET_TIMEOUT`
  * `IMPLICIT_SERVER_SIDE_QUERY_TIMEOUT`
  * `insecureMode`
  * `JDBC_DEFAULT_FORMAT_DATE_WITH_TIMEZONE`
  * `JDBC_GET_DATE_USE_NULL_TIMEZONE`
  * `jdbc_use_session_timezone`
  * `JDBC_TREAT_DECIMAL_AS_INT`
  * `loginTimeout`
  * `MAX_TLS_VERSION`
  * `maxHttpRetries`
  * `MIN_TLS_VERSION`
  * `MULTI_STATEMENT_COUNT`
  * `networkTimeout`
  * `nonProxyHosts`: For public Looker instances, the value for the `nonProxyHosts` parameter must be the public IP address of the instance.
  * `oauthAuthorizationUrl`: For public Looker instances, the value for the `oauthAuthorizationUrl` parameter must be the public IP address of the instance.
  * `oauthClientId`
  * `oauthClientSecret`
  * `oauthScope`
  * `oauthTokenRequestUrl`: For public Looker instances, the value for the `oauthTokenRequestUrl` parameter must be the public IP address of the instance.
  * `ocspFailOpen`
  * `OWNER_ONLY_STAGE_FILE_PERMISSIONS_ENABLED`
  * `passcode`
  * `passcodeInPassword`
  * `password`
  * `private_key`
  * `private_key_base64`
  * `private_key_pwd`
  * `privatekey`
  * `proxyHost`: For public Looker instances, the value for the `proxyHost` parameter must be the public IP address of the instance.
  * `proxyPassword`
  * `proxyPort`
  * `proxyProtocol`
  * `proxyUser`
  * `QUERY_TAG`
  * `queryTimeout`
  * `QUOTED_IDENTIFIERS_IGNORE_CASE`
  * `ROLE`
  * `schema`
  * `STATEMENT_QUEUED_TIMEOUT_IN_SECONDS`
  * `STATEMENT_TIMEOUT_IN_SECONDS`
  * `stringsQuotedForColumnDef`
  * `TIMESTAMP_INPUT_FORMAT`
  * `TIMESTAMP_TYPE_MAPPING`
  * `TIMEZONE`
  * `token`
  * `tracing`
  * `useProxy`
  * `user`
  * `warehouse`
  * `WEEK_OF_YEAR_POLICY`
  * `WEEK_START`
  * `workloadIdentityProvider`



## Feature support

For Looker to support some features, your database dialect must also support them.

Snowflake supports the following features as of Looker 26.20:

Feature | Supported?  
---|---  
Looker (Google Cloud core)|   
Symmetric aggregates|   
Derived tables|   
Persistent SQL derived tables|   
Persistent native derived tables|   
Stable views|   
Query killing|   
SQL-based pivots|   
Time zones|   
SSL|   
Subtotals|   
JDBC additional params|   
Case-sensitive|   
Location type|   
List type|   
Percentile|   
Distinct percentile|   
SQL Runner Show Processes|   
SQL Runner Describe Table|   
SQL Runner Show Indexes|   
SQL Runner Select 10|   
SQL Runner Count|   
SQL Explain|   
OAuth 2.0 credentials|   
Context comments|   
Connection pooling|   
HLL sketches|   
Aggregate awareness|   
Incremental PDTs|   
Milliseconds|   
Microseconds|   
Materialized views|   
Period-over-period measures|   
Approximate count distinct|   
In-database analytic models|   
Custom calendars|   
  
## Next steps

After you have connected your database to Looker, [configure sign-in options for your users](https://docs.cloud.google.com/looker/docs/getting-started-with-users).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
