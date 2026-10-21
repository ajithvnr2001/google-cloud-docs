---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/work-with-conversion-workspaces/
title: Conversion workspace actions \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:06.064091+00:00
---

# Conversion workspace actions  |  Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/work-with-conversion-workspaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview)



Send feedback 

#  Conversion workspace actions Stay organized with collections  Save and categorize content based on your preferences. 

Conversion workspaces let you fix conversion issues, modify your objects with the interactive editor, and apply converted schema to your destination database. This page provides an overview of all actions you can perform with conversion workspaces.

## Review conversion status

![Conversion workspace screen with the Conversion Overview tab where
           you can see the number of converted objects, conversion issues,
           and Gemini-assisted conversion enhancements.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/conversion_workspace_overview.png) **Figure 1.** Conversion workspace overview screen. (click to enlarge) ![Conversion workspace screen with the Conversion Overview tab where
           you can see the number of converted objects, conversion issues,
           and Gemini-assisted conversion enhancements.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/conversion_workspace_overview.png)

In the **Conversion overview** section, you can view all information regarding your schema conversion: the number and type of converted objects, their conversion status (including open or resolved issues), as well as the list of enhancements provided by [ Gemini-assisted auto-conversion](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/code-conversion-with-gemini#auto-conversion). 

You can also use the filters in each category to narrow the number of objects displayed in the tree view by their type, issue severity, outstanding or resolved issues. The **Conversion overview** is available only for  upgraded conversion workspaces. 

To view detailed information about the progress of your code and schema conversion, do the following: 

  1. In the Google Cloud console, go to **Conversion workspaces** and select your workspace. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. In the **Oracle** tab, use the schema tree view to do one of the following: 
     * Select  ![](https://docs.cloud.google.com/static/database-migration/docs/images/htm/conversion_tree_root_node.svg) **Oracle** to view the information for all the objects in all the converted schemas in your workspace. 
     * Select a specific schema or object to view conversion details for a subset of objects. 
  3. In the **Conversion overview** tab, explore the information in the **Converted object summary** section. Use the **Show objects** button to apply any filter to the tree view in the **Oracle** tab. 
  4. Use the **Conversion issues** tab to start working through the conversion issues. For more information, see  Fix conversion issues. 



## Remove objects from the source schema

Remove objects from the source schema to exclude them from conversion. You can later  add removed objects if needed.

  1. In the Google Cloud console, go to **Conversion workspaces** and select your workspace. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. In the **SQL Server** tab, next to the object you want to remove, select more_vert **More** > **Remove**. 
  3. In the **Remove object** confirmation dialog, click **Remove**.
  4. Refresh your converted schema. Click move_down **Convert source**. Database Migration Service now analyzes your changes and generates the updated PostgreSQL schema. 

You can inspect the converted schema in the **Cloud SQL for PostgreSQL draft** tab. 




## Add objects to the source schema

You can add objects previously removed from the source schema to add them to the conversion.

**Note:** This operation only includes objects that were included in the source snapshot. If your source database contains new objects that you want to add to the workspace,  pull the source snapshot again.

  1. In the Google Cloud console, go to **Conversion workspaces** and select your workspace. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. In the **SQL Server** tab, click add**Add objects**. 
  3. In the **Add objects** section, use the source list to select all entities you want add to the source schema. 

You can use the **Filter objects** button to reduce the number of displayed objects. See  Filter objects in the source schema view

  4. Click **Add objects**.
  5. Refresh your converted schema. Click move_down **Convert source**. Database Migration Service now analyzes your changes and generates the updated PostgreSQL schema. 

You can inspect the converted schema in the **Cloud SQL for PostgreSQL draft** tab. 




## Pull source schema and code snapshot

You can pull schema and code from your source database into the conversion workspace at any moment. Pulling the source gives you an opportunity to add new, or update existing objects in the conversion.

Pulling updated database schema and code doesn't reset any custom mappings that exist in the conversion workspace unless you explicitly choose to remove custom mappings.

Additionally, pulling the source doesn't override SQL changes on your code objects. You can reset these changes directly at the object level.

  1. In the Google Cloud console, go to **Conversion workspaces** and select your workspace. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. Click settings **Edit configuration** > **Pull source schema snapshot again**.
  3. In the dialog box: 
     1. Optional: Select the **Reset custom mapping** to remove existing custom mappings and DDL modifications. 
     2. Click **Pull schema snapshot**. 

Database Migration Service pulls the new snapshot from your source database.

  4. Refresh your converted schema. Click move_down **Convert source**. Database Migration Service now analyzes your changes and generates the updated PostgreSQL schema. 

You can inspect the converted schema in the **Cloud SQL for PostgreSQL draft** tab. 




## Use custom conversion mappings

You can customize the conversion logic with a _conversion mapping file_. The conversion mapping file is a text file contains precise instructions (referred to as _conversion directives_) for how your SQL Server objects should be converted into PostgreSQL objects.

### Write a custom mapping file

To write your custom mapping files:

  1. [ Review the list of supported conversion directives](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#conversion-directives-reference).

  2. Use the [ example configuration file](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#sample-mapping-file) as a point of reference.

  3. Write your custom conversion mappings in a text editor and upload it to the conversion workspace.




### Add custom mapping files

To add a custom conversion mapping file to your workspace, do the following:

  1. In the Google Cloud console, go to **Conversion workspaces** and select your workspace. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. On the conversion editor page, select settings **Edit configuration** > **Customize mapping with a configuration file**. 
  3. In the **Configuration file** box, click **Browse** and use the system file picker to select your configuration file. 
  4. Click add **Add file** > **Create mapping**. 



### Remove custom mapping files

To remove a custom conversion mapping file from your workspace, do the following:

  1. In the Google Cloud console, go to **Conversion workspaces** and select your workspace. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. On the conversion editor page, select settings **Edit configuration** > **Remove custom mapping**. 



## Review conversion results

After you perform the source conversion, you can review the conversion results and possible issues for every individual converted object in the workspace editor area. You can also use Google Cloud CLI to save all results and issues in bulk to a text file.

###  Console 

  1. In the Google Cloud console, go to **Conversion workspaces**.

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. Click the display name of the conversion workspace that you want to work with.

Conversion workspace editor opens.

  3. Select the **SQL Server** tab, and locate the object for which you want to review conversion results in the tree view table.

  4. Select the object. Use the **SQL** and **Conversion issues** tabs to review the conversion.

  5. If you determine that your issue is a warning and doesn't warrant any action, you can  mark it as resolved. Otherwise, you can investigate further and  fix it in the conversion editor.




###  gcloud 

With Google Cloud CLI you can print all conversion results or issues to the terminal. Redirect the output to a file for more convenient bulk object reviews.

#### Get a list of conversion results

gcloud CLI displays conversion results in the terminal in the form of _Data Definition Language_ (DDL) statements. To save conversion results to a file, execute the following command:
    
    
      gcloud database-migration conversion-workspaces describe-ddls \
      CONVERSION_WORKSPACE_ID \
      --region=REGION_ID \
      > OUTPUT_FILE_PATH
    

Replace:

  * `CONVERSION_WORKSPACE_ID` with the conversion workspace identifier. For information on how to retrieve conversion workspace identifiers, see [ View conversion workspace details](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/manage-conversion-workspace).
  * `REGION_ID` with the name of the region where the conversion workspace is located.
  * `OUTPUT_FILE_PATH` with the path where to the text file where you want to save the output.

Example:
        
        gcloud database-migration conversion-workspaces describe-ddls \
        my-conversion-workspace \
        --region=us-central1 \
        > ./my-ddls-list.txt
        

Result:

Your schema conversion results are saved in a text format where the first line says `DDLs` and subsequent lines are occupied by SQL statements:
        
        DDLs
        CREATE SCHEMA IF NOT EXISTS "SCHEMA1";
        ALTER TABLE "SCHEMA1"."EMPLOYEES" ADD CONSTRAINT PK_ID PRIMARY KEY ("ID");
        CREATE OR REPLACE FUNCTION mockschema.func_test_datatype(str1 VARCHAR(65000))
          RETURNS DECIMAL
          LANGUAGE plpgsql
          AS $$
            DECLARE
              str2 VARCHAR(100);
            BEGIN
              SELECT
                  employees.first_name
                INTO STRICT
                  STR2
                FROM
                  mockschema.employees
                WHERE employees.employee_id = CAST(FUNC_TEST_DATATYPE.str1 as DECIMAL)
              ;
              RAISE NOTICE '%', concat('Input : ', FUNC_TEST_DATATYPE.str1, ' Output : ', str2);
              RETURN 0;
            END;
          $$;
        CREATE OR REPLACE PROCEDURE greetings AS BEGIN dbms_output.put_line('Hello World!'); END;
        CREATE SYNONYM TABLE "SCHEMA1"."SYNONYM1" ON "SCHEMA1"."EMPLOYEES";
        CREATE OR REPLACE VIEW "SCHEMA1"."VIEW1" AS SELECT * FROM JOBS;
        




#### Get a list of conversion issues

To save conversion issues to a file, execute the following command:
    
    
      gcloud database-migration conversion-workspaces describe-issues \
      CONVERSION_WORKSPACE_ID \
      --region=REGION_ID \
      > OUTPUT_FILE_PATH
    

Replace: 

  * `CONVERSION_WORKSPACE_ID` with the conversion workspace identifier. For information on how to retrieve conversion workspace identifiers, see [ View conversion workspace details](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/manage-conversion-workspace). 
  * `REGION_ID` with the name of the region where the conversion workspace is located. 
  * `OUTPUT_FILE_PATH` with the path where to the text file where you want to save the output. 



Example:
    
    
      gcloud database-migration conversion-workspaces describe-issues \
      my-conversion-workspace \
      --region=us-central1 \
      > ./my-conversion-issues.txt
    

Result:

All the conversion issues contained in your workspace are saved in a text format where the first line contains column headers and each subsequent line contains a separate conversion issue:
    
    
      PARENT   NAME               ENTITY_TYPE       ISSUE_TYPE  ISSUE_SEVERITY  ISSUE_CODE  ISSUE_MESSAGE
      SCHEMA1  EMPLOYEES          TABLE             DDL         ERROR           500         unable to parse DDL.
      SCHEMA1  EMPLOYEES          TABLE             CONVERT     WARNING         206         no conversion done.
      SCHEMA1  STORED_PROCEDURE1  STORED_PROCEDURE  DDL         ERROR           500         invalid DDL.
      SCHEMA1  SYNONYM1           SYNONYM           CONVERT     WARNING         206         synonym warning message.
    

We also recommend that you run _Gemini quality assessment_ reports on your converted objects. These assessments analyze the converted code, providing feedback on its correctness and behavior compared to the source code. For more information, see [ Gemini quality assessments](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/code-conversion-with-gemini#quality-assessments).

## Fix conversion issues

Database Migration Service might not be able to automatically convert your entire source. For most SQL Server objects, you can use the conversion editor directly in Database Migration Service to adjust the generated SQL. For others, you might need to change the object directly in your source database and then pull the source snapshot again.

For a complete list of objects that Database Migration Service supports for editing directly in the conversion workspace, see [ Editable SQL Server objects](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#editable-objects).

To fix the conversion issues found in your schema, do the following:

  1. In the Google Cloud console, go to **Conversion workspaces** and select your workspace. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. Review the conversion results and identify possible issues. 

You can use the Google Cloud console for reviewing individual objects or gcloud CLI for reviewing all objects in bulk. 

  3. Depending on the type of your issue, you can fix it directly in the workspace editor, or you might need to provide a customized conversion mapping file. Expand the following sections for more information. 

Regardless of what type of issue you're working with, you can try the the Gemini-powered conversion assistant to find a solution. For more information, see [ Use Gemini conversion assistant](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/code-conversion-with-gemini#conversion-assistant). If you determine that your issue is a warning and doesn't warrant any action, you can  mark it as resolved. 

#### Fix issues with objects supported by the built-in editor

To fix issues encountered with objects that are supported in the workspace editor, do the following: 

     1. Find your issue in the **SQL Server** tree view, and then select the **Code** tab. 
     2. Use the SQL editor to update the generated code.Database Migration Service doesn't validate the correctness of SQL code you add in the editor. 

#### Fix issues with objects that aren't supported by the built-in editor

To fix issues encountered with objects that aren't supported in the workspace editor, perform one of the following: 

Update faulty objects in your source
    For some issues, you might need to change the SQL Server statement directly in your source database. Do the following: 
     1. Update the schema and code directly in your source database.
     2. Pull the updated sources to Database Migration Service.
     3. [ Convert the sources again](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/convert-sql) and check if the issues persist. 
Provide additional mappings with a conversion mapping file
    

You can use a conversion mapping file to provide precise definitions for how Database Migration Service should convert certain PostgreSQL objects. To use a conversion mapping file, do the following: 

     1. Write a conversion mapping file. 
     2. Add your configuration file to the workspace. 
     3. [ Convert the sources again](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/convert-sql) and check if the issues persist. 
Try removing the object from the sources tab
    Database Migration Service lets you convert . To unblock the conversion process, you can decide to look closer at the faulty object at a later time.  Remove the object from the sources tab. 

  4. Test your schema to verify Database Migration Service can correctly apply your code to the destination database. 
  5. If the tests are successful, we recommend that you use the **Conversion issues** tab to mark your issues as **Resolved**. This way you can filter out these issues from the conversion overviews and pick up later where you left off. 




## Mark issues as resolved

As you review and fix conversion issues, you might want to keep track of which issues you already fixed (or determined that they won't impact your migration and don't warrant any action). You can use the **Mark as resolved** feature to filter out such issues to make the issue list easier to navigate.

To mark an issue as resolved, do the following:

  1. In the Google Cloud console, go to **Conversion workspaces** and select your workspace. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. Use the **Source tree** view to select the object that has conversion issues. 
  3. In the **Conversion issues** tab, next to your issue, click **Mark as resolved**. Now you can filter out these issues from conversion overview. 

![Issue resolution screen where you can mark conversion issues
            as resolved to filter them out in the conversion overview screen.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/conversion_issues_mark_resolved.png) **Figure 2.** Conversion issues screen where you can mark issues as resolved. (click to enlarge) ![Issue resolution screen where you can mark conversion issues
            as resolved to filter them out in the conversion overview screen.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/conversion_issues_mark_resolved.png)



## Test your schema in the destination

Before you apply the schema to the destination database, you can first perform a test run to proactively check for possible issues. To perform the test, Database Migration Service creates a temporary database. The test run doesn't impact your destination Cloud SQL instance.

  1. Make sure your dedicated migration user has the `CREATEDB` permission. For more information, see [ Create and configure your destination Cloud SQL instance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-destination-database).

  2. In the Google Cloud console, go to **Conversion workspaces**.

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  3. Click the display name of the conversion workspace that you want to work with.

Conversion workspace editor opens.

  4. Click **Apply to destination** > **Test (recommended)**.

The wizard for applying schema to destination database appears.

  5. In the **Define destination** section, select the connection profile that points to your destination database.

  6. Click **Define and continue**.

  7. In the **Select objects and test application** section, select the schemas of database entities you want to test for your destination database.

You can use the **Filter objects** button to reduce the number of displayed objects. See  Filter objects in the source schema view.

  8. Click **Test application**.

You can review the application status in the **Cloud SQL for PostgreSQL** tab.




## Apply schema to destination

When the schema you would like to use in the destination database is converted according to your requirements and mappings, you can apply the results to the destination database. Applying schema in the destination doesn't alter any data on the source database.

**Caution:** Applying your schema to the destination instance impacts your Cloud SQL for PostgreSQL instance. Database Migration Service first cleans the destination database by running the SQL `DROP` command, and then re-creates the objects.

  1. In the Google Cloud console, go to **Conversion workspaces**.

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. Click the display name of the conversion workspace that you want to work with.

Conversion workspace editor opens.

  3. Click **Apply to destination** > **Apply**.

The wizard for applying schema to destination database appears.

  4. In the **Define destination** section, select the connection profile that points to your destination database.

  5. Click **Define and continue**.

  6. In the **Review objects and apply conversion to destination** section, select the schemas of database entities you want to create in your destination database.

You can use the **Filter objects** button to reduce the number of displayed objects. See  Filter objects in the source schema view.

  7. Click **Apply to destination**.

You can review the application status in the **Cloud SQL for PostgreSQL** tab.




## Create a migration job from the conversion editor

You can create a migration job that uses your conversion workspace directly from the conversion editor interface.

  1. In the Google Cloud console, go to **Conversion workspaces**.

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. Click the display name of the conversion workspace that you want to work with.

Conversion workspace editor opens.

  3. Click **Create migration job**.

  4. Proceed with the standard migration job steps, as outlined in [ Create a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-migration-job).




## Filter objects in the source schema view

Database schemas often contain thousands of objects, making it challenging to partition conversion work. When you add objects from the schema snapshot to the source schema view, you can use filters to limit the number of displayed objects. Filters let you add objects in a more granular fashion and focus on converting a select subset of your schema.

Use the filtered view when you add objects to the source schema view:

  1. In the **Filter** field, use one of the following filtering methods: 
  2. From the **Properties** list, select one of the following auto-suggested options: 
     1. **Object name** to filter the objects by name, for example, `ADMIN`. 
     2. **Object type** to filter the objects by several types, such as **Function** or **Table**. 
     3. **Conversion status** to filter the objects by the conversion status, such as **Action required** or **No issues**. 
     4. **Augmented by Gemini** to filter objects that were converted with [ Gemini auto-conversion](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/code-conversion-with-gemini#auto-conversion). 

You can combine filter properties with logical operators.

  3. Enter your query. For example: `type=table`. 

For more information on the filtering syntax, see  Supported filtering syntax. 

  4. Select the objects that you want to add to the source schema view. **Important:** Object selections don't persist through filter changes. If you want to add objects that meet different criteria, use a more complex query or add them in separate attempts. 



### Supported text filtering syntax

You can filter objects by name with basic free text search, or use a dedicated `type` property. Both approaches support the [ Google API formal specification for filtering](https://google.aip.dev/160), meaning you can use literals with wildcards, as well as logical and comparison operators.

Free text filtering
    

Use free text to filter the objects by name. This approach is case-sensitive and supports wildcards.

**Example** :

The `*JOB*` query uses wildcards to search for entities that contain the `JOB` substring. The filtered view returns some tables and one stored procedure:

![Screenshot of example results for filtering objects by name.](https://docs.cloud.google.com/static/database-migration/docs/images/filter_name_example.png)
Filter by using the `type` property
    

You can filter objects by all standard types supported in Database Migration Service.

The `type` property supports the following literals with the equality (`=`) and inequality (`!=`) operators: `database`, `schema`, `table`, `column`, `index`, `sequence`, `stored_procedure`, `function`, `view`, `synonym`, `materialized_view`, `udt`, `constraint`, `database_package`, `trigger`, and `event_trigger`. 

**Example** :

The `type=table` filter returns only tables present in your trait: schema:

![Screenshot of example results for filtering objects by type property.](https://docs.cloud.google.com/static/database-migration/docs/images/filter_type_example.png)

### Combine text filtering conditions

You can specify multiple conditions by combining them with logical operators.

For example, to search exclusively for tables whose names contain the `JOB` or `EMPLOYEE` substrings, use this query:
    
    
      type=table AND (*JOB* OR *EMPLOYEE*)
    

As a result, the filter displays all matching tables:

![Screenshot of example results for filtering objects by a combination of
  type and name properties.](https://docs.cloud.google.com/static/database-migration/docs/images/filter_combined_query_example.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
