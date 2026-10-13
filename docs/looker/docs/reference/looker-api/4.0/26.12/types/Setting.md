---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Setting/
title: Setting \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:21:58.850061+00:00
---

# Setting  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Setting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Setting Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.12 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

Datatype

Description

(object)

object 

instance_config

_lock_

[InstanceConfig](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/InstanceConfig)

Externally available instance configuration information

Expand InstanceConfig definition... 

feature_flags

_lock_

object 

Feature flags enabled on the instance

license_features

_lock_

object 

License features enabled on the instance

extension_framework_enabled

boolean 

Toggle extension framework on or off

extension_load_url_enabled

boolean 

(DEPRECATED) Toggle extension load url on or off. Do not use. This is temporary setting that will eventually become a noop and subsequently deleted.

marketplace_auto_install_enabled

boolean 

(DEPRECATED) Toggle marketplace auto install on or off. Deprecated - do not use. Auto install can now be enabled via marketplace automation settings

marketplace_automation

_lock_

[MarketplaceAutomation](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/MarketplaceAutomation)

Marketplace automation settings.

Expand MarketplaceAutomation definition... 

install_enabled

boolean 

Whether marketplace auto installation is enabled

update_looker_enabled

boolean 

Whether marketplace auto update is enabled for looker extensions

update_third_party_enabled

boolean 

Whether marketplace auto update is enabled for third party extensions

marketplace_enabled

boolean 

Toggle marketplace on or off

marketplace_site

_lock_

string 

Location of Looker marketplace CDN

marketplace_terms_accepted

boolean 

Accept marketplace terms by setting this value to true, or get the current status. Marketplace terms CANNOT be declined once accepted. Accepting marketplace terms automatically enables the marketplace. The marketplace can still be disabled after it has been enabled.

privatelabel_configuration

_lock_

[PrivatelabelConfiguration](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/PrivatelabelConfiguration)

Private label configuration

Expand PrivatelabelConfiguration definition... 

logo_file

string 

Customer logo image. Expected base64 encoded data (write-only)

logo_url

_lock_

string 

Logo image url (read-only)

favicon_file

string 

Custom favicon image. Expected base64 encoded data (write-only)

favicon_url

_lock_

string 

Favicon image url (read-only)

default_title

string 

Default page title

show_help_menu

boolean 

Boolean to toggle showing help menus

show_docs

boolean 

Boolean to toggle showing docs

show_email_sub_options

boolean 

Boolean to toggle showing email subscription options.

allow_looker_mentions

boolean 

Boolean to toggle mentions of Looker in emails

allow_looker_links

boolean 

Boolean to toggle links to Looker in emails

custom_welcome_email_advanced

boolean 

Allow subject line and email heading customization in customized emails”

setup_mentions

boolean 

Remove the word Looker from appearing in the account setup page

alerts_logo

boolean 

Remove Looker logo from Alerts

alerts_links

boolean 

Remove Looker links from Alerts

folders_mentions

boolean 

Remove Looker mentions in home folder page when you don’t have any items saved

custom_welcome_email

_lock_

[CustomWelcomeEmail](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/CustomWelcomeEmail)

Custom welcome email configuration

Expand CustomWelcomeEmail definition... 

enabled

boolean 

If true, custom email content will replace the default body of welcome emails

content

string 

The HTML to use as custom content for welcome emails. Script elements and other potentially dangerous markup will be removed.

subject

string 

The text to appear in the email subject line. Only available with a whitelabel license and whitelabel_configuration.advanced_custom_welcome_email enabled.

header

string 

The text to appear in the header line of the email body. Only available with a whitelabel license and whitelabel_configuration.advanced_custom_welcome_email enabled.

onboarding_enabled

boolean 

Toggle onboarding on or off

timezone

string 

Change instance-wide default timezone

allow_user_timezones

boolean 

Toggle user-specific timezones on or off

data_connector_default_enabled

boolean 

Toggle default future connectors on or off

host_url

string 

Change the base portion of your Looker instance URL setting

override_warnings

boolean 

(Write-Only) If warnings are preventing a host URL change, this parameter allows for overriding warnings to force update the setting. Does not directly change any Looker settings.

email_domain_allowlist

string[] 

embed_cookieless_v2

boolean 

(DEPRECATED) Use embed_config.embed_cookieless_v2 instead. If embed_config.embed_cookieless_v2 is specified, it overrides this value.

embed_enabled

_lock_

boolean 

True if embedding is enabled https://docs.cloud.google.com/looker/docs/r/looker-core-feature-embed, false otherwise

embed_config

_lock_

[EmbedConfig](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/EmbedConfig)

Embed configuration. Requires embedding to be enabled https://docs.cloud.google.com/looker/docs/r/looker-core-feature-embed

Expand EmbedConfig definition... 

domain_allowlist

string[] 

alert_url_allowlist

string[] 

alert_url_param_owner

string 

Owner of who defines the alert/schedule params on the base url

alert_url_label

string 

Label for the alert/schedule url

sso_auth_enabled

boolean 

Is SSO embedding enabled for this Looker

embed_cookieless_v2

boolean 

Is Cookieless embedding enabled for this Looker

embed_content_navigation

boolean 

Is embed content navigation enabled for this looker

embed_content_management

boolean 

Is embed content management enabled for this Looker

strict_sameorigin_for_login

boolean 

When true, prohibits the use of Looker login pages in non-Looker iframes. When false, Looker login pages may be used in non-Looker hosted iframes.

look_filters

boolean 

When true, filters are enabled on embedded Looks

hide_look_navigation

boolean 

When true, removes navigation to Looks from embedded dashboards and explores.

permissions

_lock_

object 

Tree of allowed embed permissions

embed_enabled

_lock_

boolean 

True if embedding is licensed for this Looker instance.

login_notification_enabled

_lock_

boolean 

Login notification enabled

login_notification_text

_lock_

string 

Login notification text

dashboard_auto_refresh_restriction

boolean 

Toggle Dashboard Auto Refresh restriction

dashboard_auto_refresh_minimum_interval

string 

Minimum time interval for dashboard element automatic refresh. Examples: (30 seconds, 1 minute)

managed_certificate_uri

string[] 

content_certification_documentation_link

string 

Link to content certification documentation.

revoke_certification_on_edits

boolean 

Allow content certification to be revoked on edits.

automated_mfa_enabled

boolean 

Automatically enable Multi-Factor Authentication for users.

is_content_certification_enabled

boolean 

Allow content certification.

auto_certify_lookml_content

boolean 

Allow auto certification of lookml content.

ca_agent_observability

boolean 

Toggle Conversational Analytics Agent Token usage

mcp_tools

[McpTools](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpTools)

Configuration for MCP Tools

Expand McpTools definition... 

enable_all

boolean 

Enable all MCP tools

add_dashboard_element

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Creates a dashboard element in the given dashboard.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

add_dashboard_filter

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Adds a filter to a specified dashboard.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

create_project_file

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Creates a new LookML file in a project.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

delete_project_file

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Deletes a LookML file in a project.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

dev_mode

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Changes the current session into and out of dev mode

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

generate_embed_url

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Generates an embeddable URL for Looker content.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

get_connection_databases

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Returns all the databases in a connection.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

get_connection_schemas

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Returns all the schemas in a connection.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

get_connection_table_columns

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Returns all the columns for each table specified.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

get_connection_tables

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Returns all the tables in a connection.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

get_connections

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Returns all the connections in the source.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

get_dashboards

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Searches for a saved Dashboard by name or description.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

get_dimensions

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Returns all the dimensions from a given explore in a given model in the source.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

get_explores

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Returns all explores for the given model from the source.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

get_filters

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Returns all the filters from a given explore in a given model in the source.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

get_looks

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Searches for saved Looks in a Looker source.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

get_measures

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Returns all the measures from a given explore in a given model in the source.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

get_models

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Returns all the models in the source.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

get_parameters

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Returns all the parameters from a given explore in a given model in the source.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

get_project_file

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Returns the contents of a LookML file.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

get_project_files

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Returns all the LookML files in a project in the source.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

get_projects

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Returns all the LookML projects in the source.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

health_analyze

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Provides a set of analytical commands for a Looker instance, allowing users to analyze projects, models, and explores.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

health_pulse

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Performs health checks on a Looker instance, with multiple actions available (e.g., checking database connections, dashboard performance, etc).

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

health_vacuum

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Provides a set of commands to audit and identify unused LookML objects in a Looker instance.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

make_dashboard

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Generates a Looker dashboard in the users personal folder in Looker

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

make_look

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Generates a Looker look in the users personal folder in Looker

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

query

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Runs an inline query using the Looker semantic model.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

query_sql

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Generates a sql query using the Looker semantic model.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

query_url

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Generates a url link to a Looker explore.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

run_dashboard

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Runs the queries associated with a dashboard.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

run_look

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Runs the query associated with a saved Look.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

update_project_file

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Updates the content of a LookML file in a project.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

validate_project

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Checks the syntax of a LookML project and reports any errors.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

get_project_directories

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Returns the directories within a specific LookML project.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

create_project_directory

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Creates a new directory in a LookML project.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

delete_project_directory

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Deletes a directory from a LookML project.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

get_lookml_tests

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Returns a list of tests which can be run to validate a project’s LookML code and/or the underlying data, optionally filtered by the file id.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

run_lookml_tests

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Runs LookML tests in the project, filtered by file, test, and/or model.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

create_view_from_table

[McpToolSetting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/McpToolSetting)

Generates boilerplate LookML views directly from the database schema.

Expand McpToolSetting definition... 

enabled

boolean 

Is this tool enabled

description

_lock_

string 

Tool description

category

_lock_

string 

Tool category

access_level

_lock_

string 

Tool access level

## Related Methods

  * [Config/set_setting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/Config/set_setting "Config/set_setting")
  * [Config/get_setting](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/Config/get_setting "Config/get_setting")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
