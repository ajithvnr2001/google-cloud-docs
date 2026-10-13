---
url: https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/SparkJob/
title: SparkJob \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:38.356775+00:00
---

# SparkJob  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/SparkJob/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Reference ](https://docs.cloud.google.com/managed-spark/docs/reference)



Send feedback 

#  SparkJob Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



A Dataproc job for running [Apache Spark](https://spark.apache.org/) applications on YARN.

JSON representation  
---  
      
    
    {
      "args": [
        string
      ],
      "jarFileUris": [
        string
      ],
      "fileUris": [
        string
      ],
      "archiveUris": [
        string
      ],
      "properties": {
        string: string,
        ...
      },
      "loggingConfig": {
        object ([LoggingConfig](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/LoggingConfig))
      },
    
      // Union field driver can be only one of the following:
      "mainJarFileUri": string,
      "mainClass": string
      // End of list of possible types for union field driver.
    }  
  
Fields  
---  
`args[]` |  `string` Optional. The arguments to pass to the driver. Do not include arguments, such as `--conf`, that can be set as job properties, since a collision may occur that causes an incorrect job submission.  
`jarFileUris[]` |  `string` Optional. HCFS URIs of jar files to add to the CLASSPATHs of the Spark driver and tasks.  
`fileUris[]` |  `string` Optional. HCFS URIs of files to be placed in the working directory of each executor. Useful for naively parallel tasks.  
`archiveUris[]` |  `string` Optional. HCFS URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip.  
`properties` |  `map (key: string, value: string)` Optional. A mapping of property names to values, used to configure Spark. Properties that conflict with values set by the Dataproc API might be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`loggingConfig` |  `object (`[LoggingConfig](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/LoggingConfig)`)` Optional. The runtime log config for job execution.  
Union field `driver`. Required. The specification of the main method to call to drive the job. Specify either the jar file that contains the main class or the main class name. To pass both a main jar and a main class in that jar, add the jar to `[jarFileUris](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/SparkJob#FIELDS.jar_file_uris)`, and then specify the main class name in `[mainClass](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/SparkJob#FIELDS.main_class)`. `driver` can be only one of the following:  
`mainJarFileUri` |  `string` The HCFS URI of the jar file that contains the main class.  
`mainClass` |  `string` The name of the driver's main class. The jar file that contains the class must be in the default CLASSPATH or specified in SparkJob.jar_file_uris.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
