---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/slack-audit/
title: Collect Slack Audit logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:16:09.166547+00:00
---

# Collect Slack Audit logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/slack-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Slack Audit logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Slack Audit logs to Google Security Operations using either Google Cloud Run functions or Amazon S3 with AWS Lambda.

Slack Audit Logs provide a detailed record of security-related events across your Slack Enterprise Grid organization. The Audit Logs API lets you monitor user actions such as logins, file downloads, app installations, and administrative changes for compliance and security monitoring purposes.

**Note:** An ingestion label identifies the parser that normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `SLACK_AUDIT` ingestion label.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Slack Enterprise Grid plan with Organization owner access.

**Important:** The app must be installed by the owner of the Enterprise organization. Organization administrator tokens are not supported by the Audit Logs API. Requests made with an organization administrator token fail with a `user_not_authorized` error.
  * Privileged access to either:

    * Google Cloud (for Option 1: Cloud Run functions and Cloud Scheduler), or
    * AWS (for Option 2: S3, IAM, Lambda, EventBridge).

**Note:** The Slack Audit Logs API is **only available for Slack Enterprise Grid** organizations. Standard, Plus, or Business+ plans do not have access to this API. To verify your plan, go to your Slack administration page and check your subscription type.

## Collect Slack credentials

### Create the Slack app

The Slack Audit Logs API requires a User OAuth Token with the `auditlogs:read` scope. This token must be obtained by installing an app at the Enterprise Grid organization level, not at the workspace level.

  1. Sign in to Slack as the owner of your Enterprise Grid organization.
  2. Go to the [Slack API Apps page](https://api.slack.com/apps).
  3. Click **Create New App**.
  4. Select **From scratch**.
  5. Provide the following configuration details: 
     * **App Name** : Enter a descriptive name (for example, `Google SecOps Audit Integration`).
     * **Pick a workspace to develop your app in** : Select your Development Slack Workspace (any workspace in the organization).
  6. Click **Create App**.



### Configure OAuth scopes

  1. In your app's settings page, select **OAuth & Permissions** from the left navigation.
  2. Navigate to the **Scopes** section.
  3. Under **User Token Scopes** (NOT Bot Token Scopes), click **Add an OAuth Scope**.
  4. Add the following scope: 
     * `auditlogs:read` — This scope enables access to the Audit Logs API for the Enterprise Grid organization.
  5. Under **Bot Token Scopes** , click **Add an OAuth Scope**.
  6. Add the following scope: 
     * `users:read` — Present so that the app can be installed at the organization level.

**Note:** The bot scope is not used to collect audit logs. Slack requires the app to carry at least one bot scope before organization-level installation becomes available, and without one the installation fails. Slack documents any bot scope as sufficient; `users:read` is the one this integration has been verified with.

### Install the app on the Enterprise organization

The Audit Logs API reads events for the whole Enterprise organization, so the app must be installed at the organization level rather than in a single workspace. Slack documents two ways to do that. Both produce the same organization-level User OAuth Token. Use one of them.

#### Option A: Install from the app settings (organization-level app)

This is the path from Slack's [Developing apps for Enterprise orgs](https://docs.slack.dev/enterprise/developing-for-enterprise-orgs) page. It needs no redirect URL, no public distribution and no web service.

  1. In your app's settings page, select **Org Level Apps** from the left navigation.
  2. Click **Opt-In**.
  3. At the confirmation prompt, click **Yes, Opt-in**.

**Note:** The opt-in appears in the app manifest as `"org_deploy_enabled": true` and enables private distribution, which lets the app reach every workspace in the organization. The app is not listed in the Slack Marketplace and cannot be installed by anyone outside your organization. If **Opt-In** is not available, confirm that the app has at least one bot scope.
  4. Sign in as the owner of the Enterprise organization.

  5. Select **OAuth & Permissions** from the left navigation.

  6. Click **Install to Organization**.

  7. Review the requested permissions on the confirmation screen and click **Allow**.

**Note:** Installing from the app settings page generates the organization-wide token automatically and shows it on the **OAuth & Permissions** page. You do not need to add the app to individual workspaces: administration APIs such as Audit Logs work at the organization level.



#### Option B: Public distribution and the Sharable URL

This is the path from Slack's [Audit Logs API](https://docs.slack.dev/admins/audit-logs-api/) page. Activating public distribution does not list the app in the Slack Marketplace; it only allows installation outside the development workspace.

  1. In your app's settings page, select **OAuth & Permissions** from the left navigation.
  2. In the **Redirect URLs** section, click **Add New Redirect URL** , enter a URL, click **Add** , and then click **Save URLs**.

**Note:** A redirect URL is required by the distribution checklist. If your organization does not run a web service to complete the OAuth exchange, enter `https://slack.com/oauth/v2/authorize`; the installation started from the Sharable URL then completes on Slack's side and the token appears on the **OAuth & Permissions** page. This is the value verified with customers. If you run your own OAuth callback, enter its URL instead and exchange the returned code with `oauth.v2.access`.
  3. Select **Manage Distribution** from the left navigation.

  4. Under **Share Your App with Other Workspaces** , confirm that all four checklist sections show a green check. If a section shows a red X, expand it and complete the required action.

  5. Select the **I've reviewed and removed any hard-coded information** checkbox.

  6. Click **Activate Public Distribution**.

  7. Sign in as the **Owner** of the Enterprise organization.

  8. Under **Share Your App with Your Workspace** , copy the **Sharable URL** and open it in your browser.

  9. In the installation screen, open the drop-down in the upper right corner and select the **Enterprise organization** , not an individual workspace.

  10. Review the requested permissions and click **Allow**.

**Note:** Apps requesting `auditlogs:read` must be installed by the Owner of the Enterprise organization. If the organization does not appear in the drop-down, verify that you are signed in as the Owner.



### Retrieve credentials

  1. After the installation completes, you return to the **OAuth & Permissions** page.
  2. In the **OAuth Tokens** section, locate the **User OAuth Token**.
  3. The token starts with `xoxp-`.
  4. Click **Copy** and save this token securely.

**Important** : This is your `SLACK_ADMIN_TOKEN` for the Cloud Run function or Lambda function. Store it securely. It provides read access to all audit logs in your Enterprise Grid organization.

  5. Note your **Organization ID** :

     1. Open Slack in a web browser using your organization URL (for example, `acmeinc.enterprise.slack.com`).
     2. After the page loads, read the URL. It has the format `https://app.slack.com/client/EXXXXXXX/CXXXXXXX`.
     3. Copy the string that begins with `E`. That is your organization ID.



### Verify permissions

To verify your app has the required permissions:

  1. Go to the [Slack API Apps page](https://api.slack.com/apps).
  2. Select your app.
  3. Select **OAuth & Permissions** from the left navigation.
  4. Under **OAuth Tokens** , verify that a **User OAuth Token** is displayed (starts with `xoxp-`).
  5. Under **Scopes** , verify that `auditlogs:read` appears under **User Token Scopes**.



### Test API access

  * Test your token before proceeding with the integration:
        
        SLACK_TOKEN="xoxp-your-token-here"
        
        curl -H "Authorization: Bearer $SLACK_TOKEN" \
          "https://api.slack.com/audit/v1/logs?limit=1"
        




A successful response contains an `entries` array with audit log events. If you receive an `invalid_auth` or `missing_scope` error, verify your token and scopes.

## Option 1: Configure Slack Audit Logs export using Google Cloud Run functions

This option uses Google Cloud Run functions and Cloud Scheduler to collect Slack Audit Logs and ingest them directly into Google SecOps using the [Google SecOps ingestion scripts](https://github.com/chronicle/ingestion-scripts).

**Note:** The latest version of the scripts is always available in the [Google SecOps ingestion-scripts GitHub repository](https://github.com/chronicle/ingestion-scripts). Always refer to the repository for the most up-to-date code, dependencies, and configuration. The code shown in this guide is a point-in-time reference.

### Before you begin (Option 1)

Make sure you have the following additional prerequisites:

  * A Google Cloud project with the following APIs enabled: 
    * Cloud Run Admin API
    * Eventarc API
    * Pub/Sub API
    * Cloud Scheduler API
    * Secret Manager API
  * Permissions to create Cloud Run functions, Pub/Sub topics, Eventarc triggers, Cloud Scheduler jobs, and secrets in Secret Manager.
  * A Google SecOps service account JSON file.



### Get the Google SecOps service account

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Click **Download** to download the **ingestion authentication file**.
  4. Save the JSON file securely. You'll upload this as a secret in Google Secret Manager.

**Note:** This JSON file contains credentials that authenticate the Cloud Run function to the Google SecOps ingestion API. Do not share or commit this file to version control.

### Prepare the function code

Download the deployment files from the [Google SecOps ingestion-scripts GitHub repository](https://github.com/chronicle/ingestion-scripts):

  1. From the [`slack`](https://github.com/chronicle/ingestion-scripts/tree/main/slack) folder, download: 
     * `.env.yml`
     * `main.py`
     * `requirements.txt`
  2. From the root of the repository, download the entire [`common`](https://github.com/chronicle/ingestion-scripts/tree/main/common) directory with all its files.

Your deployment directory should have the following structure:
         
         ```
             deployment_directory/
             ├── common/
             │   ├── __init__.py
             │   ├── auth.py
             │   ├── env_constants.py
             │   ├── ingest.py
             │   ├── status.py
             │   └── utils.py
             ├── .env.yml
             ├── main.py
             └── requirements.txt
             ```
         




### Configure secrets in Google Secret Manager

Store sensitive credentials in Secret Manager for secure access by the Cloud Run function.

#### Create a secret for the Google SecOps service account

  1. In the **Google Cloud console** , go to **Security > Secret Manager**.
  2. Click **Create Secret**.
  3. Provide the following configuration details: 
     * **Name** : Enter `chronicle-service-account`.
     * **Secret value** : Paste the entire contents of the Google SecOps service account JSON file.
  4. Click **Create Secret**.
  5. Copy the secret's resource name. The format is:
         
         projects/PROJECT_ID/secrets/chronicle-service-account/versions/latest
         




#### Create a secret for the Slack token

  1. In the **Secret Manager** page, click **Create Secret**.
  2. Provide the following configuration details: 
     * **Name** : Enter `slack-admin-token`.
     * **Secret value** : Paste the Slack User OAuth Token (starts with `xoxp-`).
  3. Click **Create Secret**.
  4. Copy the secret's resource name. The format is:
         
         projects/PROJECT_ID/secrets/slack-admin-token/versions/latest
         




### Configure environment variables

  1. Open the `.env.yml` file in your deployment directory and configure the environment variables:
         
         CHRONICLE_CUSTOMER_ID: "<your-chronicle-customer-id>"
         CHRONICLE_REGION: "us"
         CHRONICLE_SERVICE_ACCOUNT: "projects/<PROJECT_ID>/secrets/chronicle-service-account/versions/latest"
         CHRONICLE_NAMESPACE: ""
         POLL_INTERVAL: "5"
         SLACK_ADMIN_TOKEN: "projects/<PROJECT_ID>/secrets/slack-admin-token/versions/latest"
         

     * Replace the following:

       * `<your-chronicle-customer-id>`: Your Google SecOps customer ID.
       * `<PROJECT_ID>`: Your Google Cloud project ID.
       * `CHRONICLE_REGION`: Set to your Google SecOps region. Valid values: `us`, `asia-northeast1`, `asia-south1`, `asia-southeast1`, `australia-southeast1`, `europe`, `europe-west2`, `europe-west3`, `europe-west6`, `europe-west9`, `europe-west12`, `me-central1`, `me-central2`, `me-west1`, `northamerica-northeast2`, `southamerica-east1`.
       * `POLL_INTERVAL`: Frequency interval (in minutes) at which the function executes. This duration must be the same as the Cloud Scheduler job interval.
  2. Save the `.env.yml` file.




### Create a Pub/Sub topic

Cloud Scheduler triggers the Cloud Run function through a Pub/Sub topic.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. In the **Topic ID** field, enter `slack-audit-trigger`.
  4. Click **Create**.



### Deploy the Cloud Run function

  1. Open a terminal or Cloud Shell in the Google Cloud console. Navigate to your deployment directory and execute the following command:
         
         gcloud run deploy slack-audit-to-chronicle \
           --source . \
           --function main \
           --base-image google-22/python312 \
           --region <REGION> \
           --service-account <SERVICE_ACCOUNT_EMAIL> \
           --env-vars-file .env.yml \
           --memory 512Mi \
           --timeout 540 \
           --max-instances 1 \
           --no-allow-unauthenticated
         

     * Replace `<REGION>` with the region (for example, `us-central1`) and `<SERVICE_ACCOUNT_EMAIL>` with the email address of the service account you want your Cloud Run function to use.
**Note:** The service account running your Cloud Run function must have the **Cloud Run Invoker** (`roles/run.invoker`), **Eventarc Event Receiver** (`roles/eventarc.eventReceiver`), and **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`) roles.
  2. Create the Pub/Sub trigger for the function as follows:

**Note:** The trigger uses Eventarc. If the command reports that the Eventarc API is not enabled, enable it with `gcloud services enable eventarc.googleapis.com` and run the command again.
         
         gcloud eventarc triggers create slack-audit-trigger \
           --location <REGION> \
           --destination-run-service slack-audit-to-chronicle \
           --destination-run-region <REGION> \
           --event-filters "type=google.cloud.pubsub.topic.v1.messagePublished" \
           --transport-topic projects/<PROJECT_ID>/topics/slack-audit-trigger \
           --service-account <SERVICE_ACCOUNT_EMAIL>
         

     * Replace `<PROJECT_ID>` with your Google Cloud project ID.
**Note:** The Slack ingestion script exposes an HTTP-signature function, `def main(request)`, that ignores the request body. The Eventarc Pub/Sub trigger delivers each Pub/Sub message to the service as an HTTP POST, so the script runs unchanged and no code modification is required.
  3. Wait for the deployment to complete.




### Set up Cloud Scheduler

  1. In the **GCP Console** , go to **Cloud Scheduler > Create job**.
  2. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `slack-audit-scheduler`  
**Region** | Select the same region where you deployed the Cloud Run function  
**Frequency** | `*/5 * * * *` (every 5 minutes, matching the `POLL_INTERVAL` value)  
**Timezone** | Select timezone (UTC recommended)  
  3. Click **Continue**.

  4. In the **Configure the execution** section:

     * **Target type** : Select **Pub/Sub**.
     * **Topic** : Select `slack-audit-trigger`.
     * **Message body** : Enter `run`.
  5. Click **Create**.




#### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | Standard (recommended)  
Every 15 minutes | `*/15 * * * *` | Medium volume  
Every hour | `0 * * * *` | Low volume  
**Note:** The `POLL_INTERVAL` environment variable in the Cloud Run function must match the Cloud Scheduler frequency.

### Test the integration (Option 1)

  1. In the **Cloud Scheduler** console, find your job (`slack-audit-scheduler`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run**.
  5. Click the service name (`slack-audit-to-chronicle`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Retrieving the Slack Audit logs since: YYYY-MM-DDTHH:MM:SSZ
         Processing logs...
         Retrieved X audit logs from the API call
         Logs processed successfully.
         




## Option 2: Configure Slack Audit Logs export using AWS S3

This option uses AWS Lambda to collect Slack Audit Logs and store them in Amazon S3, then configures a Google SecOps feed to ingest the logs.

### Before you begin (Option 2)

Make sure you have the following additional prerequisites:

  * An AWS account with permissions to create S3 buckets, IAM users/roles/policies, Lambda functions, and EventBridge rules.



### Create an Amazon S3 bucket

  1. Create an Amazon S3 bucket following the [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) user guide.
  2. Save the bucket **Name** and **Region** for future reference (for example, `slack-audit-logs`).



### Configure IAM policy and roles for S3 uploads

  1. In the **AWS Console** , go to **IAM > Policies > Create policy > JSON** tab.
  2. Copy and paste the following policy. Replace `slack-audit-logs` if you used a different bucket name:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Sid": "AllowPutObjects",
               "Effect": "Allow",
               "Action": "s3:PutObject",
               "Resource": "arn:aws:s3:::slack-audit-logs/*"
             },
             {
               "Sid": "AllowGetStateObject",
               "Effect": "Allow",
               "Action": "s3:GetObject",
               "Resource": "arn:aws:s3:::slack-audit-logs/slack-audit-state.json"
             }
           ]
         }
         

  3. Click **Next**.

  4. Enter the policy name `SlackAuditS3Policy`.

  5. Click **Create policy**.

  6. Go to **IAM > Roles > Create role > AWS service > Lambda**.

  7. Attach the newly created policy `SlackAuditS3Policy`.

  8. Name the role `SlackAuditToS3Role` and click **Create role**.




### Create the Lambda function

  1. In the **AWS Console** , go to **Lambda > Functions > Create function**.
  2. Click **Author from scratch**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `slack_audit_to_s3`  
**Runtime** | Python 3.13  
**Architecture** | x86_64  
**Execution role** | `SlackAuditToS3Role`  
  4. Click **Create function**.

  5. After the function is created, open the **Code** tab, delete the stub and paste the following code (`slack_audit_to_s3.py`).
         
         #!/usr/bin/env python3
         # Lambda: Pull Slack Audit Logs (Enterprise Grid) to S3 (JSONL format)
         import os, json, time, urllib.parse
         from urllib.request import Request, urlopen
         from urllib.error import HTTPError, URLError
         import boto3
         
         BASE_URL = "https://api.slack.com/audit/v1/logs"
         TOKEN = os.environ["SLACK_AUDIT_TOKEN"]
         BUCKET = os.environ["S3_BUCKET"]
         PREFIX = os.environ.get("S3_PREFIX", "slack/audit/")
         STATE_KEY = os.environ.get("STATE_KEY", "slack-audit-state.json")
         LIMIT = int(os.environ.get("LIMIT", "200"))
         MAX_PAGES = int(os.environ.get("MAX_PAGES", "20"))
         LOOKBACK_SEC = int(os.environ.get("LOOKBACK_SECONDS", "3600"))
         HTTP_TIMEOUT = int(os.environ.get("HTTP_TIMEOUT", "60"))
         HTTP_RETRIES = int(os.environ.get("HTTP_RETRIES", "3"))
         RETRY_AFTER_DEFAULT = int(os.environ.get("RETRY_AFTER_DEFAULT", "2"))
         # Optional server-side filters (comma-separated 'action' values)
         ACTIONS = os.environ.get("ACTIONS", "").strip()
         
         s3 = boto3.client("s3")
         
         def _get_state() -> dict:
             try:
                 obj = s3.get_object(Bucket=BUCKET, Key=STATE_KEY)
                 st = json.loads(obj["Body"].read() or b"{}")
                 return {"cursor": st.get("cursor")}
             except Exception:
                 return {"cursor": None}
         
         def _put_state(state: dict) -> None:
             body = json.dumps(state, separators=(",", ":")).encode("utf-8")
             s3.put_object(
                 Bucket=BUCKET, Key=STATE_KEY, Body=body, ContentType="application/json"
             )
         
         def _http_get(params: dict) -> dict:
             qs = urllib.parse.urlencode(params, doseq=True)
             url = f"{BASE_URL}?{qs}" if qs else BASE_URL
             req = Request(url, method="GET")
             req.add_header("Authorization", f"Bearer {TOKEN}")
             req.add_header("Accept", "application/json")
             attempt = 0
             while True:
                 try:
                     with urlopen(req, timeout=HTTP_TIMEOUT) as r:
                         return json.loads(r.read().decode("utf-8"))
                 except HTTPError as e:
                     # Respect Retry-After on 429/5xx
                     if e.code in (429, 500, 502, 503, 504) and attempt < HTTP_RETRIES:
                         retry_after = 0
                         try:
                             retry_after = int(
                                 e.headers.get("Retry-After", RETRY_AFTER_DEFAULT)
                             )
                         except Exception:
                             retry_after = RETRY_AFTER_DEFAULT
                         time.sleep(max(1, retry_after))
                         attempt += 1
                         continue
                     raise
                 except URLError:
                     if attempt < HTTP_RETRIES:
                         time.sleep(RETRY_AFTER_DEFAULT)
                         attempt += 1
                         continue
                     raise
         
         def _write_page(data: dict, page_idx: int) -> str:
             """Extract entries from Slack API response and write as JSONL."""
             entries = data.get("entries") or []
             if not entries:
                 return None
             lines = [json.dumps(entry, separators=(",", ":")) for entry in entries]
             body = "\n".join(lines).encode("utf-8")
             ts = time.strftime("%Y/%m/%d/%H%M%S", time.gmtime())
             key = f"{PREFIX}{ts}-slack-audit-p{page_idx:05d}.json"
             s3.put_object(
                 Bucket=BUCKET, Key=key, Body=body, ContentType="application/json"
             )
             return key
         
         def lambda_handler(event=None, context=None):
             state = _get_state()
             cursor = state.get("cursor")
             params = {"limit": LIMIT}
             if ACTIONS:
                 params["action"] = [a.strip() for a in ACTIONS.split(",") if a.strip()]
             if cursor:
                 params["cursor"] = cursor
             else:
                 # First run (or reset): fetch a recent window by time
                 params["oldest"] = int(time.time()) - LOOKBACK_SEC
             pages = 0
             total = 0
             last_cursor = None
             while pages < MAX_PAGES:
                 data = _http_get(params)
                 _write_page(data, pages)
                 entries = data.get("entries") or []
                 total += len(entries)
                 # Cursor for next page
                 meta = data.get("response_metadata") or {}
                 next_cursor = meta.get("next_cursor") or data.get("next_cursor")
                 if next_cursor:
                     params = {"limit": LIMIT, "cursor": next_cursor}
                     if ACTIONS:
                         params["action"] = [
                             a.strip() for a in ACTIONS.split(",") if a.strip()
                         ]
                     last_cursor = next_cursor
                     pages += 1
                     continue
                 break
             if last_cursor:
                 _put_state({"cursor": last_cursor})
             return {
                 "ok": True,
                 "pages": pages + (1 if total or last_cursor else 0),
                 "entries": total,
                 "cursor": last_cursor,
             }
         
         if __name__ == "__main__":
             print(lambda_handler())
         

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.




### Configure Lambda environment variables

  1. Go to **Configuration > Environment variables > Edit > Add environment variable**.
  2. Enter the following environment variables, replacing with your values:

Key | Example Value  
---|---  
`SLACK_AUDIT_TOKEN` | `xoxp-...` (org-level user token with `auditlogs:read`)  
`S3_BUCKET` | `slack-audit-logs`  
`S3_PREFIX` | `slack/audit/`  
`STATE_KEY` | `slack-audit-state.json`  
`LIMIT` | `200`  
`MAX_PAGES` | `20`  
`LOOKBACK_SECONDS` | `3600`  
`HTTP_TIMEOUT` | `60`  
`HTTP_RETRIES` | `3`  
`RETRY_AFTER_DEFAULT` | `2`  
`ACTIONS` | (optional, comma-separated action filter)  
  3. Click **Save**.

  4. Select the **Configuration** tab. In the **General configuration** panel click **Edit**.

  5. Change **Timeout** to `5 minutes` (300 seconds) and click **Save**.


**Note:** Timeout is a hard upper limit. If the function is still running when the timer reaches 5 minutes, AWS Lambda will terminate it. Any shorter execution finishes normally; you are billed only for the actual run time.

### Create an EventBridge schedule

  1. Go to **Amazon EventBridge > Scheduler > Create schedule**.
  2. Provide the following configuration details: 
     * **Name** : Enter `slack-audit-1h`.
     * **Recurring schedule** : Select **Rate-based schedule**.
     * **Rate expression** : Enter `1 hours`.
     * **Flexible time window** : Select **Off**.
  3. Click **Next**.
  4. Select Target: 
     * **Target API** : Select **AWS Lambda Invoke**.
     * **Lambda function** : Select `slack_audit_to_s3`.
  5. Click **Next**.
  6. Click **Next** (skip optional settings).
  7. Review and click **Create schedule**.



### (Optional) Create a read-only IAM user for Google SecOps

  1. Go to **AWS Console > IAM > Users > Create user**.
  2. Provide the following configuration details: 
     * **User name** : Enter `secops-reader`.
     * **Access type** : Select **Programmatic access**.
  3. Click **Next**.
  4. Select **Attach policies directly**.
  5. Click **Create policy**. In the **JSON** tab, paste:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Action": ["s3:GetObject"],
               "Resource": "arn:aws:s3:::slack-audit-logs/*"
             },
             {
               "Effect": "Allow",
               "Action": ["s3:ListBucket"],
               "Resource": "arn:aws:s3:::slack-audit-logs"
             }
           ]
         }
         

  6. Click **Next**.

  7. Enter the policy name `secops-reader-policy`.

  8. Click **Create policy**.

  9. Return to the user creation page, refresh the policy list, and select `secops-reader-policy`.

  10. Click **Next**.

  11. Click **Create user**.

  12. Select the created user `secops-reader`.

  13. Go to **Security credentials > Access keys > Create access key**.

  14. Select **Third-party service**.

  15. Click **Next**.

  16. Click **Create access key**.

  17. Click **Download .csv file** to save the credentials.




### Configure a feed in Google SecOps to ingest Slack Audit logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Slack Audit Logs`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Slack Audit** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **S3 URI** : Enter the S3 bucket URI with the prefix path:
           
           ```
           s3://slack-audit-logs/slack/audit/
           ```
           
           Replace `slack-audit-logs` with your actual S3 bucket name.
           

     * **Source deletion option** : Select the deletion option according to your preference.

     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Access Key ID** : User access key with access to the S3 bucket (from the `secops-reader` Identity and Access Management (IAM) user).

     * **Secret Access Key** : User secret key with access to the S3 bucket (from the `secops-reader` IAM user).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`action` | `metadata.product_event_type` | Directly mapped from the `action` field  
`actor.type` | `principal.labels` | Directly mapped with key `actor.type`  
`actor.user.email` | `principal.user.email_addresses` | Directly mapped  
`actor.user.id` | `principal.user.product_object_id` | Directly mapped  
`actor.user.id` | `principal.user.userid` | Directly mapped  
`actor.user.name` | `principal.user.user_display_name` | Directly mapped  
`actor.user.team` | `principal.user.group_identifiers` | Directly mapped  
`context.ip_address` | `principal.ip` | Directly mapped  
`context.location.domain` | `about.resource.attribute.labels` | Directly mapped with key `context.location.domain`  
`context.location.id` | `about.resource.id` | Directly mapped  
`context.location.name` | `about.resource.name` | Directly mapped  
`context.location.name` | `about.resource.attribute.labels` | Directly mapped with key `context.location.name`  
`context.location.type` | `about.resource.resource_subtype` | Directly mapped  
`context.session_id` | `network.session_id` | Directly mapped  
`context.ua` | `network.http.user_agent` | Directly mapped  
`context.ua` | `network.http.parsed_user_agent` | Parsed user agent derived from the `context.ua` field  
`country` | `principal.location.country_or_region` | Directly mapped  
`date_create` | `metadata.event_timestamp.seconds` | Epoch timestamp converted to timestamp object  
`details.inviter.email` | `target.user.email_addresses` | Directly mapped  
`details.inviter.id` | `target.user.product_object_id` | Directly mapped  
`details.inviter.name` | `target.user.user_display_name` | Directly mapped  
`details.inviter.team` | `target.user.group_identifiers` | Directly mapped  
`details.reason` | `security_result.description` | Directly mapped; if array, concatenated with commas  
`details.type` | `about.resource.attribute.labels` | Directly mapped with key `details.type`  
`details.type` | `security_result.summary` | Directly mapped  
`entity.app.id` | `target.resource.id` | Directly mapped  
`entity.app.name` | `target.resource.name` | Directly mapped  
`entity.channel.id` | `target.resource.id` | Directly mapped  
`entity.channel.name` | `target.resource.name` | Directly mapped  
`entity.channel.privacy` | `target.resource.attribute.labels` | Directly mapped with key `entity.channel.privacy`  
`entity.file.filetype` | `target.resource.attribute.labels` | Directly mapped with key `entity.file.filetype`  
`entity.file.id` | `target.resource.id` | Directly mapped  
`entity.file.name` | `target.resource.name` | Directly mapped  
`entity.file.title` | `target.resource.attribute.labels` | Directly mapped with key `entity.file.title`  
`entity.huddle.date_end` | `about.resource.attribute.labels` | Directly mapped with key `entity.huddle.date_end`  
`entity.huddle.date_start` | `about.resource.attribute.labels` | Directly mapped with key `entity.huddle.date_start`  
`entity.huddle.id` | `about.resource.attribute.labels` | Directly mapped with key `entity.huddle.id`  
`entity.huddle.participants.0` | `about.resource.attribute.labels` | Directly mapped with key `entity.huddle.participants.0`  
`entity.huddle.participants.1` | `about.resource.attribute.labels` | Directly mapped with key `entity.huddle.participants.1`  
`entity.type` | `target.resource.resource_subtype` | Directly mapped  
`entity.user.email` | `target.user.email_addresses` | Directly mapped  
`entity.user.id` | `target.user.product_object_id` | Directly mapped  
`entity.user.name` | `target.user.user_display_name` | Directly mapped  
`entity.user.team` | `target.user.group_identifiers` | Directly mapped  
`entity.workflow.id` | `target.resource.id` | Directly mapped  
`entity.workflow.name` | `target.resource.name` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`ip` | `principal.ip` | Directly mapped  
`user_agent` | `network.http.user_agent` | Directly mapped  
`user_id` | `principal.user.product_object_id` | Directly mapped  
`username` | `principal.user.product_object_id` | Directly mapped  
| `metadata.event_type` | Defaults to `USER_COMMUNICATION`; set to `USER_CREATION` if action is `user_created`, `USER_LOGIN` if action is `user_login` or `user_login_failed`, `USER_LOGOUT` if action is `user_logout`, `USER_RESOURCE_ACCESS` if action matches `file_`, `USER_RESOURCE_UPDATE_PERMISSIONS` if action matches `app_`, `private_`, `public_`, or `auth_policy_`, `USER_CHANGE_PERMISSIONS` if action matches `pref`, `legal_hold_`, `workflow_`, `channel_`, `user_deactivated`, `user_reactivated`, `role_change_`, or `user_channel_`  
| `metadata.log_type` | Hardcoded to `SLACK_AUDIT`  
| `metadata.product_name` | Set to `Enterprise Grid` if `date_create` exists, otherwise `Audit Logs` if `user_id` exists  
| `metadata.vendor_name` | Hardcoded to `Slack`  
| `extensions.auth.mechanism` | Hardcoded to `REMOTE`  
| `extensions.auth.type` | Set to `SSO` if action contains `user_login` or `user_logout`, otherwise `MACHINE`  
| `security_result.action` | Defaults to `ALLOW`; set to `BLOCK` if action is `user_login_failed`  
| `target.application` | Set to `Slack` if `date_create` exists, otherwise `SLACK` if `user_id` exists  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/slack-audit-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
