---
url: https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards-filters/
title: Configure dashboard filters \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:11.681911+00:00
---

# Configure dashboard filters  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards-filters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure dashboard filters

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can apply filters to data source fields to refine the data displayed in applicable charts.

## Add a filter

**Note:** You must have the `chronicle.nativeDashboards.update` IAM permission to add a filter.

To add a filter, do the following:

  1. On the **Edit Dashboard** page, click filter_alt**Filter** to add a filter.

  2. On the **Manage filters** window, click add**Add** to add a new filter.

  3. In the **Field to filter** field, enter the field you want to use to filter the data. For more information about supported data sources and fields, see [Supported data sources](https://docs.cloud.google.com/chronicle/docs/reports/dashboard-data-sources-prefixes).

  4. In the **Filter name** field, enter a name for the filter.

  5. In the **Apply to field** , select the charts where the filter should be applied.

  6. Optional: Set a default value for the filter.

  7. Click **Done** to add the filter and close the **Manage filters** window.




### SOAR data source filter limitations

The default SOC workflow monitoring SOAR dashboard and the underlying SOAR data source use their own `environment` field and don't map directly to the `principal.namespace` field used by SIEM data sources.

As a result, a unified dashboard containing both SIEM and SOAR widgets cannot be filtered by environment using a single global filter mapped to `principal.namespace`. If you apply a filter on `principal.namespace`, it won't apply to the SOAR widgets. To filter both datasets, you may need to define separate filters or build custom dashboards where the filtering logic is explicitly defined for each source.

## Advanced filtering

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

Google Security Operations provides Advanced Filtering within its built-in dashboard platform. Unlike basic filters, which are tied to specific fields, advanced filters operate as query variables, also known as tokens. This capability enables security analysts to inject dynamic values, complex regular expressions, or boolean logic directly into YARA-L queries at runtime.

### Key features

  * **Flexible Filtering:** Use a single filter input (for example, `$token$`) to simultaneously filter based on multiple fields across multiple charts within a dashboard.
  * **Dynamic Dropdown Options:** Populate filter choices dynamically by using the results of a separate YARA-L query. This ensures that users always select from up-to-date data.
  * **Flexible Formatting:** Define custom prefixes, suffixes, and delimiters (for example, `/` for regular expressions or `,` for `IN` clauses) to format user-selected values before they are injected into the query.
  * **Default Values:** Configure default values to ensure dashboards load with data immediately and to support automated Scheduled Reports where no user interaction occurs.
  * **Multi-Select Support:** Enable users to select multiple values for a single token, joined by a user-defined separator.



### Security and permissions

Advanced filtering uses existing Role-Based Access Control (RBAC) permissions and new permissions aren't required. The following Identity and Access Management (IAM) permissions are relevant:

IAM Permission | Purpose  
---|---  
`nativeDashboards.update` | Create and configure Advanced Filters within a dashboard.  
`nativeDashboards.get` | View dashboards and use the filter input controls.  
`dashboardQueries.execute` | Execute the final resolved queries with substituted tokens.  
  
For Data RBAC Enforcement, queries used to populate dynamic dropdowns are executed in the context of the viewing user. This makes sure that users only see values (such as specific IPs) they are authorized to access.

### Configuring and using advanced filters

The following sections detail the process for setting up and utilizing advanced filters within Google SecOps dashboards.

#### Creating a new advanced filter

To create a new advanced filter, proceed as follows:

  1. Open the **Manage Filters** dialog in a dashboard.
  2. Select add and then **Advanced Filter** as the **Filter Type**.
  3. Enter a **Filter Name** (label) and a **Token Variable** (for example, `token`). 
     * **Token Variable Syntax Constraints:** The Token Variable name only permits alphanumeric characters and underscores (`^[a-zA-Z0-9_]+$`).
     * **Uniqueness:** Token names must be unique. Conflicts will prevent saving the filter.
  4. Select **Generate from Query** (dynamic YARA-L results) or **Manual Entry** (a static list). 
     1. When **Generate from Query** is selected: 
        1. Enter a query and define a **Time Range**.
        2. Click **Run Search**.
        3. Choose a column from the **Select Column** drop-down menu.
        4. Choose a value from the **Preview Filter Dropdown** drop-down menu.
     2. When **Manual entry** is selected, type a value in the **Manual Entry** field and click **Add**.
  5. Choose a **Prefix** and **Suffix** to wrap values for specific logic, such as regular expressions. 
     * If the token is used within regular expression delimiters in the YARA-L query (for example, `principal.ip = /$token$/`), you typically don't need to specify a **Prefix** or **Suffix**.
     * If the token is used without regular expression delimiters but is intended to function as an anchored regular expression (for example, `principal.ip = $token$`), set the **Prefix** to `/^` and the **Suffix** to `$/`.
  6. Toggle the **Allow Selection of Multiple Options** button to define a **Delimiter** (for example, `|` for regular expressions `OR` logic).
  7. Select a **Default Value** from the drop-down menu.
  8. Select or deselect the **Apply Prefix/Suffix for Default Value(s)** checkbox.
  9. Click **Done**.

**Note:** Renaming a token that is referenced in any chart queries within the dashboard will trigger a warning dialog. This is because changing the token variable name will break the queries using the old name. Users must update their chart queries to use the new token variable name to prevent rendering errors.

#### Using tokens in chart queries

Dashboard creators must manually insert the token, wrapped in `$` symbols, into the chart's query.

**Examples:**

  * `principal.hostname = $hostname$`
  * `re.regex(target.ip, $ip_regex$)`



For token validation, a yellow warning banner is displayed if a query uses an undefined token. In such cases, the system treats the token as a literal string.

#### Default behavior on load

Advanced Filters in Google SecOps dashboards operate exclusively through string substitution. Unlike standard filters, the system does not interpret the logic for you but performs a "find and replace" of your `$token$` with the selected value before the query is compiled. The query acts as a template, and the user is responsible for making sure the final, token-substituted query is syntactically correct.

### Default values and query validity

Since the system does not automatically ignore a token if no input is provided, you must define Default Values that maintain a valid query structure for initial loads and Scheduled Reports.

The following are examples of effective **Default Value** configurations:

Use Case | Query Context | Default Value Configuration | Resulting Logic  
---|---|---|---  
Exact Match | `principal.hostname = $host$` | **Incorrect:** Leaving empty results in invalid syntax (`principal.hostname =` ). **Correct:** Use a placeholder that maintains valid syntax. | **Example with empty default:** Fails because `principal.hostname =` is invalid YARA-L.  
Exact Match | `principal.hostname = "$host$"` | Leave empty | **Success:** Evaluates to `principal.hostname = ""`, which returns no results but is syntactically valid.  
Wildcard (Show All) | `principal.hostname = /.*$host$.*/` | `.*` | **Success:** Evaluates to `principal.hostname = /.*/`, a "catch-all" regular expression that returns all results.  
Regular Expression (Show All) | `principal.hostname = $host$` | `/.*/` | **Success:** Evaluates to `principal.hostname = /.*/`, which matches all hostnames.  
Regular Expression Anchor | `metadata.product_name = /^$token$$/` | `.*` | **Success:** Evaluates to `metadata.product_name = /^.*$/` on load, matching all products.  
Integers (Show All) | `principal.host = $token$` | `0 or 1=1` | **Success:** Evaluates to `principal.host = 0 or 1=1`, effectively returning all results.  
Integers (Show All) | `cast.as_string(principal.host) = $token$` | `/.*/` | **Success:** Evaluates to `cast.as_string(principal.host) = /.*/`, which matches all string representations of host integers.  
Single select token with default all logic | `$log = metadata.log_type \n $log = if($log$ = "", metadata.log_type, $log$)\n match: $log` | Leave Empty (with Prefix: `"`, Suffix: `"`) | **Success:** With an empty default, `$log` becomes `""`. The `if` statement becomes `$log = if("" = "", metadata.log_type, "")`, which simplifies to `$log = metadata.log_type`. The query then matches all log types.  
Single Specific Default Value | `$et = metadata.event_type \n $et = $et2$ \n match: $et` | `EMAIL_TRANSACTION` (with Prefix: `"`, Suffix: `"`) | **Success:** Evaluates to `$et = "EMAIL_TRANSACTION"` on load, restricting the default results to a specific event category.  
Multi-select regular expression | `$log = metadata.log_type \n $log = $logs$ \n match: $log` | `.*` (with Prefix: `/`, Suffix: `/`, Delimiter: `|`) | **Success:** Evaluates to `$log = /.*/` on load, matching all log types. Selecting multiple values (e.g. `DNS`, `DHCP`) evaluates to `$log = /DNS|DHCP/`.  
Always-True Default (Show All) | `$et = metadata.event_type \n $et = $et4$ \n match: $et` | `"USER_LOGIN" or 1=1` (with Delimiter: `" or metadata.event_type = "`, Apply Prefix/Suffix for Default Value(s): unchecked) | **Success:** Evaluates to `$et = "USER_LOGIN" or 1=1` on load, which matches all events. Selecting specific options replaces the string with explicit `OR` equality clauses.  
Full Clause Injection (Multi-select) | `$et$ \n $et = metadata.event_type \n match: $et` | Leave Empty (with Prefix: `metadata.event_type = "`, Suffix: `"`, Delimiter: `" or metadata.event_type = "`, Apply Prefix/Suffix for Default Value(s): unchecked) | **Success:** The token itself injects the entire target field predicate. Selecting `USER_LOGIN` and `NETWORK_DNS` expands to `metadata.event_type = "USER_LOGIN" or metadata.event_type = "NETWORK_DNS"`.  
Regular expression default catch-all | `$pet = metadata.product_event_type \n $pet = $pet$ \n match: $pet` | `/.*/` (with Prefix: `"`, Suffix: `"`, Apply Prefix/Suffix for Default Value(s): unchecked) | **Success:** Evaluates to `$pet = /.*/` on load, matching all product event types. Selecting a specific value applies quotes (for example, `$pet = "USER_LOGIN"`).  
  
### Syntax considerations for advanced filters

The system does not perform automatic escaping for special characters (such as quotes or slashes). Always verify that your configured Prefix, Suffix, and Separator align with the syntax of the query language (YARA-L) you are using.

### API specifications

For detailed API specifications, see [AdvancedFilterConfig](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.nativeDashboards#advancedfilterconfig).

## Manage the global time filter

The global time filter applies to all charts, regardless of the chart's [data source](https://docs.cloud.google.com/chronicle/docs/reports/dashboard-data-sources-prefixes).

**Note:** You must have the `chronicle.nativeDashboards.update` IAM permission to add a global time filter.

To select the charts for which the global time filter can be applied, do the following:

  1. On the **Edit Dashboard** page, click filter_alt**Filter** to add a filter.

  2. On the **Manage filters** window, select **Global time filter** from the filters list.

  3. Click the toggle to ensure that the global time filter is enabled.

  4. In the **Apply to** field, select the charts to apply the global time filter.

  5. In the **Set default values** field, set a time range to view data, using either absolute or relative values..

  6. Click **Done** to enable the filter and close the **Manage Filters** window.




## Apply a dashboard filter

**Note:** You must have the `chronicle.nativeDashboards.get` IAM permission to apply a filter.

To apply a filter, do the following:

  1. On the **Edit Dashboard** page, click **Back** > filter_alt**Filter** to view the dashboard filters.

  2. On the **Dashboard filters** window, select the filter you created.

  3. Enter a value for the selected field.

  4. Click **Apply**. The charts for which the filter is applicable are refreshed with new data.




## Change the global time filter

When you open a dashboard, the global time filter is applied on the applicable charts with the default time range.

**Note:** You must have the `chronicle.nativeDashboards.get` IAM permission to apply the global time filter.

To change the global time filter value, do the following:

  1. Click schedule**Schedule**.

  2. In the **Global Time Filter** dialog, select either the `past` or `between` operator.

  3. Select the date range.

  4. Click **Apply**. The selected charts update with new data based on the global time filter.




### Understand the Past operator

The `past` operator calculates a start time based on the value and unit you provide. The end time is always the current moment.

The start time calculation depends on the unit:

  * **Seconds, Minutes, Hours:** These units calculate the start time by subtracting the exact number of seconds, minutes, or hours from the current timestamp.
  * **Days, Weeks, Months, Years:** These units snap the start time to the beginning of the current or previous period (for example, the start of the current day or month).



The following table shows examples based on a current timestamp of **13:13 on July 2, 2025** :

Value | Unit | Filter start time  
---|---|---  
`n` | Seconds | 13:13:00 July 2, 2025 minus `n` seconds  
`n` | Minutes | 13:13:00 July 2, 2025 minus `n` minutes  
`n` | Hours | 13:13:00 July 2, 2025 minus `n` hours  
`1` | Day | 00:00:00 July 2, 2025 (start of the current day)  
`2` | Days | 00:00:00 July 1, 2025 (start of the previous day)  
`1` | Week | 00:00:00 of the first day of the current week. The start day of the week depends on your system's locale settings.  
`1` | Month | 00:00:00 July 1, 2025 (start of the current month)  
`2` | Months | 00:00:00 June 1, 2025 (start of the previous month)  
`1` | Year | 00:00:00 January 1, 2025 (start of the current year)  
`2` | Years | 00:00:00 January 1, 2024 (start of the previous year)  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
