---
url: https://docs.cloud.google.com/looker/docs/best-practices/looker-hosted-infrastructure-migration-information/
title: Looker-hosted infrastructure migration information \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:32.542103+00:00
---

# Looker-hosted infrastructure migration information  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/looker-hosted-infrastructure-migration-information/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Looker-hosted infrastructure migration information Stay organized with collections  Save and categorize content based on your preferences. 

Looker is in the process of upgrading our hosting infrastructure to deliver better scalability and reliability. This upgrade will also give you access to new Looker features as they are developed. 

**You will need to take action to ensure continued, uninterrupted service.** Looker is working hard to make this transition as seamless as possible. The following instructions provide details. Please review them and reach out to [Looker Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details) or your Looker team if you need any assistance or have any questions. 

Also, please be aware that, upon upgrade, all your [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#adding_persistence) will rebuild. This may cause additional load to your database. 

##  Connecting Looker to your database 

There are two ways Looker may be talking to your databases. Both will require updates to ensure continued data access. You may have several databases, each using different techniques. 

###  IP address allowlist 

If you're connecting Looker to your database by allowing specific IP addresses through your network layer, you will need to add a new IP to your list of allowed addresses on your network. This step can be done ahead of time. See the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access#option_1:_ip_address_allowlist) documentation page if you are unfamiliar with the process. 

  1. The list of IP addresses that are needed to allow network traffic from your Looker instance can be found on the Connections page in the Admin panel. Click Public IP Addresses and copy the IP address(es) that are shown. Visit the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access#next_generation_hosting) documentation page for a complete list of regions and IPs. 
  2. Allow access to the necessary IP addresses through your networking layer (the specific method will depend on the database in question). Don't remove the legacy IPs at this time. 



##  SSH tunnel 

If you're connecting Looker to your database through an SSH tunnel, your tunnel configurations will carry over to the new infrastructure. The only action you will need to take will be to update your allowed IP addresses on your network. See the [Using an SSH tunnel](https://docs.cloud.google.com/looker/docs/using-an-ssh-tunnel) documentation page if you're unfamiliar with using SSH tunnels. 

  1. The list of IP addresses that are needed to allow network traffic from your Looker instance can be found on the Connections page in the Admin panel. Click Public IP Addresses and copy the IP address(es) that are shown. Visit the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access#next_generation_hosting) documentation page for a complete list of regions and IPs. 
  2. Allow access to the necessary IP addresses through your networking layer (the specific method will depend on the database in question). Don't remove the legacy IPs at this time. 



##  Connecting Looker to third-party services 

You may have additional services that Looker communicates with. As explained in the **IP address allowlist** section, your next-generation Looker instance will have a different outbound IP address, and Looker won't be able to connect if you are restricting access. 

Notable examples of services include GitHub Enterprise accounts or a [local action hub server](https://docs.cloud.google.com/looker/docs/action-hub#setting_up_a_local_action_hub_server). These allowlist IP addresses also apply to SFTP and SMTP destinations and for LDAP servers that restrict IP traffic. 

If your infrastructure relies on lists of allowed IP addresses for connections to specific services, you need to update these lists the same way you would to allow database access. 

  1. The list of IP addresses that are needed to allow network traffic from your Looker instance can be found on the Connections page in the Admin panel. Click Public IP Addresses and copy the IP address(es) that are shown. Visit the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access#next_generation_hosting) documentation page for a complete list of regions and IPs. 
  2. Allow access to the necessary IP addresses through your networking layer (the specific method will depend on the service in question). Don't remove the legacy IPs at this time. 



* * *

**NOTE: The following section is only relevant if you are changing your hosting environment to Google Cloud. No need to read further unless you or someone at your organization has had discussions with Looker about changing from the historical default hosting provider of Amazon Web Services (AWS) to Google Cloud.**

##  Accessing Looker via the API - Google Cloud only 

Connecting to Looker from your browser will not change; humans can continue to do what they have always done. If you are using the Looker API, you may need to take action to ensure uninterrupted service. If you are not sure, you can use this [System Activity](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores) query to see if there has been recent API usage on your instance: 
    
    
        <your_instance_url>/explore/system__activity/event?
        fields=event.created_week,event.count,event.category
        &f[event.is_api_call]=Yes&sorts=event.created_week+desc
        &limit=500&total=on&row_total=right
        &vis={}
        &filter_config={"event.is_api_call":[{"type":"is","values":[{"constant":"Yes"},{}],"id":0,"error":false}]}
      

If there are no results, you are not using the API and don't have to take any further action. 

###  Custom API host URL - Google Cloud only 

  1. Check [Admin -> API](https://docs.cloud.google.com/looker/docs/admin-panel-platform-api) to see if there is a value set for **API Host URL**. 
  2. If a value _is_ set, you don't need to do anything further. 
  3. If a value _is not_ set, you have a choice: either set a value using the instructions on the [Admin settings -> API](https://docs.cloud.google.com/looker/docs/admin-panel-platform-api) documentation page and update your API processes to use it (recommended, as it will allow you to make the configuration changes ahead of time without loss of service), or proceed to the Specifying an API port section. 
  4. After configuring your custom API host URL in the Looker application, you will need to update your API processes to connect via that URL rather than specified port numbers (for example, `https://my.api.looker.com` rather than `https://my.looker.com:19999`). 



###  Specifying an API port - Google Cloud only 

If you do not use a [custom API host URL](https://docs.cloud.google.com/looker/docs/admin-panel-platform-api#api_host_url), you will need to update your API processes to connect to a new port. Our next-generation hosting infrastructure uses port `443`. If you are not using a [custom API host URL](https://docs.cloud.google.com/looker/docs/admin-panel-platform-api#api_host_url), update from the current default API port of `19999` to port `443`. 

Locate your API processes, and change the API port references from 19999 to 443 (for example, use `https://my.looker.com:443` rather than `https://my.looker.com:19999`). 

**This technique cannot be used without a service interruption.** If you choose to update the port in your API processes prior to the upgrade, the processes will not be able to access your Looker instance until the upgrade is complete. For this reason, we recommend that you do it immediately prior to the scheduled upgrade. 

If you choose to update your processes after the infrastructure upgrade, automated processes will not be able to access your Looker instance during the period in between the upgrade and the time the port change is complete. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-22 UTC."],[],[]] 
