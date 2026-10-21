---
url: https://docs.cloud.google.com/looker/docs/glossary/
title: Glossary \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:16.619313+00:00
---

# Glossary  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/glossary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Glossary Stay organized with collections  Save and categorize content based on your preferences. 

This page lists terms that are used in the Looker product and user documentation.

See the [Looker and Data Studio shared terms and concepts](https://docs.cloud.google.com/looker/docs/looker-and-studio-shared-terms-glossary) documentation page for information about the nuances between similar terms and concepts in Looker and Data Studio.

## Symbol/Numeric

`$`
    

[$](https://docs.cloud.google.com/looker/docs/sql-and-referring-to-lookml#substitution_operator_\($\)) is a substitution operator that lets you reference previously defined objects in LookML.

_see also_ **substitution operator**

## A

access, access level
    

Admins have a variety of [options](https://docs.cloud.google.com/looker/docs/admin-panel-users-content-access) for limiting what users can view and interact with in Looker.

_see also_ **content access**, **data access**, **feature access**

action
    

A [data action](https://docs.cloud.google.com/looker/docs/reference/param-field-action) lets users perform tasks in other tools, directly from Looker. For example, the action can cause an email to be sent or can set values in other applications — or it can do anything else that you can configure a receiving server to do. The receiving server must be able to accept a JSON POST.

Action Hub
    

Looker's [Action Hub](https://docs.cloud.google.com/looker/docs/action-hub) is a multi-tenant service that forwards data to Looker's integrated services. Any data your users send using an action will be processed temporarily on the Action Hub server rather than in your Looker instance. When your Looker admin or developer has set up an integrated service and a field tag to provide access to that service, you can select that service as an action when you drill into data and interact with that service. The Looker documentation often uses "action" and "integration" interchangeably.

advanced deploy mode
    

[Advanced deploy mode](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode) lets Looker developers with [`deploy` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#deploy) select any Git commit on their LookML project and deploy it to the production version of their Looker instance. This is opposed to the default Git integration, where only the latest commit on the remote production branch can be deployed to the production version of a Looker instance.

advanced filter
    

An [advanced filter](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#advanced_filters) lets users create a dashboard filter with a field from an [Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) that isn't represented on the dashboard itself.

advanced filter control
    

An [advanced filter control](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#using_advanced_controls) is a type of dashboard filter control that provides some additional flexibility in the filter conditions dashboard creators can set up. To create an advanced control, select **Advanced** in the **Control** field in the [filter configuration window](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#customizing_filter_configuration).

alert
    

[Alerts](https://docs.cloud.google.com/looker/docs/alerts-overview) enable users to specify conditions in the data of a dashboard tile that, when met or exceeded, trigger a notification to be sent at a selected frequency to specific recipients. Alerts are set on query-based or Look-linked tiles on user-defined dashboards or LookML dashboards; and they can be sent through email or with Looker's Slack or Slack Attachment (API Token) integrations.

Application Time Zone
    

[Application Time Zone](https://docs.cloud.google.com/looker/docs/using-time-zone-settings#application_time_zone) is an admin setting for the default time zone in which scheduled Looks and queries run, where supported. When User Specific Time Zones are enabled, the Application Time Zone becomes the default time zone for users who don't have a time zone value set for their accounts.

_see also_ **time zone settings**, **User Specific Time Zones**

asynchronous query
    

An asynchronous (or async) query is a data request that makes one call to start the request, one or more calls to check the completion status of the query, and one call to fetch the results of the completed query. Async queries can help avoid freezing apps, connection timeouts and long dashboard load times.

## B

base view (of an Explore)
    

A base view is the [view](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#view) used as the starting point for building an [Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores). From there, you can [join](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) other views into the base view to be used in the Explore. Typically, Explores are named after the base view, but you can also use the [`from`](https://docs.cloud.google.com/looker/docs/reference/param-explore-from) parameter to name the Explore's base view if you don't want to name the Explore after its base view.

_see also_ **view**, **Explore**

block, Looker Block
    

[Looker Blocks](https://docs.cloud.google.com/looker/docs/blocks) are prebuilt pieces of LookML that you can use and customize to your exact specification. From optimized SQL patterns to fully built-out data models, blocks can be used as a starting point for quick and flexible data modeling in Looker.

board
    

A [board](https://docs.cloud.google.com/looker/docs/presenting-content) holds a collection of manually curated dashboards, Looks, and links. Dashboards and Looks, which are stored in [folders](https://docs.cloud.google.com/looker/docs/organizing-spaces), can be pinned to multiple boards. Boards may include links and descriptions to provide context and can make it easier for users to find the information that is most relevant to them.

browse, browsing
    

[Browsing](https://docs.cloud.google.com/looker/docs/find-and-organize-content) involves viewing, sharing, sending, and downloading data from dashboards, Looks, and Explores.

## C

certified content
    

[Certified content](https://docs.cloud.google.com/looker/docs/content-certification) is a dashboard, Look, or self-service Explore that has been vetted as reliable data on your Looker instance by a user with the [`certify_content`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#certify_content) permission.

CI
    

_see_ **Continuous Integration**

closed system
    

Also called a multitenant installation, [a closed system](https://docs.cloud.google.com/looker/docs/access-levels#open_and_closed_systems_of_access_to_folders) silos content to specific groups and prevents users from different groups from knowing about each other.

code splitting
    

A technique for lazy loading of JavaScript until it is actually needed. Ideally, you want to keep the initially loaded JavaScript bundle as small as possible. This can be achieved by utilizing code splitting. Any functionality that isn't immediately required isn't loaded until it's actually needed.

Community
    

Formerly known as Discourse, the [Looker Community](https://discuss.google.dev/c/looker/19) is a user forum featuring posts, discussions, questions, and ideas shared among Looker users and experts.

component
    

Looker components are the technical implementation of the Looker Design System, built with React, TypeScript, and Styled Components. They consist of [UI components](https://looker-open-source.github.io/components/latest), [filter components](https://docs.cloud.google.com/looker/docs/components-filter), and [visualization components](https://docs.cloud.google.com/looker/docs/components-vis).

connection
    

In the **Admin** section of Looker, you establish the [database connection](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) from which a model will retrieve data.

constant
    

Constants, which are defined with the LookML [`constant`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-constant) parameter in a project manifest file, let you specify a value that can be reused throughout a project. You can reference constants anywhere in your model where strings are accepted.

content
    

In Looker's documentation, the term [**content**](https://docs.cloud.google.com/looker/docs/finding-content) typically refers to Looks and dashboards.

content access
    

[Content access](https://docs.cloud.google.com/looker/docs/admin-panel-users-content-access) controls whether a user or group can view or make changes to a board, or to a folder (called a Space prior to Looker 6.20) and its contents. The two content access levels are **View** and **Manage Access, Edit**.

Content Validator
    

Looker's [Content Validator](https://docs.cloud.google.com/looker/docs/content-validation) searches your LookML for references to model, Explore, and field names. Developers can use the Content Validator after making changes to a project to check that their changes did not impact any of their users' saved Looks or query-based dashboard tiles. The Content Validator can also be used to find and replace LookML elements to fix errors due to changes.

Continuous Integration
    

The Looker [Continuous Integration (CI)](https://docs.cloud.google.com/looker/docs/continuous-integration) features let you run tests on your LookML project to deliver more reliable, efficient, and user-friendly data experiences. You can use the CI validators to catch issues with [SQL](https://docs.cloud.google.com/looker/docs/ci-sql-validator), [data tests](https://docs.cloud.google.com/looker/docs/ci-assert-validator), [content](https://docs.cloud.google.com/looker/docs/ci-content-validator), and [LookML](https://docs.cloud.google.com/looker/docs/ci-lookml-validator) before they hit production to verify your LookML and prevent query errors for your users. You can also configure the CI validators to [run automatically](https://docs.cloud.google.com/looker/docs/ci-create-suite#triggers) when a pull request is submitted to your LookML repository.

cross-filtering
    

[Cross-filtering](https://docs.cloud.google.com/looker/docs/cross-filtering-dashboards) lets users apply ad hoc filters to dashboards. With cross-filtering, users can click a data point in one dashboard tile to have all dashboard tiles automatically filter on that value. Specific cross-filters cannot be saved to a dashboard, but they can be shared by sharing a cross-filtered dashboard's URL.

customer-hosted (deployment, instance, installation, environment)
    

A "customer-hosted" deployment — also referred to as "self-hosted" or "on-prem" throughout this documentation — means that the product is [installed](https://docs.cloud.google.com/looker/docs/customer-hosted-installation-steps) by or for the customer at the customer's premises or on a customer-controlled server within a third-party data center. A customer-hosted deployment includes the in-product services, meaning the services that are hosted by Looker and accessible through the product, specifically licensing data, configuration backups, system error reports, data actions, and support tickets, as further described in the **Application Data Shared by Looker** section of [Looker's security webpage.](https://looker.com/product/security) Looker support generally has no access to these instances for support or deployment purposes, and the customer must execute their own version updates.

To learn more about the comparative advantages of each hosting option, see the [Choosing a hosting option for a Looker (original) instance](https://docs.cloud.google.com/looker/docs/choosing-hosting-option) documentation page.

All Looker (Google Cloud core) instances are Looker hosted.

_see also_ **Looker-hosted**

## D

dashboard
    

A [dashboard](https://docs.cloud.google.com/looker/docs/viewing-dashboards) is essentially a collection of one or more saved queries, displayed as visualization or text tiles together on one page.

_see also_ **LookML dashboard**, **user-defined dashboard**

dashboard element, element
    

An element is a tile or visualization on a LookML dashboard, created using the [`element`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-element) parameter.

dashboard file
    

A LookML dashboard is defined in a LookML project [file](https://docs.cloud.google.com/looker/docs/other-project-files#dashboard_files) with the extension `.dashboard.lookml`.

_see also_ **LookML dashboard**

data access
    

[Data access](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management) controls which data a user or group is allowed to view. This type of access can be restricted or granted either at the user level or at the data level. 

Database Time Zone
    

[Database Time Zone](https://docs.cloud.google.com/looker/docs/using-time-zone-settings#database_time_zone) is an admin setting for the time zone Looker uses to interpret your raw data.

_see also_ **Query Time Zone**, **time zone settings**

datagroup
    

You can use one or more [datagroup](https://docs.cloud.google.com/looker/docs/admin-panel-database-datagroups) [parameters](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup) to define a [caching policy](https://docs.cloud.google.com/looker/docs/caching-and-datagroups), to specify when to rebuild persistent derived tables (PDTs), and to trigger schedules.

derived table
    

[Derived tables](https://docs.cloud.google.com/looker/docs/derived-tables) let you create new tables that don't already exist in your database. A derived table is defined in a Looker view file and lets the user treat the output of a query as if it were a table in the database (typically used for "fact" tables). "Derived table" is a generic term for any type of derived table, including [LookML-based (native) derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#native_derived_tables), [SQL-based derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#sql-based_derived_tables), [temporary derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#temporary_derived_tables), and [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table).

_see also_ **native derived table**, **persistent derived table**, **SQL-based derived table**, **temporary derived table**

Development Mode
    

A developer can enter [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#development_mode) to make and test LookML changes. The changes won't affect other users until they are deployed to production.

development table
    

A development table is a [persisted derived table](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table) that is [built when you query the table during development](https://docs.cloud.google.com/looker/docs/derived-tables#persisted_tables_in_development_mode). In some cases, the development table can be [used in production when you deploy your changes](https://docs.cloud.google.com/looker/docs/derived-tables#how_long_are_development_tables_persisted).

dialect
    

The SQL "flavor" of a database. Examples of supported [dialects](https://docs.cloud.google.com/looker/docs/dialects) are Amazon Redshift, PostgreSQL, MySQL, and Google BigQuery Standard SQL or Legacy SQL.

dimension
    

A dimension is a field that represents an [attribute, fact, or value](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores), which can be selected from the field picker within an Explore and can be used to filter a query. Common dimensions include such attributes as dates, names, and IDs, and often correspond to columns in your underlying data table. A dimension can also be [created within a view file](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#dimension_and_measure_fields).

dimension fill
    

Dimension fill is a feature that lets you instruct Looker to [fill in missing dates or values](https://docs.cloud.google.com/looker/docs/creating-visualizations#filling_in_missing_dates_and_values) for a given dimension, such as a **date** dimension with some years missing. You can avoid misleading graphs by preventing Looker from connecting the values in an incomplete set. The dimension fill option can be turned on or off with the [`allow_fill`](https://docs.cloud.google.com/looker/docs/reference/param-field-allow-fill) parameter.

dimension group
    

Using a [dimension group](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group), you can create multiple dimensions for a single underlying date or time column in the database. For example, you could split a `duration`-type dimension group into intervals of days, weeks, months, or other durations.

drill
    

Looker makes it possible to [drill](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#drilling_down_into_the_data) into the data on a visualization or an Explore to get more specific information about a specific data point. To drill into data on a visualization, select the part of the visualization about which you'd like more information. For the **Data** section of an Explore, select the value of a measure, or select the value of a dimension that can be drilled into.

## E

embed, embedding
    

[Embedding](https://docs.cloud.google.com/looker/docs/publishing-looks-with-public-urls#public_embedding_with_iframe_tags) involves using `iframe` code to place an object (for example, Looker charts or tables) into a website, a spreadsheet, or another location outside of Looker. An embed user is a user who is interacting with a Looker object that is embedded in a location outside of Looker. Embedded content can be public or private (requiring either a [Looker login](https://docs.cloud.google.com/looker/docs/private-embedding) or a [signed URL](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding)).

Embed edition
    

An [**Embed** edition](https://docs.cloud.google.com/looker/docs/looker-core-overview#editions) is a Looker (Google Cloud core) edition type that includes all the features of the **Enterprise** edition as well as offering [signed embedding](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding); a [private label](https://docs.cloud.google.com/looker/docs/privatelabel) option; [custom themes](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores); 500,000 Query API calls per month; and 100,000 Admin API calls per month.

Enterprise edition
    

An [**Enterprise** edition](https://docs.cloud.google.com/looker/docs/looker-core-overview#editions) is a Looker (Google Cloud core) edition type that includes all the features of the **Standard** edition, supports unlimited users, includes additional security features such as [VPC-SC](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc) and [Private connections](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip), and provides more robust monitoring through the [Elite System Activity](https://docs.cloud.google.com/looker/docs/elite-system-activity) feature.

entitlement
    

[Entitlements](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#entitlements) define the Looker resources that a [Looker extension](https://docs.cloud.google.com/looker/docs/extension-framework) can access. The extension won't be able to access a Looker resource unless that resource is listed in the entitlements. Entitlements are defined as part of an [`application` parameter](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application) included in a [LookML project manifest file](https://docs.cloud.google.com/looker/docs/other-project-files#project_manifest_files).

ephemeral derived table
    

An ephemeral derived table — more commonly called a [temporary derived table](https://docs.cloud.google.com/looker/docs/derived-tables#temporary_derived_tables) — is a derived table that isn't written to your database. A temporary derived table can be either a [LookML-based (native) derived table](https://docs.cloud.google.com/looker/docs/derived-tables#native_derived_tables) or an [ SQL-based derived table](https://docs.cloud.google.com/looker/docs/derived-tables#sql-based_derived_tables).

_see also_ **derived table**, **temporary derived table**

Explore (_n._)
    

An [Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) is the starting point for queries. An Explore shows a specified set of fields from its associated view file, and these fields can be selected from the field picker to construct a query, which can be saved as a Look or dashboard tile. Explore URLs can also be shared.

explore, exploring (_v._)
    

[Exploring](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) involves using data to answer questions in Looker.

Explore file
    

An Explore file is a LookML project [file](https://docs.cloud.google.com/looker/docs/other-project-files#explore_files) with the extension `.explore.lkml`. Can be used for extending Explores across models and for defining native derived tables.

`explore` parameter
    

The [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) parameter adds a view to Looker's menu of Explores. As a best practice, an Explore should be defined inside of a model file. Explores reference views and each Explore can contain joins to other views. An Explore can also be defined in an Explore file that is then included in a model file.

_see also_ **Explore file**

extension
    

Extensions are web applications built with Looker components that are developed through the **Looker extension framework**. Some extensions, like the **Looker Data Dictionary**, are deployed through the Looker Marketplace and are available for all customers. See the [extension-examples repository](https://github.com/looker-open-source/extension-examples) for examples. Some parts of the Looker UI refer to extensions as "applications." 

_see also_ **Looker Data Dictionary,** **Looker extension framework**

## F

fanout (_n._), fan out (_v._)
    

A [fanout](https://discuss.google.dev/t/the-problem-of-sql-fanouts/119220) occurs when one row of a primary data table can correspond to more than one row of a joined table, resulting in duplicated records and incorrectly calculated aggregations. In Looker, the fanout problem is avoided through the use of symmetric aggregates and by correctly defining the dataset's primary key.

feature access
    

[Feature access](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management#controlling_feature_and_data_access) controls the types of actions a user is allowed to take in Looker. This type of access is managed by permission sets.

field
    

Explores and views contain [fields](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#explores_are_the_starting_point_for_exploration), mostly dimensions and measures, which are the fundamental building blocks for Looker queries.

field picker
    

The [field picker](https://docs.cloud.google.com/looker/docs/changing-explore-menu-and-field-picker#field_picker) displays the dimensions and measure applicable to the data shown in an Explore. The Looker developer or admin configures these dimension and measure options. The field picker may also display filter-only fields.

filter component
    

[Filter components](https://docs.cloud.google.com/looker/docs/components-filter) are React-based, prebuilt pieces of Looker's application that can provide Looker's filter functionality for custom-built data applications and customized embedded Looker dashboards.

filter expression
    

[Filter expressions](https://docs.cloud.google.com/looker/docs/filter-expressions) are an advanced way to filter Looker queries. You can use them in the Explore section of Looker by adding a filter and choosing the **matches (advanced)** option. They are also used in LookML for elements that take a `filter` parameter. You can write filter expressions to filter on a string or to partially match strings, date and time, Boolean values, numbers, and location fields.

folder
    

  1. In the Looker UI, a folder is a [place](https://docs.cloud.google.com/looker/docs/organizing-spaces) where dashboards, Looks, and other folders (subfolders) are stored. Each user has a personal folder, and a Looker instance can also have various kinds of shared folders. Access to content in Looker is allocated at the folder level. Folders were called "Spaces" prior to Looker 6.20.
  2. In the Looker IDE, a folder is an [organizational structure](https://docs.cloud.google.com/looker/docs/ide-folders) for your LookML files.


function
    

[Looker functions](https://docs.cloud.google.com/looker/docs/functions-and-operators) let you transform your data or reference data in complex ways. They are similar in nature to Excel functions.

## G

golden query
    

_see_ **verified query**

group, user group
    

Users can be added to one or more [groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups). Groups are useful for managing users' access to particular data, features, and content within Looker, as well as for assigning roles to users in bulk.

## H

hybrid networking
    

Networking that occurs between Google Cloud and on-premises or other cloud provider environments. For a summary of hybrid networking connection options, visit the [Network segmentation and connectivity for distributed applications in Cross-Cloud Network](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/connectivity#private-connections-to-on-premises-data-centers) documentation page.

## I

IDE
    

Integrated development environment. Looker's [internal LookML editor](https://docs.cloud.google.com/looker/docs/looker-ide), or an editor used to create and modify an [extension](https://docs.cloud.google.com/looker/docs/extension-framework). Examples of the latter are Visual Studio Code, Intellij, and WebStorm.

inbound traffic
    

In networking, inbound traffic, also called northbound traffic, is traffic from a lower-level network component to a higher-level network component. In the context of Looker (Google Cloud core), inbound traffic is, for example, traffic from a client to a Looker (Google Cloud core) instance that allows users to access a Looker (Google Cloud core) instance.

incremental persistent derived table
    

An [incremental persistent derived table](https://docs.cloud.google.com/looker/docs/incremental-pdts) is a type of [persistent derived table (PDT)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table) that is built incrementally, meaning that Looker appends fresh data to the table in specified increments, instead of rebuilding the entire table. This can lead to faster build times for your PDTs and less strain on your database. The increment is defined using the [`increment_key`](https://docs.cloud.google.com/looker/docs/reference/param-view-increment-key) parameter. Incremental PDTs can be [LookML-based (native) derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#native_derived_tables), [SQL-based derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#sql-based_derived_tables), or [aggregate tables](https://docs.cloud.google.com/looker/docs/aggregate_awareness#adding_aggregate_tables_to_your_project).

_see also_ **persistent derived table**

instance
    

The server (or cluster of servers) that hosts Looker. Each client uses a production server (and, potentially, a staging server).

## J

join
    

  * **(_n._)** The [`join` parameter](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) lets you define the join relationship between an Explore and a view, so that you can [combine data from multiple views](https://docs.cloud.google.com/looker/docs/working-with-joins). You can join in as many views as you like for any given Explore.
  * **(_v._)** Combine data from multiple views by defining the relationship between an Explore and a view through a [`join` parameter](https://docs.cloud.google.com/looker/docs/reference/param-join).



## L

Labs feature
    

Labs features are a subcategory of [preview features](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features). They may be removed from the product at any time, without extended notice. Feature issues may or may not be resolved. These experimental features are intended to show you functionality that could be incorporated into Looker in the future and to get your feedback. Labs features are available only in Looker (original).

_see also_ **preview feature**

legacy feature
    

Some product features have a [**legacy feature**](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule) option that allows for the continued use of the legacy feature for a period of time (which may be useful for developing and implementing a migration plan). The **Admin** section of Looker lists the features for which the legacy feature option can be turned on.

Lexp
    

_see also_ **Looker expression**

Liquid parameter
    

In Looker, a Liquid parameter is a LookML parameter field that has been created using [elements of the Liquid templating language](https://docs.cloud.google.com/looker/docs/liquid-variable-reference).

Liquid variable
    

A Liquid variable is an [element of the Liquid templating language](https://docs.cloud.google.com/looker/docs/liquid-variable-reference) that can be used with LookML to create dynamic content.

Look (_n._)
    

A [Look](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks) is a single query table or visualization that is saved. Looks can be added to dashboards, scheduled, shared, and made public. Any changes made to a Look will be reflected in any dashboards that contain it.

Looker-hosted
    

When Looker hosts your deployment, Looker manages all necessary IT functions that are related to the Looker application on your behalf, based on resource utilization and business requirements, greatly reducing the effort required to install, configure, and maintain the Looker application. To learn more about the comparative advantages of each hosting option, see the [Choosing a hosting option for a Looker (original) instance](https://docs.cloud.google.com/looker/docs/choosing-hosting-option) documentation page.

All Looker (Google Cloud core) instances are Looker hosted.

_see also_ **customer-hosted**

Looker API
    

The [Looker API](https://docs.cloud.google.com/looker/docs/api-intro) is a secure, "RESTful" application programming interface for managing your Looker instance and fetching data through the Looker data platform. You can write applications or automation scripts to provision new Looker user accounts, run queries, schedule data deliveries, etc. Just about anything you can do in the Looker application you can do through the Looker API.

Looker Cloud
    

**Looker Cloud** means the product is installed and provisioned to a customer on a web-connected platform that is run in a third-party hosting facility designated by Looker. For more information, see the **Cloud Security Architecture** section of [Looker's security webpage](https://looker.com/product/security).

Looker connector
    

The **Looker connector** is an [integration between Looker and Data Studio](https://support.google.com/looker-studio/answer/12388266) that lets you access data from your Looker Explores within Data Studio by adding an Explore as a [data source](https://support.google.com/looker-studio/answer/6302399) in a Data Studio [report](https://support.google.com/looker-studio/answer/6302400).

Looker Data Dictionary
    

The [Looker Data Dictionary](https://docs.cloud.google.com/looker/docs/using-looker-data-dictionary) is an extension — a web application built using Looker components — developed using the [Looker extension framework](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework) and deployed through the [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace). The Looker Data Dictionary extension provides a dedicated, centralized interface for searching through all Looker fields and descriptions in an Explore. To use the Looker Data Dictionary, Looker admins must enable the [Extension Framework](https://docs.cloud.google.com/looker/docs/admin-panel-platform-extension-framework) and [Marketplace](https://docs.cloud.google.com/looker/docs/admin-panel-platform-marketplace) features.

_see also_ **extension,** **Looker extension framework**

Looker expression
    

Table calculations, custom fields, and custom filters rely on [Looker expressions](https://docs.cloud.google.com/looker/docs/creating-looker-expressions) (Lexp) to perform calculations. A Looker expression is built from a combination of functions, operators, and fields, and possibly constants or variables.

Looker extension framework
    

The [Looker extension framework](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework) is a development framework that significantly reduces the effort and complexity of building custom JavaScript data applications and tools. To use the Looker extension framework, Looker admins must enable the [Extension Framework](https://docs.cloud.google.com/looker/docs/admin-panel-platform-extension-framework) feature.

_see also_ **extension**

Looker (Google Cloud core)
    

[Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances are Looker instances with deeper Google Cloud integration, including the ability to provision and administer instances from the [Google Cloud console](https://docs.cloud.google.com/cloud-console).

Looker Marketplace
    

The [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace) is a central location for finding, deploying, and managing many types of Looker content, such as Looker Blocks (or "Models"), applications (or "extensions"), and visualizations (or "Plug-ins"). The Looker Marketplace can be accessed directly from a Looker instance or from `marketplace.looker.com`. The `marketplace.looker.com` director also lists the actions (or integrations) that are available from the Looker Action Hub.

Looker (original)
    

Looker (original) instances are Looker instances that aren't provisioned by the Google Cloud console, in contrast with Looker (Google Cloud core) instances. Usually, these instances are referred to as _Looker_ instances. 

LookML
    

[LookML](https://docs.cloud.google.com/looker/docs/what-is-lookml) is a language for describing dimensions, aggregates, calculations and data relationships in a SQL database. The Looker app uses a model written in LookML to construct SQL queries against a particular database.

LookML-based derived table
    

More often referred to as [native derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#native_derived_tables), a LookML-based derived table is a [derived table](https://docs.cloud.google.com/looker/docs/derived-tables) whose query is defined in LookML terms, referring to LookML dimensions and measures in your model. Native derived tables can be [temporary](https://docs.cloud.google.com/looker/docs/derived-tables#temporary_derived_tables) or [persistent](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table).

_see also_ **derived table**, **persistent native derived table**, **temporary derived table**

LookML dashboard
    

A LookML dashboard is [written entirely using LookML](https://docs.cloud.google.com/looker/docs/reference/lookml-dashboard-overview) (as opposed to a user-defined dashboard, which is created by using the visualization editor).

_see also_ **user-defined dashboard**

LookML Diagram
    

The LookML Diagram is an entity relationship diagram of a LookML model that visually depicts relationships between its [LookML objects](https://docs.cloud.google.com/looker/docs/glossary#lookml-object). It is an extension — a web application built using Looker components — developed using the Looker [extension framework](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework) and deployed through the [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace).

_see also_ **extension**, **Looker extension framework**, **Looker Marketplace**, **LookML object**

LookML object
    

LookML objects are the models, Explores, views, and fields that have been defined, in LookML, in a project, including [files imported from another project](https://docs.cloud.google.com/looker/docs/importing-projects). You can view LookML object relationships in the [object browser](https://docs.cloud.google.com/looker/docs/object-browser) or the [LookML Diagram extension.](https://docs.cloud.google.com/looker/docs/lookml-diagram-using)

## M

manifest, manifest file
    

A [manifest](https://docs.cloud.google.com/looker/docs/other-project-files#project_manifest_files) (or project manifest) file is where you set project-level settings, such as those for specifying other projects to [import into the current project](https://docs.cloud.google.com/looker/docs/importing-projects), defining [LookML constants](https://docs.cloud.google.com/looker/docs/sql-and-referring-to-lookml#lookml_constants), specifying [model localization settings](https://docs.cloud.google.com/looker/docs/model-localization), and adding [extensions](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework#adding_an_extension_to_looker) and [custom visualizations](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization) to your project.

Markdown tile
    

A type of [dashboard text tile](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_text) that lets you use [some HTML](https://docs.cloud.google.com/looker/docs/html-sanitization) and [a subset](https://docs.cloud.google.com/looker/docs/using-markdown-in-text-tiles) of the Markdown markup language to format the tile.

Marketplace
    

_see_ **Looker Marketplace**

materialized view
    

A [materialized view](https://docs.cloud.google.com/looker/docs/reference/param-view-materialized-view) is a type of [persistent derived table (PDT)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table) that leverages your database's persistence functionality. This functionality is available for [database dialects that support materialized views](https://docs.cloud.google.com/looker/docs/reference/param-view-materialized-view#dialect_support). Depending on your dialect, a materialized view can consume large resources, so it is important that you understand your dialect's implementation of materialized views.

measure
    

A measure is a field in an Explore that represents [measurable information about your data](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#dimension_and_measure_fields), such as sums, counts, and so forth. A measure is declared in a [view file](https://docs.cloud.google.com/looker/docs/lookml-project-files#view_files) and can be of an aggregate or non-aggregate type.

Merged Results
    

The [Merged Results](https://docs.cloud.google.com/looker/docs/merged-results) feature lets you combine data from different Explores (even from different models, projects, or connections). Using the Merged Results feature, you can create a query from an Explore, then add queries from other Explores to display the merged results in a single table. The Merged Results feature performs similarly to a left join in SQL: it's as if the added query is being left-joined into the primary query.

metadata, IDE metadata
    

The [metadata panel in the Looker IDE](https://docs.cloud.google.com/looker/docs/lookml-metadata) shows contextually relevant information for a LookML object. For example, if your cursor is on a `view` parameter in the IDE, the metadata panel will show you which Explores have that view joined in and other views that are extensions of that view.

model
    

A [model](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#model) is the semantic layer in Looker that controls logic and gates data access for users. This is created by developers as a [model file](https://docs.cloud.google.com/looker/docs/model-and-view-files) within the LookML project, and contains information about which tables to use and how they should be joined together. Multiple models can exist for the same database connection in a single LookML project, and each model can expose different data to different users. 

model file
    

Inside a LookML project, a [model file](https://docs.cloud.google.com/looker/docs/model-and-view-files#model_files) specifies a single database connection, the set of Explores that use that connection, and the Explores themselves, as well as how they should be joined together.

model set
    

A [model set](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets) defines what data and LookML fields a user or group can see. An admin can select a combination of LookML models to which a user or group should have access. It must be used as part of a role to have any effect.

_see also_ **role**

## N

native derived table
    

Sometimes referred to as LookML-based derived tables, [native derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#native_derived_tables) are [derived tables](https://docs.cloud.google.com/looker/docs/derived-tables) that have queries defined in LookML terms, referring to LookML dimensions and measures in your model. Native derived tables can be [temporary](https://docs.cloud.google.com/looker/docs/derived-tables#temporary_derived_tables) or [persistent](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table).

_see also_ **derived table**, **persistent native derived table**, **temporary derived table**

northbound traffic
    

_see_ inbound traffic.

## O

Object browser
    

The [object browser panel](https://docs.cloud.google.com/looker/docs/object-browser) in the Looker IDE lets users view all the objects in a project in one place, along with the hierarchical relationships between them.

Object
    

_see_ **LookML object**

outbound traffic
    

In networking, outbound traffic, also called southbound traffic, is traffic from a higher-level network component to a lower-level network component. In the context of Looker (Google Cloud core), outbound traffic is, for example, traffic from a Looker (Google Cloud core) instance to a backend target service, such as a database.

## P

parameter
     A parameter defines or modifies LookML elements such as models, views, Explores, and fields. See the [LookML quick reference](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference) for a list of all available parameters. 
permission
    

Admins can manage [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permissions_list) to determine which users and groups can access content, data, and features. Permissions can be model-specific or instance-wide. Permission sets must be used as part of a role to have any effect.

permission set
    

[Permission sets](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permission_sets) are combined with model sets in a role.

_see also_ **role**

persistent derived table
    

A [persistent derived table (PDT)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table) is a derived table that is stored in the scratch schema of a database and can be regenerated on a schedule of your choosing. It can be referenced in a query without running the underlying SQL each time it is called. A PDT can be a native derived table or a SQL-based derived table.

_see also_ **derived table**

persistent native derived table
    

A persistent native derived table is a [LookML-based derived table](https://docs.cloud.google.com/looker/docs/derived-tables#native_derived_tables) that is [persistent](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table), meaning it is stored in the scratch schema of a database and can be regenerated on a schedule of your choosing. It can be referenced in a query without running the underlying SQL each time it is called. 

_see also_ **derived table**, **native derived table**

persistent SQL-based derived table
    

A persistent SQL-based derived table is a [SQL-based derived table](https://docs.cloud.google.com/looker/docs/derived-tables#sql-based_derived_tables) that is [persistent](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table), meaning it is stored in the scratch schema of a database and can be regenerated on a schedule of your choosing. It can be referenced in a query without running the underlying SQL each time it is called. 

_see also_ **derived table**, **SQL-based derived table**

preview feature
    

The **Preview Features** panel under the **Admin** menu lists Looker's new [under-development features](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features). These must be enabled by a Looker admin. Formerly named _Labs feature_.

primary key
    

The [primary key](https://docs.cloud.google.com/looker/docs/reference/param-field-primary-key) is the dimension that has exactly one unique value for each row of data. When data tables are joined together in a one-to-many relationship, the primary key must be defined correctly in order to avoid a fanout.

primary query
    

A [primary query](https://docs.cloud.google.com/looker/docs/merged-results#creating_the_primary_query) is a single query created from a single Explore. When working with merged results, the primary query is a similar concept to the primary ID when joining multiple tables in SQL.

Production Mode
    

In [Production Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#production_mode), changes that have been made in Development Mode (but not pushed to production) are not yet reflected in the data model shared by all users. In Production Mode, LookML files are treated as read-only. A developer can enter Development Mode to make changes to LookML files and push those changes for others to see in Production.

project, LookML project
    

In Looker, a project is a set of [related models and other files](https://docs.cloud.google.com/looker/docs/how-project-works) (like Explores, views, and LookML dashboards) that you will use to define your data model. In general, a project corresponds to a single Git repository.

## Q

Query Time Zone
    

[Query Time Zone](https://docs.cloud.google.com/looker/docs/using-time-zone-settings#query_time_zone) is an admin setting for the time zone in which to show dates and times when querying.

_see also_ **Database Time Zone**, **time zone settings**

## R

role
    

A [role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) defines the privileges that a user or group will have for a specific set of models in Looker. Create a role by combining one model set with one permission set.

_see also_ **model set**, **permission set**

## S

scratch schema
    

A scratch schema is a schema in the underlying database that is designated to store Looker PDTs.

_see also_ **persistent derived table**

self-service Explore
    

A [self-service Explore](https://docs.cloud.google.com/looker/docs/exploring-self-service) is an Explore that is created from a user's uploaded data.

Slug
    

A slug is a securely generated random string that takes the place of the content ID value in a URL. For example, this URL points to a dashboard: `https://docserver.cloud.looker.com/dashboards/CQ1fu99Z9Y1ggq2wcHDfMm`. In this example, the string `CQ1fu99Z9Y1ggq2wcHDfMm` is the slug. To view a dashboard slug, select **Get link** from the dashboard's three-dot menu. To view an Explore slug, select **Share** from the Explore action gear menu. You can then view the slug in — or copy the slug from — the **Short URL** field.

southbound traffic
    

_see_ outbound traffic.

Space
    

A Space is a folder where dashboards, Looks, and other Spaces (subspaces) are stored. Each user has a personal Space, and a Looker instance can also have a variety of shared Spaces. Access to content in Looker is allocated at the Space level. Spaces have been renamed **folders** as of Looker 6.20.

_see also_ **folder**

SQL-based derived table
    

A [SQL-based derived table](https://docs.cloud.google.com/looker/docs/derived-tables#sql-based_derived_tables) is a [derived table](https://docs.cloud.google.com/looker/docs/derived-tables) that has a query defined with a SQL query, referring to columns in your database. SQL-based derived tables can be [temporary](https://docs.cloud.google.com/looker/docs/derived-tables#temporary_derived_tables) or [persistent](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table).

_see also_ **derived table**, **persistent SQL-based derived table**, **temporary derived table**

SQL Runner
    

Accessible through the **Develop** menu or from an Explore (with the appropriate permissions), [SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-basics) lets users run raw SQL against their allowed connections. SQL Runner can be used to perform database functions, create and add derived tables to projects, to leverage the `EXPLAIN` function, among other uses.

Standard edition
    

A [**Standard** edition](https://docs.cloud.google.com/looker/docs/looker-core-overview#editions) is a Looker (Google Cloud core) edition type that is tailored for small teams and small or medium-sized businesses with up to 50 internal platform users. In addition to many existing Looker features, the **Standard** edition brings new functionality including Google Cloud [identity access management](https://docs.cloud.google.com/iam/docs) and simplified BigQuery connectivity.

subfolder
    

A subfolder is a [folder](https://docs.cloud.google.com/looker/docs/organizing-spaces) that is stored within another folder. Folders were called **Spaces** prior to Looker 6.20.

subparameter
    

A subparameter is a parameter that can be used under another (parent) parameter in order to further define, refine, or specify how that parameter functions.

subspace
    

A subspace is a Space that is stored within another Space. Spaces have been renamed **folders** as of Looker 6.20.

substitution operator
    

The dollar sign ([`$`](https://docs.cloud.google.com/looker/docs/sql-and-referring-to-lookml#substitution_operator_\($\))) is a substitution operator in Looker, and helps to make LookML code more reusable and modular. You can use this syntax to reference LookML objects that have already been defined.

symmetric aggregates
    

[Symmetric aggregates](https://docs.cloud.google.com/looker/docs/reference/param-explore-symmetric-aggregates) are functions in Looker that successfully return results for aggregations or measures. They help define the correct relationship between tables, thereby avoiding fanouts.

system time zone
    

The system time zone is the [time zone](https://docs.cloud.google.com/looker/docs/using-time-zone-settings) for which the server running Looker is configured.

_see also_ **time zone settings**

## T

table calculation
    

[Table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) are similar to spreadsheet formulas and are performed on the results of a query, after the query has executed.

temporary derived table
    

A [temporary derived table](https://docs.cloud.google.com/looker/docs/derived-tables#temporary_derived_tables) — sometimes called an "ephemeral" derived table — is temporary and not written to your database. A temporary derived table can be either a [LookML-based (native) derived table](https://docs.cloud.google.com/looker/docs/derived-tables#native_derived_tables), or an [ SQL-based derived table](https://docs.cloud.google.com/looker/docs/derived-tables#sql-based_derived_tables).

_see also_ **derived table**, **native derived table**, **SQL-based derived table**

Text tile
    

A type of [dashboard text tile](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_text) that provides a visual editing experience.

theme
    

[Themes](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores) are a way to customize the appearance of your embedded Looker dashboards and Explores. You can use themes to customize font family, text color, background color, tile color, and other visual elements.

tile
    

Tiles are visualizations that are [added to a dashboard](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_tiles_and_text_to_a_dashboard) from an Explore or a Look. Tiles can be query-based or Look-linked. Query tiles differ from Look-linked tiles because they are stored only on dashboards.

time zone settings
    

Looker admins and users have a variety of options to convert and display time-based data in specific time zones.

_see also_ **Application Time Zone**, **Database Time Zone**, **Query Time Zone**, **system time zone**, **User Specific Time Zones**

transpile
    

The process of taking source code written in one language and transforming it into another language that has a similar level of abstraction. An example is TypeScript to JavaScript.

trigger-persisted table
    

A trigger-persisted table is a [derived table](https://docs.cloud.google.com/looker/docs/derived-tables) that has a trigger as a persistence strategy, using either the [`datagroup_trigger`](https://docs.cloud.google.com/looker/docs/reference/param-view-datagroup-trigger) parameter, the [`sql_trigger_value`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-trigger-value) parameter, or the [`interval_trigger`](https://docs.cloud.google.com/looker/docs/reference/param-view-interval-trigger) parameter. With trigger-persisted tables, Looker maintains the PDT in the database until the PDT is triggered for rebuild. When the PDT is triggered, Looker rebuilds the PDT to replace the previous version. See the [Derived tables in Looker](https://docs.cloud.google.com/looker/docs/derived-tables#the_looker_regenerator) documentation page for more information.

## U

Unsubscribe (for alerts and scheduled content deliveries)
    

By unsubscribing, users can choose to stop receiving [scheduled content deliveries](https://docs.cloud.google.com/looker/docs/scheduling) and [alert notifications](https://docs.cloud.google.com/looker/docs/alerts-overview#receiving_an_alert_notification). The consequences for unsubscribing differ depending on how the delivery is set up.

For scheduled email deliveries and alert notifications that are sent by email, any user who unsubscribes on behalf of a group email distribution will terminate email deliveries and alert notifications for all users in that group. When recipients are listed separately, when the last remaining recipient unsubscribes from a scheduled content delivery, the schedule is deleted from Looker and deliveries will no longer be sent.

When any user unsubscribes to [alert notifications to Slack](https://docs.cloud.google.com/looker/docs/alerts-overview#alerts_notifications_to_slack) through either the Slack or Slack Attachment (API Token) integration, the alert is disabled in Looker and notifications will no longer be sent.

User Specific Time Zones
    

[User Specific Time Zones](https://docs.cloud.google.com/looker/docs/using-time-zone-settings#user_specific_time_zones) is an admin option that, when enabled, lets users choose their own time zones. Queries will be created with the time zones of the users who created them.

_see also_ **Application Time Zone**, **Database Time Zone**, **Query Time Zone**, **time zone settings**

user-defined dashboard, UDD
    

User-defined dashboards are [created](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards) by adding content through Looker's user interface, rather than using LookML. This is the most common type of dashboard.

## V

verified query
    

A predefined pair that consists of a natural language question and its exact, corresponding Looker query that serves as a trusted source of truth. [Verified queries](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents#define-verified-queries) teach your Explore data agent how to handle complex business requests without guessing. Also referred to as a _golden query_.

view
    

In Looker, a [view](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#view) can represent an underlying database table or a derived table. Views are the building blocks for Explores, which make the information in a view available for querying with the [field picker](https://docs.cloud.google.com/looker/docs/changing-explore-menu-and-field-picker#field_picker) in the Explore UI. By convention, a view is defined in a [view file](https://docs.cloud.google.com/looker/docs/model-and-view-files#view_files).

view file
    

A [view file](https://docs.cloud.google.com/looker/docs/model-and-view-files#view_files) is where you define the dimensions, measures, and other fields that are used in your LookML model.

_see also_ **model**

visual drilling
    

Visual drilling isn't supported by [dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards). To enable visual drilling, LookML developers customize a drill visualization using the [`link`](https://docs.cloud.google.com/looker/docs/reference/param-field-link#example:_using_link_to_customize_drill_visualizations) parameter. Look or Explore viewers can select whether to view the custom visualization or a data table by clicking buttons at the top of the drill window.

_see also_ **model**

visualization
    

Looker offers several types of visualizations: the built-in [chart visualizations](https://docs.cloud.google.com/looker/docs/visualization-types) that appear in Looker content and the custom visualizations that can be created with a `visualization` parameter or from the **Visualizations** page in the **Admin** section of the Looker instance, or installed as visualizations or "plug-ins" from the Looker Marketplace.

visualization components
    

[Visualization components](https://docs.cloud.google.com/looker/docs/components-vis) are React-based, prebuilt pieces of Looker's application that can be used to render and modify visualizations for custom-built data applications and customized embedded Looker dashboards.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
