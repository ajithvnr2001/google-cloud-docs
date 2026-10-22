---
url: https://docs.cloud.google.com/alloydb/docs/benchmark-oltp-performance-alloydb/
title: Benchmark OLTP performance on AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:23.592052+00:00
---

# Benchmark OLTP performance on AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/benchmark-oltp-performance-alloydb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Benchmark OLTP performance on AlloyDB for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure AlloyDB for PostgreSQL and a client machine to benchmark the performance of AlloyDB using [TPC-C](http://www.tpc.org/tpcc/), an OLTP benchmark specification. This document also describes how to run customized read- and write-intensive OLTP scenarios, like Index Insert Only and Select Only.

The instructions in this document are based on a specific configuration of AlloyDB and the client machine. Use the provided values for each step in the benchmarking instructions.

## AlloyDB workload capabilities

AlloyDB provides enterprise-level reliability, scalability, and performance suitable for all businesses and critical workloads. AlloyDB provides the following components and features that enable high performance for your transactional (OLTP), analytical (OLAP), and hybrid (HTAP) workloads:

  * Log and transaction management
  * Dynamic memory management
  * Artificial intelligence and machine learning integration
  * Built-in [columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about)
  * A multi-tiered cache
  * Distributed and scalable storage



Relational database systems typically require a database administrator to optimize the database for benchmarking, which includes configuring the transaction log settings, establishing the right buffer pool sizes, and modifying other database parameters or flags and characteristics. These settings vary depending on instance size and type.

AlloyDB comes pre-configured with optimized settings for each machine type. AlloyDB doesn't require you to tune flags at the database level to achieve high OLTP performance; instead, AlloyDB has high OLTP performance built in.

**Note:** The accuracy of your results might vary depending on several factors including the type of AlloyDB instance, the type of the client machine driving the benchmark, region, zone, and network bandwidth at the time of testing.

### Supported benchmark types

This document shows you how to run OLTP benchmarks using the following tools:

**OLTP benchmark drivers** | **Use cases**  
---|---  
[HammerDB](https://www.hammerdb.com/index.html) | HammerDB measures the system's performance in terms of transactions per minute (TPM) and generates reports that include detailed statistics and performance metrics.   
  
HammerDB supports benchmark parameter customization, which lets you adjust the database size, the number of warehouses, and other workload characteristics to simulate different scenarios.   
  
HammerDB includes a [TPC-C](http://www.tpc.org/tpcc) benchmark implementation for evaluating the performance of OLTP systems. The HammerDB TPC-C implementation lets you simulate a workload similar to the TPC-C benchmark, including a mix of transactions that mimic the behavior of a wholesale supplier environment.  
[pgbench](https://www.postgresql.org/docs/13/pgbench.html) | pgbench is a benchmarking tool that comes bundled with PostgreSQL. pgbench lets you simulate transaction workloads such as inserting, updating, selecting data, and measuring the database system's performance in Transactions Per Second (TPS).  
  
When you use pgbench, you can customize the database size, number of clients and transaction mix to emulate your production workload and obtain insights into the system's behavior under different scenarios.   
pgbench includes a TPC-B implementation. The pgbench TPC-B implementation is similar to a TPC-B benchmark.   
  
## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the AlloyDB, Compute Engine, and Resource Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=alloydb.googleapis.com,compute.googleapis.com,cloudresourcemanager.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the AlloyDB, Compute Engine, and Resource Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=alloydb.googleapis.com,compute.googleapis.com,cloudresourcemanager.googleapis.com)

  8. Enable the Cloud APIs necessary to create and connect to AlloyDB for PostgreSQL.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=alloydb.googleapis.com,compute.googleapis.com,cloudresourcemanager.googleapis.com,servicenetworking.googleapis.com)

     1. In the **Confirm project** step, click **Next** to confirm the name of the project you are going to make changes to.

     2. In the **Enable APIs** step, click **Enable** to enable the following:

        * AlloyDB API
        * Compute Engine API
        * Cloud Resource Manager API
        * Service Networking API

The Service Networking API is required if you plan to configure network connectivity to AlloyDB using a VPC network that resides in the same Google Cloud project as AlloyDB. 

The Compute Engine API and Cloud Resource Manager API are required if you plan to configure network connectivity to AlloyDB using a VPC network that resides in a different Google Cloud project.




## Set up and provision the database and the client machine

Start the benchmark by creating a AlloyDB cluster and instance. Unless otherwise specified, the information in this document is based on a 16 vCPU with 128 GB RAM as a primary AlloyDB instance.

### Create an AlloyDB cluster and instance

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click **Create Cluster**.

  3. In the **Cluster ID** field, enter a name for your cluster.

  4. In **Zonal availability** , select **Multiple zones (Highly Available)** for the cluster type.

  5. Select the default network.

  6. In the **Database version** field, select one of the following:

     * **PostgreSQL 17**

     * **PostgreSQL 18**

  7. Make a note of the location of the primary zone and private IP address. Do not create a read pool.

**Note:** This benchmarking exercise is conducted without read pools. The instance must be a multi-zone, highly available instance.
  8. Click **Create Cluster**.




### Provision the client machine

To run OLTP benchmarks, you need a client machine with adequate processing power. Benchmark tools like [HammerDB](https://www.hammerdb.com/) and [pgbench](https://www.postgresql.org/docs/14/pgbench.html) run in a highly parallel way, and they consume a lot of CPU. A client machine must not be a bottleneck when you run an OLTP benchmark.

Unless otherwise specified, the instructions in this document use an E2-standard-32 machine with 128 GB disk as a client for OLTP benchmarks to drive an AlloyDB instance on a 16 vCPU machine with 128 GB RAM. You must create the client machine in the same zone as the AlloyDB primary instance.

**Important:** To run the OLTP benchmark described in this document, you must provision the Debian linux client in the same region, zone, and VPC as the AlloyDB primary instance. Benchmarking tools access the AlloyDB instance over private IP.

To run the TPC-C benchmark on an AlloyDB primary instance with 16 virtual CPUs, follow these steps to create a Compute Engine VM and provision a client machine:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the project containing the AlloyDB instance you want to connect to.
  3. Click **Create instance**.
  4. Click the **Machine configuration** section.
  5. Enter a **Name** for the instance.
  6. Configure the zone where you want to create the instance. The zone must be the same as the zone of the AlloyDB primary instance.
  7. Select a machine type of **e2-standard-32**.
  8. Retain the default values in the **OS and Storage** section.
  9. Click the **Networking** section, and set **Network interfaces** to the VPC network configured for private services access to AlloyDB.  
If **Network interfaces** is not set to the VPC network configured for private services access, expand it and then set **Network** to the VPC network.
  10. Retain the default values in the **Observability** section.
  11. Click the **Security** section.
  12. In **Identity and API access** , set **Access scopes** to **Allow full access to all Cloud APIs**.
  13. Retain the default values in the **Advanced** section.
  14. Click **Create**.
  15. After the VM is created, connect to the Compute Engine VM that you created using SSH.



### Set up the benchmark driver machine

After you install and set up the database and client machine, you configure the client machine running on Google Cloud, where you install benchmarking tools like HammerDB and pgbench.

To set up the benchmark driver machine, follow these steps:

  1. Connect to the client machine using the following [`gcloud compute ssh`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) command:
         
         gcloud compute ssh --zone "PRIMARY_ZONE" "CLIENT_MACHINE_NAME"  --project "GOOGLE_PROJECT"

  2. Install the PostgreSQL client.

     1. Use the following command to install a PostgreSQL client that includes a psql application, and then ensure you are able to connect.
            
            sudo apt-get update
            sudo apt install postgresql-client

     2. Use the following command to ensure that the client works and that you're able to connect to AlloyDB. Use the private IP address of your primary AlloyDB instance.
            
            psql -h PRIVATE_IP -U postgres

  3. Install the HammerDB-4.6 driver for the TPC-C benchmark by running the following commands:
         
         mkdir hammerdb
         pushd hammerdb
         curl -OL https://github.com/TPC-Council/HammerDB/releases/download/v4.6/HammerDB-4.6-Linux.tar.gz
         tar zxvf HammerDB-4.6-Linux.tar.gz
         

  4. Install the pgbench driver for TPC-B and miscellaneous OLTP benchmarking by running the following commands:
         
         sudo apt-get update
         sudo apt-get install postgresql-contrib
         pgbench --version
         

If the `pgbench --version` runs without errors, then this means that pgbench is installed.




## Perform a benchmark cleanup

If you're planning to execute multiple benchmarks in succession, you must perform a benchmark cleanup between each benchmark to ensure accurate and reliable benchmarking results.

A benchmark cleanup ensures that residual effects from previous benchmarks don't affect the performance measurements of the new benchmark. Benchmark cleanups also help to ensure consistency and repeatability of the benchmark results, which is essential for making meaningful comparisons between different systems or identifying areas for optimization in hardware, software, or configuration.

Follow these steps to perform a benchmark cleanup before you run another benchmark:

  1. Delete the previous benchmark data or benchmark database. To drop the previous benchmark database, use the following `psql` command from the client machine:
         
         psql -h PRIVATE_IP -U postgres -c "DROP DATABASE IF EXISTS <database_name>;"
         

For more information about using `psql`, see [Connect to a database](https://docs.cloud.google.com/alloydb/docs/connect-psql).

  2. [Reboot the AlloyDB instance](https://docs.cloud.google.com/alloydb/docs/instance-restart). This step clears caches at the database and operating system level.




## Run a TPC-C Benchmark

HammerDB is a benchmarking tool that includes a TPC-C benchmark implementation for evaluating the performance of OLTP systems. HammerDB's TPC-C implementation lets you simulate a workload similar to the TPC-C benchmark, including a mix of transactions that mimic the behavior of a wholesale supplier environment.

HammerDB measures the system's performance in terms of transactions per minute (TPM) and generates reports that include detailed statistics and performance metrics. Additionally, HammerDB supports customization of the benchmark parameters, allowing users to adjust the database size, the number of warehouses, and other workload characteristics to simulate different scenarios.

### Performance evaluation scenarios

Performance of TPC-C benchmarking is evaluated using the following methods:

  * **Partially (~30%) cached mode:** In this mode, a large TPC-C database is generated, which can only partially fit in the buffer cache. The transactions in this mode aren't always served from memory and incur I/O to the underlying storage subsystems. This scenario is applicable to the OLTP needs of many users.

  * **Fully (100%) cached mode:** In this mode, the TPC-C database fully fits in the buffer cache. The AlloyDB instance uses approximately 90% of the available 128 GB RAM, including buffer cache.

Since TPC-C transactions perform minimal I/Os —because reads are mostly served from buffer cache— in this mode, higher TPM is expected in comparison to partially-cached runs. This scenario is applicable to the OLTP needs of users with very low I/O needs.




### Set up the client machine

  1. Set up the benchmark driver machine.

  2. If you are running multiple benchmarks in succession, perform a benchmark cleanup.

  3. Open the `hammerdb/HammerDB-4.6 directory` by running the following command:
         
         cd hammerdb/HammerDB-4.6

You run commands from this directory to set up the client machine.

  4. Create the create `setup.env` file using the following commands:

**Note:** If you're using [managed connection pooling](https://docs.cloud.google.com/alloydb/docs/configure-managed-connection-pooling), then change the port number from `5432` to `6432`. Apply throughout the examples on this page.
         
         cat << EOF > setup.env
         # Private IP of the AlloyDB primary instance
         export PGHOST=PRIVATE_IP
         # Postgres default port address. You do not need to change it unless you use non-default port address.
         export PGPORT=5432   # default port to connect with postgres
         # Number of TPC-C warehouses to load. This determines the overall database size.
         export NUM_WAREHOUSE=576
         # Number of users for running the benchmark.
         export NUM_USERS=256
         EOF

**Note:** The number of users (or clients) is set to `256`. This number of users is tuned to provide the best throughput with acceptable latency on the partially and fully cached configurations.
  5. Edit the generated `setup.env` file by replacing all the highlighted parameter values with parameter values that best suited to your environment setup.

  6. Optional: Test the partially (~30%) cached mode by changing `NUM_WAREHOUSE` to `3200` in the `setup.env` file. For more information, see Performance evaluation scenarios.

  7. Optional: Test the fully (100%) cached mode by changing `NUM_WAREHOUSE` to `576` in the `setup.env file`. For more information, see Performance evaluation scenarios.




### Load TPC-C data into the database

A _load step_ refers to the process of populating the benchmark database with initial data before running the performance test.

During the load step, the database is populated with a specified number of warehouses, customers, and other entities according to the TPC-C specifications. The purpose of the load step is to create a realistic workload for the performance test, and to ensure that the test results are comparable across different systems.

After the load step is completed, the database is in a consistent state with a defined set of initial data, ready to be used for the TPC-C benchmark test.

To load the TPC-C database, follow these steps:

  1. Switch to the benchmark home directory using the following command:
         
         cd hammerdb/HammerDB-4.6

  2. Copy the following contents and then paste them into `build-tpcc.sh`:
         
         #!/bin/bash -x
         
         source ./setup.env
         
         # create role tpcc with superuser login as 'postgres' and password as 'AlloyDB#123';
         # -----------------------------------------------------
         
         ./hammerdbcli << EOF
         
         # CONFIGURE PARAMETERS FOR TPCC BENCHMARK
         # --------------------------------------
         dbset db pg
         dbset bm tpc-c
         
         # CONFIGURE POSTGRES HOST AND PORT
         # --------------------------------------
         diset connection pg_host $PGHOST
         diset connection pg_port $PGPORT
         
         # CONFIGURE TPCC
         # --------------------------------------
         diset tpcc pg_superuser postgres
         diset tpcc pg_superuserpass AlloyDB#123
         diset tpcc pg_user tpcc
         diset tpcc pg_pass AlloyDB#123
         diset tpcc pg_dbase tpcc
         
         # SET NUMBER OF WAREHOUSES AND USERS TO MANAGE EACH WAREHOUSE
         # THIS IMPORTANT METRIC ESTABLISHES THE DATABASE SCALE/SIZE
         # --------------------------------------
         diset tpcc pg_count_ware $NUM_WAREHOUSE
         diset tpcc pg_num_vu 10
         
         # LOG OUTPUT AND CONFIGURATION DETAILS
         # --------------------------------------
         vuset logtotemp 1
         print dict
         
         # CREATE AND POPULATE DATABASE SCHEMA
         # --------------------------------------
         buildschema
         
         waittocomplete
         vudestroy
         quit
         
         EOF
         

  3. Execute the following load command and wait for the command to finish.
         
         chmod +x ./build-tpcc.sh
         mkdir results
         sudo nohup ./build-tpcc.sh > results/build-tpcc.out 2>&1

  4. Validate the load. After the previous script completes, we recommend that you confirm that the database load was successful. To verify the database size, run the following:
         
         psql -h $PGHOST -p 5432 -U postgres
         postgres=> \l+ tpcc
                                                                                   List of databases
              Name     |      Owner       | Encoding | Collate |  Ctype  |           Access privileges           |  Size   | Tablespace |                Description
          --------------+------------------+----------+---------+---------+---------------------------------------+---------+------------+--------------------------------------------
          tpcc         | tpcc             | UTF8     | C.UTF-8 | C.UTF-8 |                                       | --- GB  | pg_default |
                    |                  |          |         |         |                                       | 160.000 |            |
          (1 row)
         




In a 30% cached TPC-C configuration (with 3200 warehouses), expect the size of the `tpcc` database to be around 300 GB.

In 100% cached TPC-C configuration (with 576 warehouses), expect the size of the `tpcc` database to be around 55 GB.

### Run the TPC-C benchmark

You are now ready to run the TPC-C performance test. The TPC-C benchmark is executed using the populated database from the load step. The benchmark generates a series of transactions that simulate a typical business environment, including order entry, payment processing, and inventory management. The workload is measured in _transactions per minute_ (TPM), which represents the number of complete business transactions that the system can handle in one minute.

The run step is designed to stress the database system under realistic conditions and to provide a standard way of measuring performance that you can compare across different database systems. Vendors and users often use the results of the TPC-C benchmark to evaluate the performance of different database systems and hardware configurations.

**Note:** The following script runs the TPC-C benchmark for about 1 hour after approximately 10 minutes of warm-up.

To run the TPC-C benchmark, follow these steps:

  1. Switch to benchmark home directory:
         
         cd hammerdb/HammerDB-4.6

  2. Copy the following contents and then paste them into `run-tpcc.sh`:
         
         #!/bin/bash -x
         
         source ./setup.env
         
         ./hammerdbcli << EOF
         dbset db pg
         dbset bm tpc-c
         
         # CONFIGURE PG HOST and PORT
         # -------------------------
         diset connection pg_host $PGHOST
         diset connection pg_port $PGPORT
         
         # CONFIGURE TPCC DB
         # -------------------------
         diset tpcc pg_superuser postgres
         diset tpcc pg_superuserpass AlloyDB#123
         diset tpcc pg_user postgres
         diset tpcc pg_pass AlloyDB#123
         diset tpcc pg_dbase tpcc
         
         # BENCHMARKING PARAMETERS
         # -------------------------
         diset tpcc pg_driver timed
         diset tpcc pg_rampup 10
         diset tpcc pg_duration 60
         diset tpcc pg_vacuum false
         diset tpcc pg_partition false
         diset tpcc pg_allwarehouse true
         diset tpcc pg_timeprofile true
         diset tpcc pg_connect_pool false
         diset tpcc pg_dritasnap false
         diset tpcc pg_count_ware $NUM_WAREHOUSE
         diset tpcc pg_num_vu 1
         
         loadscript
         print dict
         vuset logtotemp 1
         vuset vu $NUM_USERS
         vucreate
         vurun
         waittocomplete
         quit
         EOF
         

  3. Run the script using the following commands:
         
         chmod +x run-tpcc.sh
         mkdir results
         sudo nohup ./run-tpcc.sh > results/run-tpcc.out 2>&1

  4. Wait for the `run-tpcc.sh` script to finish. The script takes approximately 1 hour and 10 minutes to complete. After the script finishes, you can analyze the results.




### Analyze the benchmark results

In TPC-C benchmarking, New Orders Per Minute (NOPM) and Transactions Per Minute (TPM) are performance metrics used to measure the performance of a database system.

  * **NOPM:** measures the number of new order transactions that the system can handle in one minute. The new order transaction is one of the most important transactions in the TPC-C benchmark and involves creating a new order for a customer.

  * **TPM:** measures the total number of completed business transactions that the system can handle in one minute. Transactions include new order transactions as well as other types of transactions defined in the TPC-C benchmark, such as payment, delivery, and order status.

TPM is the primary performance metric for the TPC-C benchmark because it provides an overall measure of the system's ability to handle a realistic workload. NOPM can be a useful metric for systems that are focused on processing new orders, such as ecommerce or retail systems.




#### View results with 30% cached TPC-C database on a 16 vCPU machine

To extract the performance numbers for this scenario, use the following command:
    
    
    grep NOPM results/run-tpcc.out

The following is the expected output:
    
    
    Vuser 1:TEST RESULT : System achieved 252970 NOPM from 582385 PostgreSQL TPM
    

With 30% cached TPC-C database on 16 vCPU machine (with `NUM_WAREHOUSE=3200` and `NUM_USERS=256`), you observe 252,970 tpm-C (New Order Per Minute) from a cumulative 582,385 AlloyDB TPM.

#### View results with 100% cached TPC-C database on a 16 vCPU machine

On a 100% cached TPC-C database on 16 vCPU machine (with `NUM_WAREHOUSE=576` and `NUM_USERS=256`), you observe 428,316 tpm-C (New Order Per Minute) from a cumulative 974,264 AlloyDB TPM.

To extract the performance numbers for this scenario, use the following command:
    
    
    grep NOPM results/tpcc-run.out

The following is the expected output:
    
    
    Vuser 1:TEST RESULT : System achieved 428316 NOPM from 974264 PostgreSQL TPM
    

### Summary of performance results on 16 vCPU machine

The following table summarizes benchmark performance results for a 16 vCPU machine:

**TPC-C Scenario** | **NUM_WAREHOUSE** | **NUM_USERS** | **NOPM** | **Cumulative TPM**  
---|---|---|---|---  
30% cached | 3200 | 256 | 252,970 | 582,385  
100% cached | 576 | 256 | 428,316 | 974,264  
  
### Observe database performance metrics

To further understand the behavior of your database system, use AlloyDB monitoring tools to observe important system metrics like CPU usage, memory usage, and transactions per second. For more information, see [Monitor instance performance](https://docs.cloud.google.com/alloydb/docs/monitor-instance).

For example, after running this benchmark, you can observe in the AlloyDB **Overview** page in the Google Cloud console that the mean CPU utilization for the 100% cached TPC-C run is almost 90%.

## Run a TPC-C benchmark on a 64 vCPU AlloyDB instance

To run a TPC-C benchmark on a 64 vCPU AlloyDB instance, you follow the same setup steps as in Run a TPC-C benchmark, but you use different machine types.

### Set up AlloyDB and the client machine

  1. Create an AlloyDB cluster and instance, substituting `64 vCPU, 512GB` as the machine type.

  2. Provision the client machine, substituting the `n2-standard-64` as the machine type.

  3. Set up the benchmark driver machine.




### Run the benchmark

  1. If you are running multiple benchmarks in succession, perform a benchmark cleanup.

  2. Set up the client machine, substituting the following values:

     * Set `PGHOST` to the Private IP of your new 64 vCPU AlloyDB instance.
     * For the 30% Cached TPC-C scenario, set `NUM_WAREHOUSE=12800` and `NUM_USERS=1024`.
     * For 100% Cached TPC-C scenario, set `NUM_WAREHOUSE=2304` and `NUM_USERS=1024`.
  3. Set up and load a TPC-C database. To speed up the load, change the value of `pg_num_vu` to 64 in `build-tpcc.sh` as `diset tpcc pg_num_vu 64`.

  4. Run the TPC-C benchmark.




### Analyze the benchmark results

The following table summarizes benchmark performance results on a 64 vCPU machine:

**Benchmark mode** | **NUM_WAREHOUSE** | **NUM_USERS** | **NOPM** | **Cumulative TPM**  
---|---|---|---|---  
30% cached | 12800 | 1024 | 589,598 | 1,371,160  
100% cached | 2304 | 1024 | 716,138 | 1,665,438  
  
## Run a pgbench TPC-B benchmark

[TPC-B](https://www.tpc.org/tpcb/) (Transaction Processing Performance Council Benchmark B) is one of the benchmark modes available in _pgbench_ , a benchmarking tool for PostgreSQL. TPC-B simulates a banking scenario in which multiple tellers execute transactions on customer accounts. The workload consists of the following types of transactions:

  * Deposits
  * Withdrawals
  * Balance inquiries



The benchmark measures the performance of the database system by simulating a mix of these transactions and measuring the number of transactions per second that the system can handle.

The TPC-B mode in pgbench generates a synthetic database and simulates a mix of transactions that resembles the TPC-B workload, but it isn't officially certified by the TPC organization. Therefore, while the TPC-B mode in pgbench provides a useful approximation of TPC-B performance, don't use it to claim compliance with TPC-B standards.

### Scenarios to measure performance

This section describes how to measure TPC-B performance in the following critical modes. The only parameter that is different in these modes is the value of the `SCALE_FACTOR` parameter.

#### Partially-cached database scenario

In this scenario, you set up and initialize a large database (approximately 650 GB in size) by using `--scale= 50000`. Having a large database that doesn't fit in memory and causes significant disk I/O provides a realistic representation of many production workloads.

A large database that causes significant disk I/O can underscore the importance of database design and query optimization. A large database can also expose performance issues related to disk I/O, such as slow disk access or inefficient queries, that might not be apparent in a small or entirely memory-resident database.

#### Fully-cached database scenario

In this scenario, you set up and initialize a database of approximately 60GB in size by using `--scale=4000` so that it resides in the buffer pool. Benchmarking a memory-resident database is important because it lets you assess the maximum performance of the database system in a controlled environment.

A memory-resident database stores all data in the PostgreSQL buffer pool, eliminating the I/O bottleneck that can occur when accessing data from disk. This mode can help identify performance bottlenecks that aren't related to I/O, such as CPU usage or locking issues, that might not be apparent when you benchmark a database that relies on disk I/O.

### Set up the database server and client machine

To set up the infrastructure to run a pgbench TPC-B benchmark, follow These steps:

  1. Create an AlloyDB cluster and instance, substituting `16 vCPU, 128GB` as the machine type.

  2. Provision the client machine, substituting `E2-standard-16 (minimum)` as the machine type.

  3. Set up the benchmark driver machine.

  4. Perform a benchmark cleanup.




### Run the pgbench TPC-B benchmark

**Important:** We recommend that you run the benchmark for a longer duration because the throughput is lower in the first few seconds, and it takes time to reach a steady state.

  1. Connect to the client machine using the following Google Cloud CLI command:
         
         gcloud compute ssh --zone "PRIMARY_ZONE" "CLIENT_MACHINE_NAME" --project "GOOGLE_PROJECT"

  2. Create the `pgbench-setup.env` file:
         
         $ cat << EOF > pgbench-setup.env
         
         # Private IP of the AlloyDB primary instance
         export PGHOST=<private_ip>
         
         # Set PGUSER to postgres as a default user.
         export PGUSER=postgres
         
         # Password set for PGUSER
         export PGPASSWORD=<your pg password>
         
         # In pgbench, the scale factor represents the size of the test database.
         # and is defined as the number of 1 MB-sized data pages to be generated per client.
         export SCALE_FACTOR=<scale_factor>
         
         # Number of clients to drive the benchmark in throughput mode
         export NUM_CLIENTS=<num_clients>
         
         EOF
         

  3. Edit the generated `setup.env` file and replace the following parameter value with values that are suitable to your environment setup.

     * PRIVATE_IP: the private IP of your AlloyDB instance.

Use the following table to choose `<scale_factor>` and `<num_clients>` values. These values must scale with the machine type and database size (fully cached or partially cached). The examples in this guide use `SCALE_FACTOR` and `NUM_CLIENT` values corresponding to the `n2-highmem-16` machine type.

| **Fully Cached** | **Partially Cached**  
---|---|---  
**Machine Type** | SCALE_FACTOR | NUM_CLIENTS | SCALE_FACTOR | NUM_CLIENTS  
n2-highmem-2 | 500 | 48 | 6250 | 32  
n2-highmem-4 | 1000 | 96 | 12500 | 64  
n2-highmem-8 | 2000 | 192 | 25000 | 128  
n2-highmem-16 | 4000 | 384 | 50000 | 256  
n2-highmem-32 | 8000 | 768 | 100000 | 512  
n2-highmem-64 | 16000 | 1536 | 200000 | 1024  
  4. Create a `pgbench` database.
         
         source ./pgbench-setup.env
         psql -h $PGHOST -p 5432
         postgres=> create database pgbench;
         CREATE DATABASE
         

  5. Initialize and load the pgbench database by running the following commands. This step ensures that the benchmarking dataset is created and populated with realistic data, which lets you accurately simulate a TPC-B workload on the pgbench database.
         
         source ./pgbench-setup.env
         sudo nohup pgbench -i --host=$PGHOST --scale=$SCALE_FACTOR pgbench > /tmp/pgbench-tpcb-partially-cached-db-init.out 2>&1
         

**Expected load times:**

     * The partially-cached database takes approximately 6 hours to load.
     * The fully-cached database takes approximately 45 minutes to load.
  6. Optional: Perform a load accuracy check by ensuring that the contents of the `/tmp/pgbench-tpcb-partially-cached-db-init.out` file are similar to the following:
         
         generating data (client-side)...
         100000 of 400000000 tuples (0%) done (elapsed 0.02 s, remaining 99.82 s)
         .. .. ..
         .. .. ..
         399800000 of 400000000 tuples (99%) done (elapsed 534.60 s, remaining 0.27 s)
         399900000 of 400000000 tuples (99%) done (elapsed 534.72 s, remaining 0.13 s)
         400000000 of 400000000 tuples (100%) done (elapsed 534.85 s, remaining 0.00 s)
         vacuuming...
         creating primary keys...
         done in 1481.92 s (drop tables 0.01 s, create tables 0.04 s, client-side generate 540.93 s, vacuum 615.11 s, primary keys 325.84 s).
         

  7. Optional: To further validate the accuracy of your load, run the following PostgreSQL command that measures the size of all pgbench tables:

     1. Connect to the pgbench database:
            
            source ./pgbench-setup.env
            psql -h $PGHOST -p 5432 -U postgres -d pgbench
            

     2. Run the following SQL command:
            
            pgbench=> SELECT nspname AS schema_name, relname AS table_name, pg_size_pretty(pg_total_relation_size(C.oid)) AS size FROM pg_class C
            LEFT JOIN pg_namespace N ON (N.oid = C.relnamespace)
            WHERE nspname NOT LIKE 'pg_%' AND nspname != 'information_schema'
            ORDER BY pg_total_relation_size(C.oid) DESC;
            

     3. Compare the output of the previous command with the output that you obtained for the partially-cached database run (`SCALE_FACTOR=50000`).
            
            schema_name |                table_name                 |  size
             -------------+-------------------------------------------+---------
             public      | pgbench_accounts                          | 731 GB
             public      | pgbench_accounts_pkey                     | 105 GB
             public      | pgbench_tellers                           | 32 MB
             public      | pgbench_tellers_pkey                      | 11 MB
             public      | pgbench_branches                          | 2952 kB
             public      | pgbench_branches_pkey                     | 1112 kB
             .. .. ..
             public      | pgbench_history                           | 0 bytes
             .. .. ..
             (29 rows)
            

  8. Run the following commands to simulate a financial accounting system workload by executing a series of transactions involving deposits, transfers and payments, which lets you measure database performance under a heavy workload.
         
         source ./pgbench-setup.env
         mkdir -p ~/results/alloydb/pgbench
         sudo nohup pgbench --host=$PGHOST --builtin=tpcb-like --time=3900 --jobs=$NUM_CLIENTS --client=$NUM_CLIENTS --scale=$SCALE_FACTOR --protocol=prepared --progress=1 pgbench > ~/results/alloydb/pgbench/pgbench.run.out 2>&1
         




### Analyze the benchmark results

Check the output of the previous command in the `~/results/alloydb/pgbench/pgbench.run.out` file. The TPS number should be close to the numbers show in the fully-cached database and in the partially-cached database scenarios.

#### Results with a fully cached database

The output of the last command in Run the pgbench TPC-B benchmark should be similar to the following, where `--scale=4000`:
    
    
    transaction type: <builtin: TPC-B (sort of)>
    scaling factor: 4000
    query mode: prepared
    number of clients: 384
    number of threads: 384
    duration: 3900 s
    number of transactions actually processed: 84819501
    latency average = 17.654 ms
    latency stddev = 6.963 ms
    tps = 21747.831164 (including connections establishing)
    tps = 21750.579718 (excluding connections establishing)
    

To further understand the behavior of the database system, you can monitor system metrics like CPU usage, memory usage, and transactions per second by using the Google Cloud console. For more information, see [Monitor instances](https://docs.cloud.google.com/alloydb/docs/monitor-instance).

#### Results with a partially cached database

The output of the last command in Run the pgbench TPC-B benchmark should be similar to the following, where `--scale=50000`:
    
    
    pgbench: warning: scale option ignored, using count from pgbench_branches table (50000)
    starting vacuum...end.
    transaction type: <builtin: TPC-B (sort of)>
    
    scaling factor: 50000
    query mode: prepared
    number of clients: 384
    number of threads: 384
    duration: 3900 s
    number of transactions actually processed: 68073405
    latency average = 21.992 ms
    latency stddev = 29.272 ms
    tps = 17453.913041 (including connections establishing)
    tps = 17460.373303 (excluding connections establishing)
    

### Summary of performance results for a pgbench TPC-B benchmark

The following table summarizes performance results for a pgbench TPC-B benchmark:

**TPC-B Scenario** | **SCALE_FACTOR** | **TPS** | **CPU Utilization (%)**  
---|---|---|---  
Partially cached | 50000 | 17,460 | 96%  
Fully Cached | 4000 | 21,750 | 94%  
  
## Run an Index Insert Only benchmark

The Index Insert Only benchmark is a highly concurrent, write-intensive scenario that is customized in this section to show the performance benefits of AlloyDB for the majority of OLTP applications. To run this benchmark, you create multiple indexes on the `pgbench_history` table and then repeatedly perform INSERT operations on the `pgbench_history` table from multiple client connections.

Index Only Insert benchmarks measure the performance of inserting data into a database table specifically focusing on the impact of indexes on the write operation. This benchmark let you understand how quickly new rows can be added to a table with and without indexes, highlighting the potential slowdown caused by index maintenance during inserts.

AlloyDB enhances PostgreSQL write performance, which also improves OLTP workloads. To improve the performance of write-intensive OLTP scenarios, AlloyDB offers architectural innovations including tiered cache layer to help with reads, and a distributed and highly scalable storage engine technology for writes.

### Set up AlloyDB and the client machine

To set up the infrastructure to run an Index Only Insert benchmark, follow these steps:

  1. Create an AlloyDB cluster and instance, substituting `16 vCPU and 128 GB RAM` as the machine type.

  2. Provision the client machine, substituting `E2-standard-16 (minimum)` as the machine type.

  3. Set up the benchmark driver machine.

  4. Perform a benchmark cleanup.




### Run the Index Insert Only benchmark

  1. Connect to the client machine using the following example command:
         
         gcloud compute ssh --zone "<primary zone>" "<client machine name>" --project "<google-project>"

  2. Set up the environment by running the following command:
         
         export PGHOST=<private_ip>
         

**Important:** Run all the remaining commands in this procedure from the same client terminal. Then all you need to do in export the `PGHOST` environment variable one time and assign it to the private IP of your AlloyDB instance. If you connect multiple terminals to the client machine, then export the following environment variable on all the terminals.
  3. Create a `pgbench` database using the following the example. If the database already exists, then drop the database and recreate it.
         
         psql -h $PGHOST -p 5432 -U postgres -c "DROP DATABASE IF EXISTS pgbench"
         psql -h $PGHOST -p 5432 -U postgres -c "CREATE DATABASE pgbench"
         

  4. Initialize and load the pgbench database to ensure that the benchmarking dataset is created and populated with realistic data. Edit the highlighted parameters and then run the following command:
         
         sudo nohup pgbench -i  --host=$PGHOST --user=postgres --scale=25000 pgbench > /tmp/pgbench-index-insert-only-init.out 2>&1
         ...
         
         postgres=> create database pgbench;
         CREATE DATABASE pgbench
         

  5. Verify that the output of the previous command is similar to the following:
         
         dropping old tables...
         creating tables...
         generating data (client-side)...
         100000 of 2500000000 tuples (0%) done (elapsed 0.03 s, remaining 636.43 s)
         200000 of 2500000000 tuples (0%) done (elapsed 0.05 s, remaining 649.12 s)
         .. .. ..
         .. .. ..
         2499900000 of 2500000000 tuples (99%) done (elapsed 3425.42 s, remaining 0.14 s)
         2500000000 of 2500000000 tuples (100%) done (elapsed 3425.57 s, remaining 0.00 s)
         vacuuming...
         creating primary keys...
         done in 12851.19 s (drop tables 998.62 s, create tables 0.02 s, client-side generate 3460.33 s, vacuum 5299.93 s, primary keys 3092.29 s).
         

  6. Create the `index-init.sql` script using the following commands:
         
         cat > index-init.sql << EOF
         CREATE INDEX tid ON pgbench_history(tid);
         CREATE INDEX bid ON pgbench_history(bid);
         CREATE INDEX aid ON pgbench_history(aid);
         CREATE INDEX delta ON pgbench_history(delta);
         CREATE INDEX mtime ON pgbench_history(mtime);
         EOF

  7. Execute the `index-init.sql` script:
         
         psql -h $PGHOST -U postgres -d pgbench -f ./index-init.sql
         Password for user postgres:
         CREATE INDEX
         

  8. Optional: Validate the database schema and initial load:
         
         psql -h $PGHOST -U postgres -d pgbench
         
         pgbench=> \dt
                    List of relations
         Schema |       Name       | Type  |  Owner
         --------+------------------+-------+----------
          public | pgbench_accounts | table | postgres
          public | pgbench_branches | table | postgres
          public | pgbench_history  | table | postgres
          public | pgbench_tellers  | table | postgres
         (4 rows)
         
         pgbench=> \di
                                List of relations
          Schema |         Name          | Type  |  Owner   |      Table
         --------+-----------------------+-------+----------+------------------
          public | aid                   | index | postgres | pgbench_history
          public | bid                   | index | postgres | pgbench_history
          public | delta                 | index | postgres | pgbench_history
          public | mtime                 | index | postgres | pgbench_history
          public | pgbench_accounts_pkey | index | postgres | pgbench_accounts
          public | pgbench_branches_pkey | index | postgres | pgbench_branches
          public | pgbench_tellers_pkey  | index | postgres | pgbench_tellers
          public | tid                   | index | postgres | pgbench_history
         (8 rows)
         

After the load, The database size is expected to be around 365 GB:
         
         pgbench=> \l+ pgbench
                                  List of databases
         Name     |      Owner       | Encoding | Collate |  Ctype  |           Access privileges           |  Size  | Tablespace |                Description
          --------------+------------------+----------+---------+---------+---------------------------------------+--------+------------+--------------------------------------------
         ...
          pgbench      | postgres         | UTF8     | C.UTF-8 | C.UTF-8 |                                       | 365 GB | pg_default |
         ...
         

  9. Create the `index-inserts-only.sql` script using the following commands:
         
         cat > index-inserts-only.sql << EOF
         \set aid random(1, 1000000000)
         \set bid random(1, 1000000000)
         \set tid random(1, 1000000000)
         \set delta random(-500000000, 500000000)
         BEGIN;
         INSERT INTO pgbench_history (tid, bid, aid, delta, mtime) VALUES (:tid, :bid, :aid, :delta, CURRENT_TIMESTAMP);
         END;
         EOF

  10. Run the pgbench benchmark using following command:
         
         sudo nohup pgbench --host=$PGHOST --user=postgres --time=3900 --client=256 --jobs=256 --scale=25000 --progress=1 --file=./index-inserts-only.sql pgbench > /tmp/pgbench-index-insert-only-run.out 2>&1




### Analyze the benchmark results

Verify the output of the previous command in the `/tmp/pgbench-index-insert-only-run.out` file. You should see approximately 52K transactions per second and a CPU utilization rate of ~88% during this benchmark test, as shown in the following example output.
    
    
    scaling factor: 25000
    query mode: simple
    number of clients: 256
    number of threads: 256
    duration: 3900 s
    number of transactions actually processed: 201785196
    latency average = 4.947 ms
    latency stddev = 3.488 ms
    tps = 51738.604613 (including connections establishing)
    tps = 51742.459757 (excluding connections establishing)
    

## Run a Select Only benchmark on a 64 vCPU Instance

pgbench supports a built-in, select-only scenario that repeatedly executes SELECT queries from multiple client connections against a specified database. This benchmark is used to measure the read performance of the database, without introducing the overhead of data modification operations like INSERT, UPDATE, or DELETE. These SELECT queries are point lookup queries that are the fastest and most efficient type of select queries because they involve accessing only a single row of data directly from the index structures.

Running a Select Only benchmark helps you achieve the following:

  * Achieving maximum throughput: Because point lookups on an index are the most efficient form of queries in a database system, you can measure maximum possible throughput that AlloyDB can achieve.

  * Scalability: Select only benchmarks help you test the scalability of AlloyDB from 2 vCPU to the maximum vCPU configuration offered by AlloyDB.




### Set up AlloyDB and the client machine

Set up AlloyDB and the client machine on a 64 vCPU machine type.

### Run the Select Only benchmark

  1. Connect to the client machine using the following example command:
         
         gcloud compute ssh --zone "PRIMARY_ZONE" "CLIENT_MACHINE_NAME" --project "GOOGLE_PROJECT"

  2. Set up the environment using the following command:
         
         export PGHOST=<private_ip>
         

**Important:** Run all the remaining commands in this procedure from the same client terminal. Then all you need to do in export the `PGHOST` environment variable one time and assign it to the private IP of your AlloyDB instance. If you connect multiple terminals to the client machine, then export the following environment variable on all the terminals.
  3. Create the pgbench database using the following the example:
         
         psql -h $PGHOST -p 5432 -U postgres
         
         postgres=> create database pgbench;
         CREATE DATABASE
         

  4. Initialize the pgbench database. The following command initializes the pgbench database with approximately 220 GB of realistic data. You use `--scale=15000` for the fully cached Select Only benchmark.

Run the following command:
         
         sudo nohup pgbench -i --host=$PGHOST --user=postgres --scale=15000 pgbench > /tmp/pgbench-select-only-init.out 2>&1

  5. Verify that the output of previous command is similar to the following:
         
         cat /tmp/pgbench-select-only-init.out
         nohup: ignoring input
         dropping old tables...
         creating tables...
         generating data (client-side)...
         100000 of 1500000000 tuples (0%) done (elapsed 0.01 s, remaining 161.60 s)
         200000 of 1500000000 tuples (0%) done (elapsed 0.03 s, remaining 224.35 s)
         300000 of 1500000000 tuples (0%) done (elapsed 0.09 s, remaining 448.97 s)
         .. .. ..
         .. .. ..
         1499900000 of 1500000000 tuples (99%) done (elapsed 1251.03 s, remaining 0.08 s)
         1500000000 of 1500000000 tuples (100%) done (elapsed 1251.10 s, remaining 0.00 s)
         vacuuming...
         creating primary keys...
         done in 2204.62 s (drop tables 2.29 s, create tables 0.01 s, client-side generate 1271.82 s, vacuum 427.83 s, primary keys 502.66 s).
         

  6. Run pgbench. This final benchmarking step takes over one hour to complete.
         
         sudo nohup pgbench --host=$PGHOST --user=postgres  --builtin=select-only --time=3900 --jobs=256 --client=256 --scale=15000 --protocol=simple --progress=1 pgbench > /tmp/pgbench-select-only-run.out  2>&1

  7. After the benchmark completes, check the `/tmp/pgbench-select-only-run.out` file for the final results.




### Analyze the benchmark results

You should observe observed approximately 467k transactions per second and a CPU utilization rate of ~95% during this benchmark test, as shown in the following example output.
    
    
    cat /tmp/pgbench-select-only-run.out
    transaction type: <builtin: select only>
    scaling factor: 15000
    query mode: simple
    number of clients: 256
    number of threads: 256
    duration: 3900 s
    number of transactions actually processed: 1823506174
    latency average = 0.547 ms
    latency stddev = 0.267 ms
    tps = 467563.144333 (including connections establishing)
    tps = 467583.398400 (excluding connections establishing)
    

## AlloyDB benchmark results summary

The following tables summarize the AlloyDB benchmark results based on the testing performed in this document.

### HammerDB TPC-C performance summary

**AlloyDB Machine Type** | **TPC-C Workload Scenario** | **NUM_WAREHOUSE** | **NUM_USERS** | **New Orders Per Minute (NOPM)** | **Cumulative TPM** | **Converted to TPS**  
---|---|---|---|---|---|---  
16vCPU | 30% cached | 3200 | 256 | 252,970 | 582,385 | 9,706  
16vCPU | 100% cached | 576 | 256 | 428,316 | 974,264 | 16,238  
64vCPU | 30% cached | 12800 | 1024 | 589,598 | 1,371,160 | 22,853  
64vCPU | 100% cached | 2304 | 1024 | 716,138 | 1,665,438 | 27,757  
  
### pgbench performance summary

**AlloyDB Machine Type** | **pgbench Workload Scenario** | **Scale Factor** | **TPS** | **CPU %**  
---|---|---|---|---  
16vCPU | TPC-B Like, Fully Cached | 4000 | 20,359 | 96%  
16vCPU | TPC-B Like, Partially Cached | 50000 | 14,060 | 94%  
16vCPU | Index inserts only | 25000 | 51,742 | 88%  
64vCPU | Max. Throughput (Select Only) | 15000 | 467,583 | 95%  
  
## Run OLTP benchmarking on Cloud SQL for PostgreSQL

You can test equivalent OLTP performance on PostgreSQL in Cloud SQL for PostgreSQL on a 16 vCPU machine type for comparative analysis. This section describes how to set up a Cloud SQL for PostgreSQL (or any PostgreSQL server deployed on the infrastructure of your choice) that is comparable to the AlloyDB setup that is used in this guide to benchmark OLTP performance. In this scenario includes choosing 16vCPU SKU, enabling high availability (HA), and pre-configuring with storage.

### Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the AlloyDB, Compute Engine, and Resource Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=alloydb.googleapis.com,compute.googleapis.com,cloudresourcemanager.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the AlloyDB, Compute Engine, and Resource Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=alloydb.googleapis.com,compute.googleapis.com,cloudresourcemanager.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Make sure you have the Cloud SQL Admin and Compute Viewer roles on your user account. 

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

[Learn more](https://docs.cloud.google.com/sql/docs/postgres/roles-and-permissions) about roles and permissions. 




### Provision a Cloud SQL for PostgreSQL instance

  1. [Create a PostgreSQL instance](https://docs.cloud.google.com/sql/docs/postgres/create-instance#create-2nd-gen), substituting the following values:

     * Database version: PostgreSQL 14
     * Choose a configuration to start with: Production
     * Choose region and zonal availability: Select `us-central1` as the region.
     * Zonal availability: Multiple zones (Highly Available) 
       * Primary zone: `us-central1-c`
       * Secondary zone: `us-central-1-f`
     * Machine type: High Memory 16 vCPU, 104 GB machine. This is the closest machine that Cloud SQL for PostgreSQL offers to the matching AlloyDB instance that you created in the AlloyDB benchmarking section of this document.
     * Storage capacity: Custom, 1500 GB 
       * Enable automatic storage increases
     * Encryption: Google-owned and Google-managed encryption key
     * Connections: Private IP 
       * Network: `default`
       * Public IP: Enabled
  2. Click **Create instance**.

  3. After the PostgreSQL instance is created, make a note of the Private IP address. You use the IP as `PGHOST` to establish connections with the benchmark.




### Provision the client machine

  1. Provision a Cloud SQL for PostgreSQL instance. To run the OLTP benchmark of your choice, you need a client machine with significant CPU power in the same zone as the primary Cloud SQL for PostgreSQL instance in Cloud SQL.

  2. Optional: As an alternative to the previous step, you can use the same client machine that you set up for AlloyDB benchmarking, provided that the following is true:

     * The client machine is located in the same zone as the new PostgreSQL (Cloud SQL for PostgreSQL) primary instance.
     * The client machine meets the minimum CPU, RAM, and disk size requirements.

In this benchmarking guide, you reused the client machines when they were collocated in the same zone as the primary instance, and when they were large enough to bring the server to its full capacity.

  3. If you created a new client machine, set up the benchmark driver machine. Otherwise, follow the instructions in this guide for the benchmark that you're interested in running.




## What's next

  * [Monitor AlloyDB instance performance](https://docs.cloud.google.com/alloydb/docs/monitor-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
