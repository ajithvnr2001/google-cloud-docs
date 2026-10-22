---
url: https://docs.cloud.google.com/apigee/docs/api-security/security-actions/
title: Security actions overview and UI \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:31:53.592315+00:00
---

# Security actions overview and UI  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-security/security-actions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Security actions overview and UI Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Preview — Advanced API Security Actions**

This feature is covered by the [Pre-GA Offerings Terms](https://cloud.google.com/terms/service-terms#1) of the Google Cloud Terms of Service. Pre-GA features may have limited support, and changes to pre-GA features may not be compatible with other pre-GA versions. For more information, see the [ launch stage descriptions](https://cloud.google.com/products#product-launch-stages).

Support for the Preview launch of Advanced API Security Actions is available through the [ Apigee - Google Cloud Community](https://www.googlecloudcommunity.com/gc/Apigee/bd-p/cloud-apigee) forum. 

Advanced API Security **security actions** let you configure security actions defining how Apigee handles _traffic_. For example, you can create a security action to deny requests from an IP address that has been identified by Abuse Detection as abuse and block them from accessing your APIs. 

To use this feature, you must enable the add-on. If you are a Subscription customer, you can enable the add-on for your organization. See [ Manage Advanced API Security for Subscription organizations](https://docs.cloud.google.com/apigee/docs/api-security/enable-security#manage-advanced-api-security-for-subscription-organizations) for more details. If you are a Pay-as-you-go customer, you can enable the add-on in your eligible environments. For more information, see [ Manage the Advanced API Security add-on](https://docs.cloud.google.com/apigee/docs/api-platform/reference/manage-security-add-on).

This page provides an overview of the security action functionality and how to use it from the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee). You can also manage security actions using the [Security actions API](https://docs.cloud.google.com/apigee/docs/api-security/security-actions-api) or through [Terraform](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_security_action).

Also, see [ Required roles for security actions](https://docs.cloud.google.com/apigee/docs/api-security/enable-security#required-roles-for-security-actions) for the roles needed to perform security actions tasks.

**Note:** Security actions is available for Apigee and Apigee hybrid versions 1.11 and later.

## How security actions work

With security actions, you can explicitly allow, deny, or flag requests based on specific conditions. Apigee applies these actions to requests before your API proxies process them. Typically, you take action either because requests conform to patterns of unwanted behavior, or (in the case of the allow action) because you want to override a deny action for specific traffic.

The flag action allows requests to pass to your APIs, but adds up to five headers to flagged requests, so you can track them to observe their behavior.

**Note:** Blocked and flagged requests count toward your API call volume. 

One way to identify which requests to take action on is to use the **Abuse detection** [Detected traffic](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#detected-traffic) or [Incident](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#attributes) views, which show IP addresses and API keys that are sources of abuse.

### Security actions

You can take the following types of security actions.

Action type | Description | Precedence order  
---|---|---  
Allow | Allows certain requests that would otherwise be blocked by a deny action. For example, suppose you have created a security action to deny traffic that has been tagged with a detection rule. You could create an allow action to override the deny action for requests with some specific conditions. | 1  
Deny | Blocks all requests that meet the conditions of the action, for example, originating at a specified IP address. When you choose to deny requests, Apigee responds to the client with a response code that you can choose. | 2  
Flag | Flag requests that meet the specified condition so that your backend services can take action on them. When you flag a client's requests, Apigee adds up to five headers, which you define, to the request. Your backend services can process the API calls according to these flags, for example, by redirecting the calls to a different flow. The flag action provides a way to signal your backend services that an API call is suspicious. | 3  
  
### Precedence order

When a request meets the condition of more than one security action, the precedence order of the actions determines which action is performed. For example, suppose a request meets the conditions of both an allow and a deny action. Since the precedence order of an allow action is 1 and the precedence order of a deny action is 2, the allow action takes precedence, so the request is allowed access to the API.

As an example, you might want to allow requests from the IP address of an internal or trusted client, even if those requests matched a separate deny action. The precedence order ensures that an allow action for the trusted IP address would override any deny action.

**Note:** If you are using both security actions and the [AccessControl policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-control-policy) to manage traffic based on IP address, the security action always executes before the AccessControl policy. After that, neither impacts the other; the security action has no influence on the AccessControl policy and vice versa.

### Proxy-specific security actions

A security action can apply to all proxies in an environment or only to a specific proxy or proxies within the environment. See [ Limitations on security actions](https://docs.cloud.google.com/apigee/docs/api-security/security-actions#limitations-on-security-actions) for limitations on proxy-specific security actions.

### Security action statuses

Each security action has a status:

  * **Enabled** : The security action is active and affects API requests so long as it is not also expired.
  * **Disabled** : The security action is inactive and does not affect API requests.
  * **Paused** : The security action is inactive and does not affect API requests.



## Limitations on security actions

Security actions are enforced at the Apigee environment level. For each environment, security actions have the following limitations:

  * At most 1,000 enabled actions for an environment are allowed at any time. Enabled actions that are also expired count toward this limit.
  * You can add at most 5 flag headers for each action.
  * Proxy-specific security actions support a maximum of 100 proxies.
  * Proxy-specific security actions are not supported in Apigee hybrid at this time.
  * Multiple security actions with the same name are not supported. It might be possible to create multiple actions with the same name by creating multiple actions in rapid successsion. In that case, only the most recent action with that name is effective.



## Latencies

Security actions have the following latencies:

  * When you create, edit, or delete a security action, it can take up to 10 minutes for the change to take effect. Once a new action has taken effect _and_ has been applied to some API traffic, you will be able to view the action's effects in the Security action details page. **Note:** It's not possible to determine whether an action has taken effect from the Security action details page unless the action has been applied to some API traffic.
  * Enabled security actions incur a small increase (less than 2 percent) in API proxy response time.



## Manage security actions in the UI

This section describes how to use the **Security actions** page in the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee). You can also manage security actions using the [Security actions API](https://docs.cloud.google.com/apigee/docs/api-security/security-actions-api).

### Open the **Security actions** page

To open the **Security actions** page:

In the Google Cloud console, go to the **Apigee > Advanced API security > Security actions** page.

[Go to Security actions](https://console.cloud.google.com/apigee/apiSecurity/securityActions)

This opens the main **Security actions** page:

![Security actions main page.](https://docs.cloud.google.com/static/apigee/docs/api-security/images/security-actions-main-view.png)**Note:** The image above shows security actions that have already been created. If you have not yet created any security actions, no rows will be displayed in the table.

In the **Security actions** page you can:

  * Create a new security action.
  * Edit an existing security action.
  * Enable or disable security actions.
  * Pause all or some enabled security actions.
  * Delete security actions.



The **Security actions** page displays a list of security actions, with the following details:

  * **Name** : The name of the security action. Click the name to view the action's details.
  * **Status** : The status of the action. See Security action statuses.
  * **Action** : The security action type.
  * **Expiration (UTC)** : The expiration date of the action.
  * **Last updated (UTC)** : The last date and time the action was updated.
  * A three-dot menu where you can edit, disable, enable, or delete the action.



### Create or edit a security action

This section explains how to create or edit a security action. Note that you can't change the security action name or environment once you've created it. 

**Note:** Security actions for environments created before April 2024 are paused by default, so you might need to resume them. See  Enable, disable, pause, or delete security actions for information.

To create or edit a security action:

  1. Open the **Security actions** page.
  2. To create a new security action, click **Create** at the top of the page. To edit an existing security action, either click Edit in the three-dot menu for that action in the actions list or select the action and select **Edit** at the top of the page.
  3. Under **General settings** , enter or edit the following settings: 
     * **Name:** A name for the security action.
     * **Description (optional):** A brief description of the action.
     * **Environment:** The environment in which you want to create the security action.
     * **Proxies (optional):** The proxies that you want the security action to apply to. Limit the proxy list by name using the **Filter** field. 
       * Leave the **Proxies** field empty to apply the security action to all current and future proxies in the environment.
       * Select individual proxies to apply the security action to only those proxies regardless of any new proxies added to the environment later.
       * Use **Select all** to select all _current_ proxies in the environment. Any proxies added later will not be automatically included in the rule.
     * **Expiration:** The date and time when the action expires, if any. Select either **Never** , or **Custom** , and then enter the date and time when you want the action to expire. You can also modify the time zone.

![Create security action view.](https://docs.cloud.google.com/static/apigee/docs/api-security/images/create-security-action.png)

  4. Click **Next** to display the **Rule** section. In this section, enter or edit: 
     * **Action type:** The type of security action: 
       * **Allow:** The request is allowed.
       * **Deny:** The request is denied. If you select **Deny** , you can also specify the response code that is returned when a request is denied. This can be either: 
         * **Predefined:** Select an HTTP code.
         * **Custom:** Enter a response code.
       * **Flag:** The request is allowed, but also flagged with a special HTTP header that a proxy looks for to determine whether the request requires special handling. To define the header, under **Headers** If you select **Flag** , you can also create the following under **Headers** : 
         * **Header name**
         * **Header value**
     * **Conditions:** The conditions under which the security action is carried out. Under **New condition** , enter the following: 
       * **Condition type:** Can be either **Detection rules** or one of the following attributes: 
         * **IP addresses/CIDR ranges** , which can include IP addresses and IPv4 CIDR ranges at the same time.
         * **API keys** , one or more API keys.
         * **API products** , one or more Apigee API products.
         * **Access tokens** , one or more access tokens.
         * **Developers** , one or more Apigee developer email addresses.
         * **Developer apps** , one or more Apigee developer apps.
         * **User agents** , one or more user agents.
         * **HTTP methods** , [HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) such as GET or PUT.
         * **Region codes** , a list of region codes to act on. See [ISO 3166-1 alpha-2 codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). 
         * **Autonomous system numbers** (ASN), a list of ASN numbers to act on, such as "23". See [Autonomous system (Internet)](https://en.wikipedia.org/wiki/Autonomous_system_\(Internet\)). 
**Notes:**
         * For the condition types **Detection rules** and **IP addresses/CIDR ranges** , you can create at most two conditions that have those types. For any other condition type, you can create at most one condition.
         * To use the **API keys** , **API products** , **access tokens** , **developers** , or **developer apps** conditions, you need to also use either the [ Verify API Key](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy) policy or the [ OAuthV2](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy) policy. See [ How API keys work](https://docs.cloud.google.com/apigee/docs/api-platform/security/api-keys#howapikeyswork) for more information.
         * For Apigee hybrid, these conditions are available in version 1.12 and later: API keys, API products, access tokens, developers, developer apps, and user agents. These conditions are available in version 1.13 and later: autonomous system numbers, CIDR ranges, HTTP methods, and region codes.
       * **Values:** Enter one of the following: 
         * If **Condition type** is **Detection rules** , select a set of [detection rules](https://docs.cloud.google.com/apigee/docs/api-security/detection-rules) that a request must have triggered for the security action to be applied to it.
         * If **Condition type** is an attribute, enter the values of the attribute that you want the security action to be applied to. For example, if the attribute is **IP addresses/CIDR ranges** , enter the IP addresses of the sources of the requests you want the security action to be applied to. You can enter a comma-separated list of either IPv4 and IPv6 addresses.
  5. Click **Create** to create the security action.



### Enable, disable, pause, or delete security actions

This section describes how to change the status of a security action from the **Security actions** page. See Security action statuses for information on each status type and how it affects actions on API requests.

These are the actions you can take to change statuses:

  * To _disable_ an active security action, either click the three-dot menu in the row for the action and select **Disable** or click the security action name and click **Disable** at the top of the page.
  * To _enable_ a security action, either click the three-dot menu in the row for the action and select **Enable** or click the security action name and click **Enable** at the top of the page.
  * To _pause_ all active security actions to temporarily inactivate them, click **Pause Enabled Actions** at the top of the page security actions list. To _resume_ all paused actions, click **Resume Paused Actions** at the top of the page.**Note:** When you resume all enabled actions, any disabled actions remain disabled.



You can also _delete_ a security action. Deleting it permanently removes it from your configuration. To delete a security action, click the three-dot menu in the row for the action and select **Delete** or click the security action name and click **Delete** at the top of the page.

## View security action details

To view recent API traffic data related to a security action, click the security action name in the main Security actions page. This displays the Security action details page, which has two tabs, **Overview** and **Attributes**. 

### Overview

Select the **Overview** tab to display the **Overview** page:

![Security actions details page.](https://docs.cloud.google.com/static/apigee/docs/api-security/images/security-action-details.png)

The **Overview** page displays information about recent API traffic during the time period you select at the top of the page: 12 hours, 1 day, 1 week, or 2 weeks.

The page displays the following traffic data:

  * **Action type** : Deny, allow, or flag. See Security actions for information on the action types.
  * **Total environment traffic:** The total number of requests in the environment.
  * **Total detected event traffic:** The number of requests which were "detected" (triggered an abuse rule) in the environment.
  * Total traffic affected by the action: 
    * For a deny action, the number of denied requests.
    * For a flag action, the number of flagged requests.
    * For an allow action, the number of allowed requests.



The page also displays the following graphs:

  * **Environment traffic trends** : Graphs of detected traffic, flagged traffic, and total environment traffic. This graph is restricted to a recent time interval that contains all observed traffic. This interval might be shorter than the interval you select.
  * **Top rules**
  * **Top countries**
  * **Action details**



### Attributes

Select the **Attributes** tab to display the **Attributes** page.

The **Attributes** page displays data for the security action by _attributes_ —also known as [dimensions](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#dimensions)— which are groupings of the data that let you view the security action in different ways. For example, the API products attribute lets you view the security action by API product.

The information displayed in the **Attributes** page is similar the **Attributes** view for the Abuse detection [Incident details attributes](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#attributes). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
