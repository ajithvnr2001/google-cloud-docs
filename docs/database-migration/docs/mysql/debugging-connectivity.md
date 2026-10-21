---
url: https://docs.cloud.google.com/database-migration/docs/mysql/debugging-connectivity/
title: Debugging connectivity \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:21:28.309435+00:00
---

# Debugging connectivity  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/debugging-connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Debugging connectivity Stay organized with collections  Save and categorize content based on your preferences. 

You've set up connectivity between your source and destination databases, but how do you know they're connected? When your communications fail between them, how can you find out what's gone wrong and where?

The most basic tools are `ping` and `traceroute`.

### Ping

`Ping` performs a basic test to determine if the destination ("remote host") is available from the source. `Ping` sends an `ICMP Echo Request` packet to a remote host, and it expects an `ICMP Echo Reply` in return. If `ping` doesn't succeed, then there's no route from the source to the destination. Success, however, doesn't mean that your packets can get through, only that in general, the remote host can be reached.

While `ping` can tell if a host is alive and responding, it's not guaranteed to be reliable. Some network providers block `ICMP` as a security precaution, which can make connectivity debugging more difficult.

### Traceroute

`Traceroute` tests the complete route network packets take from one host to another. It shows all the steps ("hops") that the packet takes along the way, and how long each step takes. If the packet doesn't go through all the way to the destination, `traceroute` doesn't complete, but ends with a series of asterisks. In this case, look for the last IP address that was successfully reached along the way. This is where connectivity broke down.

`Traceroute` can time out. It can also fail to complete if a gateway along the way isn't configured correctly to pass the packet along to the next hop.

When `traceroute` fails to complete, you might be able to figure out where it stopped. Find the last IP address listed in the `traceroute` output, and do a browser search for `who owns [IP_ADDRESS]`. Results may or may not show the owner of the address, but it's worth a try.

### mtr

The `mtr` tool is a form of `traceroute` that remains live and continuously updated, similar to how the `top` command works for local processes.

### Locate your local IP address

If you don't know the local address of your host, then run the `ip -br address show` command. On Linux, this shows the network interface, the status of the interface, the local IP, and MAC addresses. For example: `eth0 UP 10.128.0.7/32 fe80::4001:aff:fe80:7/64`.

Alternatively, you can run `ipconfig` or `ifconfig` to see the status of your network interfaces.

### Locate the outgoing IP address

If you don't know the IP address that the source and destination databases use to communicate with each other (the outgoing IP address), then complete the following steps:

  1. Go to the SQL Instances page in the Google Cloud console.

[Go to the Cloud SQL Instances page](https://console.cloud.google.com/sql)

  2. Click the name of the instance that's associated with the migration job that you're debugging.

  3. Scroll down until the **Connect to this instance** pane appears. In this pane, the outgoing IP address appears.




### Open local ports

To verify that your host is listening on the ports you think it is, run the `ss -tunlp4` command. This tells you what ports are open and listening. For example, if you have a MySQL database running, then port `3306` should be up and listening. For SSH, you should see port 22.

### All local port activity

Use the `netstat` command to see all the local port activity. For example, `netstat -lt` shows all the currently active ports.

### Connect to the remote host using telnet

To verify that you can connect to the remote host using `TCP`, run the `telnet` command. Telnet attempts to connect to the IP address and port you give it.

If your remote host is running a MySQL database, for example, then you should be able to telnet to it on port 3306: `telnet 35.193.198.159 3306`.

On success, you see the following: `

Trying 35.193.198.159... 

Connected to 35.193.198.159. 

`.

On failure, you see `telnet` stops responding until you force-close the attempt: `

Trying 35.193.198.159... 

^C. 

`.

### Cloud Logging

Database Migration Service and Cloud SQL use Cloud Logging. See the [Cloud Logging documentation](https://docs.cloud.google.com/logging/docs) for complete information and review the [Cloud SQL sample queries](https://docs.cloud.google.com/logging/docs/view/query-library-preview#sql-filters).

#### View logs

You can view logs for Cloud SQL instances and other Google Cloud projects such as Cloud VPN or Compute Engine instances. To view logs for your Cloud SQL instance log entries:

### Console

  1. [Go to the Logs Explorer](https://console.cloud.google.com/logs/query)
  2. Select an existing Cloud SQL project at the top of the page.
  3. In the Query builder, add the following:
     * Resource: Select **Cloud SQL Database**. In the dialog, select a Cloud SQL instance.
     * Log names: Scroll to the Cloud SQL section and select appropriate log files for your instance. For example: 
       * cloudsql.googlapis.com/mysql-general.log
       * cloudsql.googleapis.com/mysql.err
     * Severity: Select a log level.
     * Time range: Select a preset or create a custom range.



### gcloud

Use the [`gcloud logging`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command to view log entries. In the example below, replace `PROJECT_ID`. The [`limit`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read#--limit) flag is an optional parameter that indicates the maximum number of entries to return.
    
    
    gcloud logging read "projects/[PROJECT_ID]/logs/cloudsql.googleapis.com/mysql-general.log" --limit=10

### Private IP addresses

Connections to a Cloud SQL instance using a private IP address are automatically authorized for [RFC 1918 address ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges). Non-RFC 1918 address ranges must be configured in Cloud SQL as [authorized networks](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks). You also need to update the network peering to Cloud SQL to export any Non-RFC 1918 routes. For example: `gcloud compute networks peerings update cloudsql-mysql-googleapis-com --network=NETWORK --export-subnet-routes-with-public-ip --project=PROJECT`

The IP range 172.17.0.0/16 is reserved for the Docker bridge network. Any Cloud SQL instances created with an IP address in that range will be unreachable. Connections from any IP address within that range to Cloud SQL instances using private IP address will fail.

### VPN troubleshooting

See the [Google Cloud Cloud VPN troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting#common_problems_and_solutions) page.

## Troubleshooting reverse SSH tunnel issues

SSH tunneling is a method to forward some communication on top of an SSH connection. Reverse SSH tunneling allows setting up an SSH tunnel, but maintaining that the destination network is the one that initiates the tunnel connection. This is useful when you don't want to open a port in your own network for security purposes.

What you're trying to achieve is to setup the following: Cloud SQL DB \---> Compute Engine VM bastion \---> **tunnel** \---> source network bastion \---> source DB

Although Database Migration Service migrates data from a source to a destination, you should enable connectivity from the destination to the source.

It's assumed that:

  * The Compute Engine VM bastion can access the Cloud SQL DB.

  * The source network bastion can access the source DB (this is achieved by peering the Cloud SQL network to the Compute Engine VM network).




You then set up an SSH tunnel from the source network bastion to the Compute Engine VM bastion, which routes any incoming connections to some port on the Compute Engine VM bastion through the tunnel to the source DB.

Each link in the above scenario can be setup improperly and prevent the entire flow from working. Troubleshoot each link, one by one:

### source network bastion \---> source DB

  1. Connect to the source network bastion using SSH, or from the terminal if it's the local machine.
  2. Test connectivity to the source DB using one of the following methods: 
     * `telnet [source_db_host_or_ip] [source_db_port]` \- expect to see the mysql password prompt (something like `5.7.12-logPuN0%`D5G??f9nVS'Pmysql_native_passwordConnection`)
     * `[db_client] -h[source_db_host_or_ip] -P[source_db_port]` \- expect to see access denied (something like `ERROR 1045 (28000): Access denied for user...`)



If this fails, then you need to verify that you enabled access from this bastion to the source DB.

### Compute Engine VM bastion \---> source DB

  1. SSH to the Compute Engine VM bastion (using `gcloud compute ssh VM_INSTANCE_NAME`)
  2. Test connectivity to the source DB using one of the following methods: 
     * `telnet 127.0.0.1 [tunnel_port]` \- expect to see the mysql password prompt (something like `5.7.12-logPuN0%`D5G??f9nVS'Pmysql_native_passwordConnection`)
     * `[db_client] -h127.0.0.1 -P[tunnel_port]` \- expect to see access denied (something like `ERROR 1045 (28000): Access denied for user...`)



If this fails, then you need to verify that the tunnel is up and running properly. Running `sudo netstat -tupln` shows all listening processes on this VM, and you should see `sshd listening on the tunnel_port`.

### Cloud SQL DB \---> source DB

This is best tested by [`testing the migration job`](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job#test-create) from Database Migration Service. If this fails, then it means there's some issue with VPC peering or routing between the Cloud SQL network and the Compute Engine VM bastion network.

The source database server's firewall must be configured to allow the entire **internal IP range** allocated for the **private service connection** of the VPC network that the Cloud SQL destination instance is going to use as the **privateNetwork** field of its [**ipConfiguration** settings](https://cloud.google.com/sql/docs/mysql/replication/replication-from-external#setup-replica-instance).

To find the **internal IP range** in the console:

  1. [Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list) in the Google Cloud console.

  2. Select the VPC network that you want to use.

  3. Select **Private services access** > **Allocated IP ranges for services**.

  4. Find the **Internal IP range** associated with the connection created by **servicenetworking-googleapis-com**.




You can also view the traffic between the Cloud SQL instance and the Compute Engine VM instance in the [Cloud Logging](https://console.cloud.google.com/logs) console in the `Cloud VPN gateway` project. In the Compute Engine VM logs, look for traffic coming from the Cloud SQL instance. In the Cloud SQL instance's logs, look for traffic from the Compute Engine VM.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
