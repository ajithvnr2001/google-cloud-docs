---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/site24x7/
title: Site24x7 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:26.545434+00:00
---

# Site24x7  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/site24x7/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Site24x7

This document provides guidance on how to integrate Site24x7 with Google SecOps.

## How to configure integration

  1. As an API root select one of the following values:

     * United States - https://www.site24x7.com/api
     * Europe - https://www.site24x7.eu
     * China - https://www.site24x7.cn
     * India - https://www.site24x7.in
     * Australia - https://www.site24x7.net.au/api
  2. Navigate to Zoho API console:

     * United States - [https://accounts.zoho.com](https://accounts.zoho.com/)
     * Europe -[https://accounts.zoho.eu](https://accounts.zoho.eu/)
     * China -[https://accounts.zoho.com.cn](https://accounts.zoho.com.cn/)
     * India -[https://accounts.zoho.in](https://accounts.zoho.in/)
     * Australia -[https://accounts.zoho.com.au](https://accounts.zoho.com.au/)
  3. Press on "Add Client".

  4. Create Self Client.

  5. Navigate to **"Client Secret"** Tab and copy **"Client ID"** and **"Client Secret"**.

  6. Provide **"Client ID"** and **"Client Secret"** in the integration configuration.

  7. Navigate to **"Generate Code"** Tab, provide the following scopes: "Site24x7.Operations.Read,Site24x7.Admin.Read" and some custom "Scope Description".

  8. Press on the **"Create"** button and copy the authorization code.

  9. Navigate to action **"Generate Refresh Token"** , provide authorization code and execute it.

  10. From the JSON result copy **"refresh_token"** and put the value in the **"Refresh Token"** in the integration configuration.




## Configure Site24x7 integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://www.site24x7.{region} | Yes | API root of the Site24x7 instance.  
Client ID | String | N/A | Yes | Client ID of the Site24x7 instance.  
Client Secret | Password | N/A | Yes | Client Secret of the Site24x7 instance.  
Refresh Token | Password | N/A | Yes | Refresh Token of the Site24x7 instance.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Site24x7 server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to Site24x7 with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Case | Success | Fail | Message  
---|---|---|---  
if successful | true | false | Successfully connected to the Site24x7 server with the provided connection parameters!  
not successful | false | true | Failed to connect to the Site24x7 server! Error: {0}".format(exception.stacktrace)  
  
### Generate Refresh Token

#### Description

Generate a refresh token needed for Integration configuration.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Authorization Code | Password | N/A | Yes | Specify the authorization code.  
  
#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
    "refresh_token": "{refresh token}"
    }
    ``` ##### Case Wall
    
    <table>
    <thead>
    <tr>
    <th>Result type</th>
    <th>Value/Description</th>
    <th>Type</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>Output message*</td>
    <td><p><strong>The action should not fail nor stop a playbook execution:</strong><br><strong>if successful and no "error" in the response:</strong> <em></em> "Successfully generated the refresh token. Copy that refresh token and put it in the Integration configuration."</p><p><em></em></p><p><strong>The action should fail and stop a playbook execution:</strong><br><strong>if not successful:</strong> "Error executing action "{}". Reason: " {0}".format(exception.stacktrace)<br><strong></strong></p><p><strong>If "error" in the response (fail):</strong> "Error executing action "{}". Reason: " {0}".format(errors)</p></td>
    <td>General</td>
    </tr>
    </tbody>
    </table>
    
    ## Connector
    
    ## Site24x7 - Alerts Log Connector
    
    #### Description
    
    Pull information about alert logs from Site24x7.
    
    #### Known Limitations
    
    1.  If the monitor has a whitespace in it, the connector won't be able to
        extract it. Example: "backup site".
    1.  If the monitor name is "Critical", "Down", "Up" or "Trouble", the connector
        may return unexpected results.
    
    #### Configure Site24x7 - Alerts Log Connector in Google SecOps
    
    For detailed instructions on how to configure a connector in
    Google SecOps, see [Configuring the
    connector](/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).
    
    ##### Connector parameters
    
    Use the following parameters to configure the connector:
    
    <table>
    <thead>
    <tr>
    <th>Parameter Display Name</th>
    <th>Type</th>
    <th>Default Value</th>
    <th>Is Mandatory</th>
    <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>Product Field Name</td>
    <td>String</td>
    <td>Product Name</td>
    <td>Yes</td>
    <td>Enter the source field name in order to retrieve the Product Field name.</td>
    </tr>
    <tr>
    <td>Event Field Name</td>
    <td>String</td>
    <td>eventType</td>
    <td>Yes</td>
    <td>Enter the source field name in order to retrieve the Event Field name.</td>
    </tr>
    <tr>
    <td>Environment Field Name</td>
    <td>String</td>
    <td>""</td>
    <td>No</td>
    <td><p>Describes the name of the field where the environment name is stored.</p>
    <p>If the environment field isn't found, the environment is the default environment.</p></td>
    </tr>
    <tr>
    <td>Environment Regex Pattern</td>
    <td>String</td>
    <td>.*</td>
    <td>No</td>
    <td><p>A regex pattern to run on the value found in the "Environment Field Name" field.</p>
    <p>Default is .* to catch all and return the value unchanged.</p>
    <p>Used to allow the user to manipulate the environment field via regex logic.</p>
    <p>If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.</p></td>
    </tr>
    <tr>
    <td>Script Timeout (Seconds)</td>
    <td>Integer</td>
    <td>180</td>
    <td>Yes</td>
    <td>Timeout limit for the python process running the current script.</td>
    </tr>
    <tr>
    <td>API Root</td>
    <td>String</td>
    <td>https://www.site24x7.{region}</td>
    <td>Yes</td>
    <td><p>API root of the Site24x7 instance. Possible api roots:</p>
    <p>United States<br>https://www.site24x7.com</p>
    <p>Europe<br>https://www.site24x7.eu</p>
    <p>China<br>https://www.site24x7.cn</p>
    <p>India<br>https://www.site24x7.in</p>
    <p>Australia<br>https://www.site24x7.net.au</p></td>
    </tr>
    <tr>
    <td>Client ID</td>
    <td>String</td>
    <td>N/A</td>
    <td>Yes</td>
    <td>Client ID of the Site24x7 instance.</td>
    </tr>
    <tr>
    <td>Client Secret</td>
    <td>Password</td>
    <td>N/A</td>
    <td>Yes</td>
    <td>Client Secret of the Site24x7 instance.</td>
    </tr>
    <tr>
    <td>Refresh Token</td>
    <td>String</td>
    <td></td>
    <td>Yes</td>
    <td>Site24x7 Refresh token. You can generate this token using action "Get Refresh Token"</td>
    </tr>
    <tr>
    <td>Max Days Backwards</td>
    <td>Integer</td>
    <td>1</td>
    <td>No</td>
    <td>Amount of days from where to fetch alert logs.</td>
    </tr>
    <tr>
    <td>Max Alert Logs To Fetch</td>
    <td>Integer</td>
    <td>10</td>
    <td>No</td>
    <td>How many alert logs to process per one connector iteration. Default: 100.</td>
    </tr>
    <tr>
    <td>Use whitelist as a blacklist</td>
    <td>Checkbox</td>
    <td>Checked</td>
    <td>Yes</td>
    <td>If enabled, whitelist will be used as a blacklist.</td>
    </tr>
    <tr>
    <td>Disable Overflow</td>
    <td>Checkbox</td>
    <td></td>
    <td>Yes</td>
    <td>If enabled, the connector will ignore the overflow mechanism.</td>
    </tr>
    <tr>
    <td>Verify SSL</td>
    <td>Checkbox</td>
    <td>Checked</td>
    <td>Yes</td>
    <td>If enabled, verify the SSL certificate for the connection to the Site24x7 server is valid.</td>
    </tr>
    <tr>
    <td>Proxy Server Address</td>
    <td>String</td>
    <td>N/A</td>
    <td>No</td>
    <td>The address of the proxy server to use.</td>
    </tr>
    <tr>
    <td>Proxy Username</td>
    <td>String</td>
    <td>N/A</td>
    <td>No</td>
    <td>The proxy username to authenticate with.</td>
    </tr>
    <tr>
    <td>Proxy Password</td>
    <td>Password</td>
    <td>N/A</td>
    <td>No</td>
    <td>The proxy password to authenticate with.</td>
    </tr>
    </tbody>
    </table>
    
    #### Connector rules
    
    ##### Proxy support
    
    The connector supports proxy.
    
    **Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)
    
    
      
      
    
      
        

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
