---
url: https://docs.cloud.google.com/alloydb/docs/use-pgbench/
title: Analyze the performance of an AlloyDB instance with pgbench \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:24.211523+00:00
---

# Analyze the performance of an AlloyDB instance with pgbench  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/use-pgbench/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Analyze the performance of an AlloyDB instance with pgbench Stay organized with collections  Save and categorize content based on your preferences. 

To evaluate baseline database throughput and latency, you can connect an AlloyDB for PostgreSQL instance and a [Compute Engine](https://cloud.google.com/compute) VM instance on a [Virtual Private Cloud (VPC)](https://cloud.google.com/vpc) network, install `pgbench` on the Compute Engine VM, and run performance benchmarks against your AlloyDB instance.

**Note:** While you can use `pgbench` to run basic performance tests with AlloyDB, for Online Transaction Processing (OLTP) benchmarking, see the tools and methodology described in the [AlloyDB Transactional (OLTP) Benchmarking Guide](https://services.google.com/fh/files/misc/alloydb_oltp_benchmarking_guide.pdf).

### Objectives

In this tutorial, you learn how to:

  * Create a VPC network for your AlloyDB instance and your Compute Engine VM instance so that communication can pass between the instance and the VM securely.
  * Create an AlloyDB instance and a Compute Engine VM instance, and assign and configure your VPC network for both instances.
  * Install `pgbench` on the Compute Engine VM instance, run it against the AlloyDB instance, and use it to conduct performance tests against the AlloyDB instance.



### Costs

This tutorial uses billable components of Google Cloud, including VPC network, AlloyDB, and Compute Engine. Use the [pricing calculator](https://cloud.google.com/products/calculator) to generate a cost estimate based on your projected usage.

### Before you begin

  1. In the Google Cloud Console, on the project selector page, select or create a Google Cloud project.

**Note:** If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to the project selector page](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Make sure that billing is enabled for your Google Cloud project. [Learn how to confirm that billing is enabled for your project.](https://docs.cloud.google.com/billing/docs/how-to/modify-project)

  3. Enable the VPC network, AlloyDB, and Compute Engine APIs.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute,servicenetworking.googleapis.com)

  4. Make sure that you have the AlloyDB Admin role assigned to your user account.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam?apiid=compute,servicenetworking.googleapis.com)




## Create a VPC network

In this section, you create a VPC network for your AlloyDB instance and your Compute Engine VM instance so that communication can pass between the instance and the VM securely.

  1. Go to the **VPC networks** page in the Google Cloud Console.

[Go to the VPC networks page](https://console.cloud.google.com/networking/networks)

  2. Click **Create VPC network**. The **Create a VPC network** page appears.

  3. Enter `my-vpc-network` for the **Name** of your VPC network.

  4. In the **Subnet creation mode** section, select the **Custom** option.

  5. Click **ADD SUBNET**.

  6. Enter `my-subnet` for the **Name** of your subnet.

  7. Select a **Region** and enter an **IP address range** for your subnet.

  8. Click **DONE**.

  9. Click **CREATE**.


**Note:** It may take a few seconds for your VPC network to be created. Also, to learn more about VPC networks, see [VPC network overview](https://docs.cloud.google.com/vpc/docs/vpc).

## Create an AlloyDB instance

In this section, you create an AlloyDB instance, and assign and configure your VPC network for the instance.

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click **Create cluster**.

  3. Configure your cluster as follows:

     1. In the **Cluster ID** field of the **Basic info** section, enter `my-cluster`.

     2. In the **Password** field, enter any password you'd like. Take note of this password—you use it again later in this tutorial.

     3. In the **Region** field of the **Location** section, select `us-central1 (Iowa)`.

     4. In the **Database version** field, keep the default value.

     5. From the **Network** menu, select **my-vpc-network**. You created this VPC network in Create a VPC network.

     6. Because your VPC network hasn't yet initialized private service access, click **Set up connection**.

**Note:** A private service connection enables your AlloyDB instance and the Compute Engine VM that you'll be creating to communicate exclusively by using internal IP addresses.
     7. In the **Create a private service connection** pane that appears:

        1. Select the **Use an automatically allocated IP range** option to have Google Cloud select an automatically allocated IP range in your network.

        2. Click **Continue**.

        3. Click **Create connection**.

**Note:** It might take a few seconds for your private service connection to be created. After this happens, the **Create a private service connection** pane disappears, and the **Private service connection for network[VPC-network-name] is successfully created.** status message appears.
  4. Configure your primary instance as follows:

     1. In the **Instance ID** field, enter an ID for your primary instance.

     2. Under **Zonal availability** , select one of the following options:

        1. To create a highly available production instance with automated failover, select **Multiple zones (Highly available)**.

        2. To create a basic instance that does not need to be highly available, select **Single zone**.

     3. Select a machine type.

  5. Click **Create cluster** to create the cluster and the primary instance together.

**Note:** It may take a few minutes for your AlloyDB instance to be created.
  6. Make a note of the private IP address of your AlloyDB instance that appears on the **AlloyDB Instances** page. You'll need this address to verify the integration between the AlloyDB instance and the Compute Engine VM instance.




## Create a Compute Engine VM instance

In this section, you create a Compute Engine VM instance, and assign and configure your VPC network for the instance.

  1. Go to the **VM instances** page in the Google Cloud Console.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. In the **Name** field of the **Create an instance** page, enter a unique identifier for the Compute Engine VM instance that you're creating. For this tutorial, enter `my-compute-engine-vm-instance` in the field.

  4. In the **Access scopes** section of the page, select the **Allow full access to all Cloud APIs** option.

  5. Expand **Advanced options** , and then complete the following steps:

     1. Click the **Networking** subtab.

     2. Click **Add a network interface**.

     3. From the **Network** menu, select **my-vpc-network**. You created this VPC network in Create a VPC network.

     4. Click **Done**. Two VPC networks appear in the **Network interfaces** section of the page: **default** and **my-vpc-network**

  6. Click _delete_ **Delete** to delete the **default** VPC network.

By deleting the **default** VPC network, you force your Compute Engine VM instance to use the VPC network that you created in this tutorial.

  7. Click **Create**.

It may take a few seconds for your Compute Engine VM instance to be created. After this happens, the instance appears in the **VM instances** page, and the status of this instance is **Running** (as indicated by the check mark).




## Verify the integration

In this section, you install `pgbench` on the Compute Engine VM instance, run it against the AlloyDB instance, and use it to conduct performance tests against the AlloyDB instance.

  1. Connect to your Compute Engine VM instance. To do so, click the **SSH** menu to the right of your VM instance, and then select **Open in browser window**.

  2. Install the Contributed Extensions and Additions to PostgreSQL package on your Compute Engine VM instance.
         
         sudo apt-get -y install postgresql-contrib

  3. Initialize a database for `pgbench` on your AlloyDB for PostgreSQL instance. For example, use the default `postgres` database:
         
         pgbench -i --host=INSTANCE_PRIVATE_IP --port=PORT_NUMBER --username=USERNAME

Replace the following:

     * `INSTANCE_PRIVATE_IP`: The private IP address of your AlloyDB instance. You made a note of this IP address when you created the instance.
     * `PORT_NUMBER`: The port number reserved for your AlloyDB instance. For this tutorial, the port number is `5432`.
     * `USERNAME`: The administrator username for your AlloyDB instance. For this tutorial, the username is `postgres`.
  4. At the `Password` prompt, enter the password for your AlloyDB instance. When you created the instance, you either supplied a password for it or had AlloyDB generate a password for you.

  5. Run `pgbench` with no arguments to verify basic features.
         
         pgbench --host=INSTANCE_PRIVATE_IP --port=PORT_NUMBER --username=USERNAME

  6. At the `Password` prompt, enter the password for your AlloyDB instance.

You should see output similar to the following:
         
         starting vacuum...end.
         transaction type: <builtin: TPC-B (sort of)>
         scaling factor: 1
         query mode: simple
         number of clients: 1
         number of threads: 1
         number of transactions per client: 10
         number of transactions actually processed: 10/10
         latency average = 3.794 ms
         tps = 263.560171 (including connections establishing)
         tps = 345.375423 (excluding connections establishing)

  7. Use some options to make a useful test. Some important options are `-c` (the number of clients) and `--transactions` (the number of transactions per client).

For this tutorial, conduct a performance test against `10` clients that are accessing your AlloyDB for PostgreSQL database and `100` transactions for each client.
         
         pgbench --host=INSTANCE_PRIVATE_IP --port=PORT_NUMBER --username=USERNAME -c 10 --transactions=100

  8. At the `Password` prompt, enter the password for your AlloyDB instance.

You should see output similar to the following:
         
         starting vacuum...end.
         transaction type: TPC-B (sort of)>
         scaling factor: 1
         query mode: simple
         number of clients: 10
         number of threads: 1
         number of transactions per client: 100
         number of transactions actually processed: 1000/1000
         latency average = 36.421 ms
         tps = 274.563444 (including connections establishing)
         tps = 275.733225 (excluding connections establishing)




## Clean up

After you've finished this tutorial, you can clean up the resources that you created so they won't take up quota and you won't be billed for them in the future.

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, follow these steps.

  1. Use the Google Cloud console to delete your project, AlloyDB instance, Compute Engine VM instance, and VPC network.



The following sections describe how to delete or turn off these resources.

### Delete your project

The easiest way to eliminate billing is to delete the project that you created for this tutorial.

Deleting a project has the following effects:

  * **Everything in the project is deleted.** If you used an existing project for this tutorial, then when you delete it, you also delete any other work you've done in the project.
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `**appspot.com**` URL, delete selected resources inside the project instead of deleting the whole project.



If you plan to explore multiple tutorials and quickstarts, then reusing projects can help you avoid exceeding project quota limits.

  1. Go to the **Manage resources** page in the Google Cloud Console.

[Go to the Manage resources page](https://console.cloud.google.com/cloud-resource-manager)

  2. In the project list, select the project that you want to delete, and then click **Delete**.

  3. In the dialog, type the project ID, and then click **Shut down** to delete the project.




### Delete the AlloyDB instance

  1. Go to the **AlloyDB Clusters** page in the Google Cloud Console.

[Go to the AlloyDB Clusters page](https://console.cloud.google.com/alloydb/clusters)

  2. Click the name of your AlloyDB instance. For this tutorial, click **my-instance**.

  3. Click **DELETE**.

  4. In the dialog, enter the name of your AlloyDB instance in the text field, and then click **DELETE**.




### Delete the Compute Engine VM instance

  1. Go to the **VM instances** page in the Google Cloud Console.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click the name of your Compute Engine VM instance. For this tutorial, click **my-compute-engine-vm-instance**.

  3. Click the **Delete** icon. This icon resembles a trashcan.

  4. In the dialog, click **DELETE**.

**Note:** It may take a few seconds for your Compute Engine VM instance to be deleted.



### Delete the VPC network

  1. Go to the **VPC networks** page in the Google Cloud Console.

[Go to the VPC networks page](https://console.cloud.google.com/networking/networks)

  2. Click the name of your VPC network. For this tutorial, click **my-vpc-network**.

  3. Click **DELETE VPC NETWORK**.

  4. In the dialog, click **DELETE**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
