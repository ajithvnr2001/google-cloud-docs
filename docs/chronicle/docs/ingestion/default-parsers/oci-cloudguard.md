---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oci-cloudguard/
title: Collect Oracle Cloud Infrastructure - Oracle Cloud Guard logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:47.480913+00:00
---

# Collect Oracle Cloud Infrastructure - Oracle Cloud Guard logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oci-cloudguard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Oracle Cloud Infrastructure - Oracle Cloud Guard logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to configure Oracle Cloud Infrastructure Cloud Guard to push logs to Google Security Operations using webhooks.

Oracle Cloud Guard is a cloud-native security service that monitors, identifies, and helps maintain a strong security posture on Oracle Cloud Infrastructure (OCI). Cloud Guard examines OCI resources for security weaknesses related to configuration and detects anomalous activity. When Cloud Guard discovers a deviation from a detector rule, it creates a Problem event that provides comprehensive security monitoring across your OCI tenancy. This integration uses the OCI Events Service and OCI Functions to forward Cloud Guard problem events to Google SecOps in near-real time.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * An active Oracle Cloud Infrastructure tenancy with Cloud Guard enabled
  * Administrator access to the Oracle Cloud Infrastructure Console
  * Permissions to create and manage OCI Functions applications
  * Permissions to create OCI Events rules and Notifications topics
  * Access to OCI Cloud Shell or a local environment with Fn Project CLI installed
  * Docker installed (for building OCI Functions locally)
  * Access to Google Cloud Console (for API key creation)



## Create webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `OCI Cloud Guard Problems`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Oracle Cloud Infrastructure - Oracle Cloud Guard** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** (optional): Leave empty (each function invocation sends a single event).
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



### Generate and save secret key

After creating the feed, you must generate a secret key for authentication:

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. **Copy and save** the secret key securely.



**Important** : The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.

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



## Enable Cloud Guard Cloud Event responder

Cloud Guard uses the Cloud Event responder to emit problem details to the OCI Events Service. The Cloud Event responder is part of the Responder recipe and must be enabled and set to execute automatically.

### Enable the Cloud Event rule in the Responder recipe

  1. Sign in to the **Oracle Cloud Infrastructure Console**.
  2. Open the **navigation menu** and select **Identity & Security > Cloud Guard > Recipes**.
  3. Select **Responder Recipes**.
  4. Click the responder recipe attached to your target.
  5. In the **Responder Rules** section, locate the **Cloud Events** rule.
  6. If the status is **Disabled** : 
     1. Open the **Actions** menu (three dots) and select **Edit**.
     2. Change the **Status** to **Enabled**.
     3. Click **Save**.



### Configure auto-execution on the target

  1. In the **Oracle Cloud Infrastructure Console** , open the **navigation menu** and select **Identity & Security > Cloud Guard > Configuration > Targets**.
  2. Select the target compartment.
  3. Under **Resources** , select **Responder Recipes**.
  4. Click the responder recipe link.
  5. Locate the **Cloud Event** responder rule.
  6. Open the **Actions** menu (three dots) and select **Edit**.
  7. Set **Rule Trigger** to **Execute Automatically**.
  8. Select the **CONFIRM EXECUTE AUTOMATICALLY** checkbox.
  9. Click **Save**.

**Note:** The Cloud Event responder does not require additional IAM policies. It is enabled by default in new responder recipes, but verify the configuration for existing recipes.



## Create OCI Functions application

Create an OCI Functions application that will host the function responsible for forwarding Cloud Guard events to Google SecOps.

### Create the application

  1. In the **Oracle Cloud Infrastructure Console** , open the **navigation menu** and select **Developer Services > Functions > Applications**.
  2. Select the compartment where you want to create the application.
  3. Click **Create Application**.
  4. Provide the following configuration details: 
     * **Name** : Enter `cloudguard-chronicle-forwarder`
     * **VCN** : Select a VCN with internet access (required for the function to reach the Chronicle webhook endpoint)
     * **Subnets** : Select a public subnet or a private subnet with a NAT gateway configured
  5. Click **Create**.



### Create and deploy the function

Use OCI Cloud Shell or a local environment with Fn Project CLI to create and deploy the function.

  1. Open **OCI Cloud Shell** from the Oracle Cloud Infrastructure Console (click the Cloud Shell icon in the top navigation bar).
  2. Set up the Fn context for your OCI Functions application:
         
         fn list context
         fn use context <your-region-context>
         fn update context oracle.compartment-id <compartment_OCID>
         fn update context registry <region-key>.ocir.io/<tenancy-namespace>/cloudguard-chronicle
         

  3. Initialize a new Python function:
         
         fn init --runtime python cloudguard-to-chronicle
         cd cloudguard-to-chronicle
         

  4. Replace the contents of the `func.py` file with the following code:
         
         import io
         import json
         import logging
         import requests
         
         from fdk import response
         
         def handler(ctx, data: io.BytesIO = None):
             """
             OCI Function that receives Cloud Guard events from OCI Events Service
             and forwards them to Google SecOps (Chronicle) webhook endpoint.
             """
             logger = logging.getLogger()
         
             try:
                 cfg = ctx.Config()
                 chronicle_endpoint = cfg.get("CHRONICLE_ENDPOINT")
                 chronicle_api_key = cfg.get("CHRONICLE_API_KEY")
                 chronicle_secret = cfg.get("CHRONICLE_SECRET")
         
                 if not all([chronicle_endpoint, chronicle_api_key, chronicle_secret]):
                     logger.error("Missing required configuration: CHRONICLE_ENDPOINT, CHRONICLE_API_KEY, or CHRONICLE_SECRET")
                     return response.Response(
                         ctx, response_data=json.dumps({"error": "Missing configuration"}),
                         headers={"Content-Type": "application/json"}, status_code=500
                     )
         
                 event_data = json.loads(data.getvalue())
                 logger.info(f"Received Cloud Guard event: {event_data.get('eventType', 'unknown')}")
         
                 webhook_url = f"{chronicle_endpoint}?key={chronicle_api_key}&secret={chronicle_secret}"
         
                 headers = {
                     "Content-Type": "application/json"
                 }
         
                 resp = requests.post(
                     webhook_url,
                     json=event_data,
                     headers=headers,
                     timeout=30
                 )
         
                 if resp.status_code >= 200 and resp.status_code < 300:
                     logger.info(f"Successfully forwarded event to Chronicle (HTTP {resp.status_code})")
                 else:
                     logger.error(f"Failed to forward event to Chronicle (HTTP {resp.status_code}): {resp.text}")
         
                 return response.Response(
                     ctx, response_data=json.dumps({"status": resp.status_code}),
                     headers={"Content-Type": "application/json"}, status_code=200
                 )
         
             except Exception as e:
                 logger.error(f"Error processing Cloud Guard event: {str(e)}")
                 return response.Response(
                     ctx, response_data=json.dumps({"error": str(e)}),
                     headers={"Content-Type": "application/json"}, status_code=500
                 )
         

  5. Replace the contents of the `requirements.txt` file:
         
         fdk>=0.1.0
         requests>=2.25.0
         

  6. Deploy the function to the application:
         
         fn -v deploy --app cloudguard-chronicle-forwarder
         

  7. Wait for the deployment to complete.




### Configure function environment variables

  1. In the **Oracle Cloud Infrastructure Console** , open the **navigation menu** and select **Developer Services > Functions > Applications**.
  2. Click the **cloudguard-chronicle-forwarder** application.
  3. Under **Resources** , select **Functions**.
  4. Click the **cloudguard-to-chronicle** function.
  5. Under **Resources** , select **Configuration**.
  6. Click **Edit** and add the following key-value pairs:

Key | Value  
---|---  
`CHRONICLE_ENDPOINT` | The Chronicle webhook endpoint URL (for example, `https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import`)  
`CHRONICLE_API_KEY` | The Google Cloud API key created for the Chronicle webhook  
`CHRONICLE_SECRET` | The Chronicle webhook secret key  
  7. Click **Save**.

**Note:** OCI Functions configuration values are stored as encrypted environment variables. Alternatively, use OCI Vault secrets for enhanced security.



## Create IAM policies for OCI Functions

The OCI Functions service and the Events Service require IAM policies to invoke the function.

### Create a dynamic group for the function

  1. In the **Oracle Cloud Infrastructure Console** , open the **navigation menu** and select **Identity & Security > Domains**.
  2. Select the **Default** domain.
  3. Under **Identity domain resources** , select **Dynamic Groups**.
  4. Click **Create Dynamic Group**.
  5. Provide the following configuration details:

     * **Name** : Enter `cloudguard-chronicle-functions`
     * **Description** : Enter `Dynamic group for Cloud Guard to Chronicle forwarder function`
     * **Matching Rules** : Enter the following rule:
    
    ALL {resource.type = 'fnfunc', resource.compartment.id = '<compartment_OCID>'}
    

  6. Click **Create**.

**Note:** Replace `<compartment_OCID>` with the OCID of the compartment where the function application is deployed.



### Create IAM policies

  1. In the **Oracle Cloud Infrastructure Console** , open the **navigation menu** and select **Identity & Security > Policies**.
  2. Ensure you are in the **root compartment**.
  3. Click **Create Policy**.
  4. Provide the following configuration details: 
     * **Name** : Enter `cloudguard-chronicle-policy`
     * **Description** : Enter `Allows Events Service to invoke Cloud Guard Chronicle forwarder function`
     * **Compartment** : Ensure the root compartment is selected.
  5. In the **Policy Builder** section, toggle **Show manual editor**.
  6. In the **Statement** field, enter the following policy statements:
         
         Allow dynamic-group cloudguard-chronicle-functions to use fn-function in compartment <compartment_name>
         Allow dynamic-group cloudguard-chronicle-functions to use fn-invocation in compartment <compartment_name>
         Allow service cloudguardevents to use fn-function in compartment <compartment_name>
         Allow service cloudguardevents to use fn-invocation in compartment <compartment_name>
         

  7. Click **Create**.

**Note:** Replace `<compartment_name>` with the name of the compartment where the function application is deployed.



## Create OCI Events rule for Cloud Guard

Create an Events rule that triggers the OCI Function when Cloud Guard detects, dismisses, or remediates a problem.

### Create the Events rule

  1. In the **Oracle Cloud Infrastructure Console** , open the **navigation menu** and select **Observability & Management > Events Service > Rules**.

**Important:** You must be in the **Cloud Guard reporting region** to create the Events rule. The reporting region may be different from your home region.
  2. Click **Create Rule**.

  3. Provide the following configuration details:

     * **Display Name** : Enter `cloudguard-to-chronicle`
     * **Description** : Enter `Forwards Cloud Guard problem events to Google SecOps via OCI Functions`
  4. In the **Rule Conditions** section:

     1. Set **Condition** to **Event Type**.
     2. Set **Service Name** to **Cloud Guard**.
     3. Set **Event Type** to the following (select multiple): 
        * **Detected - Problem**
        * **Dismissed - Problem**
        * **Remediated - Problem**
  5. In the **Actions** section:

     1. Set **Action Type** to **Functions**.
     2. Set **Function Compartment** to the compartment containing the function application.
     3. Set **Function Application** to **cloudguard-chronicle-forwarder**.
     4. Set **Function** to **cloudguard-to-chronicle**.
  6. Click **Create Rule**.




### Optional: Filter by risk level

To forward only high-severity problems, add an attribute filter to the Events rule:

  1. In the **Rule Conditions** section, click **\+ Another Condition**.
  2. Set **Condition** to **Attribute**.
  3. Set **Attribute Name** to `riskLevel`.
  4. Set **Attribute Values** to the desired risk levels:

     * `CRITICAL`
     * `HIGH`
**Note:** Available risk levels are `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, and `MINOR`.



## Verify the integration

### Test the function manually

  1. In the **Oracle Cloud Infrastructure Console** , open the **navigation menu** and select **Developer Services > Functions > Applications**.
  2. Click the **cloudguard-chronicle-forwarder** application.
  3. Under **Resources** , select **Functions**.
  4. Click the **cloudguard-to-chronicle** function.
  5. Click **Invoke** to test the function with sample data, or use OCI Cloud Shell:
         
         echo '{"eventType":"com.oraclecloud.cloudguard.problemdetected","cloudEventsVersion":"0.1","eventID":"test-event-001","data":{"compartmentId":"ocid1.compartment.oc1..example","resourceName":"test-problem","additionalDetails":{"riskLevel":"HIGH","problemDescription":"Test problem for integration verification","status":"OPEN","region":"us-ashburn-1"}}}' | fn invoke cloudguard-chronicle-forwarder cloudguard-to-chronicle
         

  6. Verify the function logs by navigating to **Developer Services > Functions > Applications > cloudguard-chronicle-forwarder** and selecting the **Logs** section.

  7. Look for log entries confirming successful forwarding:
         
         Received Cloud Guard event: com.oraclecloud.cloudguard.problemdetected
         Successfully forwarded event to Chronicle (HTTP 200)
         




### Verify in Google SecOps

  1. Sign in to **Google SecOps**.
  2. Go to **Search** and query for events with the log type `OCI_CLOUDGUARD`.
  3. Verify that Cloud Guard problem events appear in the search results.



If events do not appear:

  * Verify the Chronicle webhook endpoint URL, API key, and secret key in the function configuration
  * Check that the Events rule is in the correct OCI region (Cloud Guard reporting region)
  * Confirm that the Cloud Event responder is enabled and set to auto-execute
  * Review function logs for error messages



## Cloud Guard event types reference

Cloud Guard emits the following event types through the OCI Events Service:

Event Type | Trigger  
---|---  
`com.oraclecloud.cloudguard.problemdetected` | A new problem is detected  
`com.oraclecloud.cloudguard.problemdismissed` | A problem is dismissed  
`com.oraclecloud.cloudguard.problemremediated` | A problem is remediated  
`com.oraclecloud.cloudguard.sightingdetected` | A new sighting is detected  
  
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
        




**Advantages:**

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

Chronicle accepts the following header names for authentication:

  * **For API key:**

    * `x-goog-chronicle-auth` (recommended)
    * `X-Goog-Chronicle-Auth` (case-insensitive)
  * **For secret key:**

    * `x-chronicle-auth` (recommended)
    * `X-Chronicle-Auth` (case-insensitive)
**Note:** The OCI Function in this guide uses query parameter authentication (Method 2). To use custom header authentication (Method 1), modify the function code to include `x-goog-chronicle-auth` and `x-chronicle-auth` headers instead of appending credentials to the URL.



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
contentType | additional.fields | Merged from various additional fields  
cloudEventsVersion | additional.fields |   
data.additionalDetails.reason | additional.fields |   
data.additionalDetails.tenantId | additional.fields |   
data.additionalDetails.problemType | additional.fields |   
data.resourceName | additional.fields |   
data.resourceId | additional.fields |   
status | additional.fields |   
problem_recommendation | additional.fields |   
compartment_id | additional.fields |   
compartment_name | additional.fields |   
product_event | extensions.auth.type | Set to "AUTHTYPE_UNSPECIFIED" if product_event matches login  
data.additionalDetails.problemDescription | metadata.description | Value from data.additionalDetails.problemDescription if not empty, else data.additionalDetails.description  
data.additionalDetails.description | metadata.description |   
has_user | metadata.event_type | Set to USER_RESOURCE_ACCESS if has_user and has_target_resource, USER_UNCATEGORIZED if has_user, USER_LOGIN if product_event matches login, STATUS_UPDATE if has_principal, else GENERIC_EVENT  
has_target_resource | metadata.event_type |   
product_event | metadata.event_type |   
has_principal | metadata.event_type |   
eventType | metadata.product_event_type | Value from eventType if not empty, else product_event  
product_event | metadata.product_event_type |   
eventID | metadata.product_log_id | Value copied directly  
version | metadata.product_version | Value copied directly  
observer | observer.domain.name | Extracted domain from observer using grok  
observer | observer.hostname | Value from observer if not IP  
observer | observer.ip | Value from observer if IP  
principal | principal.administrative_domain | Extracted domain from principal or principal_host using grok  
principal_host | principal.administrative_domain |   
data.additionalDetails.problemAdditionalDetails.public_ips | principal.asset.ip | Value from data.additionalDetails.problemAdditionalDetails.public_ips if not empty, else vnicDetails.0.vnicPublicIp if not empty, else from principal if IP, else principal_host if IP  
vnicDetails.0.vnicPublicIp | principal.asset.ip |   
principal | principal.asset.ip |   
principal_host | principal.asset.ip |   
principal | principal.hostname | Value from principal if not IP, else principal_host if not IP  
principal_host | principal.hostname |   
data.additionalDetails.problemAdditionalDetails.public_ips | principal.ip | Value from data.additionalDetails.problemAdditionalDetails.public_ips if not empty, else vnicDetails.0.vnicPublicIp if not empty, else from principal if IP, else principal_host if IP  
vnicDetails.0.vnicPublicIp | principal.ip |   
principal | principal.ip |   
principal_host | principal.ip |   
data.additionalDetails.region | principal.location.name | Value copied directly  
principal_port | principal.port | Converted to integer from principal_port  
data.additionalDetails.resourceName | principal.resource.name | Value from data.additionalDetails.resourceName if not empty, else data.additionalDetails.principalResourceName  
data.additionalDetails.principalResourceName | principal.resource.name |   
data.additionalDetails.resourceId | principal.resource.product_object_id | Value from data.additionalDetails.resourceId if not empty, else data.additionalDetails.principalResourceId  
data.additionalDetails.principalResourceId | principal.resource.product_object_id |   
data.additionalDetails.resourceType | principal.resource.resource_subtype | Value from data.additionalDetails.resourceType if not empty, else data.additionalDetails.principalResourceType  
data.additionalDetails.principalResourceType | principal.resource.resource_subtype |   
data.additionalDetails.resourceName | principal.user.userid | Value from data.additionalDetails.resourceName if data.additionalDetails.resourceType == "User", else from data.additionalDetails.principalResourceName if data.additionalDetails.principalResourceType == "User"  
data.additionalDetails.principalResourceName | principal.user.userid |   
action | security_result.action | Set to BLOCK if action matches block, ALLOW if success, FAIL if fail, else UNKNOWN  
action | security_result.action_details | Value copied directly  
data.additionalDetails.tacticName | security_result.attack_details.tactics | Value copied directly to tactic_data.name, then merged  
data.additionalDetails.techniqueName | security_result.attack_details.techniques | Value copied directly to technique_data.name, then merged  
data.additionalDetails.confidence | security_result.confidence_score | Value copied directly  
sightingType | security_result.detection_fields | Merged from sightingType, sightingScore, riskScore labels  
sightingScore | security_result.detection_fields |   
riskScore | security_result.detection_fields |   
data.additionalDetails.detectorRuleId | security_result.rule_id | Value copied directly  
data.additionalDetails.detectorRuleType | security_result.rule_name | Value copied directly  
severity | security_result.severity | Set to INFORMATIONAL if severity in INFO, LOW if Low, MEDIUM if WARN, HIGH if High, CRITICAL if Critical  
severity | security_result.severity_details | Value copied directly  
target | target.administrative_domain | Extracted domain from target or target_host using grok  
target_host | target.administrative_domain |   
target | target.hostname | Value from target if not IP, else target_host if not IP  
target_host | target.hostname |   
target | target.ip | Value from target if IP, else target_host if IP  
target_host | target.ip |   
target_port | target.port | Converted to integer from target_port  
targetId | target.resource.attribute.labels | Merged from various label fields  
labels | target.resource.attribute.labels |   
vnicAttachmentId | target.resource.attribute.labels |   
vnicAttachmentDisplayName | target.resource.attribute.labels |   
subnets | target.resource.attribute.labels |   
instance_ocid | target.resource.attribute.labels |   
route_table_ocids | target.resource.attribute.labels |   
security_list_ocids | target.resource.attribute.labels |   
data.additionalDetails.impactedResourceName | target.resource.name | Value from data.additionalDetails.impactedResourceName if not empty, else vnicDetails.0.vnicDisplayName  
vnicDetails.0.vnicDisplayName | target.resource.name |   
data.additionalDetails.impactedResourceId | target.resource.product_object_id | Value from data.additionalDetails.impactedResourceId if not empty, else vnicDetails.0.vnicId  
vnicDetails.0.vnicId | target.resource.product_object_id |   
data.additionalDetails.impactedResourceType | target.resource.resource_subtype | Value copied directly  
target_url | target.url | Value copied directly  
target_user | target.user.userid | Value copied directly  
product | metadata.product_name | Value copied directly  
vendor | metadata.vendor_name | Value copied directly  
`data.additionalDetails.tacticName` | `security_result.attack_details.tactics.name` | Mapped from changelog  
`data.additionalDetails.techniqueName` | `security_result.attack_details.techniques.name` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oci-cloudguard-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
