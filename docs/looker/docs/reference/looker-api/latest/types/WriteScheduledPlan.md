---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/WriteScheduledPlan/
title: WriteScheduledPlan \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:41:10.151469+00:00
---

# WriteScheduledPlan  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/WriteScheduledPlan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  WriteScheduledPlan Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

Datatype

Description

(object)

object 

name

string 

Name of this scheduled plan

user_id

string 

User Id which owns this scheduled plan

run_as_recipient

boolean 

Whether schedule is run as recipient (only applicable for email recipients)

enabled

boolean 

Whether the ScheduledPlan is enabled

look_id

string 

Id of a look

dashboard_id

string 

Id of a dashboard

lookml_dashboard_id

string 

Id of a LookML dashboard

filters_string

string 

Query string to run look or dashboard with

dashboard_filters

string 

(DEPRECATED) Alias for filters_string field

require_results

boolean 

Delivery should occur if running the dashboard or look returns results

require_no_results

boolean 

Delivery should occur if the dashboard look does not return results

require_change

boolean 

Delivery should occur if data have changed since the last run

send_all_results

boolean 

Will run an unlimited query and send all results.

crontab

string 

Vixie-Style crontab specification when to run

datagroup

string 

Name of a datagroup; if specified will run when datagroup triggered (can't be used with cron string)

timezone

string 

Timezone for interpreting the specified crontab (default is Looker instance timezone)

scheduled_plan_destination

[ScheduledPlanDestination](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ScheduledPlanDestination)[] 

Expand ScheduledPlanDestination definition... 

id

_lock_

string 

Unique Id

scheduled_plan_id

string 

Id of a scheduled plan you own

format

string 

The data format to send to the given destination. Supported formats vary by destination, but include: "txt", "csv", "inline_json", "json", "json_detail", "xlsx", "html", "wysiwyg_pdf", "assembled_pdf", "wysiwyg_png"

apply_formatting

boolean 

Are values formatted? (containing currency symbols, digit separators, etc.

apply_vis

boolean 

Whether visualization options are applied to the results.

address

string 

Address for recipient. For email e.g. 'user@example.com'. For webhooks e.g. 'https://example.domain/path'. For Amazon S3 e.g. 's3://bucket-name/path/'. For SFTP e.g. 'sftp://host-name/path/'. 

looker_recipient

_lock_

boolean 

Whether the recipient is a Looker user on the current instance (only applicable for email recipients)

type

string 

Type of the address ('email', 'webhook', 's3', or 'sftp')

parameters

string 

JSON object containing parameters for external scheduling. For Amazon S3, this requires keys and values for access_key_id and region. For SFTP, this requires a key and value for username.

secret_parameters

string 

(Write-Only) JSON object containing secret parameters for external scheduling. For Amazon S3, this requires a key and value for secret_access_key. For SFTP, this requires a key and value for password.

include_filters

boolean 

Whether or not to include filters context

message

string 

Optional message to be included in scheduled emails

run_once

boolean 

Whether the plan in question should only be run once (usually for testing)

include_links

boolean 

Whether links back to Looker should be included in this ScheduledPlan

include_dashboard_summary

boolean 

Whether to include a dashboard summary in the scheduled email

custom_url_base

string 

Custom url domain for the scheduled entity

custom_url_params

string 

Custom url path and parameters for the scheduled entity

custom_url_label

string 

Custom url label for the scheduled entity

show_custom_url

boolean 

Whether to show custom link back instead of standard looker link

pdf_paper_size

string 

The size of paper the PDF should be formatted to fit. Valid values are: "letter", "legal", "tabloid", "a0", "a1", "a2", "a3", "a4", "a5".

pdf_landscape

boolean 

Whether the PDF should be formatted for landscape orientation

embed

boolean 

Whether this schedule is in an embed context or not

color_theme

string 

Color scheme of the dashboard if applicable

long_tables

boolean 

Whether or not to expand table vis to full length

pdf_page_breaks

boolean 

Whether or not to add page breaks between tabs

include_filters

boolean 

Whether or not to include filters context

tab_ids

string[] 

inline_table_width

integer 

The pixel width at which we render the inline table visualizations

query_id

string 

Query id

## Related Methods

  * [ScheduledPlan/scheduled_plan_run_once_by_id](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ScheduledPlan/scheduled_plan_run_once_by_id "ScheduledPlan/scheduled_plan_run_once_by_id")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
