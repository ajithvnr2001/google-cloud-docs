---
url: https://docs.cloud.google.com/knowledge-catalog/docs/reuse-data-quality-rules/
title: Reuse data quality rules \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:37:37.391953+00:00
---

# Reuse data quality rules  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/reuse-data-quality-rules/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Reuse data quality rules Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to reuse Knowledge Catalog (formerly Dataplex Universal Catalog) data quality rules to define and manage standardized business rules.

Rule reusability lets you share complex or standardized business rule definitions across multiple data quality rules and scans by using rule templates. This document also describes how to set up, create, and manage reusable rule templates, and how to attach data quality rules to catalog entries as metadata aspects.

## Use cases

You can use data quality rule reusability for the following scenarios:

  * **Standardize and share rule definitions** : Use _custom rule templates_ to store complex or standardized business rule definitions. This reduces the time and effort required to distribute common definitions by using templatized SQL expressions. For example, a central data governance team can define a standard _valid email_ or _valid SSN_ template that is reused across the entire organization, ensuring consistency and reducing the operational overhead of managing duplicate rules.
  * **Implement governance-driven quality** : Declare _data rules as metadata_ by using Knowledge Catalog aspects on BigQuery table and business glossary term entries. This makes your rules searchable and reusable. For example, when you link a column to a glossary term, it can automatically inherit the validation rules defined for that term, enabling automated governance policies through semantic metadata inheritance.
  * **Search and discover reusable rules** : Find existing rules within your organization through semantic search. This allows data analysts and engineers to discover verified, standardized rule sets (such as "Baseline Financial Constants") and bootstrap data quality for new projects without writing SQL from scratch.
  * **Eliminate cold-start problems** : Leverage _system rule templates_ for frequently used evaluations, such as null checks or range expectations. These built-in templates let you quickly set up data quality monitoring for common scenarios without needing to write custom SQL.
  * **Enable separation of concerns** : Allow central governance teams to author verified rule templates, while engineering teams focus on applying these rules to their data assets without having to write or maintain complex SQL. This clear division of responsibilities improves organizational agility and ensures that data quality standards are consistently applied across the enterprise.



## Before you begin

  1. Enable the Dataplex API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)




Before you use data quality rule reusability, ensure that you have completed the following requirements.

### Set up the Dataplex API environment

To use the REST API examples in this document, set up an alias for `gcurl` and configure the `${DATAPLEX_API}` environment variable.

  1. Set an alias of `gcurl`. This creates a shortcut that includes your authentication token and sets the JSON content-type for API requests:
         
         alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
         

  2. Set the `DATAPLEX_API` variable:
         
         DATAPLEX_API="dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION"

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `LOCATION`: the location where your scan or resources are located (for example, `us-central1`).



### Set up a service account

A service account is mandatory for running data quality scans with reusable rules. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) that has the following Identity and Access Management roles and permissions:

  * You must have the `iam.serviceAccounts.actAs` permission on the project hosting the service account (typically by using the `roles/iam.serviceAccountUser` role).
  * Grant the Dataplex Service Agent (`service-PROJECT_ID@gcp-sa-dataplex.iam.gserviceaccount.com`) for the scan project the `iam.serviceAccounts.getAccessToken` permission on the service account (for example, by using the `roles/iam.serviceAccountTokenCreator` role).
  * The service account must have the following permissions: 
    * `bigquery.tables.getData` on the table to be scanned (for example, by using `roles/bigquery.dataViewer`).
    * `bigquery.jobs.insert` in the scan project (for example, by using `roles/bigquery.jobUser`).
    * `roles/bigquery.dataEditor` on the export dataset (if using export).



### Required roles and permissions

Ensure you have the following IAM roles for your specific tasks:

  * **Data scan management** : [Required data scan roles](https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality#permissions) to manage data scan resources.
  * **Rule template management** : To create or update rule templates, you must have the necessary permissions to manage entries within the rule template's entry group or project. Specifically, `roles/dataplex.catalogEditor` or `roles/dataplex.entryOwner` grants these permissions.
  * **Referencing rule templates from rules** : You must have `dataplex.entries.get` and `dataplex.entries.getData` permissions on the rule template's entry group or project being referenced by a rule.
  * **Attaching data quality rules to BigQuery tables** : To attach data quality rules as Knowledge Catalog metadata, you must have one of the following: 
    * `bigquery.tables.update` or `roles/bigquery.dataEditor` on the table and `dataplex.entryGroups.useDataRulesAspect` on the `@bigquery` entry group in the table location.
    * `roles/dataplex.catalogEditor` on the `@bigquery` entry group.
  * **Attaching data quality rules to business glossary terms** : To attach data quality rules as Knowledge Catalog metadata, you must have one of the following: 
    * `dataplex.glossaryTerms.update` on the term and `dataplex.entryGroups.useDataRulesAspect` on the `@dataplex` entry group.
    * `roles/dataplex.catalogEditor` on the `@dataplex` entry group.
  * **Creating data quality scans with entry-based rules** : You must have one of the following: 
    * `bigquery.tables.get` and `bigquery.tables.getData` on the table.
    * `dataplex.entries.get` and `dataplex.entries.getData` on the `@bigquery` entry group in the table location.



## SQL query syntax for rule templates

When you write the SQL logic for a rule template, you must provide a statement that returns invalid rows. If the query returns any rows, the rule fails. For more information, see [SqlAssertion](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualityRule#sqlassertion).

Follow these guidelines for writing rule template SQL:

  * Omit the trailing semicolon from the SQL statement.
  * Use `${param(name)}` to reference input parameters, for example, `${param(min_value)}`.
  * Use `$${...}` to escape a literal `${...}` and prevent it from being replaced as a parameter.
  * Parameter variables are case-sensitive.



### System-supported parameters

You can use the following system-supported parameters in your rule template SQL:

  * `${project()}`: The project ID of the resource being scanned.
  * `${dataset()}`: The BigQuery dataset ID of the resource being scanned, formatted as `PROJECT_ID.DATASET_ID`.
  * `${table()}`: The BigQuery table ID of the resource being scanned, formatted as `PROJECT_ID.DATASET_ID.TABLE_ID`.
  * `${column()}`: The column the rule is evaluated on. An error occurs during rule evaluation if the rule is attached to the table level but references `${column()}`.
  * `${data()}`: A reference to the data source table and all of its precondition filters like row filters, sampling percentages, and incremental filters defined in the scan specification. For more information, see [Data reference parameter](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#data-reference-parameter).



### Example 1: Validate column values are between two values

The following example validates that all values in a column are between a minimum and maximum value:
    
    
    SELECT *
    FROM ${data()}
    WHERE
      NOT ((${column()}>=${param(min_value)} AND ${column()}<=${param(max_value)}) IS TRUE)
    

Note the following:

  * Using `NOT(condition) IS TRUE` returns invalid rows, including rows with `NULL` values in the column.
  * Using `${data()}` limits the scope of rows evaluated to the source table and its filters, such as row filters, sampling percentages, and incremental filters.
  * Using `${column()}` lets you reference the column that the rule using this template is evaluated on.



### Example 2: Foreign key validation

The following example verifies that each value in a column exists in a primary key column of another table:
    
    
    SELECT t.*
    FROM ${data()} AS t
    LEFT JOIN `${param(reference_table)}` AS s
      ON t.${column()} = s.`${param(reference_column)}`
    WHERE s.`${param(reference_column)}` IS NULL
    

Input parameters for this template are as follows:

  * `reference_table`: The name of the reference table containing the primary keys. Use the format `PROJECT_ID.DATASET_ID.TABLE_ID`.

  * `reference_column`: The name of the primary key column in the reference table.




## System rule templates

Knowledge Catalog provides system rule templates that can be used in any region. Knowledge Catalog manages these templates in the `dataplex-templates` project under the `rule-library` entry group. An example of a full resource name is `projects/dataplex-templates/locations/global/entryGroups/rule-library/entries/non_null_expectation`.

To view the list of all the available system rule templates, see [System rule templates list](https://docs.cloud.google.com/knowledge-catalog/docs/system-rule-templates-list).

To find the available list of system rule templates, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. Click **Rule libraries** > **System**.

  3. To see the list of available system rule templates, click **rule-library**.




When creating a new rule, you can select the system rule templates in the **Choose rule types** menu.

### REST

To find the available list of system rule templates, use the `entries.list` method:
    
    
    gcurl "https://dataplex.googleapis.com/v1/projects/dataplex-templates/locations/global/entryGroups/rule-library/entries"

### Known differences between system rule templates and built-in rules

The following table describes the differences between system rule templates and [built-in rules](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#predefined-rules):

Feature | System rule templates | Built-in rules  
---|---|---  
**Source** | Reusable templates in the catalog | Built-in in the API  
**Referencing** | Can be referenced by catalog entries and scans | Can only be used in scans  
  
The following list describes additional differences in how metrics are calculated for system rule templates:

  * **Assertion Row Count metric** : This metric is populated for all template reference rules, not just SQL assertion rules.
  * **Statistic Range Expectation rule template** : As an aggregate rule, this template doesn't support the `ignore null` capability and doesn't report a `nullCount` metric. Instead, the rule passes if the calculated aggregate statistic falls within the specified range.
  * **Uniqueness Expectation rule template** : This template calculates `passedCount` differently than the built-in `UniquenessExpectation` rule. The rule template returns all rows for which duplicate values or null rows exist, which can result in fewer passing rows if duplicates are present.

For example, if a column contains the values `(a, a, b, b, c, d, e)`:

    * **Built-in uniqueness rule** : Returns 5 passing rows: `(a, b, c, d, e)`.
    * **Uniqueness rule template** : Returns 4 failing rows: `(a, a, b, b)`. The number of passing rows is 3 (7 total rows minus 4 failed rows): `(c, d, e)`.



## Manage data quality rule templates

This section describes how to create, edit, and delete rule templates.

### Create a rule library

To create a rule library, you must create a Knowledge Catalog entry group.

### Console

  1. In the Google Cloud console, go to the **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. Go to **Rule libraries** > **Custom** , and click **Create**.

  3. In the **Create rule library** window, fill in the following fields:

     1. Optional: Enter a display name.
     2. In **Rule library ID** , enter an ID. For more information, see the [resource naming conventions](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
     3. Optional: Enter a description.
     4. In the **Location** menu, select a location. It can't be changed later.
     5. Optional: Add labels. Labels are key-value pairs that let you group related objects together or with other Google Cloud resources.
     6. Click **Save**.



### REST

To create a rule library by using the API, you must create an entry group with the required label `goog-dataplex-entry-group-type: rule_library`:
    
    
    gcurl -X POST "https://${DATAPLEX_API}/entryGroups?entryGroup_id=RULE_LIBRARY_ID" \
    --data @- << EOF
    {
    "labels": {
      "goog-dataplex-entry-group-type": "rule_library"
    },
    "description": "DESCRIPTION"
    }
    EOF

Replace the following:

  * `RULE_LIBRARY_ID`: a unique ID for your rule library.
  * `DESCRIPTION`: an optional description for the rule library.



### Terraform

To create a rule library, use the [`google_dataplex_entry_group`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_entry_group) resource:
    
    
    resource "google_dataplex_entry_group" "rule_library" {
    project        = "PROJECT_ID"
    location       = "LOCATION"
    entry_group_id = "RULE_LIBRARY_ID"
    description    = "DESCRIPTION"
    
    labels = {
    "goog-dataplex-entry-group-type" = "rule_library"
    }
    }

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: the location for your rule library (for example, `us-central1`).
  * `RULE_LIBRARY_ID`: a unique ID for your rule library.
  * `DESCRIPTION`: an optional description for the rule library.



### Create a rule template

To create a custom rule template, select one of the following:

### Console

  1. In the Google Cloud console, go to the **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. Go to **Rule libraries** > **Custom**.

  3. Click the rule library where you want to add a template, and then click **Create**.

  4. In the **Create rule template** window, fill in the following fields:

     1. Optional: Enter a name for the template.
     2. In **Template ID** , enter an ID. For more information, see the [resource naming conventions](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
     3. Optional: Enter a description.
     4. In the **Dimension** menu, select a dimension. For more information, see [Dimensions](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#dimensions).
     5. In the **SQL query** field, enter the following example query that validates each column value is between two values:
            
            SELECT * FROM ${data()} WHERE NOT(${column()}>=${param(min_value)} AND ${column()}<=${param(max_value)}) IS TRUE
            

     6. Optional: To enable the rule referencing this template to specify a threshold for success criteria, select **Support threshold**.

     7. Optional: To allow rules referencing this template to ignore null values in the column for determining success criteria, select **Support ignore null**.

     8. In **Input Parameters** , click **Add input parameter** , and then for each parameter used in the SQL query, enter an input name, description, and default value. In the preceding example, the names would be `min_value` and `max_value`.

     9. Click **Save**.




### REST

To create a custom rule template, create an entry of type `data-quality-rule-template`:
    
    
    gcurl -X POST "https://${DATAPLEX_API}/entryGroups/ENTRY_GROUP_ID/entries?entry_id=TEMPLATE_ID" \
    --data @- << EOF
    {
    "entryType": "projects/dataplex-types/locations/global/entryTypes/data-quality-rule-template",
    "entrySource": {
      "displayName": "DISPLAY_NAME",
      "description": "DESCRIPTION"
    },
    "aspects": {
      "dataplex-types.global.data-quality-rule-template": {
         "data": {
           "dimension": "VALIDITY",
           "sqlCollection": [
             {
               "query": "SELECT t.* FROM ${data()} AS t LEFT JOIN `${param(reference_table)}` AS s ON t.${column()} = s.`${param(reference_column)}` WHERE s.`${param(reference_column)}` IS NULL"
             }
           ],
           "inputParameters": {
             "PARAMETER_NAME": { "description": "PARAMETER_DESCRIPTION" }
           },
           "capabilities": ["THRESHOLD"]
         }
      }
    }
    }
    EOF

Replace the following:

  * `ENTRY_GROUP_ID`: the ID of the entry group that stores your rule template.
  * `TEMPLATE_ID`: a unique ID for your rule template.
  * `DISPLAY_NAME`: a display name for the rule template.
  * `DESCRIPTION`: a description of the rule template.
  * `PARAMETER_NAME`: the name of an input parameter used in the SQL query.
  * `PARAMETER_DESCRIPTION`: a description of the input parameter.



### Terraform

To create a custom rule template, use the [`google_dataplex_entry`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_entry) resource:
    
    
    resource "google_dataplex_entry" "rule_template" {
    project        = "PROJECT_ID"
    location       = "LOCATION"
    entry_id       = "TEMPLATE_ID"
    entry_group_id = "ENTRY_GROUP_ID"
    
    entry_type = "projects/dataplex-types/locations/global/entryTypes/data-quality-rule-template"
    
    entry_source {
    display_name = "DISPLAY_NAME"
    description  = "DESCRIPTION"
    }
    
    aspects {
    aspect_key = "dataplex-types.global.data-quality-rule-template"
    aspect {
      data = jsonencode({
        dimension = "VALIDITY"
        sqlCollection = [
          {
            query = "SELECT t.* FROM $${data()} AS t LEFT JOIN `$${param(reference_table)}` AS s ON t.$${column()} = s.`$${param(reference_column)}` WHERE s.`$${param(reference_column)}` IS NULL"
          }
        ]
        inputParameters = {
          "PARAMETER_NAME" = { description = "PARAMETER_DESCRIPTION" }
        }
        capabilities = ["THRESHOLD"]
      })
    }
    }
    }

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: the location for your rule template (for example, `us-central1`).
  * `ENTRY_GROUP_ID`: the ID of the entry group that stores your rule template.
  * `TEMPLATE_ID`: a unique ID for your rule template.
  * `DISPLAY_NAME`: a display name for the rule template.
  * `DESCRIPTION`: a description of the rule template.
  * `PARAMETER_NAME`: the name of an input parameter used in the SQL query.
  * `PARAMETER_DESCRIPTION`: a description of the input parameter.



### Update a rule template

To update an existing rule template, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. Go to **Rule libraries** > **Custom**.

  3. Click the rule library that contains the template you want to update.

  4. In the **Rule templates** list, click the template that you want to update.

  5. On the rule template details page, click edit**Edit**.

  6. Update the fields, and then click **Save**.




### REST

To update a custom rule template, patch the entry or specific aspect:
    
    
    gcurl -X PATCH "https://${DATAPLEX_API}/entryGroups/ENTRY_GROUP_ID/entries/TEMPLATE_ID?updateMask=aspects" \
    --data @- << EOF
    {
     "aspects": {
       "dataplex-types.global.data-quality-rule-template": {
         "data": {
           "dimension": "VALIDITY",
           "sqlCollection": [
             {
               "query": "SELECT * FROM ${data()} WHERE ${column()} IS NOT NULL"
             }
           ]
         }
       }
     }
    }
    EOF

Replace the following:

  * `ENTRY_GROUP_ID`: the ID of the entry group that stores your rule template.
  * `TEMPLATE_ID`: the ID of the rule template that you want to update.



### Terraform

To update a custom rule template, use the [`google_dataplex_entry`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_entry) resource:
    
    
    resource "google_dataplex_entry" "rule_template" {
    project        = "PROJECT_ID"
    location       = "LOCATION"
    entry_id       = "TEMPLATE_ID"
    entry_group_id = "ENTRY_GROUP_ID"
    
    entry_type = "projects/dataplex-types/locations/global/entryTypes/data-quality-rule-template"
    
    aspects {
    aspect_key = "dataplex-types.global.data-quality-rule-template"
    aspect {
      data = jsonencode({
        dimension = "VALIDITY"
        sqlCollection = [
          {
            query = "SELECT * FROM $${data()} WHERE $${column()} IS NOT NULL"
          }
        ]
      })
    }
    }
    }

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: the location for your rule template (for example, `us-central1`).
  * `ENTRY_GROUP_ID`: the ID of the entry group that stores your rule template.
  * `TEMPLATE_ID`: the ID of the rule template that you want to update.



### Delete a rule template

To delete an existing rule template, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. Go to **Rule libraries** > **Custom**.

  3. Click the rule library that contains the template you want to delete.

  4. In the **Rule templates** list, click the template that you want to delete.

  5. Click **Delete** , and then click **Delete** again to confirm.




### REST

To delete a custom rule template, delete the entry:
    
    
    gcurl -X DELETE \
    "https://${DATAPLEX_API}/entryGroups/ENTRY_GROUP_ID/entries/TEMPLATE_ID"

Replace the following:

  * `ENTRY_GROUP_ID`: the ID of the entry group that stores your rule template.
  * `TEMPLATE_ID`: the ID of the rule template that you want to delete.



## Create a data quality scan using template rules

Use your custom templates to define rules for a data quality scan.

### Console

  1. In the Google Cloud console, go to the **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. Follow the steps to [create a data quality scan](https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality#create-scan), but update the following:

     1. In the **Define scan** window, in the **Credential type** menu, select **Service account** , and then enter a service account. A service account is mandatory for using rule templates.
     2. In the **Data quality rules** window, define the rules to configure for this data quality scan: 
        1. Click **Add rules** > **Template rules**.
        2. You can either select **Attach rule to entire table** , or in **Choose columns** , browse and select the columns to apply rules for.
        3. In **Choose rule templates** , select the rule templates to use. Only the rule templates in the same location as the scan or in a global location can be used. Alternatively, you can also select system rule templates from the list.
        4. Click **OK**.
        5. Click edit**Edit rule** , and then add rule specific parameters.
        6. Click **Save**.
        7. Select the rules that you want to add, and then click **Select**. The rules are now added to your current rules list.
        8. Optional: Repeat the previous steps to add additional rules to the data quality scan.
        9. Click **Continue**.
     3. Proceed with the remaining scan configuration.
     4. Click **Create** to only create the scan, or click **Run scan** to create and immediately run the scan.



### REST

To create a data quality scan that references a rule template, specify the `templateReference`. Custom rule templates use project-specific paths, while system rule templates use a global path: `projects/dataplex-templates/locations/global/entryGroups/rule-library/entries/<var>SYSTEM_TEMPLATE_ID</var>`.

The following example creates a scan that uses a custom rule template and includes a filter to selectively run rules:
    
    
    gcurl -X POST "https://${DATAPLEX_API}/dataScans?data_scan_id=DATASCAN_ID" \
    --data @- << EOF
    {
    "data": {
      "resource": "//bigquery.googleapis.com/projects/BIGQUERY_PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID"
    },
    "executionIdentity": {
      "serviceAccount": { "email": "SERVICE_ACCOUNT_EMAIL" }
    },
    "executionSpec": { "trigger": { "onDemand": {} } },
    "type": "DATA_QUALITY",
    "dataQualitySpec": {
      "rules": [
        {
          "templateReference": {
            "name": "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID/entries/TEMPLATE_ID",
            "values": { "PARAMETER_NAME": { "value" : "PARAMETER_VALUE" } }
          },
          "column": "COLUMN_NAME",
          "name": "RULE_NAME"
        }
      ],
      "filter": "FILTER_CONDITION"
    }
    }
    EOF

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: the location for your rule template and scan (for example, `us-central1`).
  * `DATASCAN_ID`: the ID of the data quality scan.
  * `BIGQUERY_PROJECT_ID`: the project ID of the BigQuery table.
  * `DATASET_ID`: the BigQuery dataset ID.
  * `TABLE_ID`: the BigQuery table ID.
  * `SERVICE_ACCOUNT_EMAIL`: the email ID of the service account to run the scan.
  * `ENTRY_GROUP_ID`: the ID of the entry group that stores your rule template.
  * `TEMPLATE_ID`: the ID of the custom rule template.
  * `SYSTEM_TEMPLATE_ID`: the ID of the system rule template (for example, `non_null_expectation`).
  * `PARAMETER_NAME`: the name of an input parameter for the rule template.
  * `PARAMETER_VALUE`: the value for the input parameter.
  * `COLUMN_NAME`: the column to apply the rule to.
  * `RULE_NAME`: a name for the rule instance.
  * `FILTER_CONDITION`: an optional [AIP-160 filter string](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#rule-filtering) to selectively run rules (for example, `name = "RULE_NAME"`).



### Terraform

To create a data quality scan that references a rule template, use the [`google_dataplex_datascan`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_datascan) resource:
    
    
    resource "google_dataplex_datascan" "scan" {
    data_scan_id = "DATASCAN_ID"
    location     = "LOCATION"
    project      = "PROJECT_ID"
    
    data {
    resource = "//bigquery.googleapis.com/projects/BIGQUERY_PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID"
    }
    
    execution_spec {
    service_account = "SERVICE_ACCOUNT_EMAIL"
    trigger {
      on_demand {}
    }
    }
    
    data_quality_spec {
    rules {
      column    = "COLUMN_NAME"
      name      = "RULE_NAME"
      dimension = "VALIDITY"
    
      template_reference {
        name = "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID/entries/TEMPLATE_ID"
        values = {
          "PARAMETER_NAME" = { value = "PARAMETER_VALUE" }
        }
      }
    }
    filter = "FILTER_CONDITION"
    }
    }

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: the location for your rule template and scan (for example, `us-central1`).
  * `DATASCAN_ID`: the ID of the data quality scan.
  * `BIGQUERY_PROJECT_ID`: the project ID of the BigQuery table.
  * `DATASET_ID`: the BigQuery dataset ID.
  * `TABLE_ID`: the BigQuery table ID.
  * `SERVICE_ACCOUNT_EMAIL`: the email ID of the service account to run the scan.
  * `ENTRY_GROUP_ID`: the ID of the entry group that stores your rule template.
  * `TEMPLATE_ID`: the ID of the custom rule template.
  * `PARAMETER_NAME`: the name of an input parameter for the rule template.
  * `PARAMETER_VALUE`: the value for the input parameter.
  * `COLUMN_NAME`: the column to apply the rule to.
  * `RULE_NAME`: a name for the rule instance.
  * `FILTER_CONDITION`: an optional [AIP-160 filter string](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#rule-filtering) to selectively run rules.



## Run and monitor data quality scans

After you create a data quality scan, you must run it to validate your data. For more information, see [Run a data quality scan](https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality#run-scans).

You can then monitor the scan jobs and view the results. For more information, see [View the data quality scan results](https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality#results).

## Attach data quality rules to catalog entries

You can declare data quality rules as aspects in Knowledge Catalog to make them searchable and reusable across scans.

### BigQuery table

To define rules directly on a BigQuery table entry, select one of the following:

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. Search for and select the table that you want to attach rules to.

  3. Click **Data quality** > **Rules management** > **Create rules**.

  4. In the **Create rules** window, do the following:

     1. In the **Choose create option** menu, select **Create new rule**.
     2. In **Choose columns** , click **Browse**. Select the columns to apply rules for.
     3. In the **Choose rule types** menu, select the rule templates to use. Only the rule templates in the same location as the scan can be used.
     4. Click edit**Edit rule** , and then add rule specific parameters.
     5. Click **Save**.

The **Rules management** page displays all entry rules.




### REST

To attach rules to a specific column using the API, patch the `@bigquery` entry with a `data-rules` aspect targeted to that column:
    
    
    gcurl -X PATCH "https://${DATAPLEX_API}/entryGroups/@bigquery/entries/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/tables/TABLE_ID?updateMask=aspects&aspect_keys=projects/dataplex-types/locations/global/aspectTypes/data-rules@Schema.COLUMN_NAME" \
    --data @- << EOF
    {
    "aspects": {
      "dataplex-types.global.data-rules@Schema.COLUMN_NAME": {
        "aspectType": "projects/dataplex-types/locations/global/aspectTypes/data-rules",
        "data": {
          "rules": [
            {
              "templateReference": "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID/entries/TEMPLATE_ID",
              "column": "COLUMN_NAME",
                "values": { "PARAMETER_NAME": { "value" : "PARAMETER_VALUE" } }
              }
          ]
        }
      }
    }
    }
    EOF

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: the location for your rule template and aspect.
  * `DATASET_ID`: the BigQuery dataset ID.
  * `TABLE_ID`: the BigQuery table ID.
  * `COLUMN_NAME`: the column to apply the rule to.
  * `ENTRY_GROUP_ID`: the ID of the entry group that stores your rule template.
  * `TEMPLATE_ID`: the ID of the rule template.
  * `PARAMETER_NAME`: the name of an input parameter for the rule template.
  * `PARAMETER_VALUE`: the value for the input parameter.



### Terraform

To attach rules to a specific column, use the [`google_dataplex_entry`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_entry) resource:
    
    
    resource "google_dataplex_entry" "bq_table_metadata" {
      project        = "PROJECT_ID"
      location       = "LOCATION"
      entry_id       = "bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID"
      entry_group_id = "@bigquery"
    
      aspects {
        aspect_key = "dataplex-types.global.data-rules@Schema.COLUMN_NAME"
        aspect {
          data = jsonencode({
            rules = [
              {
                name      = "RULE_NAME"
                dimension = "VALIDITY"
                templateReference = "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID/entries/TEMPLATE_ID"
                   values = {
                     "PARAMETER_NAME" = { value = "PARAMETER_VALUE" }
                   }
                }
            ]
          })
        }
      }
    }

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: the location for your rule template and aspect.
  * `DATASET_ID`: the BigQuery dataset ID.
  * `TABLE_ID`: the BigQuery table ID.
  * `COLUMN_NAME`: the column to apply the rule to.
  * `ENTRY_GROUP_ID`: the ID of the entry group that stores your rule template.
  * `TEMPLATE_ID`: the ID of the rule template.
  * `PARAMETER_NAME`: the name of an input parameter for the rule template.
  * `PARAMETER_VALUE`: the value for the input parameter.
  * `RULE_NAME`: a unique name for the rule.



### Business glossary terms

You can attach rules to business glossary terms. Rules attached to terms are automatically inherited by linked BigQuery tables.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. Search for and select the business glossary term.

  3. In the **Data quality rules** section, click add **Add**.

  4. In the **Create rules** window, do the following:

     1. In the **Choose create option** menu, select **Create new rule**.
     2. In the **Choose rule types** menu, select the rule templates to use. Only the rule templates in the same location as the scan can be used.
     3. Click edit**Edit rule** , and then add rule specific parameters.
     4. Click **Save**.
  5. Attach the term to a BigQuery table or columns. For more information, see [Manage links between terms and data assets](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries#links-terms-asset).




### REST

To attach rules to a term using the API, patch the `@dataplex` entry for the glossary term:
    
    
    gcurl -X PATCH "https://${DATAPLEX_API}/entryGroups/@dataplex/entries/projects/PROJECT_ID/locations/LOCATION/glossaries/GLOSSARY_ID/terms/TERM_ID?updateMask=aspects&aspect_keys=projects/dataplex-types/locations/global/aspectTypes/data-rules" \
    --data @- << EOF
    {
    "aspects": {
      "dataplex-types.global.data-rules": {
        "aspectType": "projects/dataplex-types/locations/global/aspectTypes/data-rules",
        "data": {
          "rules": [
            {
              "templateReference": "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID/entries/TEMPLATE_ID",
              "column": "COLUMN_NAME",
                "values": { "PARAMETER_NAME": { "value" : "PARAMETER_VALUE" } }
              }
          ]
        }
      }
    }
    }
    EOF

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: the location for your rule template and aspect.
  * `GLOSSARY_ID`: the ID of the business glossary.
  * `TERM_ID`: the ID of the glossary term.
  * `ENTRY_GROUP_ID`: the ID of the entry group that stores your rule template.
  * `TEMPLATE_ID`: the ID of the rule template.
  * `COLUMN_NAME`: the column to apply the rule to.
  * `PARAMETER_NAME`: the name of an input parameter for the rule template.
  * `PARAMETER_VALUE`: the value for the input parameter.



### Terraform

To attach rules to a business glossary term, use the [`google_dataplex_entry`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_entry) resource:
    
    
    resource "google_dataplex_entry" "glossary_term_rules" {
      project        = "PROJECT_ID"
      location       = "LOCATION"
      entry_id       = "projects/PROJECT_ID/locations/LOCATION/glossaries/GLOSSARY_ID/terms/TERM_ID"
      entry_group_id = "@dataplex"
    
      aspects {
        aspect_key = "dataplex-types.global.data-rules"
        aspect {
          data = jsonencode({
            rules = [
              {
                name      = "RULE_NAME"
                dimension = "VALIDITY"
                templateReference = "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID/entries/TEMPLATE_ID"
                  values = {
                    "PARAMETER_NAME" = { value = "PARAMETER_VALUE" }
                  }
                }
            ]
          })
        }
      }
    }

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: the location for your rule template and aspect.
  * `GLOSSARY_ID`: the ID of the business glossary.
  * `TERM_ID`: the ID of the glossary term.
  * `ENTRY_GROUP_ID`: the ID of the entry group that stores your rule template.
  * `TEMPLATE_ID`: the ID of the rule template.
  * `PARAMETER_NAME`: the name of an input parameter for the rule template.
  * `PARAMETER_VALUE`: the value for the input parameter.
  * `RULE_NAME`: a unique name for the rule.



### Import rules from another table

You can import data quality rules from an existing BigQuery table entry to your current table.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. Select the table you want to manage rules for.

  3. Click **Data quality** > **Rules management**.

  4. Click **Create rules**.

  5. In the **Create rules** window, do the following:

     1. In the **Choose create option** menu, select **Import rules from another table**.
     2. In **Table** , click **Browse**. Search for and select the source table containing the rules that you want to copy.
     3. Select the rules. You can also edit the rules.
     4. Click **Save**.

The **Rules management** tab displays the new rules.




### REST

To import rules, you must fetch the `data-rules` aspect from the source entry and apply it to the target entry.

  1. Get the `data-rules` aspect from the source entry:
         
         gcurl "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP_ID/entries/SOURCE_ENTRY_ID?view=FULL"

  2. Extract the `rules` list from the `dataplex-types.global.data-rules` aspect.

  3. Attach the rules to a target entry.

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `LOCATION`: the location of the source entry.
     * `ENTRY_GROUP_ID`: the ID of the entry group for the source entry.
     * `SOURCE_ENTRY_ID`: the ID of the source entry.



### View data quality rules for BigQuery table

You can view all rules applicable to a table, including rules attached directly and rules inherited from linked glossary terms.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. Search for and select the table.

  3. Click **Data quality** > **Rules management** to view all rules.




## Create a data quality scan using rules from catalog

You can selectively run rules declared on catalog entries in a scan.

### Console

  1. In the Google Cloud console, go to the **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. Follow the steps to [create a data quality scan](https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality#create-scan), but update the following:

     1. In the **Define scan** window, do the following: 
        1. In the **Credential type** menu, select **Service account** , and then enter a service account. A service account is mandatory for using rule templates.
        2. For **Rule type** , select **Create with entry based rule**.
     2. In the **Data quality rules** section, rules applicable to the table entry are displayed, including rules inherited from linked glossary terms. To filter the rules, do the following: 
        1. In the **Filter items** field, [filter items to selectively run rules](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#rule-filtering).
        2. Click **Apply**. Filtered rules are displayed.
     3. Proceed with the remaining scan configuration.
     4. Click **Create** to only create the scan, or click **Run scan** to create and immediately run the scan.

Subsequent runs evaluate rules attached to the entry or inherited from glossary terms as observed at the time of execution.




### REST

To run rules from catalog entries, set `enableCatalogBasedRules` to `true`. You can also specify a filter.

To create the scan, use the following code:
    
    
    gcurl -X POST "https://${DATAPLEX_API}/dataScans?data_scan_id=DATASCAN_ID" \
    --data @- << EOF
    {
    "type": "DATA_QUALITY",
    "data": {
      "resource": "//bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID"
    },
    "executionIdentity": {
      "serviceAccount": { "email": "SERVICE_ACCOUNT_EMAIL" }
    },
    "executionSpec": { "trigger": { "onDemand": {} } },
    "dataQualitySpec": {
      "enableCatalogBasedRules": true,
      "filter": "FILTER_CONDITION"
    }
    }
    EOF

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: the location for your data scan.
  * `DATASCAN_ID`: the ID of the data quality scan.
  * `DATASET_ID`: the BigQuery dataset ID.
  * `TABLE_ID`: the BigQuery table ID.
  * `SERVICE_ACCOUNT_EMAIL`: the email ID of the service account to run the scan.
  * `FILTER_CONDITION`: an [AIP-160 filter string](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#rule-filtering) to selectively run rules (for example, `attributes.environment = "prod"`).



### Terraform

To run rules from catalog entries, use the [`google_dataplex_datascan`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_datascan) resource:
    
    
    resource "google_dataplex_datascan" "scan" {
    data_scan_id = "DATASCAN_ID"
    location     = "LOCATION"
    project      = "PROJECT_ID"
    
    data {
    resource = "//bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID"
    }
    
    execution_spec {
    service_account = "SERVICE_ACCOUNT_EMAIL"
    trigger {
      on_demand {}
    }
    }
    
    data_quality_spec {
    enable_catalog_based_rules = true
    filter = "FILTER_CONDITION"
    }
    }

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: the location for your data scan.
  * `DATASCAN_ID`: the ID of the data quality scan.
  * `DATASET_ID`: the BigQuery dataset ID.
  * `TABLE_ID`: the BigQuery table ID.
  * `SERVICE_ACCOUNT_EMAIL`: the email ID of the service account to run the scan.
  * `FILTER_CONDITION`: an [AIP-160 filter string](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#rule-filtering) to selectively run rules.



## Metadata aspects

This section describes the fields and values for the `data-rules` and `data-quality-rule-template` aspect types.

### `data-rules` aspect fields

To define data rules, use the `dataplex-types.global.data-rules` aspect. The following table describes the fields for this aspect.

Field | Type | Description  
---|---|---  
`rules` | Array | Required. A list of data quality rules.  
`rules[].name` | String | Required. A name for the rule.  
`rules[].dimension` | String | Optional. The data quality [dimension](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#dimensions) for the rule.  
`rules[].description` | String | Optional. The description of the rule.  
`rules[].suspended` | Boolean | Optional. Whether the rule is active or suspended. Default is `false`.  
`rules[].threshold` | Double | Optional. The passing threshold for the rule, from `0.0` to `1.0`. Default is `1.0`.  
`rules[].type` | Enum | Required. The type of the rule. The only supported value is `TEMPLATE_REFERENCE`.  
`rules[].ignore_null` | Boolean | Optional. If `true`, rows with null values in the column are ignored when determining the success criteria.  
`rules[].attributes` | Map | Optional. Custom key-value pairs associated with the rule.  
`rules[].templateReference` | Object | Required. A reference to the rule template.  
`rules[].templateReference.name` | String | Required. The resource name of the rule template.  
`rules[].templateReference.values` | Map | Optional. The parameter names and values for the rule template.  
`rules[].templateReference.values[].parameterValue.value` | String | Required. The value for the parameter.  
**Note:** The column that a rule applies to isn't specified as a field in the aspect data. Instead, it's determined by the path where the aspect is attached. For BigQuery table entries, this is the column path. For glossary terms, it's the column mapped through the term's [`entryLink`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entryLinks#resource:-entrylink).

The following example shows a `data-rules` aspect in a `payload.json` file:
    
    
    {
      "aspects": {
        "dataplex-types.global.data-rules": {
          "data": {
            "rules": [
              {
                "name": "valid-email",
                "dimension": "VALIDITY",
                "type": "TEMPLATE_REFERENCE",
                "templateReference": {
                  "name": "projects/my-project/locations/us-central1/entryGroups/my-rules/entries/email-check",
                  "values": {
                    "column_name": {
                        "value": "email"
                    }
                  }
                }
              }
            ]
          }
        }
      }
    }
    

### `data-quality-rule-template` aspect fields

Use the `data-quality-rule-template` aspect to define a custom data quality rule template. The following table describes the fields for the `dataplex-types.global.data-quality-rule-template` aspect.

Field | Type | Description  
---|---|---  
`dimension` | String | Required. The [dimension](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview#dimensions) for the rule template.  
`sqlCollection` | Array | Required. A list of SQL queries for the rule template.  
`sqlCollection[].sql.query` | String | Required. The SQL query that returns invalid rows.  
`inputParameters` | Map | Optional. A map of input parameters for the rule template.  
`inputParameters[].parameterDescription.description` | String | Optional. The description of the input parameter.  
`inputParameters[].parameterDescription.defaultValue` | String | Optional. The default value for the parameter if no value is provided.  
`capabilities` | Array | Optional. A list of template capabilities, such as `THRESHOLD` or `IGNORE_NULL`.  
  
The following example displays the structure of a `data-quality-rule-template` aspect:
    
    
    {
      "entryType": "projects/dataplex-types/locations/global/entryTypes/data-quality-rule-template",
      "aspects": {
        "dataplex-types.global.data-quality-rule-template": {
          "data": {
            "dimension": "COMPLETENESS",
            "sqlCollection": [
              {
                  "query": "SELECT * FROM ${data()} WHERE ${column()} > ${param(p1)}"
              }
            ],
            "inputParameters": {
              "p1": {
                  "description": "The parameter description"
              }
            },
            "capabilities": [
              "THRESHOLD",
              "IGNORE_NULL"
            ]
          }
        }
      }
    }
    

## Pricing

Using Knowledge Catalog rule reusability involves the following pricing elements:

  * **BigQuery charges** : BigQuery charges for the job that runs in the scan project. For more information, see [BigQuery pricing](https://docs.cloud.google.com/bigquery/pricing).
  * **Knowledge Catalog data quality scan** : There's no charge for processing since BigQuery charges for the job.
  * **Metadata storage** : `data-rules` aspect and `data-quality-rule-template` aspect storage is charged as metadata storage. For more information, see [Knowledge Catalog pricing](https://docs.cloud.google.com/dataplex/pricing).



## What's next

  * Learn more about [auto data quality overview](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview).
  * Learn how to [use auto data quality scans](https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality).
  * View a complete list of [system rule templates](https://docs.cloud.google.com/knowledge-catalog/docs/system-rule-templates-list).
  * Learn about [metadata management](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
