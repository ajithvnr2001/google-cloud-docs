---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/troubleshoot-data-stores/
title: Troubleshoot Gemini Enterprise data stores \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:01.399541+00:00
---

# Troubleshoot Gemini Enterprise data stores  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/troubleshoot-data-stores/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Troubleshoot Gemini Enterprise data stores Stay organized with collections  Save and categorize content based on your preferences. 

Use this page to diagnose and resolve any issues with Gemini Enterprise data stores. When a data store fails to retrieve information, you can independently debug the issue by moving through a cohesive, step-by-step observability journey.

To get a complete picture of an error, understand how Google Cloud's observability tools work together:

  * **[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs):** Detects **when** there is a problem. Use it to view high-level trends, error rates, and set up alerts for your data stores.
  * **[Cloud Trace](https://docs.cloud.google.com/trace/docs/overview):** Discovers **where** the problem is occurring. Use it to view the lifecycle of a request, analyze spans, and identify exactly which step caused high latency or failure.
  * **[Cloud Logging](https://docs.cloud.google.com/logging/docs/overview):** Explains **why** the problem is occurring. Use it to read the exact error messages and payloads associated with a failed request.
  * **[Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit):** Identifies **who** or what policy blocked the action. Use it to track security compliance, permission changes, and administrative actions that might be causing access denials.



## Debugging workflow

When investigating a data store issue, follow this sequential workflow to isolate and resolve the root cause:

  1. Check error rate trends
  2. Find the specific failing request
  3. View the error payload
  4. Cross-reference usage audit logs



### Check error rate trends

  1. In the Google Cloud console, go to the **Metrics Explorer** page.

[Go to Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. Check your dashboards and review your data store request counts and filter by **Tool ID** and **Engine ID**. You can determine if the issue is a one-off error or a widespread systemic spike that requires immediate attention.




### Find the specific failing request

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/stackdriver/images/trace-explorer-icon.png)**Trace explorer** page: 

[Go to **Trace explorer**](https://console.cloud.google.com/traces/explorer)

You can also find this page by using the search bar.

  2. Examine the scatter plot for traces with an error icon (a red exclamation mark) or unusually high latency.
  3. Click a trace to view its Gantt chart.
  4. Check the `invoke_connector` span to see where the process stalled or failed.
  5. Additionally, you can find the unique assist token associated with a specific request. If you need to escalate a complex issue to Google Cloud Support, share this assist token to expedite the investigation.



### View the error payload

  1. Click the failing span in **Trace Explorer**.
  2. In the details pane, click **Show logs**.
  3. This automatically pivots you into Cloud Logging, filtered to that exact request. Here, you can read the raw log payload to identify the exact error signature (such as `RESOURCE_EXHAUSTED` or `PERMISSION_DENIED`).



### Cross-reference usage audit logs

If the log payload indicates an IAM issue, a missing scope, or a permission denial, cross-reference your Cloud Audit Logs:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Review the administrative history. Verify if your administrator recently modified an action filter or revoked a required permission.




## Example: Trace a failed data store request

Imagine a user prompts your Gemini Enterprise agent to get the status of a Jira issue, but the agent returns a generic failure message. Here is how you would use the observability workflow to find the root cause:

  1. **Check error trends:** Before looking for individual errors, you want to know how widespread the issue is. Open the **Metrics Explorer** in Cloud Monitoring and filter your data store request metrics by the `tool_id: get_issue`. You may see a massive, sudden spike in `RESOURCE_EXHAUSTED` errors. This confirms it is a systemic issue, not just a one-off user typo.
  2. **Find the failed request:** Open the **Trace Explorer** and set the time filter to the last one hour. In the scatter plot, you notice a cluster of traces with a red error icon indicating failures. Click one of these recent traces to investigate.
  3. **Examine the Gantt chart:** The Gantt chart visualizes the request's journey. You see a successful parent span for the initial agent routing, but nested underneath it is a failing `invoke_connector` span specifically targeting the Jira Cloud data store.
  4. **Pivot to logs:** Click the failing `invoke_connector` span. In the Trace details pane, click **Show logs**.
  5. **Identify the root cause:** The **Logs Explorer** opens, pre-filtered to the exact trace ID. You can now examine the log payload generated by the data store to identify the exact error:
         
         "message": "Connector Error: Cause: Failed to execute spec-based tool 'get_issue': Request failed: HTTP error 403: {\"errorMessages\":[\"permission denied: [User] does not have access to [Resource]"],\"errors\":{}}"
         
         

In this payload error message, you can see the specific tool (`get_issue`) that failed and the explicit message indicating that the user executing the request lacks access to the specific resource in the target system.

  6. **Resolve:** Using the Common errors section, you can identify this as a Missing end-user resource access error. The Gemini Enterprise agent successfully connected to Jira Cloud, but Jira Cloud rejected the query because the user lacks permissions. To resolve this, ask your Jira Cloud administrator to grant the user access to the specific resource.




## Common errors

When reviewing your error payloads in Cloud Logging, focus on the broad error signatures. Most data store errors are fully self-resolvable. Find the error you encountered in the following list to determine the root cause and fix.

### Authentication & access errors

These errors occur when there are issues with credentials, scopes, or administrative policies preventing access to the required resources. If you encounter these errors, Cloud Audit Logs is useful for debugging recent IAM changes, action filter updates, or revoked permissions.

#### Expired or invalid OAuth token

  * **Error Signature:** `HTTP request failed with status code 401 / 401 Unauthorized`
  * **Root Cause:** The OAuth token has expired or is invalid.
  * **Resolution:** Re-authorize the data store in your Gemini Enterprise settings to generate a fresh token.



#### Tool blocked by an action filter

  * **Error Signature:** `Permission "connectors.tool.execute" denied ... rejected by admin filter configuration`
  * **Root Cause:** The administrator has blocked the tool using an action filter.
  * **Resolution:** The administrator must update the action or tool allowlist.



#### Missing OAuth scopes

  * **Error Signatures:** `Access to [Resource] in [Third-Party API] requires [Scope] ... only [Scope] granted` OR `Cause: Insufficient Permission`
  * **Root Cause:** The application registration in the third-party platform is missing the required scopes.
  * **Resolution:** An administrator must grant the exact scopes named in the log and re-authorize the app.



#### Missing IAM project permissions

  * **Error Signature:** `Access Denied: User does not have [permission] / mcp.tools.call permission`
  * **Root Cause:** The caller or service account is missing required Google Cloud IAM permissions in the target project.
  * **Resolution:** Grant the named IAM permission to the caller.



### Performance & throttling errors

These errors are triggered when request volumes exceed the limits set by the target API or service. Cloud Trace helps identify exactly how long these throttled requests are hanging before they fail.

#### Third-party API 429 throttling

  * **Error Signature:** `Cause: Request has been rate limited`
  * **Root Cause:** You are making requests faster than the third-party API allows.
  * **Resolution:** Reduce your request rate, implement backoff strategies, or request a quota increase from the third-party provider.



#### "Enable actions" button is not visible

  * **Error Signature:** **Enable actions** button is not visible or disabled in the console after creating a data store.
  * **Root Cause:** The data store has limited functionality (such as federated search only, ingestion only, or search only) and doesn't support actions.
  * **Resolution:** Actions can't be enabled on these data store types.



### Visibility and resource errors

These errors indicate that while authentication might be successful, the user or application does not have the specific rights to view or interact with the requested data.

#### Third-party visibility restriction

  * **Error Signature:** `422 ... you do not have permission to view [Resource/Users]`
  * **Root Cause:** A visibility restriction or organization policy in the third-party platform is preventing data retrieval.
  * **Resolution:** Adjust your third-party organization membership, or reduce the limit of your query scope.



#### Missing end-user resource access

  * **Error Signature:** `permission denied: [user] does not have access to [Resource]`
  * **Root Cause:** The end-user executing the request lacks access to the specific component or resource in the target system.
  * **Resolution:** Grant the user access to the resource directly within the target system.



### System and server-side errors

These errors result from infrastructure issues, timeouts, or backend misconfigurations and are typically not self-resolvable.

#### Slow or overloaded third-party endpoint

  * **Error Signature:** `context deadline exceeded`
  * **Root Cause:** The third-party endpoint is slow or overloaded, causing the Google-side request to time out.
  * **Resolution:** Retry the request. If the error is persistent, contact Google Cloud Support for timeout tuning.



#### MCP server credential binding misconfiguration

  * **Error Signature:** `CredsPermissionException: auth.creds.useNormalUserEUC not granted / EUC_PRESENTER`
  * **Root Cause:** There is a server-side policy issue where the MCP server credential binding is misconfigured. This is not customer-actionable.
  * **Resolution:** Contact Google Cloud Support.



## Get support

If you encounter a persistent `context deadline exceeded` or a `CredsPermissionException` error, you may need to file a support ticket with Google Cloud Support.

To expedite resolution, please gather the following artifacts from your observability tools before opening a ticket:

  * **From Cloud Logging:** The full JSON log payload of the error.
  * **From Cloud Trace:** The assist token and specific span details (including trace ID) associated with the failed request.
  * **From Usage Audit Logs:** Any relevant IAM modification timestamps or policy changes that might have triggered the issue.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
