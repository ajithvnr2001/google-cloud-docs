---
url: https://docs.cloud.google.com/managed-spark/docs/tutorials/spark-hbase/
title: Use Apache Spark with HBase on Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:30.226741+00:00
---

# Use Apache Spark with HBase on Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/tutorials/spark-hbase/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Use Apache Spark with HBase on Managed Service for Apache Spark Stay organized with collections  Save and categorize content based on your preferences. 

**Deprecated:** Starting with Managed Service for Apache Spark [version 2.1](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.1), you can no longer use the optional HBase component. Managed Service for Apache Spark [version 1.5](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.5) and Managed Service for Apache Spark [version 2.0](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.0) offer a Beta version of HBase with no support. However, due to the ephemeral nature of Managed Service for Apache Spark clusters, using HBase is not recommended. 

## Objectives

This tutorial shows you how to:

  1. Create a Managed Service for Apache Spark cluster, installing Apache HBase and Apache ZooKeeper on the cluster
  2. Create an HBase table using the HBase shell running on the master node of the Managed Service for Apache Spark cluster
  3. Use Cloud Shell to submit a Java or PySpark Spark job to the Managed Service for Apache Spark that writes data to, then reads data from, the HBase table



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/pricing)
  * [Compute Engine](https://docs.cloud.google.com/compute/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

If you haven't already done so, create a Google Cloud Platform project.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Dataproc and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc,compute_component&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Dataproc and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc,compute_component&redirect=https%3A//console.cloud.google.com)




## Create a Managed Service for Apache Spark cluster

  1. Run the following command in a [Cloud Shell](https://docs.cloud.google.com/shell/docs) session terminal to:

     * Install the [HBase](https://docs.cloud.google.com/managed-spark/docs/concepts/components/hbase) and [ZooKeeper](https://docs.cloud.google.com/managed-spark/docs/concepts/components/zookeeper) components
     * Provision three worker nodes (three to five workers are recommended to run the code in this tutorial)
     * Enable the [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways)
     * Use image version 2.0
     * Use the `--properties` flag to add the HBase config and HBase library to the Spark driver and executor classpaths.


    
    
    gcloud dataproc clusters create cluster-name \
        --region=region \
        --optional-components=HBASE,ZOOKEEPER \
        --num-workers=3 \
        --enable-component-gateway \
        --image-version=2.0 \
        --properties='spark:spark.driver.extraClassPath=/etc/hbase/conf:/usr/lib/hbase/*,spark:spark.executor.extraClassPath=/etc/hbase/conf:/usr/lib/hbase/*'
    

### Verify connector installation

  1. From the Google Cloud console or a Cloud Shell session terminal, [SSH into the Managed Service for Apache Spark cluster master node](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh).

  2. Verify the installation of the [Apache HBase Spark connector](https://github.com/apache/hbase-connectors/tree/master/spark) on the master node: 
         
         ls -l /usr/lib/spark/jars | grep hbase-spark
         

Sample output: 
         
         -rw-r--r-- 1 root root size date time hbase-spark-connector.version.jar
         

  3. Keep the SSH session terminal open to:

     1. Create an HBase table
     2. (Java users): run commands on the master node of the cluster to determine the versions of components installed on the cluster
     3. Scan your Hbase table after you run the code



## Create an HBase table

Run the commands listed in this section in the master node SSH session terminal that you opened in the previous step.

  1. Open the HBase shell: 
         
         hbase shell
         

  2. Create an HBase 'my-table' with a 'cf' column family: 
         
         create 'my_table','cf'
         

     1. To confirm table creation, in the Google Cloud console, click **HBase** in the [Google Cloud console Component Gateway links](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways#viewing_and_accessing_component_gateway_urls) to open the Apache HBase UI. `my-table` is listed in the **Tables** section on the **Home** page. ![](https://docs.cloud.google.com/static/managed-spark/images/my-table.png)



## View the Spark code

### Java
    
    
    package hbase;
    
    import org.apache.hadoop.hbase.spark.datasources.HBaseTableCatalog;
    import org.apache.spark.sql.Dataset;
    import org.apache.spark.sql.Row;
    import org.apache.spark.sql.SparkSession;
    
    import java.io.Serializable;
    import java.util.Arrays;
    import java.util.HashMap;
    import java.util.Map;
    
    public class SparkHBaseMain {
        public static class SampleData implements Serializable {
            private String key;
            private String name;
    
    
            public SampleData(String key, String name) {
                this.key = key;
                this.name = name;
            }
    
            public SampleData() {
            }
    
            public String getName() {
                return name;
            }
    
            public void setName(String name) {
                this.name = name;
            }
    
            public String getKey() {
                return key;
            }
    
            public void setKey(String key) {
                this.key = key;
            }
        }
        public static void main(String[] args) {
            // Init SparkSession
            SparkSession spark = SparkSession
                    .builder()
                    .master("yarn")
                    .appName("spark-hbase-tutorial")
                    .getOrCreate();
    
            // Data Schema
            String catalog = "{"+"\"table\":{\"namespace\":\"default\", \"name\":\"my_table\"}," +
                    "\"rowkey\":\"key\"," +
                    "\"columns\":{" +
                    "\"key\":{\"cf\":\"rowkey\", \"col\":\"key\", \"type\":\"string\"}," +
                    "\"name\":{\"cf\":\"cf\", \"col\":\"name\", \"type\":\"string\"}" +
                    "}" +
                    "}";
    
            Map<String, String> optionsMap = new HashMap<String, String>();
            optionsMap.put(HBaseTableCatalog.tableCatalog(), catalog);
    
            Dataset<Row> ds= spark.createDataFrame(Arrays.asList(
                    new SampleData("key1", "foo"),
                    new SampleData("key2", "bar")), SampleData.class);
    
            // Write to HBase
            ds.write()
                    .format("org.apache.hadoop.hbase.spark")
                    .options(optionsMap)
                    .option("hbase.spark.use.hbasecontext", "false")
                    .mode("overwrite")
                    .save();
    
            // Read from HBase
            Dataset dataset = spark.read()
                    .format("org.apache.hadoop.hbase.spark")
                    .options(optionsMap)
                    .option("hbase.spark.use.hbasecontext", "false")
                    .load();
            dataset.show();
        }
    }
    

### Python
    
    
    from pyspark.sql import SparkSession
    
    # Initialize Spark Session
    spark = SparkSession \
      .builder \
      .master('yarn') \
      .appName('spark-hbase-tutorial') \
      .getOrCreate()
    
    data_source_format = ''
    
    # Create some test data
    df = spark.createDataFrame(
        [
            ("key1", "foo"),
            ("key2", "bar"),
        ],
        ["key", "name"]
    )
    
    # Define the schema for catalog
    catalog = ''.join("""{
        "table":{"namespace":"default", "name":"my_table"},
        "rowkey":"key",
        "columns":{
            "key":{"cf":"rowkey", "col":"key", "type":"string"},
            "name":{"cf":"cf", "col":"name", "type":"string"}
        }
    }""".split())
    
    # Write to HBase
    df.write.format('org.apache.hadoop.hbase.spark').options(catalog=catalog).option("hbase.spark.use.hbasecontext", "false").mode("overwrite").save()
    
    # Read from HBase
    result = spark.read.format('org.apache.hadoop.hbase.spark').options(catalog=catalog).option("hbase.spark.use.hbasecontext", "false").load()
    result.show()

## Run the code

  1. Open a [Cloud Shell](https://console.cloud.google.com/?cloudshell=true) session terminal.

**Note:** Run the commands listed in this section in a Cloud Shell session terminal. Cloud Shell has the tools required by this tutorial pre-installed, including [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), [git](https://git-scm.com/), [Apache Maven](https://maven.apache.org/download.cgi), [Java](https://www.java.com/en/), and [Python](https://www.python.org/), plus [other tools](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works#tools).
  2. Clone the GitHub [GoogleCloudDataproc/cloud-dataproc](https://github.com/GoogleCloudDataproc/cloud-dataproc) repository into your Cloud Shell session terminal: 
         
         git clone https://github.com/GoogleCloudDataproc/cloud-dataproc.git
         

  3. Change to the `cloud-managed-spark/spark-hbase` directory: 
         
         cd cloud-managed-spark/spark-hbase
         

Sample output: 
         
         user-name@cloudshell:~/cloud-managed-spark/spark-hbase (project-id)$
         

  4. Submit the Managed Service for Apache Spark job.




### Java

  1. Set component versions in `pom.xml` file. 
     1. The Managed Service for Apache Spark [2.0.x release versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.0) page lists the Scala, Spark, and HBase component versions installed with the most recent and last four image 2.0 subminor versions. 
        1. To find the subminor version of your 2.0 image version cluster, click the cluster name on the [**Clusters**](https://console.cloud.google.com/dataproc/clusters) page in the Google Cloud console to open the **Cluster details** page, where the cluster **Image version** is listed. ![](https://docs.cloud.google.com/static/managed-spark/images/image-version.png)
     2. Alternatively, you can run the following commands in an [SSH session terminal](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh) from the master node of your cluster to determine component versions: 
        1. Check scala version: 
               
               scala -version
               

        2. Check Spark version (control-D to exit): 
               
               spark-shell
               

        3. Check HBase version: 
               
               hbase version
               

        4. Identify the Spark, Scala, and HBase version dependencies in the Maven [`pom.xml`](https://github.com/apache/hbase-connectors/blob/master/spark/pom.xml): 
               
               <properties>
                 <scala.version>scala full version (for example, 2.12.14)</scala.version>
                 <scala.main.version>scala main version (for example, 2.12)</scala.main.version>
                 <spark.version>spark version (for example, 3.1.2)</spark.version>
                 <hbase.client.version>hbase version (for example, 2.2.7)</hbase.client.version>
                 <hbase-spark.version>[1.0.0](https://mvnrepository.com/artifact/org.apache.hbase.connectors.spark/hbase-spark)(the current Apache HBase Spark Connector version)>
               </properties>
               

Note: The `hbase-spark.version` is the current Spark HBase connector version; leave this version number unchanged.
     3. Edit the `pom.xml` file in the Cloud Shell editor to insert the the correct Scala, Spark, and HBase version numbers. Click **Open Terminal** when you finish editing to return to the Cloud Shell terminal command line. 
            
            cloudshell edit .
            

     4. Switch to Java 8 in Cloud Shell. This JDK version is needed to build the code (you can ignore any plugin warning messages): 
            
            sudo update-java-alternatives -s java-1.8.0-openjdk-amd64 && export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
            

     5. Verify Java 8 installation: 
            
            java -version
            

Sample output: 
            
            openjdk version "1.8..."
             

  2. Build the `jar` file: 
         
         mvn clean package
         

The `.jar` file is placed in the `/target` subdirectory (for example, **`target/spark-hbase-1.0-SNAPSHOT.jar`**.
  3. Submit the job. 
         
         gcloud dataproc jobs submit spark \
             --class=hbase.SparkHBaseMain  \
             --jars=target/filename.jar \
             --region=cluster-region \
             --cluster=cluster-name
         

     * `--jars`: Insert the name of your `.jar` file after "target/" and before ".jar".
     * If you did not set the Spark driver and executor HBase classpaths when you created your cluster, you must set them with each job submission by including the following `‑‑properties` flag in you job submit command: 
           
           --properties='spark.driver.extraClassPath=/etc/hbase/conf:/usr/lib/hbase/*,spark.executor.extraClassPath=/etc/hbase/conf:/usr/lib/hbase/*'
                  

  4. View HBase table output in the Cloud Shell session terminal output: 
         
         Waiting for job output...
         ...
         +----+----+
         | key|name|
         +----+----+
         |key1| foo|
         |key2| bar|
         +----+----+
         




### Python

  1. Submit the job. 
         
         gcloud dataproc jobs submit pyspark scripts/pyspark-hbase.py \
             --region=cluster-region \
             --cluster=cluster-name
         

     * If you did not set the Spark driver and executor HBase classpaths when you created your cluster, you must set them with each job submission by including the following `‑‑properties` flag in you job submit command: 
           
           --properties='spark.driver.extraClassPath=/etc/hbase/conf:/usr/lib/hbase/*,spark.executor.extraClassPath=/etc/hbase/conf:/usr/lib/hbase/*'
                  

  2. View HBase table output in the Cloud Shell session terminal output: 
         
         Waiting for job output...
         ...
         +----+----+
         | key|name|
         +----+----+
         |key1| foo|
         |key2| bar|
         +----+----+
         




### Scan the HBase table

You can scan the content of your HBase table by running the following commands in the master node SSH session terminal that you opened in Verify connector installation:

  1. Open the HBase shell: 
         
         hbase shell
         

  2. Scan 'my-table': 
         
         scan 'my_table'
         

Sample output: 
         
         ROW               COLUMN+CELL
          key1             column=cf:name, timestamp=1647364013561, value=foo
          key2             column=cf:name, timestamp=1647364012817, value=bar
         2 row(s)
         Took 0.5009 seconds
         




## Clean up

After you finish the tutorial, you can clean up the resources that you created so that they stop using quota and incurring charges. The following sections describe how to delete or turn off these resources. 

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the cluster

  * To delete your cluster: 
        
        gcloud dataproc clusters delete cluster-name \
            --region=${REGION}
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
