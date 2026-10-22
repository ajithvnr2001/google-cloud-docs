---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lenel-onguard/
title: Collect LenelS2 OnGuard logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:17.155377+00:00
---

# Collect LenelS2 OnGuard logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lenel-onguard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect LenelS2 OnGuard logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect logs from LenelS2 (Honeywell) OnGuard and forward them to Google Security Operations using a webhook feed. Because OnGuard does not natively support direct webhook or HTTP POST delivery, this guide uses a custom middleware script that polls the OnGuard OpenAccess REST API for events and forwards them to the Google SecOps webhook ingestion endpoint.

LenelS2 OnGuard is a physical access control and badge management system that manages cardholders, credentials, readers, panels, and access events across enterprise facilities. The OpenAccess REST API provides programmatic access to OnGuard data including logged events such as access granted, access denied, door held open, door forced open, and alarm events.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * An OnGuard server (version 7.5 or later) with the OpenAccess license activated
  * The following OnGuard services running on the OpenAccess server:

    * LS Communication Server
    * LS Event Context Provider
    * LS Web Event Bridge
    * LS OpenAccess
    * LS Web Service
  * An internal OnGuard user account with the following minimum permissions:

    * **System Permissions** : Under **Access control hardware** , **Query** permission on **Access Panels** , **Readers** , and **Alarm Panels**
    * **System Permissions** : Under **Access control** , **Query** permission on **Segments**
    * **Monitor Permissions** : Under **Control** , **Open doors** and **Relay and reader outputs**
  * Network connectivity from the middleware host to the OnGuard server on TCP port `8080` (default OpenAccess port)

  * Network connectivity from the middleware host to the internet (to reach the Google SecOps webhook endpoint)

  * Python 3.8 or later installed on the middleware host

  * Access to Google Cloud Console (for API key creation)




## Create webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `LenelS2 OnGuard Events`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Lenel OnGuard** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** : Enter `\n` (newline delimiter, because the middleware sends events in NDJSON format)
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



### Generate and save secret key

After creating the feed, you must generate a secret key for authentication:

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. **Copy and save** the secret key securely.

**Note:** The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.

### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. The URL format is:
         
         https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import
         

Where `{region}` is the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`), and `{parent}` is the resource path in the format `projects/<PROJECT_ID>/locations/<LOCATION>/instances/<INSTANCE_ID>/logTypes/<LOG_TYPE>`.

  4. Save this URL for the next steps.

  5. Click **Done**.




## Create Google Cloud API key

Chronicle requires an API key for authentication. Create a restricted API key in the Google Cloud Console.

### Create the API key

  1. Go to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Chronicle instance).
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.



### Restrict the API key

  1. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Chronicle Webhook API Key`)
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** dropdown, search for and select **Google SecOps API** (or **Chronicle API**).
  3. Click **Save**.
  4. **Copy** the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Chronicle API, reducing security risk if the key is compromised.

## Verify OnGuard OpenAccess prerequisites

Before configuring the middleware, verify that the OnGuard OpenAccess API is operational.

### Verify the OpenAccess service is running

  1. On the OnGuard server, open **Windows Services** (`services.msc`).
  2. Confirm that the following services are running: 
     * **LS OpenAccess**
     * **LS Communication Server**
     * **LS Event Context Provider**
     * **LS Web Event Bridge**
     * **LS Web Service**
     * **LS Message Broker** (RabbitMQ)
  3. If any service is stopped, right-click the service and select **Start**.



### Verify the OpenAccess API is accessible

  1. Open a web browser on the middleware host.
  2. Navigate to the following URL:
         
         https://<ONGUARD_SERVER>:8080/api/access/onguard/openaccess/version?version=1.0
         

  3. Replace `<ONGUARD_SERVER>` with the IP address or hostname of your OnGuard server.

  4. The API returns a JSON response containing the OpenAccess version details, confirming the service is accessible.




### Retrieve the authentication directory

  1. Send a GET request to retrieve the available authentication directories:
         
         https://<ONGUARD_SERVER>:8080/api/access/onguard/openaccess/directories?version=1.0
         

  2. The response contains a list of directories. Note the `ID` and `Name` of the directory you will use for authentication (typically the internal OnGuard directory).




### Verify the OnGuard user account

  1. Open the **OnGuard System Administration** application on the OnGuard server.
  2. Navigate to **Administration > Users**.
  3. Select the user account designated for API access.
  4. Click the **Permissions** tab.
  5. Under **System Permission Group** , confirm the following permissions are enabled: 
     * Under **Access control hardware** : **Query** on **Access Panels** , **Readers** , and **Alarm Panels**
     * Under **Access control** : **Query** on **Segments**
  6. Under **Monitor Permission Group** , confirm the following permissions are enabled: 
     * Under **Control** : **Open doors**
     * Under **Control** : **Relay and reader outputs**



### Obtain an Application ID

Each application using the OpenAccess API must have a unique Application ID. This is a string value you define (for example, `ChronicleForwarder`). The Application ID is sent as the `Application-Id` HTTP header with every API request.

## Configure the OnGuard-to-Chronicle middleware

Because OnGuard does not natively support outbound webhooks or HTTP POST delivery, a middleware script is required to poll the OpenAccess REST API for logged events and forward them to the Google SecOps webhook endpoint.

### Construct the Chronicle webhook URL

  * Combine the Chronicle endpoint URL and API key:
        
        <ENDPOINT_URL>?key=<API_KEY>
        

  * **Example:**
        
        https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...
        




### Create the middleware script

  1. On the middleware host, create a directory for the script:
         
         mkdir -p /opt/onguard-chronicle-forwarder
         cd /opt/onguard-chronicle-forwarder
         

  2. Install the required Python package:
         
         pip3 install requests
         

  3. Create the forwarder script:
         
         nano onguard_to_chronicle.py
         

  4. Add the following content to the script:
         
         #!/usr/bin/env python3
         """LenelS2 OnGuard to Google SecOps (Chronicle) Event Forwarder.
         
         Polls the OnGuard OpenAccess REST API for logged events and forwards
         them to a Chronicle webhook ingestion endpoint.
         """
         
         import json
         import logging
         import os
         import sys
         import time
         from datetime import datetime, timedelta, timezone
         
         import requests
         import urllib3
         
         # Suppress SSL warnings if using self-signed certificates
         urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
         
         # ── Configuration ──────────────────────────────────────────────────
         ONGUARD_HOST = os.environ.get("ONGUARD_HOST", "192.168.1.100")
         ONGUARD_PORT = os.environ.get("ONGUARD_PORT", "8080")
         ONGUARD_USERNAME = os.environ.get("ONGUARD_USERNAME", "")
         ONGUARD_PASSWORD = os.environ.get("ONGUARD_PASSWORD", "")
         ONGUARD_DIRECTORY_ID = os.environ.get("ONGUARD_DIRECTORY_ID", "")
         APPLICATION_ID = os.environ.get("APPLICATION_ID", "ChronicleForwarder")
         VERIFY_SSL = os.environ.get("VERIFY_SSL", "false").lower() == "true"
         
         CHRONICLE_ENDPOINT = os.environ.get("CHRONICLE_ENDPOINT", "")
         CHRONICLE_API_KEY = os.environ.get("CHRONICLE_API_KEY", "")
         CHRONICLE_SECRET_KEY = os.environ.get("CHRONICLE_SECRET_KEY", "")
         
         POLL_INTERVAL_SECONDS = int(os.environ.get("POLL_INTERVAL_SECONDS", "30"))
         PAGE_SIZE = int(os.environ.get("PAGE_SIZE", "100"))
         LOOKBACK_MINUTES = int(os.environ.get("LOOKBACK_MINUTES", "5"))
         
         # ── Logging ────────────────────────────────────────────────────────
         logging.basicConfig(
             level=logging.INFO,
             format="%(asctime)s [%(levelname)s] %(message)s",
             handlers=[
                 logging.StreamHandler(sys.stdout),
                 logging.FileHandler("/opt/onguard-chronicle-forwarder/forwarder.log"),
             ],
         )
         logger = logging.getLogger(__name__)
         
         BASE_URL = f"https://{ONGUARD_HOST}:{ONGUARD_PORT}/api/access/onguard/openaccess"
         
         class OnGuardClient:
             """Client for the OnGuard OpenAccess REST API."""
         
             def __init__(self):
                 self.session_token = None
                 self.headers = {
                     "Content-Type": "application/json",
                     "Application-Id": APPLICATION_ID,
                 }
         
             def authenticate(self):
                 """Authenticate to OpenAccess and obtain a session token."""
                 url = f"{BASE_URL}/authentication?version=1.0"
                 payload = {
                     "user_name": ONGUARD_USERNAME,
                     "password": ONGUARD_PASSWORD,
                     "directory_id": ONGUARD_DIRECTORY_ID,
                 }
                 try:
                     resp = requests.post(
                         url,
                         headers=self.headers,
                         json=payload,
                         verify=VERIFY_SSL,
                         timeout=30,
                     )
                     resp.raise_for_status()
                     data = resp.json()
                     self.session_token = data.get("session_token")
                     self.headers["Session-Token"] = self.session_token
                     logger.info("Successfully authenticated to OnGuard OpenAccess.")
                 except requests.exceptions.RequestException as exc:
                     logger.error("Authentication failed: %s", exc)
                     raise
         
             def keepalive(self):
                 """Renew the session idle timeout."""
                 url = f"{BASE_URL}/keepalive?version=1.0"
                 try:
                     resp = requests.get(
                         url, headers=self.headers, verify=VERIFY_SSL, timeout=15
                     )
                     resp.raise_for_status()
                 except requests.exceptions.RequestException:
                     logger.warning("Keepalive failed. Re-authenticating.")
                     self.authenticate()
         
             def get_logged_events(self, start_time, page_number=1):
                 """Retrieve a page of logged events since start_time."""
                 url = f"{BASE_URL}/logged_events?version=1.0"
                 params = {
                     "filter": f"timestamp >= '{start_time}'",
                     "page_number": page_number,
                     "page_size": PAGE_SIZE,
                     "order_by": "timestamp",
                 }
                 try:
                     resp = requests.get(
                         url,
                         headers=self.headers,
                         params=params,
                         verify=VERIFY_SSL,
                         timeout=30,
                     )
                     resp.raise_for_status()
                     return resp.json()
                 except requests.exceptions.RequestException as exc:
                     logger.error("Failed to retrieve logged events: %s", exc)
                     return None
         
             def logout(self):
                 """Logout and invalidate the session token."""
                 url = f"{BASE_URL}/authentication?version=1.0"
                 try:
                     requests.delete(
                         url, headers=self.headers, verify=VERIFY_SSL, timeout=15
                     )
                     logger.info("Logged out of OnGuard OpenAccess.")
                 except requests.exceptions.RequestException:
                     pass
         
         def send_to_chronicle(events):
             """Send a batch of events to the Chronicle webhook endpoint."""
             if not events:
                 return True
         
             url = f"{CHRONICLE_ENDPOINT}?key={CHRONICLE_API_KEY}"
             headers = {
                 "Content-Type": "application/json",
                 "x-chronicle-auth": CHRONICLE_SECRET_KEY,
             }
             # Send events as NDJSON (newline-delimited JSON)
             body = "\n".join(json.dumps(event) for event in events)
         
             try:
                 resp = requests.post(url, headers=headers, data=body, timeout=30)
                 resp.raise_for_status()
                 logger.info("Sent %d events to Chronicle.", len(events))
                 return True
             except requests.exceptions.RequestException as exc:
                 logger.error("Failed to send events to Chronicle: %s", exc)
                 return False
         
         def main():
             """Main polling loop."""
             logger.info("Starting OnGuard-to-Chronicle forwarder.")
             client = OnGuardClient()
             client.authenticate()
         
             last_poll_time = datetime.now(timezone.utc) - timedelta(minutes=LOOKBACK_MINUTES)
         
             while True:
                 try:
                     current_time = datetime.now(timezone.utc)
                     start_time_str = last_poll_time.strftime("%Y-%m-%dT%H:%M:%SZ")
         
                     all_events = []
                     page = 1
                     while True:
                         result = client.get_logged_events(start_time_str, page_number=page)
                         if result is None:
                             # Session may have expired; re-authenticate
                             client.authenticate()
                             result = client.get_logged_events(
                                 start_time_str, page_number=page
                             )
                             if result is None:
                                 break
         
                         events = result.get("logged_events", [])
                         if not events:
                             break
                         all_events.extend(events)
         
                         total = result.get("total_items", 0)
                         if page * PAGE_SIZE >= total:
                             break
                         page += 1
         
                     if all_events:
                         success = send_to_chronicle(all_events)
                         if success:
                             last_poll_time = current_time
                     else:
                         last_poll_time = current_time
                         logger.debug("No new events found.")
         
                     # Send keepalive to maintain session
                     client.keepalive()
         
                 except KeyboardInterrupt:
                     logger.info("Shutting down.")
                     client.logout()
                     sys.exit(0)
                 except Exception as exc:
                     logger.error("Unexpected error: %s", exc)
                     try:
                         client.authenticate()
                     except Exception:
                         pass
         
                 time.sleep(POLL_INTERVAL_SECONDS)
         
         if __name__ == "__main__":
             main()
         

  5. Save and close the file.




### Configure environment variables

  1. Create an environment file for the forwarder:
         
         nano /opt/onguard-chronicle-forwarder/.env
         

  2. Add the following configuration values:
         
         ONGUARD_HOST=<ONGUARD_SERVER_IP_OR_HOSTNAME>
         ONGUARD_PORT=8080
         ONGUARD_USERNAME=<ONGUARD_API_USERNAME>
         ONGUARD_PASSWORD=<ONGUARD_API_PASSWORD>
         ONGUARD_DIRECTORY_ID=<DIRECTORY_ID>
         APPLICATION_ID=ChronicleForwarder
         VERIFY_SSL=false
         CHRONICLE_ENDPOINT=<CHRONICLE_WEBHOOK_ENDPOINT_URL>
         CHRONICLE_API_KEY=<GOOGLE_CLOUD_API_KEY>
         CHRONICLE_SECRET_KEY=<CHRONICLE_FEED_SECRET_KEY>
         POLL_INTERVAL_SECONDS=30
         PAGE_SIZE=100
         LOOKBACK_MINUTES=5
         

     * **ONGUARD_HOST** : The IP address or hostname of the OnGuard server running the OpenAccess service (for example, `192.168.1.100`)
     * **ONGUARD_PORT** : The port the OpenAccess service listens on (default: `8080`)
     * **ONGUARD_USERNAME** : The OnGuard internal user account username
     * **ONGUARD_PASSWORD** : The password for the OnGuard user account
     * **ONGUARD_DIRECTORY_ID** : The directory ID retrieved from the `GET /directories` endpoint
     * **APPLICATION_ID** : A unique identifier for this integration (for example, `ChronicleForwarder`)
     * **VERIFY_SSL** : Set to `true` if the OnGuard server uses a trusted SSL certificate, or `false` for self-signed certificates
     * **CHRONICLE_ENDPOINT** : The webhook endpoint URL from the Chronicle feed configuration
     * **CHRONICLE_API_KEY** : The Google Cloud API key created earlier
     * **CHRONICLE_SECRET_KEY** : The secret key generated during Chronicle feed creation
     * **POLL_INTERVAL_SECONDS** : How frequently (in seconds) to poll for new events (default: `30`)
     * **PAGE_SIZE** : Number of events to retrieve per API page (default: `100`, maximum: `1000`)
     * **LOOKBACK_MINUTES** : On initial startup, how many minutes of historical events to retrieve (default: `5`)
  3. Secure the environment file:
         
         chmod 600 /opt/onguard-chronicle-forwarder/.env
         




### Install as a systemd service

  1. Create a systemd service file:
         
         sudo nano /etc/systemd/system/onguard-chronicle-forwarder.service
         

  2. Add the following content:
         
         [Unit]
         Description=LenelS2 OnGuard to Chronicle Event Forwarder
         After=network.target
         
         [Service]
         Type=simple
         User=root
         WorkingDirectory=/opt/onguard-chronicle-forwarder
         EnvironmentFile=/opt/onguard-chronicle-forwarder/.env
         ExecStart=/usr/bin/python3 /opt/onguard-chronicle-forwarder/onguard_to_chronicle.py
         Restart=always
         RestartSec=10
         
         [Install]
         WantedBy=multi-user.target
         

  3. Enable and start the service:
         
         sudo systemctl daemon-reload
         sudo systemctl enable onguard-chronicle-forwarder.service
         sudo systemctl start onguard-chronicle-forwarder.service
         

  4. Verify the service is running:
         
         sudo systemctl status onguard-chronicle-forwarder.service
         

  5. Check the forwarder log for successful operation:
         
         tail -f /opt/onguard-chronicle-forwarder/forwarder.log
         

A successful startup shows:
         
         Starting OnGuard-to-Chronicle forwarder.
         Successfully authenticated to OnGuard OpenAccess.
         Sent <N> events to Chronicle.
         




## OpenAccess API reference

The middleware uses the following OnGuard OpenAccess REST API endpoints. All endpoints are relative to `https://<ONGUARD_SERVER>:8080/api/access/onguard/openaccess`.

### Authentication

Method | Endpoint | Description  
---|---|---  
`POST` | `/authentication?version=1.0` | Login and retrieve a session token  
`DELETE` | `/authentication?version=1.0` | Logout and invalidate the session token  
`GET` | `/directories?version=1.0` | Get available authentication directories  
`GET` | `/keepalive?version=1.0` | Renew the session idle timeout  
  
**Required HTTP headers for all authenticated requests:**

Header | Description  
---|---  
`Application-Id` | Unique application identifier string (for example, `ChronicleForwarder`)  
`Session-Token` | Session token returned by `POST /authentication`  
`Content-Type` | `application/json`  
  
### Events

Method | Endpoint | Description  
---|---|---  
`GET` | `/logged_events?version=1.0` | Retrieve a page of logged events  
`POST` | `/event_subscriptions?version=1.0` | Create a real-time event subscription  
`GET` | `/event_subscriptions?version=1.0` | List event subscriptions  
  
### Event types

OnGuard generates the following categories of events that are forwarded to Google SecOps:

  * **Access Granted Events** : Badge swipe accepted at a reader
  * **Access Denied Events** : Badge swipe rejected (invalid badge, expired, wrong access level)
  * **Door Held Open Events** : Door remains open beyond the configured time
  * **Door Forced Open Events** : Door opened without a valid badge swipe
  * **Alarm Events** : Alarm input triggered or acknowledged
  * **Status Events** : Panel online/offline, communication failure, tamper
  * **Cardholder Events** : Cardholder added, modified, or deleted
  * **Badge Events** : Badge activated, deactivated, or lost
  * **Visitor Events** : Visitor signed in or signed out



## Authentication methods reference

Chronicle webhook feeds support multiple authentication methods. Choose the method that your vendor supports.

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
        




**Advantages:** \- API key and secret not visible in URL \- More secure (headers not logged in web server access logs) \- Preferred method when vendor supports it

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

Chronicle accepts the following header names for authentication:

**For API key:**

  * `x-goog-chronicle-auth` (recommended)
  * `X-Goog-Chronicle-Auth` (case-insensitive)



**For secret key:**

  * `x-chronicle-auth` (recommended)
  * `X-Chronicle-Auth` (case-insensitive)



## Troubleshooting

### OpenAccess API connection failures

If the middleware cannot connect to the OpenAccess API:

  1. Verify the OnGuard server is reachable from the middleware host:
         
         curl -k https://<ONGUARD_SERVER>:8080/api/access/onguard/openaccess/version?version=1.0
         

  2. Confirm that port `8080` is open on the OnGuard server firewall.

  3. On the OnGuard server, run the following command to verify the port is listening:
         
         netstat -anb | findstr 8080
         

  4. Restart the LS OpenAccess service if the port is not listening:

     * Open **Windows Services** (`services.msc`) on the OnGuard server.
     * Right-click **LS OpenAccess** and select **Restart**.



### Authentication failures

If the middleware receives authentication errors:

  1. Verify the OnGuard username and password are correct.
  2. Confirm the `ONGUARD_DIRECTORY_ID` matches a valid directory returned by `GET /directories`.
  3. Ensure the OnGuard user account is not locked out due to brute force protection. OnGuard locks accounts after multiple failed login attempts.
  4. If the `openaccess.ini` file exists at `C:\ProgramData\lnl\openaccess.ini`, verify its configuration is correct.



### No events received in Chronicle

If the middleware runs without errors but no events appear in Chronicle:

  1. Verify that events are being generated in OnGuard by checking the **Alarm Monitoring** application.
  2. Confirm that event publishing is enabled in the OnGuard database. On the OnGuard database server, run the following SQL query:
         
         SELECT * FROM LNL_SYSTEMSETTINGS WHERE SETTINGNAME = 'EventPublishingDisabled'
         

     * A result of `0` or no results means event publishing is enabled.
     * A result of `1` means event publishing is disabled and must be re-enabled.
  3. Check the forwarder log file at `/opt/onguard-chronicle-forwarder/forwarder.log` for error messages.

  4. Verify the Chronicle webhook endpoint URL, API key, and secret key are correct in the `.env` file.




### Request pool full errors

If the middleware receives `request pool full` errors from OpenAccess:

  1. On the OnGuard server, create or edit the file `C:\ProgramData\Lnl\OpenAccess.ini`.
  2. Add the following content:
         
         [http_request]
         request_pool_size=128
         

  3. Restart the **LS OpenAccess** service for the change to take effect.




## Webhook limits and best practices

### Request limits

Limit | Value  
---|---  
**Max request size** | 4 MB  
**Max QPS (queries per second)** | 15,000  
**Request timeout** | 30 seconds  
**Retry behavior** | Automatic with exponential backoff  
  
## UDM mapping table

Original log field | UDM mapping | Logic  
---|---|---  
`timestamp` | `metadata.event_timestamp` | Mapped directly from the event timestamp  
`description` | `metadata.description` | Event description text  
`event_type` | `metadata.product_event_type` | OnGuard event type identifier  
`badge_id` | `principal.user.product_object_id` | Badge number associated with the event  
`cardholder_first_name` | `principal.user.first_name` | First name of the cardholder  
`cardholder_last_name` | `principal.user.last_name` | Last name of the cardholder  
`device` | `principal.asset.hostname` | Reader or panel name  
`source` | `target.asset.hostname` | Source device or panel  
`serial_number` | `principal.asset.hardware.serial_number` | Panel serial number  
`access_result` | `security_result.action` | ALLOW or BLOCK based on access granted or denied  
`cardnumber", "device", "eid", "machine", "serialnum", and "site` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/lenel-onguard-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
