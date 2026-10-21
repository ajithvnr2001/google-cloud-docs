---
url: https://docs.cloud.google.com/sql/docs/postgres/debugging-connectivity/
title: Debug connection issues \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:41.434221+00:00
---

# Debug connection issues  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/debugging-connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Debug connection issues Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/debugging-connectivity "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/debugging-connectivity "View this page for the SQL Server database engine")

## Introduction

Generally, connection issues fall into one of the following three areas:

  * Connecting - are you able to reach your instance over the network?
  * Authorizing - are you authorized to connect to the instance?
  * Authenticating - does the database accept your database credentials?



Each of those can be further broken down into different paths for investigation. The following section includes examples of questions you can ask yourself to help further narrow down the issue:

## Connection issues checklist

  * **Connecting**
    * Private IP
      * Have you [enabled the `Service Networking API`](https://console.cloud.google.com/apis/library/servicenetworking.googleapis.com) for your project?
      * Are you [using a Shared VPC](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip#api_and_iam_requirements)?
      * Does your user or service account have the [required IAM permissions](https://docs.cloud.google.com/sql/docs/postgres/private-ip#api_and_iam_requirements) to manage a private services access connection?
      * Is [private services access connection](https://docs.cloud.google.com/sql/docs/postgres/configure-private-services-access) configured for your project?
      * Did you [allocate an IP address range](https://docs.cloud.google.com/sql/docs/postgres/configure-private-services-access#allocating_an_ip_address_range) for the private connection?
      * Did your [allocated IP address ranges](https://docs.cloud.google.com/sql/docs/postgres/private-ip#allocated_ip_address_rangese) contain at least a /24 space for every region where you are planning to create postgres instances?
      * If you are specifying an [allocated IP address range](https://docs.cloud.google.com/sql/docs/postgres/private-ip#allocated_ip_address_rangese) for your postgres instances, does the range contain at least a /24 space for every region where you are planning to create postgres instances in this range?
      * Is the [private connection](https://docs.cloud.google.com/sql/docs/postgres/configure-private-services-access#creating_a_private_connection) created?
      * If the private connection was changed, were the [vpc-peerings](https://docs.cloud.google.com/sql/docs/postgres/configure-private-services-access#change-psa-config) updated?
      * Do the [VPC logs](https://docs.cloud.google.com/vpc/docs/flow-logs) indicate any errors?
      * Is your source machine's IP a [non-RFC 1918 address](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip#non-rfc1918)?
      * Have you run a Connectivity Test to trace the packet path and check for dropped packets?
    * Public IP
      * Is your source IP listed as an [authorized network](https://docs.cloud.google.com/sql/docs/postgres/configure-ip#add)?
      * Are SSL/TLS certificates [required](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl#enforcing_ssltls_encryption)?
      * Does your user or service account have the [required IAM permissions](https://docs.cloud.google.com/sql/docs/postgres/roles-and-permissions#introduction) to connect to a Cloud SQL instance?
  * **Authorizing**
    * Cloud SQL Auth Proxy
      * Is the Cloud SQL Auth Proxy [up to date](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy#keep-current)?
      * Is the Cloud SQL Auth Proxy [running](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#start-the-cloud-sql-proxy)?
      * Is the instance [connection name](https://console.cloud.google.com/sql/instances) formed correctly in the [Cloud SQL Auth Proxy connection command](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#connect-to-the-cloud-sql-proxy)?
      * Have you checked the Cloud SQL Auth Proxy output? Pipe the output to a file, or watch the Cloud Shell terminal where you started the Cloud SQL Auth Proxy.
      * Does your user or service account have the [required IAM permissions](https://docs.cloud.google.com/sql/docs/postgres/roles-and-permissions#introduction) to connect to a Cloud SQL instance?
      * Have you [enabled the `Cloud SQL Admin API`](https://console.cloud.google.com/apis/library/sqladmin.googleapis.com) for your project?
      * If you have an outbound firewall policy, make sure it allows connections to port 3307 on the target Cloud SQL instance.
      * If you are connecting using UNIX domain sockets, confirm that the sockets were created by listing the directory specified with the **-dir** when you started the Cloud SQL Auth Proxy.
    * Cloud SQL connectors and language-specific code
      * Is the [connection string](https://docs.cloud.google.com/sql/docs/postgres/connect-overview#languages) formed correctly?
      * Have you compared your code with the [sample code](https://docs.cloud.google.com/sql/docs/postgres/connect-overview#languages) for your programming language?
      * Are you using a runtime or framework for which we don't have [sample code](https://docs.cloud.google.com/sql/docs/postgres/connect-overview#languages)?
        * If so, have you [looked to the community](https://docs.cloud.google.com/sql/docs/postgres/getting-support#get_support_from_the_community) for relevant reference material?
    * Self-managed SSL/TLS certificates
      * Is the client certificate [installed](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl#overview) on the source machine?
      * Is the client certificate spelled correctly in the [connection arguments](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip#connect-ssl)?
      * Is the client certificate [still valid](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl#ssltls_certificates)?
      * Are you getting errors when [connecting using SSL](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip#connect-ssl)?
      * Is the server certificate still valid?
    * Authorized networks
      * Is the [source IP address](https://docs.cloud.google.com/sql/docs/postgres/configure-ip#add) included?
      * Are you using a [non-RFC 1918 IP address](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip#non-rfc1918)?
      * Are you using an [unsupported IP address](https://docs.cloud.google.com/sql/docs/postgres/authorize-networks#limitations)?
    * Connection failures
      * Are you authorized to connect?
      * Are you seeing connection limit errors?
      * Is your application closing connections properly?
  * **Authenticating**
    * Native database authentication (username/password)
      * Are you seeing `access denied` errors?
      * Are the [username and password](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users#creating) correct?
    * IAM database authentication
      * Have you [enabled the `cloudsql.iam_authentication` flag ](https://docs.cloud.google.com/sql/docs/postgres/create-edit-iam-instances#configuring_existing_instances_for)on your instance?
      * Did you [add a policy binding](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#creating-a-database-user) for the account?
      * Are you using the Cloud SQL Auth Proxy with the [`-enable_iam_login` or an Oauth 2.0 token](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#troubleshooting-a-login-failure) as the database password?
      * If using a service account, are you using the [shortened email name](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#creating-a-database-user)?
      * Learn more about [IAM database authentication in PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/authentication).



## Error messages

For specific API error messages, see the [Error messages](https://docs.cloud.google.com/sql/docs/error-messages) reference page.

## Additional connectivity troubleshooting

For other issues, see the [ Connectivity](https://docs.cloud.google.com/sql/docs/postgres/troubleshooting#connectivity) section in the troubleshooting page.

## Common connection issues

### Verify that your application is closing connections properly

If you see errors containing "`Aborted connection nnnn to db:`", it usually indicates that your application is not stopping connections properly. Network issues can also cause this error. The error does not mean that there are problems with your Cloud SQL instance. You are also encouraged to run `tcpdump` to inspect the packets to track down the source of the problem.

For examples of best practices for connection management, see [Managing database connections](https://docs.cloud.google.com/sql/docs/postgres/manage-connections).

### Verify that your certificates have not expired

If your instance is configured to use SSL, go to the [Cloud SQL Instances page](https://console.cloud.google.com/sql/instances) in the Google Cloud console and open the instance. Open its **Connections** page, select the **Security** tab and make sure that your server certificate is valid. If it has expired, you must add a new certificate and rotate to it. 

### Verify that you are authorized to connect

If your connections are failing, check that you are authorized to connect: 

  * If you are having trouble connecting using an IP address, for example, you are connecting from your on-premises environment with the psql client, then make sure that the IP address you are connecting from [is authorized to connect](https://docs.cloud.google.com/sql/docs/postgres/configure-ip) to the Cloud SQL instance. 

Connections to a Cloud SQL instance using a private IP address are automatically authorized for [RFC 1918 address ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges). This way, all private clients can access the database without going through the Cloud SQL Auth Proxy. Non-RFC 1918 address ranges must be configured as [authorized networks](https://docs.cloud.google.com/sql/docs/postgres/authorize-networks). 

Cloud SQL doesn't learn Non-RFC 1918 subnet routes from your VPC by default. You need to update the network peering to Cloud SQL to export any Non-RFC 1918 routes. For example: 
        
        gcloud compute networks peerings update cloudsql-postgres-googleapis-com \
        --network=NETWORK \
        --export-subnet-routes-with-public-ip \
        --project=PROJECT_ID

  * Here's your [current IP address](http://www.google.com#q=whats+my+ip).

  * Try the [`gcloud sql connect`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/connect) command to connect to your instance. This command authorizes your IP address for a short time. You can run this command in an environment with [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) and psql client installed. You can also run this command in [Cloud Shell](https://docs.cloud.google.com/shell/docs), which is available in the Google Cloud console and has [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) and the psql client pre-installed. Cloud Shell provides a Compute Engine instance that you can use to connect to Cloud SQL. 
  * Temporarily allow all IP addresses to connect to an instance by authorizing `0.0.0.0/0`. **Note:** Authorizing all IP addresses opens your database to any client that tries to connect. If you have sensitive or proprietary data in your database, don't use this method to investigate connectivity issues. 



### Verify how you connect

If you get an error message like: 
    
    
    FATAL: database `user` does not exist.
    

The `gcloud sql connect --user` command only works with the default user (`postgres`). The workaround is to connect using the default user, then use the `"\c"` psql command to reconnect as the different user.

### Determine how connections are being initiated

You can see information about your current connections by connecting to your database and running the following command:
    
    
    SELECT * from pg_stat_activity ;

Connections that show an IP address, such as `1.2.3.4`, are connecting using IP. Connections with `cloudsqlproxy~1.2.3.4` are using the Cloud SQL Auth Proxy, or else they originated from App Engine. Connections from `localhost` may be used by some internal Cloud SQL processes.

### Connection limits

There are no QPS limits for Cloud SQL instances. However, there are connection, size, and App Engine specific limits in place. See [Quotas and Limits](https://docs.cloud.google.com/sql/docs/postgres/quotas).

Database connections consume resources on the server and the connecting application. Always use good connection management practices to minimize your application's footprint and reduce the likelihood of exceeding Cloud SQL [connection limits](https://docs.cloud.google.com/sql/docs/postgres/quotas#configurable-limits). For more information, see [Managing database connections](https://docs.cloud.google.com/sql/docs/postgres/manage-connections). 

### Show connections and threads

To see the processes that are running on your database, use the [pg_stat_activity](https://www.postgresql.org/docs/current/static/monitoring-stats.html#PG-STAT-ACTIVITY-VIEW) table:
    
    
    select * from pg_stat_activity;
    

### Connections timeout (from Compute Engine)

Connections with a Compute Engine instance timeout after 10 minutes of inactivity, which can affect long-lived unused connections between your Compute Engine instance and your Cloud SQL instance. For more information, see [Networking and Firewalls](https://docs.cloud.google.com/compute/docs/networks-and-firewalls) in the Compute Engine documentation.

To keep long-lived unused connections alive, you can set the [TCP keepalive](http://tldp.org/HOWTO/TCP-Keepalive-HOWTO/usingkeepalive.html). The following commands set the TCP keepalive value to one minute and make the configuration permanent across instance reboots.

Display the current tcp_keepalive_time value.
    
    
    cat /proc/sys/net/ipv4/tcp_keepalive_time

Set tcp_keepalive_time to 60 seconds and make it permanent across reboots.
    
    
    echo 'net.ipv4.tcp_keepalive_time = 60' | sudo tee -a /etc/sysctl.conf

Apply the change.
    
    
    sudo /sbin/sysctl --load=/etc/sysctl.conf

Display the tcp_keepalive_time value to verify the change was applied.
    
    
    cat /proc/sys/net/ipv4/tcp_keepalive_time

## Tools for debugging connectivity

**Note:** Tools that are based on the Internet Control Message Protocol (ICMP), such as `ping` and `traceroute`, do not work with Cloud SQL. Do not use these tools for troubleshooting because they can return false negatives.

### tcpdump

The `tcpdump` is a tool to capture packets. It's highly encouraged to run `tcpdump` to capture and inspect the packets between your host and the Cloud SQL instances when you are debugging the connectivity problems.

### Locate your local IP address

If you don't know the local address of your host, then run the `ip -br address show` command. On Linux, this shows the network interface, the status of the interface, the local IP, and MAC addresses. For example: `eth0 UP 10.128.0.7/32 fe80::4001:aff:fe80:7/64`.

Alternatively, you can run `ipconfig` or `ifconfig` to see the status of your network interfaces.

### Test with Connectivity Test

[Connectivity Test](https://cloud.google.com/network-intelligence-center/docs/connectivity-tests) is a diagnostics tool that lets you check connectivity between endpoints in your network. It analyzes your configuration and in some cases performs run-time verification. It supports [Cloud SQL](https://cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/test-google-managed-services) now. Follow [these instructions](https://cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests) to run tests with your Cloud SQL instances.

### Test your connection

You can use the psql client to test your ability to connect from your local environment. For more information, see [Connecting the psql client using IP addresses](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip) and [Connecting the psql client using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy).

### Determine the IP address for your application

To determine the IP address of a computer running your application so you can authorize access to your Cloud SQL instance from that address, use one of the following options: 

  * If the computer is not behind a proxy or firewall, log in to the computer and use the [What is my IP?](https://ip4.me/) site to determine its IP address.
  * If the computer is behind a proxy or firewall, log in to the computer and use a tool or service like [whatismyipaddress.com](https://www.whatismyip.com/proxy-check/) to determine its true IP address. 



### Open local ports

To verify that your host is listening on the ports you think it is, run the `ss -tunlp4` command. This tells you what ports are open and listening. For example, if you have a PostgreSQL database running, then port 5432 should be up and listening. For SSH, you should see port 22. 

### All local port activity

Use the `netstat` command to see all the local port activity. For example, `netstat -lt` shows all the currently active ports.

### Connect to your Cloud SQL instance using telnet

To verify that you can connect to your Cloud SQL instance using `TCP`, run the `telnet` command. Telnet attempts to connect to the IP address and port you give it.

If your Cloud SQL instance is running a PostgreSQL database, for example, then you should be able to telnet to it on port 5432: `telnet 35.193.198.159 5432`. 

On success, you see the following: `

Trying 35.193.198.159... 

Connected to 35.193.198.159. 

`.

On failure, you see `telnet` hangs until you force-close the attempt: `

Trying 35.193.198.159... 

^C. 

`.

### Client authentication

Client authentication is controlled by a configuration file, which is named `pg_hba.conf` (HBA stands for host-based authentication).

Make sure the replication connections section of the `pg_hba.conf` file on the source database is updated to accept connections from the Cloud SQL VPC's IP address range. 

### Cloud Logging

Cloud SQL uses Cloud Logging, which lets you store, search, analyze, monitor, and alert on logging data. For more information, see the [Cloud Logging documentation](https://docs.cloud.google.com/logging/docs). For a list of queries to analyze your Cloud SQL logs, see [Cloud SQL sample queries](https://docs.cloud.google.com/logging/docs/view/query-library-preview#sql-filters).

#### View logs

You can view logs for Cloud SQL instances and other Google Cloud projects such as Cloud VPN or Compute Engine instances. To view logs for your Cloud SQL instance log entries:

### Console

  1. In the Google Cloud console, go to the **Cloud Logging** page.

[Go to Cloud Logging](https://console.cloud.google.com/logs/query)

  2. Select an existing Cloud SQL project at the top of the page.
  3. In the Query builder, add the following:
     * Resource: Select **Cloud SQL Database**. In the dialog, select a Cloud SQL instance.
     * Log names: Scroll to the Cloud SQL section and select appropriate log files for your instance. For example: 
       * cloudsql.googleapis.com/postgres.log
     * Severity: Select a log level.
     * Time range: Select a preset or create a custom range.



### gcloud

Use the [`gcloud logging`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command to view log entries. In the example below, replace `PROJECT_ID`. The [`limit`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read#--limit) flag is an optional parameter that indicates the maximum number of entries to return.
    
    
    gcloud logging read "projects/PROJECT_ID/logs/cloudsql.googleapis.com/postgres.log" \
    --limit=10

### Private IP addresses

Connections to a Cloud SQL instance using a private IP address are automatically authorized for [RFC 1918 address ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges). Non-RFC 1918 address ranges must be configured in Cloud SQL as [authorized networks](https://docs.cloud.google.com/sql/docs/postgres/authorize-networks). You also need to update the network peering to Cloud SQL to export any Non-RFC 1918 routes. For example: 
    
    
    gcloud compute networks peerings update cloudsql-postgres-googleapis-com   
    
    --network=NETWORK   
    
    --export-subnet-routes-with-public-ip   
    
    --project=PROJECT_ID

### Diagnose VPC network and private IP connection failures

When connecting to or from a Cloud SQL instance over a VPC network (such as with private services access or VPC Network Peering), connection failures often produce generic "Connection timed out" or "Connection refused" errors without indicating the root cause.

To diagnose why a connection is failing (for example, whether traffic is blocked by a firewall rule, a missing route, or an inactive peering), use [Network Intelligence Center Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests).

#### Run a Connectivity Test

You can test connectivity from a client VM instance to a Cloud SQL instance (or in reverse, such as when connecting from Cloud SQL to a source database during migration):

### Console

  1. In the Google Cloud console, go to the **Connectivity Tests** page: 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests)

  2. Click **Create connectivity test**.
  3. Under **Source** : 
     * Specify the source endpoint (for example, your client Compute Engine VM instance or IP address and VPC network).
  4. Under **Destination** : 
     * Specify the destination endpoint: 
       * **IP address** : Enter the private IP address of your Cloud SQL instance.
       * **Network** : Select your VPC network.
       * **Port** : Enter the database port (`3306` for MySQL, `5432` for PostgreSQL, or `1433` for SQL Server).
       * **Protocol** : Select `TCP`.
  5. Click **Create**.
  6. Review the test results: 
     * **Reachable** : The network path between the source and destination is open. If you still cannot connect, verify database user credentials and verify the database process is running.
     * **Unreachable / Dropped** : Expand the trace details to see the exact hop where traffic was dropped: 
       * **Dropped by firewall** : Check the firewall rule displayed in the trace and add an ingress allow rule on the destination network for the database port.
       * **No route** : Check that custom routes are exported and imported across the VPC Network Peering connection.
       * **Peering inactive** : Verify that the VPC Network Peering connection is in an `ACTIVE` state in both networks.



### gcloud

  1. Enable the Network Management API: 
         
         gcloud services enable networkmanagement.googleapis.com --project=PROJECT_ID
             

  2. Create and run a connectivity test from your source VM or IP to the Cloud SQL instance: 
         
         gcloud network-management connectivity-tests create TEST_NAME \
             --project=PROJECT_ID \
             --source-network=projects/PROJECT_ID/global/networks/VPC_NETWORK_NAME \
             --source-ip=SOURCE_IP \
             --destination-ip=INSTANCE_PRIVATE_IP \
             --destination-port=DB_PORT \
             --protocol=TCP \
             --round-trip
             

Replace the following:

     * `TEST_NAME`: A name for the test, such as `cloudsql-vpc-test`.
     * `SOURCE_IP`: The internal IP address of your client VM.
     * `INSTANCE_PRIVATE_IP`: The private IP address of your Cloud SQL instance.
     * `DB_PORT`: The database port (`3306` for MySQL, `5432` for PostgreSQL, or `1433` for SQL Server).
  3. View the diagnostic trace and drop cause: 
         
         gcloud network-management connectivity-tests describe TEST_NAME \
             --project=PROJECT_ID
             

The output indicates whether packets reach the destination or where they are dropped (such as a specific firewall rule or missing route).




#### Verify VPC Network Peering and firewall rules

If the connectivity test indicates packet loss or you are unable to establish the connection, verify the following:

  * **VPC Network Peering state:** Verify that the peering connection state is `ACTIVE`: 
        
        gcloud compute networks peerings list \
            --network=VPC_NETWORK_NAME \
            --project=PROJECT_ID
            

  * **Exchanged routes:** Check the routes exchanged across the peering connection: 
        
        gcloud compute networks peerings list-routes PEERING_NAME \
            --network=VPC_NETWORK_NAME \
            --region=REGION \
            --direction=OUTGOING \
            --project=PROJECT_ID
            

  * **Ingress firewall rules:** Make sure your VPC network has an ingress rule allowing traffic on the database port from the client IP range: 
        
        gcloud compute firewall-rules list \
            --project=PROJECT_ID \
            --filter="network:VPC_NETWORK_NAME AND allowed[].ports:DB_PORT"
            




### VPN troubleshooting

See the [Cloud VPN troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting#common_problems_and_solutions) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
