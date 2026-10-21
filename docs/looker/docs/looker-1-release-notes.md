---
url: https://docs.cloud.google.com/looker/docs/looker-1-release-notes/
title: 1.x Release Notes \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:23:03.322150+00:00
---

# 1.x Release Notes  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-1-release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  1.x Release Notes Stay organized with collections  Save and categorize content based on your preferences. 

## Looker 1.28 2014-03-30

### Dashboards

  * Dashboard filters to provide interactive dashboards ([see documentation](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard))
  * Added "Explore SQL" to go directly to SQL query for dashboard element
  * Limit number of queries that run simultaneously



### Database

  * Redshift timezone support



### Derived Tables

  * `persist_for` works inside of base views ([see documentation](https://docs.cloud.google.com/looker/docs/derived-tables#persist_for))



### Model Development

  * Leaving Developer Mode experience was improved to avoid 404 pages
  * Added "check all" to select all files during the git comm list of files in Git commits



## Looker 1.26 2014-03-05

### Dashboards

  * Single-value dashboard elements are now drillable
  * Dashboards can reference multiple models (e.g., 2+ connections powering one dashboard)



### Model Development

  * Keyboard shortcut help added to editor
  * "Revert All" now deletes untracked files



### Derived Tables

  * Introducing [compound derived tables](https://docs.cloud.google.com/looker/docs/derived-tables)



### Admin & Setup

  * Public URL alert: Message is displayed on public URLs if your instance is using a self-signed SSL certificate.
  * Add User alert: When adding a user with a domain that has not been previously used, a warning alerts you that you are adding an email address from a foreign domain.
  * Database Connections: Ability to add parameters to the JDBC connection string



## Looker 1.24 2014-02-09

### Looks

  * Fixed email attachments consistently in Outlook for scheduled Looks



### Model Development

  * File list now shows model name for the include files



### Admin & Setup

  * Added international timezone support



## Looker 1.22 2014-01-12

### Persistent Derived Tables

  * [Using Persistent Derived Tables](https://docs.cloud.google.com/looker/docs/derived-tables)
  * [Reference: Persistent Derived Tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_tables_\(pdts\))
  * [Reference: Derivation Design Patterns](https://docs.cloud.google.com/looker/docs/derived-tables)
  * [Temp Schema and Database Setup](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#temp_database)



## Looker 1.20 2013-11-29

### Explore (Query Builder)

  * Sort fields in sidebar by label instead of name
  * Generate field grouping by scope instead of by view name
  * Model errors displayed on initial page load instead of after query is run



### Dashboard

  * Added Explore Data link on the dashboard pulldown menu to access the query
  * Added `show_points` parameter for line charts



### LookML

  * Support for Month-over-Month totals (percent of total and percent of previous). [See the documentation](https://docs.cloud.google.com/looker/docs/table-calculations) for the new syntax
  * Added `one_to_one` as a join option; allowing you to bring in measures on a join for one-to-one relationships on a join. [See the documentation](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-relationship) for the new syntax.



### Model Development

  * Changes to browser tab behavior: If model file is open in a browser tab, `go to definition` goes to the opened tab
  * Generator improvements 
    * Selective generation and regeneration of models
    * Improved ID field recognition
  * Improved Git user interface to indicate current state of the developer mode
  * Error messages now shown on `save` for parse errors
  * SQL Runner now generates LookML for the query
  * Added option to reset developer directory to match production model files (accessed on Account page)



### Database

  * Improved MSSQL, Aster and Vertica SQL Runner and Model Generator
  * Improved diagnostics for failed database connections
  * Fixex year filter bug on Redshift
  * Added Redshift support for derived tables
  * Added support for SAP Hana



### Admin

  * Added usage panel to view Looker product usage across the installation
  * All Public Look URLs are now viewable by admins



## Looker 1.18 2013-10-06

### Dashboards

  * Beta release of dashboards
  * [How to Build Dashboards](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards) and [Reference for Dashboards](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard)



### LookML Changes

  * Improved counts



### Administration Changes

  * Automatic Developer Model directory setup
  * Add users now provides list of models for access permissioning



### Model Development Changes

  * Model file list is simplified and files can now be added, deleted, and renamed
  * Updated LookML Editor, with improved search, smarter file status messages, and improved syntax highlighting
  * Generator and SQL Runner moved to Model section
  * Generator optimizations including improvements for Redshift



### Database Changes

  * Connections page now actively runs tests and shows detailed analysis of connections
  * SSL support for Redshift



## Looker 1.16.5 2013-08-05

### Introducing Looks

  * `Bookmarks` have been renamed to `Looks` with an updated visual layout for Looks
  * Additional subscription frequency intervals have been added



### Updated Support Docs

  * Support Docs link available for all users
  * New docs added for Using Looker and Developing in Looker
  * Docs are now searchable



### Navigation and User Interface Changes

  * Added `clear` query button
  * Query builder icon changes
  * User avatars with [gravatar](https://en.gravatar.com/) support
  * Mobile layout improvements



### LookML Changes

  * Better Joins: LookML now has a better way to write joins. [See the documentation](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) for the new syntax.
  * Aliasing Tables: Introduction of `sql_table_name` to handle table names with spaces and table prefixes. [See the documentation](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name) for the new syntax.
  * New field attributes: `hidden: true` and `deprecated: true`. Both hidden and deprecated fields don't show in the Looker Explorer but will show results. Deprecated fields show a warning that the field has been deprecated. These flags keep queries with old fields working but discourages people from using them.



### Administration Changes

  * Log File rotation; internal rotation can be set to daily, weekly or monthly. If an external log rotator is being used, set to "Never" and send USR2 signal to the Looker process to trigger reopening of log file.
  * In-App End User License Agreement (EULA) verification process. Post update, the first user to log in to the system will be prompted to agree to the EULA.
  * SQL Runner improvements
  * Allow user to change account email



### Database Changes

  * Added dialects for BitYota, Vertica, Vectorwise
  * MS SQL dialect improvements
  * Redshift performance improvements



## Looker 1.12.10 2013-03-30

### Navigation and User Interface Changes

  * Keyboard shortcuts added for `Run Last Query` (control+shift+L) and `Enter Developer Mode` (control+shift+D)
  * `Run Last Query` added to user drop-down menu
  * `Return to Last Query` always shows on model pages
  * `History` moved to user drop-down menu
  * `Chat` functionality now activated by clicking on Chat icon in top navigation menu
  * `Support Site` link takes you to documentation from the ? icon in top navigation menu
  * Improved layout and fixed navigation bugs for mobile devices
  * Added navigation on Bookmarks page to more easily view another user's bookmarks
  * New column header drop-down to allow for easy access to filter on column, pivot/unpivot column and go to field definition from the column header drop-down.



### Query Builder

  * Expanded clickable area for hiding/showing sidebar
  * Added alert and prompt to re-run query when changes are made
  * Query results restricted to 3000 unless exporting
  * Implemented reasonable default sort order when no sort is specified



### LookML Changes

  * Changes to default filters syntax with the addition of `Conditionally Filter` [(see revised documentation)](https://docs.cloud.google.com/looker/docs/reference/param-explore-conditionally-filter)
  * Support for 'from' in the base view



### Miscellaneous

  * Epoch Hours: display in the form 'YYYY-MM-DD HH' so they filter properly when clicked on
  * Database connections: allow max connections to be set for each database connection
  * Database connections: added SSL option



## Looker 1.11.30 2013-03-05

  * New look and feel for the interface with usability improvements
  * Redesigned query interface
  * Git integration in the interface (eliminating the need to SSH to deploy changes) [(see revised documentation)](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode)
  * Database support for Redshift



## Looker 1.11.23 2013-02-19

### Product Updates

  * Improved SSL security
  * Automatic reconnection to Postgres databases
  * Generator now supports model generation for a single table
  * Improved handling and display of ERB errors
  * Option when adding new users to make them administrators
  * Filter help in new query interface



### LookML Language Updates

  * "yesno" supported as a timeframe
  * "datatype" attribute for timeframe fields; specifies underlying database field type (epoch, timestamp, datetime, date)



## Looker 1.11.13 2012-12-21

### Improved History Log

History is displayed in a more readable format. Queries display the parameters for view, fields and sort instead of an unreadable English sentence.

### Date Filters Allow NULL Values

NULL, NOT NULL and -NULL are all allowed in date filters.

### Error Handling

Improved error handling in Looker Development Mode to catch incorrectly named parameters and statements.

### Field Scoping

Added '- scoping: true' for language simplifications. With 'scoping: true', all field names and set names are scoped to the view. Set names and field names without a '.' in them are assumed scoped to the view. The full name for a set or a field always contains a '.'. For example the fields full name below would be named 'foo.bar' but can be referenced as 'bar' inside the view:

#### After (scoping: true)
    
    
    - view: foo
      fields:
        - dimension: bar
    

#### Before (without scoping)
    
    
    - view: foo
      fields:
        - name: foo_bar
    

  * Models that don't have 'scoping: true' continue to function as they always have
  * The generator now generates scoped models



### Derived Table Support

Views can be built on sub queries (derived tables). This is great for building up facts about entities. Derived tables are constructed before the main query runs. In mySQL, to use this feature, you will need write access to a database named "TMP", even though Looker never writes to this database. Looker only uses 'CREATE TEMPORARY TABLE TMP'.

#### Derived Table Example
    
    
    - base_view: orders
      view: orders
    
    - view: orders
      fields:
      - dimension: amount
        type: number
      - dimension: total_amount
        type: sum
        sql: ${amount}
      - join: users
        sql_on: orders.user_id=users.id
        base_only: true
      - join: user_orders_facts
        sql_on: orders.user_id=user_orders_facts.user_id
        base_only: true
    
    - view: users
      fields:
      - dimension: name
    
    - view: user_orders_facts
       derived_table:
         sql: |
            SELECT
                users.id as user_id
                , COUNT(*) as lifetime_orders
                , MAX(orders.date) as most_recent_purchase_date
            FROM orders
            GROUP BY user.id
         indexes: [user_id]
       fields:
       - dimension: lifetime_orders
         type: number
       - dimension: most_recent_order
         type: time
         timeframes: [date, week, month, year]
         sql: $$.most_recent_purchase_date
    

### Database Support Improvements

  * Postgres reserved words are now quoted when creating models
  * MSSQL is now a supported SQL dialect



## Looker 1.10.13 2012-11-06

### In-app support chat

Admins will now see 'Chat with Looker Eng' box in the bottom-right corner. Now it's even easier to access the Looker engineering team to help you solve questions big and small. If you get stuck, grab us on Looker chat. We're here to help.

### Non-admin users can view the LookML model

All Looker users now have the opportunity to inspect the underlying LookML model through the "view" link beside each field, or from the Models link in the header.

### Terminology Updates

We've standardized on some new terminology for Looker:

  * LookML - The Looker language, based on YAML, that enables the definition of a logical business model for a given database connection.
  * Field - Represents a piece of data, either directly from a column in a database or calculated from one or more columns in a database. Defined in LookML.
  * Dimension - A field that is used to bucket results in a query into distinct groups.
  * Measure - A field that is used to aggregate data across rows in a database.
  * Query - The execution of a SQL statement based on selected fields and dimensions in a given view.
  * View - A collection of fields and joins that describe a business entity (user, order, etc). Written in LookML. Formerly labeled Query in the header.
  * Model - A collection of views and associated meta-data that describe a business's logical model. Formerly labeled Dictionary in the header.
  * With these changes also come some updates to the header in the Looker web UI. Dictionary and Query have now been collapsed into a single Explore drop-down. There is now a Models link in the header (described above).



### Mail Subscription Updates

Mail subscriptions can now be created with custom start & repeat times. You can also add additional subscribers that will be CC'ed on the mail, either inside or outside of your organization. People that are mailed outside of the organization can be managed via the Manage Outsiders section of the Admin panel.

As always, we welcome feedback and suggestions!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
