---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-bitbucket/
title: Collect Atlassian Bitbucket logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:51:21.838940+00:00
---

# Collect Atlassian Bitbucket logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-bitbucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Atlassian Bitbucket logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to configure Atlassian Bitbucket to push logs to Google Security Operations using webhooks.

Atlassian Bitbucket is a Git-based source code repository hosting service. It provides code collaboration, pull request workflows, and CI/CD pipelines for development teams. Bitbucket supports both cloud and self-hosted (Data Center) deployments.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * An Atlassian Bitbucket Cloud or Data Center instance with administrator access
  * Access to Google Cloud Console (for API key creation)



## Create webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Bitbucket Webhook Logs`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Atlassian Bitbucket** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** (optional): Enter a delimiter to split multi-line events. Common values: 
       * `\n` \- Newline delimiter (most common for NDJSON)
       * Leave empty if each request contains a single event
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



### Generate and save secret key

After creating the feed, you must generate a secret key for authentication:

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. **Copy and save** the secret key securely.

**Important:** The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.

### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. The URL format is:
         
         https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import
         

Where `{region}` is the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`), and `{parent}` is the resource path in the format `projects/<PROJECT_ID>/locations/<LOCATION>/instances/<INSTANCE_ID>/logTypes/<LOG_TYPE>`.

  4. Save this URL for the next steps.

  5. Click **Done**.




## Create Google Cloud API key

Google SecOps requires an API key for authentication. Create a restricted API key in the Google Cloud Console.

### Create the API key

  1. Go to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Google SecOps instance).
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.



### Restrict the API key

  1. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Webhook API Key`)
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** dropdown, search for and select **Google SecOps API**.
  3. Click **Save**.
  4. **Copy** the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Google SecOps API, reducing security risk if the key is compromised.



## Configure Atlassian Bitbucket webhook

### Construct the webhook URL

  * Combine the Google SecOps endpoint URL and API key:
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
        

  * Example:
        
        https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...&secret=abcd1234...
        




### Create webhook in Bitbucket Cloud

  1. Sign in to **Bitbucket Cloud** as a workspace or repository administrator.
  2. Navigate to the repository where you want to configure the webhook.
  3. Go to **Repository settings > Webhooks**.
  4. Click **Add webhook**.
  5. Provide the following configuration details: 
     * **Title** : Enter a descriptive name (for example, `SIEM Webhook`).
     * **URL** : Paste the complete endpoint URL with API key and secret from above.
     * **Status** : Select **Active**.
     * **Triggers** : Select **Choose from a full list of triggers** and select the events to send: 
       * **Repository** : Push, Fork, Commit Comment Created
       * **Pull Request** : Created, Updated, Approved, Unapproved, Merged, Declined, Comment Created
       * **Issue** : Created, Updated, Comment Created
  6. Click **Save**.



### Create webhook in Bitbucket Data Center

  1. Sign in to **Bitbucket Data Center** as a project or repository administrator.
  2. Navigate to the project or repository where you want to configure the webhook.
  3. Go to **Project settings > Webhooks** (for project-level) or **Repository settings > Webhooks** (for repository-level).
  4. Click **Create webhook**.
  5. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `SIEM Webhook`).
     * **URL** : Paste the complete endpoint URL with API key and secret from above.
     * **Status** : Select **Active**.
     * **Events** : Select the events to forward: 
       * **Repository** : Refs changed, Fork, Comment added
       * **Pull Request** : Opened, Source branch updated, Modified, Reviewer updated, Approved, Unapproved, Needs work, Merged, Declined, Deleted, Comment added
  6. Click **Save**.



### Verify webhook delivery

  1. After creating the webhook, perform an action in your repository (for example, push a commit).
  2. Go to **Repository settings > Webhooks**.
  3. Click **View requests** next to your webhook.
  4. Verify that the request shows a **200** status code indicating successful delivery.



For more information, see the [Bitbucket Cloud webhook documentation](https://support.atlassian.com/bitbucket-cloud/docs/manage-webhooks/) or the [Bitbucket Data Center webhook documentation](https://confluence.atlassian.com/bitbucketserver/manage-webhooks-938025878.html).

**Note:** A webhook created at the project level in Bitbucket Data Center is inherited by all repositories in that project.

## Authentication methods reference

Google SecOps webhook feeds support multiple authentication methods. Choose the method that your vendor supports.

### Method 1: Custom headers (Recommended)

If your vendor supports custom HTTP headers, use this method for better security.

  * **Request format:**
        
        POST <ENDPOINT_URL> HTTP/1.1
        Content-Type: application/json
        x-goog-chronicle-auth: <API_KEY>
        x-chronicle-auth: <SECRET_KEY>
        
        {
                "event": "data",
                "timestamp": "2025-01-15T10:30:00Z"
        }
        

  * **Advantages:**

    * API key and secret not visible in URL
    * More secure (headers not logged in web server access logs)
    * Preferred method when vendor supports it



### Method 2: Query parameters

If your vendor does not support custom headers, append credentials to the URL.

  * **URL format:**
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
        

  * **Example:**
        
        https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...&secret=abcd1234...
        

  * **Request format:**
        
        POST <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY> HTTP/1.1
        Content-Type: application/json
        
        {
                "event": "data",
                "timestamp": "2025-01-15T10:30:00Z"
        }
        




**Disadvantages:**

  * Credentials visible in URL
  * May be logged in web server access logs
  * Less secure than headers



### Method 3: Hybrid (URL + Header)

Some configurations use API key in URL and secret key in header.

  * **Request format:**
        
        POST <ENDPOINT_URL>?key=<API_KEY> HTTP/1.1
        Content-Type: application/json
        x-chronicle-auth: <SECRET_KEY>
        
        {
                "event": "data",
                "timestamp": "2025-01-15T10:30:00Z"
        }
        




### Authentication header names

Google SecOps accepts the following header names for authentication:

**For API key:**

  * `x-goog-chronicle-auth` (recommended)
  * `X-Goog-Chronicle-Auth` (case-insensitive)



**For secret key:**

  * `x-chronicle-auth` (recommended)
  * `X-Chronicle-Auth` (case-insensitive)



## Webhook limits and best practices

### Request limits

Limit | Value  
---|---  
**Max request size** | 4 MB  
**Max QPS (queries per second)** | 15,000  
**Request timeout** | 30 seconds  
**Retry behavior** | Automatic with exponential backoff  
  
## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`actor.display_name` | `principal.user.user_display_name` | Value taken from the `actor.display_name` field.  
`actor.nickname` | `principal.user.userid` | Value taken from the `actor.nickname` field.  
`actor.account_id` | `principal.user.product_object_id` | Value taken from the `actor.account_id` field.  
`actor.uuid` | `principal.user.product_object_id` | Value taken from the `actor.uuid` field when `actor.account_id` is not present.  
`actor.links.html.href` | `principal.url` | Value taken from the `actor.links.html.href` field.  
`repository.full_name` | `target.resource.name` | Value taken from the `repository.full_name` field.  
`repository.uuid` | `target.resource.product_object_id` | Value taken from the `repository.uuid` field.  
`repository.links.html.href` | `target.url` | Value taken from the `repository.links.html.href` field.  
`repository.project.key` | `target.resource.attribute.labels` | Added as a key-value pair with key "project_key".  
`repository.project.name` | `target.resource.attribute.labels` | Added as a key-value pair with key "project_name".  
`repository.workspace.slug` | `target.resource.attribute.labels` | Added as a key-value pair with key "workspace".  
`push.changes[].new.name` | `target.resource.attribute.labels` | Added as a key-value pair with key "branch_name".  
`push.changes[].new.target.hash` | `target.resource.attribute.labels` | Added as a key-value pair with key "commit_hash".  
`push.changes[].new.target.message` | `target.resource.attribute.labels` | Added as a key-value pair with key "commit_message".  
`push.changes[].new.target.date` | `target.resource.attribute.labels` | Added as a key-value pair with key "commit_date".  
`push.changes[].new.target.author.raw` | `target.user.email_addresses` | Email address extracted from author raw field.  
`pullrequest.id` | `target.resource.attribute.labels` | Added as a key-value pair with key "pullrequest_id".  
`pullrequest.title` | `target.resource.attribute.labels` | Added as a key-value pair with key "pullrequest_title".  
`pullrequest.state` | `target.resource.attribute.labels` | Added as a key-value pair with key "pullrequest_state".  
`pullrequest.author.display_name` | `target.user.user_display_name` | Value taken from the `pullrequest.author.display_name` field.  
`pullrequest.source.branch.name` | `target.resource.attribute.labels` | Added as a key-value pair with key "source_branch".  
`pullrequest.destination.branch.name` | `target.resource.attribute.labels` | Added as a key-value pair with key "destination_branch".  
`date` | `metadata.event_timestamp` | Parsed as an ISO8601 timestamp. Used as event timestamp when present in the webhook payload.  
| `metadata.event_type` | Set to "GENERIC_EVENT" initially. Changed to "USER_RESOURCE_ACCESS", "USER_RESOURCE_UPDATE_CONTENT", or "USER_UNCATEGORIZED" based on the event key and presence of principal and target fields.  
| `metadata.product_event_type` | Set based on the `X-Event-Key` webhook header value (for example, `repo:push`, `pullrequest:created`, `pullrequest:updated`).  
| `metadata.product_name` | Set to "Atlassian Bitbucket".  
| `metadata.vendor_name` | Set to "Atlassian".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/atlassian-bitbucket-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
