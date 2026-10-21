---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-emc-powerstore/
title: Collect Dell EMC PowerStore logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:27:30.172600+00:00
---

# Collect Dell EMC PowerStore logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-emc-powerstore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Dell EMC PowerStore logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Dell EMC PowerStore logs to Google Security Operations using Bindplane.

## Before you begin

Make you have the following prerequisites:

  * Google SecOps instance
  * Windows 2016 or later, or a Linux host with `systemd`
  * If running behind a proxy, firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open
  * Privileged access to Dell PowerStore



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

For additional installation options, consult the [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file: 
     * Locate the `config.yaml` file. Typically, it's in the `/etc/bindplane-agent/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
             udplog:
                 # Replace the port and IP address as required
                 listen_address: "0.0.0.0:514"
         
         exporters:
             chronicle/chronicle_w_labels:
                 compression: gzip
                 # Adjust the path to the credentials file you downloaded in Step 1
                 creds_file_path: '/path/to/ingestion-authentication-file.json'
                 # Replace with your actual customer ID from Step 2
                 customer_id: <customer_id>
                 endpoint: malachiteingestion-pa.googleapis.com
                 # Add optional ingestion labels for better organization
                 ingestion_labels:
                     log_type: 'DELL_EMC_POWERSTORE'
                     raw_log_field: body
         
         service:
             pipelines:
                 logs/source0__chronicle_w_labels-0:
                     receivers:
                         - udplog
                     exporters:
                         - chronicle/chronicle_w_labels
         

  3. Replace the port and IP address as required in your infrastructure.

  4. Replace `<customer_id>` with the actual customer ID.

  5. Update `/path/to/ingestion-authentication-file.json` to the path where the authentication file was saved in the [Get Google SecOps ingestion authentication file](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-emc-powerstore#get-auth-file) section.




## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart bindplane-agent
        

  * To restart the Bindplane agent in Windows, you can either use the **Services** console or enter the following command:
        
        net stop BindPlaneAgent && net start BindPlaneAgent
        




## Configure Syslog for Dell EMC PowerStore

  1. Sign in to the **Dell PowerStore** management console.
  2. Go to **Settings > Security > Remote Logging**.
  3. Click **\+ Add**.
  4. Provide the following configuration details: 
     * **Host IP address** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number (for example, `514` for UDP).
     * **Protocol** : Select UDP.
     * **Audit Types** : Select **Authentication** , **Authorization** , **Config** , **Logout** and **System**.
  5. Click **Save**.



## Supported Dell EMC PowerStore sample logs

  * **Service script execution audit**
        
        {
          "description": "Dell EMC PowerStore - Service Script Execution Audit",
          "format": "SYSLOG + KV",
          "raw_log": "<110>Sep 24 14:05:32 NODE-ALPHA-01 [222]: 2024-09-23T17:02:20 NODE-ALPHA-01 PS-ID-88291 222@9XJLYZ4 Service "
                     "[PowerStore_audit_event@1139 id=\"\"881726\"\" user=\"\"user_svc_01\"\" resource_type=\"\"not applicable\"\" "
                     "action=\"\"not applicable\"\" client_ip=\"\"not applicable\"\" appliance=\"\"APPLIANCE-X1\"\" status=\"\"success\"\"] "
                     "User user_svc_01 executed the service script command [/usr/local/bin/svc_diagnostic list] from NODE-ALPHA-02 via shell."
        }
        

  * **Configuration change (create)**
        
        {
          "description": "Dell EMC PowerStore - Configuration Change (Create)",
          "format": "SYSLOG + KV",
          "raw_log": "<110>Sep 25 07:09:41 NODE-BETA-05 [222]: 2024-09-24T14:40:52 NODE-BETA-05 PS-ID-11042 222@9XJLYZ4 Config "
                     "[PowerStore_audit_event@1139 id=\"\"992837\"\" user=\"\"user_adm_01\"\" resource_type=\"\"datacollection\"\" "
                     "action=\"\"create\"\" client_ip=\"\"192.0.2.15\"\" appliance=\"\"APPLIANCE-X1\"\" status=\"\"success\"\"] "
                     "Successfully created Data Collection for resource type: appliance, resource ids: [ \"\"A1\"\" ], logs from timestamp: "
                     "and logs to timestamp: with ID: 4f12a333-b8ea-9ccc-a186-0f27752da1a2."
        }
        

  * **Alert management**
        
        {
          "description": "Dell EMC PowerStore - Alert Management",
          "format": "SYSLOG + KV",
          "raw_log": "<110>Sep 25 07:09:43 NODE-GAMMA-09 [222]: 2024-09-24T21:19:45 NODE-GAMMA-09 PS-ID-22941 222@9XJLYZ4 Config "
                     "[PowerStore_audit_event@1139 id=\"\"445566\"\" user=\"\"not applicable\"\" "
                     "resource_type=\"\"alert\"\" action=\"\"modify\"\" client_ip=\"\"not applicable\"\" "
                     "appliance=\"\"APPLIANCE-X1\"\" status=\"\"success\"\"] "
                     "Successfully force cleared alert with ID: 7d88bc21-5a91-4b11-975b-edbefacc8036."
        }
        




## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-emc-powerstore-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
