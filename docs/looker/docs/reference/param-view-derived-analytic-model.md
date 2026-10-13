---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-derived-analytic-model/
title: derived_analytic_model \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:26.562233+00:00
---

# derived_analytic_model  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-derived-analytic-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  derived_analytic_model Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms](https://cloud.google.com/terms/service-terms#1) section of the Service Specific Terms. Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

If you encounter an issue during the Public Preview of Looker support of in-database analytic models, report it to [database_analytic_models_feedback@google.com](mailto:database_analytic_models_feedback@google.com).

## Usage
    
    
    # SQL-based derived analytic model
    view: view_name {
      derived_analytic_model: {
        publish_as_db_analytic_model: yes | no
        sql: analytic_model_definition ;;
      }
    }
    
    # LookML-based derived analytic model
    view: view_name {
      derived_analytic_model: {
        publish_as_db_analytic_model: yes | no
        model_source: explore_name {
          fields: [field_1, field_2, ...]
          join: +joined_view_name {
            foreign_key: field_name
          }
        }
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) `derived_analytic_model` |  Default Value None Special Rules Analytic models are supported only for BigQuery and Snowflake connections.   
---|---  
  
## Definition

For BigQuery and Snowflake connections, the `derived_analytic_model` parameter defines an [in-database analytic model](https://docs.cloud.google.com/looker/docs/analytic-models) (a [BigQuery Graph](https://docs.cloud.google.com/bigquery/docs/graph-overview) or a [semantic view in Snowflake](https://docs.snowflake.com/en/user-guide/views-semantic/overview)) that is managed by Looker.

Unlike [derived tables](https://docs.cloud.google.com/looker/docs/derived-tables), Looker-managed analytic model objects don't persist any data within the database and aren't incrementally refreshed. Instead, they represent semantic models that define relationships and measures directly in the database.

**Note:** The `derived_analytic_model` parameter lets you define a new analytic model that Looker will create in your database. If you already have an analytic model that is created and managed in your database, you can use the [`sql_analytic_model_name`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-analytic-model-name) parameter to create a LookML view based on the existing analytic model.

Looker supports two types of derived analytic models:

  * **SQL-based derived analytic models**: You define the analytic model by using SQL [Data Definition Language (DDL)](https://en.wikipedia.org/wiki/Data_definition_language) statements. Looker generates the analytic model within your database by executing the SQL statements that you specify.
  * **LookML-based derived analytic models**: You define the analytic model by referencing an existing LookML Explore. Looker automatically translates your Explore topology, joins, dimensions, and measures into database-native analytic model DDL statements and creates and manages the model in your database.



## SQL-based derived analytic models

In a SQL-based derived analytic model, Looker generates the analytic model within your database by executing the appropriate SQL [Data Definition Language (DDL)](https://en.wikipedia.org/wiki/Data_definition_language) statements that you specify in the definition of the `derived_analytic_model` LookML parameter. The SQL syntax that you define in the `derived_analytic_model` parameter must be supported by your database.

To define a SQL-based analytic model, use one of the following subparameters of the `derived_analytic_model` parameter:

  * `sql`
  * `sql_create`
  * `create_process`



In addition, if you define your analytic view with the `sql` subparameter, you can use the publish_as_db_analytic_model subparameter of the `derived_analytic_model` parameter to create a stable analytic model that can be queried outside of Looker. 

After you define the analytic model inside the `derived_analytic_model` parameter, you can define LookML dimensions and measures that map to your analytic model. See the SQL-based derived analytic model examples section for more information.

### `sql`

Use the `sql` parameter if you want to provide the SQL for only the definition of the analytic model and have Looker manage the creation of the analytical model. When you use the `sql` subparameter, don't include a `CREATE` or a `CREATE OR REPLACE` statement, because Looker will automatically generate the DDL statement to create the analytic model on the database side. 

See Creating a derived analytic model with `sql` for an example of using the `sql` parameter to create an analytic model on your database.

### `sql_create`

Use the `sql_create` parameter to define a full SQL statement to create an analytic model. When you use the `sql_create` parameter, you need to include a `CREATE OR REPLACE` statement (or a `CREATE` statement, if your dialect doesn't support `CREATE OR REPLACE`).

Note the following when you use the `sql_create` subparameter:

  * For BigQuery connections, use a `CREATE OR REPLACE` statement to create the analytic model.
  * Use `${SQL_TABLE_NAME}` to substitute in the computed name of the analytic model being created. This ensures that the SQL statement will correctly include the analytic model name that you provide in the LookML `view` parameter. 



See Creating a derived analytic model with `sql_create` for an example of using the `sql_create` parameter to create an analytic model on your database.

### `create_process`

Use the `create_process` parameter when you need to define multiple, sequential SQL statements to define the analytic model. Under the `create_process` parameter, use the `sql_step` subparameter to specify the individual SQL statements. Your database will execute the `sql_step` statements one at a time, in the order that you specified them. Looker issues the SQL statements in the `sql_step` subparameters as you define them, with no wrapper, which means that you have to include a step with a `CREATE OR REPLACE` statement (or a `CREATE` statement, if your dialect doesn't support `CREATE OR REPLACE`).

See Creating a derived analytic model with `create_process` for an example of using the `create_process` parameter to create an analytic model on your database.

### `publish_as_db_analytic_model`

For derived analytic models that are created with the `sql` parameter, you can define your derived analytic model with `publish_as_db_analytic_model: yes` to prompt Looker to create a stable analytic model that can be queried outside of Looker.

The stable analytic model will be published (created) on the next cycle of the [Looker regenerator](https://docs.cloud.google.com/looker/docs/derived-tables#the_looker_regenerator) after the derived analytic model's LookML is [deployed to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#deploying_to_production) with `publish_as_db_analytic_model: yes`.

When you specify `publish_as_db_analytic_model: yes`, the Looker regenerator creates two analytic models in your database: one with an internal name and one with a stable name. Otherwise, the regenerator creates only one analytic model in the database, using the internal name.

See the Accessing the stable analytic model section for information about getting the name of the stable analytic model so that you can use the name to query the stable analytic model outside of Looker.

### Create LookML dimensions and measures based on your SQL-based analytic view

After you define your analytic model, in the same view file you can then define LookML dimensions and measures that are based on the analytic model.

See your dialect's documentation for information about the proper syntax to use for defining your analytic model, and for referring to elements in your analytic model. For example, to create a LookML dimension from a BigQuery Graph entity, you must use underscores to separate elements when scoping. For example, for BigQuery Graph, this LookML dimension is based on the `location_id` property in the `Stores` node table:
    
    
      dimension: location_id {
        type: number
        sql: Stores_location_id ;;
      }
    

However, to create a LookML dimension that's based on a Snowflake semantic view, you must use the unqualified name of a metric or dimension.

### SQL-based derived analytic model examples

The following sections provide examples of creating an analytic view by using the different subparameters of `derived_analytic_model`:

  * Creating a derived analytic model with `sql`
  * Creating a derived analytic model with `create_process`
  * Creating a derived analytic model with `sql_create`



#### Creating a derived analytic model with `sql`

The following is an example LookML view file that defines a SQL-based analytic model for a BigQuery database using the `sql` subparameter of `derived_analytic_model`. Looker will create the analytic model within the database by executing the SQL DDL commands that are provided in the `sql` parameter. 

**Note:** This example is for a BigQuery Graph, so the model definition is specific to BigQuery. Consult the documentation for your database dialect to get the proper syntax for your dialect.

Note the following in the example:

  * The `sql` subparameter contains only the definition of the analytic model itself. There is no `CREATE` statement, because with `sql` Looker automatically handles the `CREATE` commands for the analytic model.
  * The analytic model is defined with `publish_as_db_analytic_model: yes`, so Looker will create a stable analytic model that can be queried outside of Looker.


    
    
    view: MyWarehouseOrdersView {
      derived_analytic_model: {
        publish_as_db_analytic_model: yes
    
        # Defining the analytic model
        
        sql:
          NODE TABLES (
            Customers
            KEY(customer_id)
            PROPERTIES(
              country_code,
              concat(first_name, ' ', last_name) AS name,
              age,
              MEASURE(AVG(age)) AS AvgAge 
            ),
          Orders
            KEY(order_id)
            PROPERTIES (
              customer_id,
              employee_id,
              date,
              discount,
              MEASURE(AVG(discount)) AS AvgDiscount
            )
    
          EDGE TABLES (
            -- Relationship: Orders -> Customers
            looker_test.orders AS orders_to_users
              KEY(id)
              SOURCE KEY (order_id) REFERENCES orders (order_id)
              DESTINATION KEY (customer_id) REFERENCES Customers (customer_id)
              NO PROPERTIES
          ) ;;
      }
    
      # Mapping dimensions/measures to the dimensions/measures
      # provided by the analytic model
    
      dimension: customer_id {
        type: number
        sql: Customers_customer_id ;;
      }
    
      dimension: customer_age {
        type: number
        sql: Customers_age ;;
      }
    
      measure: orders_avg_discount {
        type: number
        sql: Orders_AvgDiscount ;; 
      }
    }
    

#### Creating a derived analytic model with `create_process`

The following is an example LookML view file that defines a SQL-based analytic model for a BigQuery database by using the `create_process` subparameter of `derived_analytic_model`. In this example, you need to define multiple, sequential SQL statements to define the analytic model. The first step drops the analytic model if it already exists, and the second step creates the analytic model.
    
    
    view: university_statistics {
      derived_analytic_model: {
        create_process: {
          sql_step: 
            DROP PROPERTY GRAPH IF EXISTS ${SQL_TABLE_NAME} ;;
          sql_step: 
            CREATE PROPERTY GRAPH ${SQL_TABLE_NAME}
             NODE TABLES (
              university.College
                KEY(college_id)
                PROPERTIES(college_id, college_name),
              university.Department
                KEY(dept_id)
                PROPERTIES(dept_id, dept_name, college_id,
                  budget OPTIONS(description="Department budget in USD"),
                  MEASURE(SUM(budget)) AS total_budget),
              university.Course
                KEY(course_id)
                PROPERTIES(
                  course_id,
                  course_name,
                  credits,
                  dept_id,
                  MEASURE(AVG(credits)) AS avg_credits,
                  MEASURE(SUM(credits)) AS total_credits,
                  MEASURE(COUNT(course_id)) AS course_count)
            )
            EDGE TABLES (
              university.Department AS CollegeDept
                SOURCE KEY (college_id) REFERENCES College (college_id)
                DESTINATION KEY (dept_id) REFERENCES Department (dept_id),
              university.Course AS DeptCourse
                SOURCE KEY (dept_id) REFERENCES Department (dept_id)
                DESTINATION KEY (course_id) REFERENCES Course (course_id)
            );;
        }
      }
    
      # Mapping dimensions/measures to the dimensions/measures
      # provided by the analytic model
    
      dimension: college_id {
        type: number
        sql: College_college_id ;;
      }
    
      dimension: course_name {
        type: string
        sql: Course_course_name ;;
      }
      
      ...
    }
    

#### Creating a derived analytic model with `sql_create`

The following is an example LookML view file that defines a SQL-based analytic model for a BigQuery database by using the `sql_create` subparameter of `derived_analytic_model`. In this example, the `sql_create` parameter defines the full `CREATE OR REPLACE` statement to execute to create the analytic model in a single step.
    
    
    view: MyWarehouseOrdersView {
      derived_analytic_model: {
        sql_create:
          CREATE OR REPLACE PROPERTY GRAPH ${SQL_TABLE_NAME}
            NODE TABLES(
              accounting.Loan AS Loan
                KEY(loanId)
                LABEL Loan PROPERTIES(
                  loanId,
                  loanAmount,
                  balance,
                  createTime,
                  interestRate,
                  accountId,
                  balance + 100 AS derived_balance,
                  CASE WHEN balance > 1000 THEN "High" ELSE "Low" END AS risk_level,
                  CONCAT("ID-", CAST(loanId AS STRING)) AS full_id,
                  DATE(2024, 1, 1) AS fixed_date,
                  MEASURE(AVG(interestRate)) AS avg_interest_rate
                ),
              accounting.AccountView AS Account
                KEY(accountId)
                LABEL Account PROPERTIES(
                  accountId,
                  createTime,
                  isBlocked,
                  accountType,
                  amount,
                  ownerId,
                  MEASURE(MIN(createTime)) AS oldest_account_create_time,
                  MEASURE(MAX(createTime)) AS newest_account_create_time,
                  MEASURE(AVG(amount)) AS avg_account_amount,
                  MEASURE(SUM(amount)) AS total_account_amount,
                  MEASURE(COUNT(DISTINCT accountType)) AS account_type_count
                ),
              accounting.PersonMV AS Person
                KEY(personId)
                LABEL Person PROPERTIES(
                  personId,
                  personName,
                  age,
                  age_tier,
                  MEASURE(AVG(age)) AS avg_age,
                  MEASURE(COUNT(DISTINCT age_tier)) AS age_tier_count
                )
            )
            EDGE TABLES(
              accounting.Loan AS Account_Repay_Loan
                KEY(loanId)
                SOURCE KEY(loanId) REFERENCES Loan(loanId)
                DESTINATION KEY(accountId) REFERENCES Account(accountId)
                LABEL Repay NO PROPERTIES,
              accounting.Account AS Person_Own_Account
                KEY(accountId)
                SOURCE KEY(accountId) REFERENCES Account(accountId)
                DESTINATION KEY(ownerId) REFERENCES Person(personId)
                LABEL Own NO PROPERTIES
            );;
      }
    
      # Mapping dimensions/measures to the dimensions/measures
      # provided by the analytic model
    
      dimension: loan_id {
        type: number
        sql: Loan_loanId ;;
      }
    
      dimension: account_ID {
        type: number
        sql: Account_accountID ;;
      }
    
      ...
    
    }
    

### Accessing the stable analytic model

If you created your derived analytic model by using the `sql` subparameter and you included the `publish_as_db_analytic_model: yes` statement under your `derived_analytic_model` parameter, Looker will publish (create) the stable analytic model on the next cycle of the [Looker regenerator](https://docs.cloud.google.com/looker/docs/derived-tables#the_looker_regenerator) after the derived analytic model's LookML is [deployed to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#deploying_to_production) with `publish_as_db_analytic_model: yes`.

When the stable analytic model is published, you can query it directly by using its stable name. There are two ways to get the stable name for an analytic model:

  * PDT details modal
  * SQL tab of an Explore



#### PDT details modal

If you are an admin or a user with the [`see_pdts`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_pdts) permission, you can follow these steps to use the **Persistent Derived Tables** page in the **Admin** section of Looker to get the stable analytic model name for an analytic model:

  1. Click the Looker **Main menu** icon menu and select **Admin** , if the **Admin** menu isn't already displayed. (If you are in the **Explore** or **Develop** section of the Looker **Main menu** , you may have to click the back arrow to see the **Admin** menu.)
  2. From the **Admin** menu, select **Persistent Derived Tables**.
  3. On the **Persistent Derived Tables** page, search for the name of your analytic model.
  4. Click the three-dot menu for your analytic model, and then select **PDT Details**.
  5. In the [**PDT Details** modal](https://docs.cloud.google.com/looker/docs/admin-panel-database-pdts#pdt_details_modal), look for the **Stable Name** field.



To query the stable analytic model directly, add the scratch schema name before the model name. For example, if the scratch schema name is `tmp`, you can query the stable analytic model with a command like this:

`SELECT * from tmp.PA_bq_analytic_model_sales_semantic_view`

#### SQL tab of an Explore

If you don't have access to the **Persistent Derived Tables** admin page, you can determine the stable name from the information that is included on the **SQL** tab in the **Data** section of an Explore query of the analytic model. Follow these steps to get the stable name for an analytic model:

  1. Open the [Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) for your analytic model's view.

**Tip:** If you're in the Looker IDE, you can use the [**See file actions** drop-down menu](https://docs.cloud.google.com/looker/docs/looker-ide#testing_the_fields_in_the_explore) to open an Explore directly from the analytic model's view file or from a model file that defines an Explore for the analytic model's view.
  2. In the Explore, select any dimensions or measures from the field picker.

  3. Click the **SQL** tab of the **Data** section.

  4. In the **SQL** tab, locate one of the following SQL statements:

     * For BigQuery Graph: 
       * `CREATE PROPERTY GRAPH`
       * `SELECT ... FROM GRAPH_EXPAND('PROPERTY_GRAPH_NAME')`
     * For Snowflake semantic view: 
       * `CREATE SEMANTIC VIEW`
       * `SELECT ... FROM SEMANTIC_VIEW_NAME`
  5. The stable name is a view that Looker creates in the scratch schema, which points to the actual obfuscated table shown in the SQL tab. To get the stable name for the analytic view, fill in the following information from the SQL statement:
         
         SCRATCH_SCHEMA_NAME.CONNECTION_REGISTRATION_KEY_MODEL_NAME_VIEW_NAME
         

     * SCRATCH_SCHEMA_NAME: The scratch schema name is the beginning of the string following the `CREATE` or `SELECT` statement, before the "`.`"
     * CONNECTION_REGISTRATION_KEY: The connection registration key is two characters; depending on your database dialect, it will follow either a dollar sign or the first underscore in the table name in the `CREATE` or `SELECT` statement.
     * MODEL_NAME: The name of the LookML model.
     * VIEW_NAME: The name of the view where the analytic model is defined.



For example, here is the text from the **SQL** tab of an Explore query for a BigQuery connection. The analytic model is defined in the view that's named `sales_analytic_model`, and the name of the LookML model is `thelook`. In this case, Looker has already created the analytic model, so there is no `CREATE` statement. But the `SELECT ... FROM GRAPH_EXPAND` statement contains the table name information:
    
    
    -- use existing sales_analytic_model in `looker-test-db.looker_scratch.LG_J7LSZ1778710001008_sales_analytic_model`
    SELECT
        sales_analytic_model.orders_id  AS sales_analytic_model_orders_id,
        AGG(sales_analytic_model.orders_count_orders ) AS sales_analytic_model_count_orders
    FROM GRAPH_EXPAND("looker-test-db.looker_scratch.LG_J7LSZ1778710001008_sales_analytic_model") AS sales_analytic_model
    GROUP BY
        1
    ORDER BY
        2 DESC
    LIMIT 500
    

Here are the values that you need to derive the stable name of the analytic model:

  * SCRATCH_SCHEMA_NAME is `looker-test-db.looker_scratch`
  * CONNECTION_REGISTRATION_KEY is `J7`
  * MODEL_NAME is `thelook`
  * VIEW_NAME is `sales_analytic_model`



Therefore, the stable name for the analytic model is the following:

`looker-test-db.looker_scratch.J7_thelook_sales_analytic_model`

Once you have the stable name of the analytic model, you can query the analytic model directly. 

## LookML-based derived analytic models

LookML-based derived analytic models let you define an in-database analytic model (such as a [BigQuery Graph](https://docs.cloud.google.com/bigquery/docs/graph-overview) or a [Snowflake semantic view](https://docs.snowflake.com/en/user-guide/views-semantic/overview)) directly from an existing LookML Explore without needing to write database-specific SQL DDL statements.

Use the following parameters to define a LookML-based derived analytic model:

  * `model_source`
    * `fields` (subparameter of `model_source`)
    * `join` (subparameter of `model_source`; join itself has subparameters)
  * `publish_as_db_analytic_model` (this parameter applies to both LookML-based and SQL-based derived analytic models)



To create a LookML-based derived analytic model, you use the `model_source` parameter to point to a source Explore that defines your data topology. Looker then automatically translates your LookML views, joins, dimensions, and measures into database-native analytic model DDL statements:

  * **Nodes / Tables:** Each LookML view in the source Explore becomes a node table in BigQuery Graph or a table in a Snowflake semantic view.
  * **Edges / Relationships:** Each join that's defined with the `foreign_key` parameter in the source Explore becomes an edge table in BigQuery Graph or a relationship in a Snowflake semantic view.
  * **Properties / Dimensions and Metrics:** LookML dimensions and measures from the source views become node properties in BigQuery Graph or dimensions and metrics in a Snowflake semantic view.



When you query an Explore that is based on a LookML-based derived analytic model view, Looker generates and executes the database DDL to create the analytic model in your database scratch schema, and then executes the query against the generated analytic model. Once the analytic model is created, Looker persists it so that subsequent queries reference the existing model directly until its LookML definition is modified.

### `model_source`

The `model_source` parameter specifies the name of the LookML Explore that serves as the topology and relationship source for the analytic model.
    
    
    view: sales_analytic_model {
      derived_analytic_model: {
        model_source: order_items {
          fields: [order_items.id, orders.id, orders.status, users.name]
        }
      }
    }
    

Views that are included in the source Explore must have a primary key that's defined by using [`primary_key: yes`](https://docs.cloud.google.com/looker/docs/reference/param-field-primary-key) on their primary key dimension.

`model_source` accepts the following subparameters:

Parameter | Description  
---|---  
`fields` | Optional. Specifies an allowlist or denylist of fields from the source Explore to export to the analytic model.  
`join` (or `joins`) | Optional. Defines or refines joins from the source Explore specifically for the analytic model.  
  
### `fields`

By default, all available fields from the views in the source Explore are exported to the analytic model (some fields from the source Explore may not be available if the source Explore itself is defined with a [`fields`](https://docs.cloud.google.com/looker/docs/reference/param-explore-fields) parameter). You can use the `fields` subparameter inside `model_source` to specify a subset of fields to export, or to exclude specific fields by using standard LookML list syntax:
    
    
      view: sales_analytic_model {
        derived_analytic_model: {
          model_source: order_items {
            fields: [
              order_items.id,
              order_items.price,
              orders.id,
              orders.status,
              users.name
            ]
          }
        }
      }
    

### `join`

The `join` parameter inside `model_source` lets you add refinements to the joins that are already specified in the source Explore. Adding refinements lets you make adjustments that are scoped exclusively to the analytic model without altering the source Explore definition. 

In the `join` parameter under `model_source`, specify the name of a join from the source Explore with the `+` refinement indicator. For example, `join: +view_name`. Then use the `join` subparameters to refine the join from the source Explore as you need to in your analytic model. See step 2 for an example.

The `join` parameter within `model_source` takes only join refinements. You can't add a new join to the analytic model that doesn't already exist in the source Explore.

The `join` parameter within `model_source` supports the following subparameters:

Subparameter | Description  
---|---  
`foreign_key` | Specifies the foreign key column or dimension that establishes the relationship for the analytic model. For an example with the `foreign_key` parameter, see the example in step 1.  
`relationship` | Defines the join cardinality (`many_to_one`, `one_to_one`, `one_to_many`, or `many_to_many`).  
  
### Setting up a LookML-based derived analytic model

To set up a LookML-based derived analytic model, follow these steps:

  1. Define the base views and source Explore with `foreign_key` joins
  2. Create the derived analytic model view
  3. Define LookML dimensions and measures in the analytic model view
  4. Create an Explore for the analytic model view
  5. Query the analytic model in Looker



#### Step 1: Define the base views and source Explore with `foreign_key` joins

First, ensure that your base views (such as `order_items`, `orders`, and `users`) are defined with primary keys.

Next, define an Explore in your LookML model file that specifies the relationships between the views. Building relationships within an in-database analytic model strictly requires the `foreign_key` parameter on each join in the source Explore:
    
    
    explore: order_items {
      fields: [ALL_FIELDS*]
    
      join: orders {
        relationship: many_to_one
        foreign_key: order_id
      }
    
      join: users {
        relationship: many_to_one
        foreign_key: orders.user_id
      }
    }
    

**Tip:** If your existing Explore joins lack a `foreign_key` parameter, add a join refinement under the `model_source` parameter. The refinement lets you define the `foreign_key` specifically for the analytic model without modifying the base Explore definition. See Step 2 in the following section.

#### Step 2: Create the derived analytic model view

Create a new view file (for example, `sales_analytic_model.view.lkml`) and add a `derived_analytic_model` block with the `model_source` parameter that points to your source Explore:
    
    
    view: sales_analytic_model {
      derived_analytic_model: {
        model_source: order_items {
          # Optional: Use fields to restrict the properties exported to the analytic model
          # fields: [order_items.id, orders.id, orders.status, users.name]
    
          # Optional: Use join refinements to refine the relationships from the source Explore
          # join: +orders {
          #   foreign_key: order_id
          # }
          # join: +users {
          #   foreign_key: orders.user_id
          # }
        }
      }
      ...
    

#### Step 3: Define LookML dimensions and measures in the analytic model view

In the same analytic model view file, define the dimensions, dimension groups, and measures that map to the properties in the generated analytic model so they can be queried in Looker Explores.

Reference fields from the underlying model by using `${TABLE}.<view_name>_<field_name>` (or `${TABLE}.<property_name>`):
    
    
      # Dimensions
      dimension: order_items_id {
        type: number
        sql: ${TABLE}.order_items_id ;;
      }
    
      dimension: orders_id {
        type: number
        sql: ${TABLE}.orders_id ;;
      }
    
      dimension: orders_status {
        type: string
        sql: ${TABLE}.orders_status ;;
      }
    
      dimension_group: orders_created {
        type: time
        timeframes: [raw, time, date, week, month, quarter, year]
        sql: ${TABLE}.orders_created_at ;;
      }
    
      dimension: users_name {
        type: string
        sql: ${TABLE}.users_name ;;
      }
    
      dimension_group: users_created {
        type: time
        timeframes: [raw, time, date, week, month, quarter, year]
        sql: ${TABLE}.users_created_at ;;
      }
    
      # Measures
      measure: count_users {
        type: number
        sql: ${TABLE}.users_count_users ;;
      }
    
      measure: count_orders {
        type: number
        sql: ${TABLE}.orders_count_orders ;;
      }
    
      measure: total_order_amount {
        type: number
        sql: ${TABLE}.orders_total_order_amount ;;
      }
    
      measure: total_order_item_amount {
        type: number
        sql: ${TABLE}.order_items_total_order_item_amount ;;
      }
    }
    

#### Step 4: Create an Explore for the analytic model view

In your model file (such as `sales.model.lkml`), create an Explore for the analytic model view by using the view's name:
    
    
    explore: sales_analytic_model {}
    

An Explore that's based on an analytic model view cannot contain joins, because the relationships are defined internally within the analytic model itself.

#### Step 5: Query the analytic model in Looker

Open the new Explore (for example, **Sales Analytic Model**) in Looker, select dimensions and measures, and run your query.

To inspect the generated SQL, follow these steps:

  1. Click the **SQL** tab in the **Data** panel.
  2. In the **SQL** tab, you can view the database-specific DDL statement that Looker generates (such as `CREATE PROPERTY GRAPH ...` with `NODE TABLES` and `EDGE TABLES` for BigQuery Graph) and the query that executes against the analytic model (such as `FROM GRAPH_EXPAND(...) AS sales_analytic_model`).
  3. When the query executes, Looker persists the analytic model in the database scratch schema. Subsequent queries reuse the persisted model, avoiding DDL re-execution until the LookML definition changes.



### Considerations for LookML-based derived analytic models

When defining LookML-based derived analytic models, keep the following considerations in mind:

  * **Primary keys:** Every view in the source Explore must have a primary key dimension that's defined by using [`primary_key: yes`](https://docs.cloud.google.com/looker/docs/reference/param-field-primary-key).
  * **Acyclic topology:** The relationships that are defined by joins in the source Explore must form a strict acyclic tree structure. Cyclic relationships are not supported.
  * **Source view requirements:** Views that are included in the source Explore must be standard database tables or persistent derived tables (PDTs) with a stable name. Ephemeral (non-persistent) derived tables and views that are based on other analytic models cannot be used as sources.
  * **Explore parameters:** Dynamic runtime filtering parameters (`sql_always_where`, `always_filter`, `access_filter`) and `sql_always_join` on the source Explore are ignored during analytic model generation. 



## Things to consider

When using in-database analytic models, keep the following considerations and limitations in mind:

  * **Data types:** Only the following data types for [dimensions](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types) and [measures](https://docs.cloud.google.com/looker/docs/reference/param-measure-types) are supported with analytic models: 

    * Supported for dimensions and measures: 
      * `string`
      * `number`
      * `date`
      * `yesno`
    * Supported for dimensions only: 
      * `time`
      * `date_time`
  * **Measures:**

    * **Base measures must be predefined:** Base measures must be predefined in the underlying database analytic model. Looker can't define a new base measure by performing an aggregation (such as [`type: sum`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum) or [`type: count`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count)) on a dimension from an analytic model.
    * **Measures that are based on other measures are supported:** You can use the `sql` parameter of a LookML measure to perform non-aggregate computations that use predefined base measures from the analytic model. When you create a measure that's based on other measures, you can't define the new measure as an aggregate measure type such as `sum` or `count`. You must define the new measure as a non-aggregate measure type, such as [`string`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#string), [`number`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#number), [`date`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#date), or [`yesno`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#yesno). See the following example:
          
          measure: average_order_amount {
            type: number
            sql: ROUND(${total_order_amount} / NULLIF(${count_orders}, 0), 2) ;;
          }
          

  * **Joins:** An Explore whose base view is based on an analytic model can't include any joins. Similarly, a view that's based on an analytic model can't be joined into an Explore that has a standard LookML base view.

  * **Implicit joins:** Features that rely on implicit joins aren't supported for analytic models. Some examples of features that rely on implicit joins are [custom calendars](https://docs.cloud.google.com/looker/docs/custom-calendars) and fields that are defined with [`type: location`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location), [`type: distance`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#distance), or [`type: zipcode`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#zipcode). 

  * The following features are not supported with analytic models:

    * [Filtered measures](https://docs.cloud.google.com/looker/docs/reference/param-field-filters)
    * [Aggregate awareness](https://docs.cloud.google.com/looker/docs/aggregate_awareness)
    * [Looker legacy runtime](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#new_lookml_runtime)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
