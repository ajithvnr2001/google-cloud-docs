---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-build-findings-query-console/
title: Query findings in the console \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:30:50.807334+00:00
---

# Query findings in the console  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-build-findings-query-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Query findings in the console Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes how to create and edit Security Command Center findings queries by using the **Query editor** panel on the **Findings** page.

Use queries to retrieve specific findings and filter the findings that are displayed in the findings query results.

**Tip:** Managing high-volume datasets  
If your organization generates a high volume of findings, running queries on large datasets or with highly complex filters in the console can degrade query performance or timeout.  
  
For continuous monitoring, custom dashboards, or complex cross-project analysis, [export your findings to BigQuery](https://docs.cloud.google.com/security-command-center/docs/bulk-exports-to-big-query). Querying findings within BigQuery uses Google Cloud's serverless data warehouse to analyze millions of findings efficiently, rather than processing them live in the console. 

## Edit findings queries

In the **Query editor** panel, you can add filters to your queries to select findings based on their property or attribute values. You can filter for things like the presence of values, the absence of values, or the matching of a partial string.

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

If [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) is enabled for your organization, you must access the page using the jurisdictional console. For more information, see [Use the console with data residency enabled](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#console-jconsole).

Finding queries return only those findings stored in your selected data location.
  2. Select your Google Cloud project or organization. The **Findings** page loads with the default query displayed in the **Query preview** field.
  3. At the right of the **Query preview** section, click _edit_ **Edit Query** to open the **Query editor** panel.
  4. Select **Add filter** to navigate, search for, and add predefined attribute filters to the query. 

The **Add filter** menu lets you choose supported finding attributes and values.

     1. In the **Select filter** menu, select a finding attribute or type its name in the **Search finding attributes** box. A list of the available sub-attributes displays.
     2. Select a sub-attribute. A selection field displays where you can build the query statement using the sub-attribute you selected, a query operator, and one or more values for the sub-attribute. 
     3. Select the operator and one or more values for the sub-attribute from the panel. For more information about query operators and functions that they use, see [Query operators in the **Add filters** menu](https://docs.cloud.google.com/security-command-center/docs/how-to-build-findings-query-console#query_operators_in_the_add_filters_menu).

If you want to start over, click **Reset**.

     4. Click **Apply**.

The menu closes and your query is updated.

     5. Repeat until the findings query contains all the attributes you want.



When you're working in the query editor on the **Findings** page, the **Quick filters** section is deactivated to avoid conflicts between the two.

Alternatively, you can manually form a findings query the same way you [form a findings filter using the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings). As you type in your query, an autocomplete menu appears, where you can select filter names, functions, and values. To manually open the autocomplete menu, press `Control+Space`.

**Note:** When forming a query in the query editor, don't include escape characters. For example, instead of `\\"string-value\\"`, use `"string-value"`.

As you edit a query, the editor highlights any errors in the query so that you can correct the errors before you submit the query.

## Query operators

The query statements for Security Command Center findings support the operators that most Google Cloud APIs support.

The following list shows the use of various operators:

  * `state**=** "ACTIVE" **AND NOT** mute**=** "MUTED"`
  * `create_time**>** "2023-08-15T19:05:32.428Z"`
  * `resource.parent_name**:** "prod"`
  * `severity**=** "CRITICAL" **OR** severity**=** "HIGH"`



The following list shows all of the operators and functions that are supported in query statements for findings:

  * For strings:

    * `=` for an exact match

For example, `resource.parent_name="prod"` matches the value `prod`. It doesn't match `production` or `canaryprod`.

    * `:` for a partial match

For example, `resource.parent_name:"prod"` matches the values `prod`, `production`, and `canaryprod`.

  * For numbers (except int64):

    * `<`, `>`, `<=`, `>=` for inequalities
    * `=`, `!=` for equality
  * For numbers (int 64):

    * `=`, `!=` for equality
  * For booleans:

    * `=` for equality
  * For logical relationships:

    * `AND`
    * `OR`
    * `NOT` or `-`
  * For grouping expressions:

    * `(`, `)` (parentheses)


  * For arrays: 
    * `contains()`, a function for querying findings with an array field that contains at least one element that matches the specified filter
    * `containsOnly()`, a function for querying findings with an array field that only contains elements that match the specified filter
  * For IP addresses: 
    * `inIpRange()`, a function for querying IP addresses within a specified CIDR range



### Query operators in the Add filters menu

In the filter_alt **Add filter** menu of the **Query editor** , query operators and functions are represented by words or phrases, such as the following:

  * **Equals** : matches findings with this exact attribute value.
  * **Does not equal** : matches findings that don't have this exact attribute value.
  * **After** : matches findings with a creation or update time after a specified time.
  * **Before** : matches findings with a creation or update time before a specified time.
  * **Greater than** : matches findings with attribute values that are higher than your specified value.
  * **Less than** : matches findings with attribute values that are lower than your specified value.
  * **Has** : matches findings with attribute values that contain the text you enter in the **Keyword** field.
  * **Does not have** : matches findings with attribute values that don't contain the text you enter in the **Keyword** field.
  * For finding attributes that contain arrays: 
    * **Contains any** : matches findings that have an array value that contains any of the text that you enter in the **Keyword** field.
    * **Contains all** : matches findings that have an array value that contains all of the text that you enter in the **Keyword** field.
    * **Contains none** : matches findings that don't have an array value that contains the text you enter in the **Keyword** field.
    * **Contains only** : matches findings that have an array attribute that contains only the value that you enter in the **Keyword** field, and no other values.
  * For IP addresses: 
    * **Any within IP range** : matches findings that have an IP address in a specified CIDR range.
    * **Does not have any within IP range** : matches findings that have an IP address that is not in a specified CIDR range.



## Query functions

A query function provides more complex evaluations of attribute values than the common query operators.

### The `contains` function

Use the `contains` function to evaluate attributes or attribute subfields that can appear multiple times in the same finding.

Internally, these attributes or attribute subfields are stored in the elements of an array data structure, so they are referred to as _array-type attributes_.

For example, certain findings can reference multiple network connections, so the `connections` attribute is an array-type attribute. Similarly, certain threat findings can reference multiple IP addresses as indicators of a compromise, so the `ip_addresses` subfield of the `indicator` attribute is an array-type attribute.

The `contains` function uses the following syntax:
    
    
    contains(ARRAY_ATTRIBUTE_NAME, SUBFILTER)

Replace the following:

  * `ARRAY_ATTRIBUTE_NAME`: the name of the array-type attribute that is stored in an array. If the array-type attribute is a subfield of another attribute, specify the attribute name and the subfield name separated by a dot.

In the following example, the array-type attribute, `ip_addresses`, is a subfield of `indicator`, so both are specified in the `ARRAY_ATTRIBUTE_NAME` position:
        
        contains(indicator.ip_addresses, elem="192.0.2.80")

  * `SUBFILTER`: an expression that defines how to evaluate each instance of the array-type attribute. Standard Security Command Center query operators and evaluation statements are supported.

If the value to check is in a subfield of an array-type attribute, specify the subfield name on the left of the expression. The following `contains` function evaluates each element of an array of `connections`, which is an array-type attribute that contains subfields. The values being queried for are in the `destination_ip` subfield, which is not an array-type field. The values to query for are specified with the subfield name, `destination_ip`, instead of the `elem` parameter.
        
        contains(connections, **destination_ip** ="192.0.2.80")

If the subfield is the array-type attribute, specify the array-type attribute on the left of the expression with its parent and use the `elem` parameter on the right of the expression to specify the value to search for. For example, the following `contains` function evaluates each element of an array of `ip_addresses`, which is a subfield of the `indicator` attribute. The `indicator` attribute is not an array-type field.
        
        contains(indicator.ip_addresses, **elem** ="192.0.2.80")




#### The `contains` function in the Add filter menu

In the **Add filter** menu, depending on the finding attribute that you are evaluating, the `contains` function is listed explicitly or it gets included automatically when you select another filter option that requires it.

For example, for the **IP addresses** sub-field of the **Indicator** attribute, you can select the following filter options:

  * **Contains any**
  * **Contains all**
  * **Contains none**



In contrast, if you are filtering on the **Destination IP** sub-field of the **Connections** attribute and select **Any within IP range** , the `contains` functions get added to the query statement automatically, as shown in the following example:
    
    
    contains(connections, inIpRange(destination_ip, "2001:db8::/32"))

For more information about the `contains` function, see [Filtering on array-type fields](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings#array-contains-filtering).

### The `containsOnly` function

The `containsOnly` function lets you query findings for array-type attributes or subfields that contain only the values that are specified in the subfilter, and no others.

The `containsOnly` function uses the following syntax:
    
    
    containsOnly(ARRAY_ATTRIBUTE_NAME,SUBFILTER)

Replace the following:

  * `ARRAY_ATTRIBUTE_NAME`: the name of the array-type attribute. If the array-type attribute is a subfield of another attribute, specify the attribute name and the subfield name separated by a dot. When you are running queries using the Google Cloud console, this function only supports the `iam_bindings.member` and the `iam_bindings.role` array attributes.

  * `SUBFILTER`: an expression that defines how to evaluate each element of the array-type attribute. Standard Security Command Center query operators and evaluation statements are supported.




In the **Add filter** menu, the following filter options use the `containsOnly` function:

  * **IAM binding > Member**: selects only findings that include the specified users, service accounts, or groups.

  * **IAM binding > Role**: selects only findings that include the specified roles.




The following example shows a findings query in the Google Cloud console that returns active, unmuted findings for users in the `example-group` group:
    
    
    state="ACTIVE"
      AND NOT mute="MUTED"
      **AND containsOnly(iam_bindings,member="group:example-group@example.com")**

### The `inIpRange` function

The `inIpRange` function checks whether the IP address in a selected finding attribute is within a range of IP addresses that you specify by using CIDR notation (a CIDR range). The following shows the syntax of the `inIpRange` function:
    
    
    inIpRange(ATTRIBUTE_WITH_IP, "CIDR_RANGE")

In the **Add filter** menu, the following filter options use the `inIpRange` function:

  * **Any within IP range** : selects only findings that contain IP addresses within the specified range.
  * **Does not have any within IP range** : selects only findings that don't contain IP addresses within the specified range.



The following example shows a findings query in the Google Cloud console that returns active, unmuted findings in which the `caller_ip` sub-field of the `access` object contains an IPv6 address in the CIDR range of `2001:db8::/32`:
    
    
    state="ACTIVE"
    AND NOT mute="MUTED"
    **AND inIpRange(access.caller_ip, "2001:db8::/32")**
    

The following example shows a findings query that returns active, unmuted findings in which the `caller_ip` sub-field of the `access` object does not contain an IP address in the IPv4 CIDR range of `192.0.2.0/24`:
    
    
    state="ACTIVE"
    AND NOT mute="MUTED"
    **AND NOT inIpRange(access.caller_ip, "192.0.2.0/24")**
    

If an IP address is in an attribute that can appear multiple times in a finding, use the `contains` function with the `inIpRange` function to check each instance of the attribute for the IP address. For example:
    
    
    contains(connections, inIpRange(source_ip, "192.0.2.0/24"))

For more information about the `contains()` function, see The `contains` function.

## Finding attributes for queries

Security Command Center selects the findings to display by evaluating the attributes of each stored finding against the attribute filters that you specify in the query.

You can query most finding attributes. Some attributes are common to all findings. Other attributes might be specific to a particular security issue, finding category, or detection service.

In the **Add filter** menu of the **Query editor** panel, the options that you can apply to an attribute filter are different depending on the type of attribute you select and whether the attribute has sub-fields or an array of values.

In the **Add filter** menu, click any of the following top-level attributes to display the sub-attributes and values that you can use in a findings query:

  * Finding
  * Resource
  * Access ([`access`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings#access))
  * Attack exposure score
  * Backup Disaster Recovery
  * Compliances ([`compliances[]`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings#compliance))
  * Connections ([`connections[]`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings#connection))
  * Contacts
  * Containers
  * Database
  * Data Access Events
  * Data Flow Events
  * Data Retention Deletion Events ([`DataRetentionDeletionEvent`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings#dataretentiondeletionevent))
  * Exfiltration ([`exfiltration`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings#exfiltration))
  * Files
  * IAM binding ([`iamBindings[]`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings#iambinding))
  * Indicator
  * Kernel rootkit
  * Kubernetes
  * MITRE ATT&CK ([`mitreAttack`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings#mitreattack))
  * Processes ([`processes[]`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings#process))
  * Security posture
  * Sensitive Data Protection
  * Vulnerability



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
