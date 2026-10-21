---
url: https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance/
title: Connect to a Redis instance \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:51.067956+00:00
---

# Connect to a Redis instance  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Connect to a Redis instance Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you are looking for the Memorystore for Redis Cluster documentation, see [Connect to a Memorystore for Redis Cluster instance](https://docs.cloud.google.com/memorystore/docs/cluster/connect-cluster-instance).

This page describes how to connect to your Redis instance using Telnet and `redis-cli`. In addition, this page provides instructions for how to connect when using features such as read replicas, AUTH, and in-transit encryption. Finally, this page provides instructions on connecting from a Google Kubernetes Engine environment.

For a list of Google Cloud environments that Memorystore for Redis supports, see [Supported environments](https://docs.cloud.google.com/memorystore/docs/redis/supported-environments). Some serverless environments that Memorystore supports require a Serverless VPC Access connector. See [Serverless VPC Access connector requirement](https://docs.cloud.google.com/memorystore/docs/redis/supported-environments#serverless-vpc-access-connector-requirement) for more details.

**Note:** If your instance uses [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/memorystore/docs/redis/use-cmek) and the [Cloud Key Management Service API](https://docs.cloud.google.com/kms/docs/reference/rest) is unavailable because of an outage, then when you reconnect to your instance, you might need to use a different IP address.

## Connect to a Redis instance from a Compute Engine VM using telnet

You can connect to the Memorystore for Redis instance from any Compute Engine VM that uses the instance's authorized network with a [supported RFC 1918 IP address](https://docs.cloud.google.com/memorystore/docs/redis/networking#supported_and_unsupported_networks).

  1. If you don't have a Compute Engine VM that uses that same authorized network as your instance, then create one and connect to the VM by using SSH. To do this, follow the steps in [Create a Linux VM instance in Compute Engine](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).

  2. Use `apt-get` to install `telnet`:
         
         sudo apt-get install telnet
         

  3. From the terminal, telnet to the IP address of the instance. Replace VARIABLES with appropriate values.
         
         telnet INSTANCE_IP_ADDRESS 6379
         

If you can connect to the instance, then the command returns this result:
         
         Trying INSTANCE_IP_ADDRESS…
         Connected to INSTANCE_IP_ADDRESS
         

  4. In the telnet session, enter some Redis commands:

Enter:
         
         PING
         

Result:
         
         PONG
         

Enter
         
         SET HELLO WORLD
         

Result:
         
         +OK
         

Enter:
         
         GET HELLO
         

Result:
         
         $5
         WORLD
         




## Connect to a Redis instance from a Compute Engine VM using `redis-cli`

You can connect to the Redis instance from any Compute Engine VM that uses the Redis instance's authorized network with a [supported RFC 1918 IP address](https://docs.cloud.google.com/memorystore/docs/redis/networking#supported_and_unsupported_networks).

  1. If you don't already have a Compute Engine VM that uses the authorized network for your Redis instance, create one and connect to it by following [Create a VM instance in a specific subnet](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#create_a_vm_instance_in_a_specific_subnet).

  2. Install `redis-cli` on the Compute Engine VM by running the following command from the Compute Engine SSH terminal:
         
         sudo apt-get install redis-tools
         

  3. Run the following command in the [Compute Engine terminal](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance#connect_to_your_instance), replacing variables with appropriate values.
         
         redis-cli -h redis-instance-ip-address
         

You are now connected to your Redis instance using `redis-cli`.

  4. Once you are done testing your connection to the Redis instance, you should consider [deleting the Compute Engine VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance#clean-up) you used to connect to the Redis instance. Doing so helps you avoid incurring charges to your Cloud Billing account.




## Connect to a Redis instance that uses AUTH

This section describes how to connect to a Redis instance that has the [AUTH](https://docs.cloud.google.com/memorystore/docs/redis/auth-overview) feature enabled.

  1. If you don't already have a Compute Engine VM that uses the same authorized network as your Redis instance, create one and connect to it by following [Quickstart Using a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).

  2. Install `redis-cli` on the Compute Engine VM by running the following command from the Compute Engine SSH terminal:
         
         sudo apt-get install redis-tools
         

  3. [Get](https://docs.cloud.google.com/memorystore/docs/redis/managing-auth#getting_the_auth_string) your instance's AUTH string

  4. Run the following command to use `redis-cli` to authenticate and connect to your instance, replacing variables with appropriate values:
         
         redis-cli -h instance-ip-address -a auth-string
         

Or:
         
         redis-cli -h instance-ip-address
         AUTH auth-string
         

  5. Run a Redis `SET` and `GET` command to verify that you have established an authenticated connection to your instance.

  6. Once you are done testing your connection to the Redis instance, you should consider [deleting the Compute Engine VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance#clean-up) you used to connect to the Redis instance. Doing so helps you avoid incurring charges to your Cloud Billing account.




## Connect to a Redis instance using the read endpoint

If your instance has [read replicas](https://docs.cloud.google.com/memorystore/docs/redis/read-replicas) enabled, you can connect to the read endpoint using the following instructions:

  1. If you don't already have a Compute Engine VM that uses that same authorized network as your Redis instance, create one and connect to it by following [Quickstart using a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).

  2. Install `telnet` using `apt-get`:
         
         sudo apt-get install telnet
         

  3. To find the IP address of your instance's read endpoint, [view read replica information for your instance](https://docs.cloud.google.com/memorystore/docs/redis/manage-read-replicas#view_read_replica_information_for_your_instance).

  4. From the terminal, telnet to the read endpoint IP address of the Redis instance, replacing variables with appropriate values.
         
         telnet read-endpoint-ip 6379
         

If successful, the command will return this result:
         
         Trying read-endpoint-ip…
         Connected to read-endpoint-ip
         

  5. In the telnet session, enter some Redis commands:

Enter:
         
         PING
         

Result:
         
         PONG
         




## Connect to a Redis instance securely by using Stunnel and telnet

This section provides an example of how to connect to a Redis instance that has in-transit encryption enabled using Stunnel. Stunnel is a proxy that adds Transport Layer Security (TLS) encryption functionality to clients and servers without changing their code. For more information, see the [_Stunnel_](https://www.stunnel.org/docs.html) documentation.

  1. If you don't have a Redis instance that has in-transit encryption enabled, then create one. For more information, see [Creating a Redis instance with in-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/enabling-in-transit-encryption#creating_a_redis_instance_with_in-transit_encryption).

  2. If you don't have a Compute Engine VM that uses the same authorized network as the Redis instance from the previous step, then create one and connect to it. For more information, see [Create a Linux VM instance in Compute Engine](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).

  3. Install the necessary tools for this procedure by running the following commands:
         
         sudo apt-get install stunnel4
         
         
         sudo apt-get install telnet
         

The remaining steps in this procedure occur in the SSH terminal of the Compute Engine VM that you created and connected to, unless otherwise specified.

  4. Configure your Compute Engine VM for use with Stunnel:

     1. Create a file for your [Certificate Authority](https://docs.cloud.google.com/memorystore/docs/redis/in-transit-encryption#certificate_authority) (CA) by running the following command:
            
            sudo vim /tmp/server_ca.pem
            

     2. View your Redis instance's CA(s) by running the following command in the standard terminal that you use to manage your Google Cloud resources (not the Compute Engine terminal):
            
            gcloud redis instances describe INSTANCE_ID --region=REGION
            

Make the following replacements:

        * INSTANCE_ID: the ID of your Redis instance
        * REGION: the region where the instance is located

There can up to three CAs.

     3. Copy all of the CAs, including the `-----BEGIN CERTIFICATE-----` line and the   
`-----END CERTIFICATE-----` line, and paste and save the contents in the `server_ca.pem` file that you created.

Make sure that the text of the CA is completely left justified and there's no leading whitespace on any line of the CA.

     4. Create a file for your Stunnel configuration information by running the following command:
            
            sudo vim /etc/stunnel/redis-client.conf
            

     5. Paste the following text in the file, replacing REDIS_INSTANCE_IP with the instance's IP address:
            
            output=/tmp/stunnel.log
            CAfile=/tmp/server_ca.pem
            client=yes
            pid=/var/run/stunnel.pid
            verifyChain=yes
            sslVersion=TLSv1.2
            [redis]
            accept=127.0.0.1:6378
            connect=REDIS_INSTANCE_IP:6378
            

     6. Start Stunnel by running the following command:
            
            sudo stunnel /etc/stunnel/redis-client.conf
            

     7. Verify that Stunnel is running:
            
            ps aux | grep stunnel
            

     8. Restart Stunnel by running the following command:
            
            sudo systemctl restart stunnel4
            

You can use the `ps aux | grep stunnel` command before and after restarting Stunnel to confirm that the restart is successful. If the Stunell process ID, shown by the `ps aux | grep stunnel` command, is different, then Stunell restarted successfully.

  5. To connect to your Redis instance using telnet, run the following command:
         
         telnet localhost 6378
         

  6. In the telnet session, test your connection.

     1. Optional: If your instance has Redis AUTH enabled, then you must authenticate before you test the connection.

Run the following command:
            
            AUTH AUTH_STRING
            

Replace AUTH_STRING with the instance's authentication string.

Result:
            
            OK
            

Run the following command:
    
    PING
    

Result:
    
    PONG
    

  7. Optional: As an alternative to telnet, you can connect by using `redis-cli` through the local Stunnel port and pass the AUTH string.

Run the following command:
         
         redis-cli -h 127.0.0.1 -p 6378 -a AUTH_STRING
         




## Connect from a local machine by using port forwarding

It can be helpful to connect to your Redis instance from your local machine during development. To do so you must create a Compute Engine instance to use for port forwarding to the Redis instance.

  1. Create a Compute Engine instance by running the following command:
         
         gcloud compute instances create COMPUTE_VM_NAME --machine-type=f1-micro --zone=ZONE
         

Where:

     * COMPUTE_VM_NAME is the name you designate for the Compute Engine VM.
     * ZONE is the zone where you want to provision the VM.

This command creates a Compute Engine VM with the [`f1-micro` machine type](https://docs.cloud.google.com/compute/docs/machine-types#machine_types) for cost-effectiveness. You can choose other machine types.

  2. Open a new terminal on your local machine.

  3. To create an SSH tunnel that port forwards traffic through the Compute Engine VM, run the following command:
         
         gcloud compute ssh COMPUTE_VM_NAME --zone=ZONE -- -N -L 6379:REDIS_INSTANCE_IP_ADDRESS:6379
         

Where:

     * COMPUTE_VM_NAME is the name of the Compute Engine VM.
     * ZONE is the same zone where the Compute Engine VM is located.
     * REDIS_INSTANCE_IP_ADDRESS is the IP address of your Redis instance.
  4. To test the connection, open a new terminal window and run the following command:
         
         redis-cli ping
         

If working properly, the result should return:
         
         PONG
         

You are now connected to the Redis instance, and you can send commands to the Redis instance using this open SSH tunnel. If you have not already installed `redis-cli`, install it so you can run this command.

  5. The SSH tunnel remains open as long as you keep the terminal window with the SSH tunnel connection up and running.




## Connect to a Redis instance from a Google Kubernetes Engine cluster

**Note:** To connect to a Redis instance that uses the [private services access connect mode](https://docs.cloud.google.com/memorystore/docs/redis/networking#private_services_access) you must have VPC-native/IP aliasing enabled on your GKE cluster. To use GKE to connect to a Redis instance that uses the [direct peering connect mode](https://docs.cloud.google.com/memorystore/docs/redis/networking#direct_peering), use the workaround in step 5.

To verify if your cluster uses IP aliasing, use [`gcloud container clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/describe).

You can connect to your Redis instance from Google Kubernetes Engine clusters that use the same authorized network as your Redis instance.

### Connect from a pod running a bash shell

  1. Go to the GKE page in the Google Cloud console.  
[GKE](https://console.cloud.google.com/kubernetes/list)
  2. Click the GKE cluster you'd like to connect from. If you don't already have a cluster, create one with IP aliases enabled. For instructions on how to create a cluster with IP aliases enabled, see [Creating a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).
  3. Click the **Connect** button to the right of your cluster's name, then click the **Run in Cloud Shell** button in the window that appears.
  4. Configure `kubectl` command line access by running the following command: 
         
         gcloud container clusters get-credentials CLUSTER_NAME --zone=CLUSTER_ZONE --project=PROJECT_ID

     * `CLUSTER_NAME` is the name of your cluster.
     * `CLUSTER_ZONE` is the zone your cluster is in. Must also be the zone your Redis instance is in.
     * `PROJECT_ID` is the project where your cluster and your Redis instances exist.
You should get the success message: `kubeconfig generated for CLUSTER_NAME`
  5. If your cluster is version 1.8 or higher **and** has IP aliases enabled, skip this step. If your cluster is version 1.7 or lower, or your version 1.8 or higher cluster doesn't have IP aliases enabled, follow these workaround steps before trying to connect to your instance: 

#### Workaround

Run the following commands, replacing `RESERVED_IP_RANGE` with the reserved IP range of your instance:
         
         git clone https://github.com/bowei/k8s-custom-iptables.git
         
         cd k8s-custom-iptables/
         
         TARGETS="RESERVED_IP_RANGE" ./install.sh

If you don't know the reserved IP range of your instance, you can find out by entering this command: `gcloud redis instances describe INSTANCE_ID --region=REGION`

For more information about IP aliases, including how to create a cluster with this setting enabled, see [Creating a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips). 
  6. Use the following command to connect to a bash shell: 
         
         kubectl run -i --tty busybox --image=busybox -- sh

  7. Telnet to your Redis instance using the host address and port number: 
         
         telnet HOST-IP PORT

  8. Enter a basic Redis command to verify the connection: 
         
         PING
         +PONG

  9. To close the telnet connection, press Control+C (or Command+C on Mac). To exit the bash shell in your pod, enter return. If you are done and no longer need to connect to Redis, run the following command from the `/k8s-custom-iptables/` directory: 
         
         ./uninstall.sh




### Connect to a Redis instance from a Google Kubernetes Engine pod

Before you begin, you need a GKE cluster. If you don't already have a cluster, create one with IP aliases enabled. For instructions on how to create a cluster with IP aliases enabled, see [Creating a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).

  1. From the top-right corner of the console, click **Activate Cloud Shell** ![In this step, you activate Cloud Shell.](https://docs.cloud.google.com/static/memorystore/img/cloud-shell-connect.png) button.
  2. Configure `kubectl` command line access by running the following command: 
         
         gcloud container clusters get-credentials CLUSTER_NAME --zone CLUSTER_ZONE --project PROJECT_ID

     * `CLUSTER_NAME` is the name of your cluster.
     * `CLUSTER_ZONE` is the zone your cluster is in. Must also be the zone your Redis instance is in.
     * `PROJECT_ID` is the project where your cluster and your Redis instances exist.
You should get the success message: `kubeconfig generated for CLUSTER_NAME`
  3. If your cluster is version 1.8 or higher **and** has IP aliases enabled, skip this step. If your cluster is version 1.7 or lower, or your version 1.8 or higher cluster doesn't have IP aliases enabled, follow these workaround steps before trying to connect to your instance: 

#### Workaround

Run the following commands, replacing `RESERVED_IP_RANGE` with the reserved IP range of your instance:
         
         git clone https://github.com/bowei/k8s-custom-iptables.git
         
         cd k8s-custom-iptables/
         
         TARGETS="RESERVED_IP_RANGE" ./install.sh

If you don't know the reserved IP range of your instance, you can find out by entering this command: `gcloud redis instances describe INSTANCE_ID --region [REGION]`

For more information about IP aliases, including how to create a cluster with this setting enabled, see [Creating a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips). 
  4. Use the following command to start a Redis pod running the `redis-cli`: 
         
         kubectl run -i --tty redisbox --image=redis:7.2 -- sh

  5. Run a `redis-cli` command, replacing `HOST-IP` with the host IP address of your Redis instance: 
         
         redis-cli -h HOST-IP info

  6. Optionally, run a [Redis benchmark](https://redis.io/topics/benchmarks) command, again replacing `HOST-IP` with the host IP address of your Redis instance: 
         
         redis-benchmark -c 100 -n 100000 -d 1024 -r 100000 -t PING,SET,GET,INCR,LPUSH,RPUSH,LPOP,RPOP,SADD,SPOP,MSET -h HOST-IP -q

  7. To exit the Redis pod, enter `return`. If you are done and no longer need to connect to Redis, run the following command from the `/k8s-custom-iptables/` directory: 
         
         ./uninstall.sh




## What's next

Connect to your Redis instance using a sample application that runs on:

  * [Compute Engine](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-gce)
  * [GKE](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-gke)
  * [Cloud Run](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-cloud-run)
  * [App Engine standard environment](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-standard)
  * [App Engine flexible environment](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-flex)
  * [Cloud Run functions](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-functions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
