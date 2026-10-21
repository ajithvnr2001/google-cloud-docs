---
url: https://docs.cloud.google.com/managed-spark/docs/guides/manage-spark-dependencies/
title: Manage Java and Scala dependencies for Apache Spark \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:26.667374+00:00
---

# Manage Java and Scala dependencies for Apache Spark  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/manage-spark-dependencies/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Manage Java and Scala dependencies for Apache Spark Stay organized with collections  Save and categorize content based on your preferences. 

Spark applications often depend on third-party Java or Scala libraries. Here are recommended approaches to including these dependencies when you submit a Spark job to a Managed Service for Apache Spark cluster:

  1. When submitting a job from your local machine with the [`gcloud dataproc jobs submit`](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job#submitting_a_job) command, use the `--properties spark.jars.packages=[DEPENDENCIES]` flag.  
  
**Example:**
         
         gcloud dataproc jobs submit spark \
             --cluster=my-cluster \
             --region=region \
             --properties=spark.jars.packages='com.google.cloud:google-cloud-translate:1.35.0,org.apache.bahir:spark-streaming-pubsub_2.11:2.2.0'
         

  2. When [submitting a job directly on your cluster](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job#submit_a_job_directly_on_your_cluster) use the `spark-submit` command with the `--packages=[DEPENDENCIES]` parameter.  
  
**Example:**
         
         spark-submit --packages='com.google.cloud:google-cloud-translate:1.35.0,org.apache.bahir:spark-streaming-pubsub_2.11:2.2.0'
         

  3. When including custom JAR files or bundles:

     * **Job-specific dependencies:** Specify the Cloud Storage path to your JAR by using the `--jars` flag, the Google Cloud console **Jar files** field, or the API `jarFileUris` field when you [submit a job](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job).
     * **Cluster-wide dependencies:** Use the `spark:spark.jars` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties) during cluster creation (`--properties="spark:spark.jars=gs://<var>your-bucket</var>/<var>your-jarfile</var>.jar"`).
**Caution:** Don't copy custom JAR files directly into cluster system directories such as `/usr/lib/spark/jars/`. Placing custom JARs in system directories pollutes the Managed Service for Apache Spark agent classpath and can cause job cancellation failures and orphaned YARN applications.



## Avoid dependency conflicts

The earlier approaches might fail if Spark application dependencies conflict with Hadoop's dependencies. This conflict can arise because Hadoop injects its dependencies into the application's [classpath](https://en.wikipedia.org/wiki/Classpath), so its dependencies take precedence over the application's dependencies. When a conflict occurs, `NoSuchMethodError` or other errors can be generated.

**Example:**  
[Guava](https://github.com/google/guava) is the Google core library for Java that is used by many libraries and frameworks, including Hadoop. A dependency conflict can occur if a job or its dependencies require a version of Guava that is newer than the one used by Hadoop.

Hadoop v3.0 [resolved](https://issues.apache.org/jira/browse/HADOOP-11804)

this issue, but applications that rely on earlier Hadoop versions require the following two-part workaround to avoid possible dependency conflicts.

  1. Create a single JAR that contains the application's package and all of its dependencies.
  2. Relocate the conflicting dependency packages within the uber JAR to prevent their path names from conflicting with those of Hadoop's dependency packages. Instead of modifying your code, use a plugin (see below) to automatically perform this relocation (aka "shading") as part of the packaging process.



### Create a shaded uber JAR with Maven

[Maven](https://maven.apache.org/) is a package management tool for building Java applications. The [Maven scala](https://davidb.github.io/scala-maven-plugin/) plugin can be used to build applications written in Scala, the language used by Spark applications. The [Maven shade](http://maven.apache.org/plugins/maven-shade-plugin/)

plugin can be used to create a shaded JAR.

The following is a sample `pom.xml` configuration file that shades the Guava library, which is located in the `com.google.common` package. This configuration instructs Maven to rename the `com.google.common` package to `repackaged.com.google.common` and to update all references to the classes from the original package.
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <project xmlns="http://maven.apache.org/POM/4.0.0"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
    
      <properties>
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
      </properties>
    
      <groupId><!-- YOUR_GROUP_ID --></groupId>
      <artifactId><!-- YOUR_ARTIFACT_ID --></artifactId>
      <version><!-- YOUR_PACKAGE_VERSION --></version>
    
      <dependencies>
    
        <dependency>
          <groupId>org.apache.spark</groupId>
          <artifactId>spark-sql_2.11</artifactId>
          <version><!-- YOUR_SPARK_VERSION --></version>
          <scope>provided</scope>
        </dependency>
    
        <!-- YOUR_DEPENDENCIES -->
    
      </dependencies>
    
      <build>
        <plugins>
    
          <plugin>
            <groupId>net.alchim31.maven</groupId>
            <artifactId>scala-maven-plugin</artifactId>
            <executions>
              <execution>
                <goals>
                  <goal>compile</goal>
                  <goal>testCompile</goal>
                </goals>
              </execution>
            </executions>
            <configuration>
              <scalaVersion><!-- YOUR_SCALA_VERSION --></scalaVersion>
            </configuration>
          </plugin>
    
          <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-shade-plugin</artifactId>
            <executions>
              <execution>
                <phase>package</phase>
                <goals>
                  <goal>shade</goal>
                </goals>
                <configuration>
                  <transformers>
                    <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                      <mainClass><!-- YOUR_APPLICATION_MAIN_CLASS --></mainClass>
                    </transformer>
                    <!-- This is needed if you have dependencies that use Service Loader. Most Google Cloud client libraries do. -->
                    <transformer implementation="org.apache.maven.plugins.shade.resource.ServicesResourceTransformer"/>
                  </transformers>
                  <filters>
                    <filter>
                      <artifact>*:*</artifact>
                      <excludes>
                        <exclude>META-INF/maven/**</exclude>
                        <exclude>META-INF/*.SF</exclude>
                        <exclude>META-INF/*.DSA</exclude>
                        <exclude>META-INF/*.RSA</exclude>
                      </excludes>
                    </filter>
                  </filters>
                  <relocations>
                    <relocation>
                      <pattern>com</pattern>
                      <shadedPattern>repackaged.com.google.common</shadedPattern>
                      <includes>
                        <include>com.google.common.**</include>
                      </includes>
                    </relocation>
                  </relocations>
                </configuration>
              </execution>
            </executions>
          </plugin>
    
        </plugins>
      </build>
    
    </project>

To run the build: 
    
    
    mvn package
    

**Notes about`pom.xml`:**

  * [ManifestResourceTransformer](https://maven.apache.org/plugins/maven-shade-plugin/examples/resource-transformers.html#ManifestResourceTransformer) processes attributes in the uber JAR's manifest file (`MANIFEST.MF`). The manifest can also specify the entry point for your application.
  * Spark's [scope](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#Dependency_Scope) is `provided`, since Spark is installed on Managed Service for Apache Spark.
  * Specify the version of Spark that is installed on your Managed Service for Apache Spark cluster (see [Managed Service for Apache Spark Version List](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions) . If your application requires a Spark version that is different from the version installed on your Managed Service for Apache Spark cluster, you can write an [initialization action](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/init-actions) or construct a [custom image](https://docs.cloud.google.com/managed-spark/docs/guides/images) that installs the Spark version used by your application.
  * The `<filters>` entry exclude signature files from your dependencies' `META-INF` directories. Without this entry, a `java.lang.SecurityException: Invalid signature file digest for Manifest main attributes` run-time exception can occur because the signature files are invalid in the context of your uber JAR.
  * You may need to shade multiple libraries. To do so, include multiple paths. The next example shades the Guava and Protobuf libraries. 
        
        <relocation>
          <pattern>com</pattern>
          <shadedPattern>repackaged.com</shadedPattern>
          <includes>
            <include>com.google.protobuf.**</include>
            <include>com.google.common.**</include>
          </includes>
        </relocation>




### Create a shaded uber JAR with SBT

[SBT](https://www.scala-sbt.org/) is a tool for building Scala applications. To create a shaded JAR with SBT, add the [`sbt-assembly`](https://github.com/sbt/sbt-assembly)

plugin to your build definition, first by creating a file called `assembly.sbt` under the `project/` directory: 
    
    
    ├── src/
    └── build.sbt
    └── project/
        └── assembly.sbt
    

... then by adding the following line in `assembly.sbt`: 
    
    
    addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "0.14.6")

The following is a sample `build.sbt` configuration file that shades the Guava library, which is located in the `com.google.common package`:
    
    
    lazy val commonSettings = Seq(
     organization := "YOUR_GROUP_ID",
     name := "YOUR_ARTIFACT_ID",
     version := "YOUR_PACKAGE_VERSION",
     scalaVersion := "YOUR_SCALA_VERSION",
    )
    
    lazy val shaded = (project in file("."))
     .settings(commonSettings)
    
    mainClass in (Compile, packageBin) := Some("YOUR_APPLICATION_MAIN_CLASS")
    
    libraryDependencies ++= Seq(
     "org.apache.spark" % "spark-sql_2.11" % "YOUR_SPARK_VERSION" % "provided",
     // YOUR_DEPENDENCIES
    )
    
    assemblyShadeRules in assembly := Seq(
      ShadeRule.rename("com.google.common.**" -> "repackaged.com.google.common.@1").inAll
    )

To run the build: 
    
    
    sbt assembly
    

**Notes about`build.sbt`**:

  * The shade rule in the preceding example may not solve all dependency conflicts because SBT uses strict conflict resolution strategies. Therefore, you may need to provide more granular rules that explicitly merge specific types of conflicting files using `MergeStrategy.first`, `last`, `concat`, `filterDistinctLines`, `rename`, or `discard` strategies. See `sbt-assembly`'s [merge strategy](https://github.com/sbt/sbt-assembly#merge-strategy) for more details.
  * You may need to shade multiple libraries. To do so, include multiple paths. The next example shades the Guava and Protobuf libraries. 
        
        assemblyShadeRules in assembly := Seq(
          ShadeRule.rename("com.google.common.**" -> "repackaged.com.google.common.@1").inAll,
          ShadeRule.rename("com.google.protobuf.**" -> "repackaged.com.google.protobuf.@1").inAll
        )




## Submit the uber JAR to Managed Service for Apache Spark

After you have created a shaded uber JAR that contains your Spark application and its dependencies, upload the JAR to Cloud Storage and [submit a job](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job) to Managed Service for Apache Spark (using the `--jars` flag in the Google Cloud CLI CLI, the **Jar files** field in the Google Cloud console, the API `jarFileUris` field, or by specifying your shaded JAR as the main application JAR).

## What's next

  * See [spark-translate](https://github.com/GoogleCloudDataproc/cloud-dataproc/tree/main/spark-translate), a sample Spark application that contains configuration files for both Maven and SBT.
  * [Write and run Spark Scala jobs](https://docs.cloud.google.com/managed-spark/docs/tutorials/spark-scala) on Managed Service for Apache Spark. quickstart to learn how to write and run Spark Scala jobs on a Managed Service for Apache Spark cluster.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
