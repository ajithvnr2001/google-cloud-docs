---
url: https://docs.cloud.google.com/vmware-engine/docs/environment/howto-forward-syslog/
title: Forwarding syslog messages to a remote server \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:39.933226+00:00
---

# Forwarding syslog messages to a remote server  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/environment/howto-forward-syslog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Forwarding syslog messages to a remote server

Google Cloud VMware Engine provides the option to send syslog messages to your remote syslog server. This configuration lets you collate and process syslog messages using remote logging and monitoring systems.

**Caution:** Don't update your syslog server configuration using the vCenter Server Appliance Management Interface (VAMI). VMware Engine automatically reverts any changes made this way. To configure ESXi syslog forwarding, use the Google Cloud console, Google Cloud CLI, or the VMware Engine API.

## Before you begin

The steps in this document assume that you have done the following:

  * If you want to reference your remote syslog host by name, complete the following:

    * For Standard VMware Engine networks, [configure DNS bindings](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-create-dns-bindings).
    * For Legacy VMware Engine networks, configure [conditional DNS forwarding rules](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-legacy-conditional-dns-forwarding).



## Forward logs

The method of forwarding logs depends on the management appliance that you want to forward logs for.

  * For vCenter and ESXi logs, including NSX Distributed Firewall (DFW) Log, use VMware Engine.
  * For NSX Manager and NSX Edge VMs, use the NSX appliance.



### Forward logs by using VMware Engine

To configure ESXi or vCenter to forward logs to the syslog server by using the Google Cloud console, Google Cloud CLI or VMware Engine API, do the following. If you plan to forward syslog from ESXi Hosts, change the default port on which the log agent listens from `5142` to `514`. In that case, use the same port (`514`) for forwarding syslog from vCenter as well as NSX.

###  Console 

To forward ESXi or vCenter logs to the syslog server by using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project that contains the private cloud.

  3. Select the **Syslog** tab.

  4. Click **Create Source**. The subtask for logging server creation displays.




###  gcloud 

To configure ESXi or vCenter to forward logs to the syslog server by using the Google Cloud CLI, use the [`gcloud vmware private-clouds logging-servers create` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/logging-servers/create).
    
    
    gcloud vmware private-clouds logging-servers create LOGGING_SERVER_ID \
      --project=PROJECT_ID \
      --hostname="HOST_NAME" \
      --port="PORT" \
      --source-type="SOURCE_TYPE" \
      --protocol="PROTOCOL" \
      --private-cloud=PRIVATE_CLOUD_ID \
      --location=ZONE

Replace the following:

  * `LOGGING_SERVER_ID`: the logging server ID for this request.
  * `PROJECT_ID`: the project for this request.
  * `HOST_NAME`: the IP address or fully qualified domain name for this request.
  * `PORT`: the port number for this request.
  * `SOURCE_TYPE`: the source type, either ESXi or vCenter, for this request.
  * `PROTOCOL`: the protocol, either UDP or TCP, for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud ID for this request.
  * `ZONE`: the zone for this request.



### API

To configure ESXi or vCenter to forward logs to the syslog server by using the VMware Engine API, make a `POST` request:
    
    
        GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID/loggingServers?logging_server_id=LOGGING_SERVER_ID" -d '{
          "hostname": "HOST_NAME",
          "port": "PORT",
          "sourceType": "SOURCE_TYPE",
          "protocol": "PROTOCOL"
        }'

Replace the following:

  * `PROJECT_ID`: the project for this request.
  * `ZONE`: the zone for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud ID for this request.
  * `LOGGING_SERVER_ID`: the logging server ID for this request.
  * `HOST_NAME`: the IP address or fully qualified domain name for this request.
  * `PORT`: the port number for this request.
  * `SOURCE_TYPE`: the source type, either ESXi or VCSA, for this request.
  * `PROTOCOL`: the protocol, either UDP or TCP, for this request.



### Forward logs by using the NSX appliance

The process varies depending on whether you want to forward NSX Manager or NSX Edge VM logs.

###  NSX Manager 

To configure NSX Manager in your VMware Engine private cloud to forward logs to your remote syslog server, do the following:

  1. Sign in to the NSX appliance in your private cloud. See [Accessing management appliances](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-access-management).
  2. Go to **System > Fabric > Profiles > Node Profiles**.
  3. To forward logs from all NSX nodes, select **All NSX Nodes**. Otherwise, select only the nodes you want to send the logs from.
  4. In the **Syslog Servers** section, click **Add**.
  5. In the **FQDN or IP Address** field, enter the IP address of your remote syslog host.
  6. In the **Port** field, enter the port number on which the remote syslog server listens.
  7. In the **Protocol** field, select a communication protocol.
  8. In the **Log Level** field, select the level of log you want to forward.
  9. Click **Add**.



###  NSX Edge VM 

To configure NSX Edge VM in your VMware Engine private cloud to forward logs to your remote syslog server, contact Cloud Customer Care.

## Manage logging servers on VMware Engine

The following procedures explain how to describe, list, edit, or delete your logging server.

### Describe logging server

You can get the description of a logging server using the Google Cloud console, Google Cloud CLI or VMware Engine API by doing the following:

###  Console 

To get the description of a configured logging server using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where you want to view the logging server details.

  3. Select the **Syslog** tab. Logging server details are listed in the Syslog table.




###  gcloud 

To get the description of a configured logging server using the Google Cloud CLI, use the [`gcloud vmware private-clouds logging-servers describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/logging-servers/describe).
    
    
    gcloud vmware private-clouds logging-servers describe LOGGING_SERVER_ID \
      --project=PROJECT_ID \
      --private-cloud=PRIVATE_CLOUD_ID \
      --location=ZONE

Replace the following:

  * `LOGGING_SERVER_ID`: the logging server ID for this request.
  * `PROJECT_ID`: the project for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud ID for this request.
  * `ZONE`: the zone for this request.



### API

To get the description of a configured logging server using the VMware Engine API, make the following request:
    
    
         GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID/loggingServers/LOGGING_SERVER_ID"
      

Replace the following:

  * `PROJECT_ID`: the project for this request.
  * `ZONE`: the zone for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud ID for this request.
  * `LOGGING_SERVER_ID`: the logging server ID for this request.



### List logging server

You can get a list of logging servers using the Google Cloud console, Google Cloud CLI or VMware Engine API by doing the following:

###  Console 

To get a list of configured logging servers using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where you want to list logging server details.

  3. Select the **Syslog** tab. All configured logging servers are listed in the Syslog table.




###  gcloud 

To get a list of configured logging servers using the Google Cloud CLI, use the [`gcloud vmware private-clouds logging-servers list` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/logging-servers/list).
    
    
    gcloud vmware private-clouds logging-servers list \
      --project=PROJECT_ID \
      --private-cloud=PRIVATE_CLOUD_ID \
      --location=ZONE

Replace the following:

  * `PROJECT_ID`: the project for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud ID for this request.
  * `ZONE`: the zone for this request.



### API

To get a list of configured logging servers using the VMware Engine API, make the following request:
    
    
         GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID/loggingServers/"
      

Replace the following:

  * `PROJECT_ID`: the project for this request.
  * `ZONE`: the zone for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud ID for this request.



### Edit a logging server

If you want to update a logging server using the Google Cloud console, Google Cloud CLI or VMware Engine API, do the following:

###  Console 

If you want to update a configured logging server using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where you want to edit the logging server details.

  3. Select the **Syslog** tab.

  4. Click the **More** more_vert icon at the end of a row and select **Edit**.

  5. Make your update in the logging server edit window.




###  gcloud 

To update a configured logging server using the Google Cloud CLI, use the [`gcloud vmware private-clouds logging-servers update` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/logging-servers/update).
    
    
    gcloud vmware private-clouds logging-servers update LOGGING_SERVER_ID \
      --project=PROJECT_ID \
      --hostname="HOST_NAME" \
      --port="PORT" \
      --source-type="SOURCE_TYPE" \
      --protocol="PROTOCOL" \
      --private-cloud=PRIVATE_CLOUD_ID \
      --location=ZONE

Replace the following:

  * `LOGGING_SERVER_ID`: the logging server ID for this request. 
    * `PROJECT_ID`: the project for this request.
    * `HOST_NAME`: the IP address or fully qualified domain name for this request.
    * `PORT`: the port number for this request.
    * `SOURCE_TYPE`: the source type, either ESXi or VCSA, for this request.
    * `PROTOCOL`: the protocol, either UDP or TCP, for this request.
    * `PRIVATE_CLOUD_ID`: the private cloud ID for this request.
    * `ZONE`: the zone for this request.



### API

To update a configured logging server using the VMware Engine API, make a `PATCH` request:
    
    
         PATCH "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID/loggingServers/LOGGING_SERVER_ID?updateMask=hostname,sourceType,protocol,port" -d '{
            "hostname": "HOST_NAME",
            "port": "PORT",
            "sourceType": "SOURCE_TYPE",
            "protocol": "PROTOCOL"
         }'
      

Replace the following:

  * `PROJECT_ID`: the project for this request.
  * `ZONE`: the zone for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud ID for this request.
  * `LOGGING_SERVER_ID`: the logging server ID for this request.
  * `HOST_NAME`: the IP address or fully qualified domain name for this request.
  * `PORT`: the port number for this request.
  * `SOURCE_TYPE`: the source type, either ESXi or VCSA, for this request.
  * `PROTOCOL`: the protocol, either UDP or TCP, for this request.



### Delete a logging server

If you want to delete a logging server using the Google Cloud console, Google Cloud CLI or VMware Engine API, do the following:

###  Console 

If you want to delete a configured logging server using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where you want to delete the logging server.

  3. Select the **Syslog** tab.

  4. Click the **More** more_vert icon at the end of a row and select **Delete**.




###  gcloud 

To delete a configured logging server using the Google Cloud CLI, use the [`gcloud vmware private-clouds logging-servers delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/logging-servers/delete).
    
    
    gcloud vmware private-clouds logging-servers delete LOGGING_SERVER_ID \
      --project=PROJECT_ID \
      --private-cloud=PRIVATE_CLOUD_ID \
      --location=ZONE

Replace the following:

  * `LOGGING_SERVER_ID`: the logging server ID for this request.
  * `PROJECT_ID`: the project for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud ID for this request.
  * `ZONE`: the zone for this request.



### API

To delete a configured logging server using the VMware Engine API, make the a `DELETE` request:
    
    
         GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID/loggingServers/NETWORK_ID"
      

Replace the following:

  * `PROJECT_ID`: the project for this request.
  * `ZONE`: the zone for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud ID for this request.
  * `NETWORK_ID`: the network ID for this request.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
