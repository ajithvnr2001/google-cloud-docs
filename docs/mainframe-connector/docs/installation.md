---
url: https://docs.cloud.google.com/mainframe-connector/docs/installation/
title: Install Mainframe Connector on your mainframe \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:10.104842+00:00
---

# Install Mainframe Connector on your mainframe  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/installation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-connector/docs/overview)



Send feedback 

#  Install Mainframe Connector on your mainframe Stay organized with collections  Save and categorize content based on your preferences. 

Mainframe Connector is launched as a Java virtual machine (JVM) process within the context of an [MVS batch job](https://www.ibm.com/docs/en/zos/3.1.0?topic=names-mvs-batch-jobs). Mainframe Connector is typically deployed using a JAR file containing some required dependencies other than the IBM libraries included with the JVM. The following sections describe the Mainframe Connector installation process in detail.

## Before you begin

  * Complete the [initial setup for Mainframe Connector](https://docs.cloud.google.com/mainframe-connector/docs/get-started). The initial setup includes granting the required roles to your service account, setting up security for your assets, and setting up network connectivity between your mainframe and Google Cloud.
  * Configure [Java 8](https://www.java.com/en/download/help/java8.html) or [Java 17](https://docs.oracle.com/en/java/javase/17/install/overview-jdk-installation.html).
  * Install the JZOS Batch Launcher and Toolkit ([Java 8](https://www.ibm.com/docs/en/sdk-java-technology/8?topic=components-jzos-batch-launcher-toolkit) or [Java 17](https://docs.cloud.google.com/mainframe-connector/docs/installation/)).



## Install Mainframe Connector

To install Mainframe Connector, use the following steps:

  1. Download the prebuilt [Mainframe Connector JAR file](https://docs.cloud.google.com/mainframe-connector/docs/installation/) to a directory that your user account has write permissions.

### Important

Be aware that Mainframe Connector uses Google Analytics to collect usage data. This helps us improve the software and provide a better user experience. By default, Google Analytics is enabled. However, you can opt out by configuring an [environment variable](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#disable_analytics) when running Mainframe Connector.   
  
The use of Google Analytics is subject to the Google Analytics [Terms of Service and Privacy Policy](https://www.google.com/analytics/terms). By downloading Mainframe Connector, you acknowledge that you have read, understood, and accepted the terms and conditions.

[Download](https://storage.googleapis.com/mainframe-connector-release/latest/mainframe-connector.tgz) Cancel

  2. Copy the _mainframe-connector-shadow- VERSION-all.jar_ file to the path specified in the _Java Classpath_ section of the BQSH [job control language (JCL)](https://www.ibm.com/docs/en/zos-basic-skills?topic=collection-basic-jcl-concepts) procedure shown in step 8. VERSION is the version of Mainframe Connector.

  3. To access Google Cloud services from your mainframe, you must create and download a service account key as a JSON key file. For more information about creating a JSON key file, see [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#iam-service-account-keys-create-console).

  4. Copy the JSON key file to the Unix file system using file transfer protocol (FTP) in binary transfer mode. Ensure that you store the unmodified JSON key file on the file system, with its original UTF-8 encoding.

There is no default path for storing the JSON key file in the IBM z/OS Unix file system. You must choose a path that is readable only by users with permissions to access the service account. The JSON key file won't be readable from UNIX System Services (USS) if it was transferred correctly.

  5. Use FTP in binary mode to upload the JAR file you downloaded in step 1 to the following location on your mainframe.
         
         /opt/google/mainframe-connector/VERSION/
         

Replace Version with the version of the JAR file.

Note that this is the recommended path to deploy the JAR file. You can also use any path chosen by a site administrator.

  6. Run the following command to validate that the JAR file was transferred correctly. Note that the `-t` option lists the contents of the JAR file.
         
         jar -tvf JAR_FILE_NAME
         

Replace JAR_FILE_NAME with the name of the JAR file.

  7. Make a copy of the following BQSH JCL procedure.
         
         /BQSH PROC
         //*******************************************************************
         //*
         //* Copyright 2022 Google LLC All Rights Reserved
         //*
         //* Licensed under the Apache License, Version 2.0 (the "License");
         //* you may not use this file except in compliance with the License.
         //* You may obtain a copy of the License at
         //*
         //*     http://www.apache.org/licenses/LICENSE-2.0
         //*
         //* Unless required by applicable law or agreed to in writing, software
         //* distributed under the License is distributed on an "AS IS" BASIS,
         //* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         //* See the License for the specific language governing permissions and
         //* limitations under the License.
         //*
         //*******************************************************************
         //BQSH EXEC PGM=JVMLDM86,REGION=0M,
         //  PARM='/+I com.google.cloud.bqsh.Bqsh'
         //SYSPRINT DD SYSOUT=*
         //SYSOUT   DD SYSOUT=*
         //STDOUT   DD SYSOUT=*
         //STDERR   DD SYSOUT=*
         //CEEDUMP  DD SYSOUT=*
         //ABNLIGNR DD DUMMY
         //STDIN    DD DUMMY
         //QUERY    DD DUMMY
         //INFILE   DD DUMMY
         //COPYBOOK DD DUMMY
         //KEYFILE  DD DUMMY
         //STDENV   DD *,SYMBOLS=EXECSYS
         
         # Service Account Keyfile
         # Edit the line below to specify a unix filesystem path where
         # the service account keyfile is stored.
         # The service account should be granted Storage, BigQuery and Logging permissions.
         export GKEYFILE="GKEY_FILE_PATH"
         
         # Path to directory containing google jar file
         # Edit this to set actual path selected for your site
         # it's recommended to have a path with a version identifier
         # and create a symlink to the directory of the latest version
         export GOOGLE_DIR="JAR_FILE_PATH"
         export GOOGLE_CLASSPATH="$GOOGLE_DIR/*"
         
         # Do not modify the 3 lines below
         # Collect system symbols from JES
         export JOBNAME=&JOBNAME
         export JOBDATE=&YYMMDD
         export JOBTIME=&HHMMSS
         
         # IBM JZOS JDK Location
         export JAVA_HOME="/usr/lpp/java/J8.0_64"
         export PATH="/bin:$JAVA_HOME/bin"
         
         # Log Level
         export BQSH_ROOT_LOGGER=DEBUG
         
         # Cloud Logging
         export LOG_PROJECT="PROJECT_NAME"
         export LOG_ID="LOG_ID_NAME"
         
         # Google Analytics
         # Uncomment the following line to disable Google Analytics
         #export DISABLE_ANALYTICS=True
         
         # Binary Data Sets
         # Uncomment the following line to set a default output bucket for scp.
         # The DSN of the input file is used as the object name.
         # this may greatly reduce effort across many job steps
         #export GCSDSNURI="gs://[BUCKET]/[PREFIX]"
         
         # Generational Data Sets
         # Uncomment the line below to set a default output bucket for scp GDG datasets.
         # The Cloud GDG feature emulates a GDG dataset in a versioned object.
         # Cloud Storage objects take precedence over local DSN when this is set.
         #export GCSGDGURI="gs://[BUCKET]/[PREFIX]"
         
         # Uncomment the line below to set a default output bucket for the gszutil command.
         #export GCSOUTURI="gs://[BUCKET]/[PREFIX]"
         
         # Mainframe Connector gRPC service
         # Uncomment and edit the lines below to set the Hostname or IP Address and
         # port of the gRPC data set transcoding service.
         # The gRPC service converts z/OS datasets to ORC format on VMs running in
         # Google Cloud VPC. This is strongly recommended when processing high volumes
         # of data.
         #export SRVREMOTE=
         #export SRVPORT=
         
         # Native Libraries
         export JL="$JH/lib"
         export LP="/lib:/usr/lib:$JH/bin:$JL/s390x:$JL/s390x/j9vm:$JH/bin/classic"
         export LIBPATH="$LP:/usr/lib/java_runtime64"
         
         # Java Classpath
         CP="$JL:$JL/ext:/usr/include/java_classes/*"
         export CLASSPATH="$CP:$GOOGLE_CLASSPATH"
         
         # JVM options
         IJO="-Xms512m -Xmx512m -Xcompressedrefs -Djava.net.preferIPv4Stack=true"
         IJO="$IJO -Dbqsh.dataset.encoding=IBM-1047"
         export IBM_JAVA_OPTIONS="$IJO"
         export JZOS_MAIN_ARGS=""
         /*
         // PEND
         

Replace the following:

     * GKEY_FILE_PATH: the path to the JSON key file described in step 3.
     * JAR_FILE_PATH: the path to the directory containing the JAR file.
     * PROJECT_NAME: the project for which the log is being created in Cloud Logging.
     * LOG_ID_NAME: the name of the log.
     * To disable debug logging, comment out the line `BQSH_ROOT_LOGGER=DEBUG`.
     * To configure Mainframe Connector to write logging information to Cloud Logging, set the `LOG_PROJECT` and `LOG_ID` environment variables.
     * To disable Google Analytics, set the `DISABLE_ANALYTICS` environment variable to `True`.
     * To specify the default character encoding used for mainframe dataset operations (DSN and DD), set the `bqsh.dataset.encoding` property. If unset on z/OS, Mainframe Connector attempts to dynamically detect the encoding using the `native.encoding` or `sun.jnu.encoding` system properties, falling back to `IBM-1047`. On non-mainframe environments, it falls back to the JVM default charset.

For the complete list of environment variables supported by Mainframe Connector, see [Environment variables](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables).

  8. To configure Mainframe Connector to work with a TLS intercepting proxy, set the following Java system properties in the BQSH JCL procedure.

     * `javax.net.ssl.trustStore`
     * `javax.net.ssl.trustStorePassword`
     * `https.proxyHost`
     * `https.proxyUser`
     * `https.proxyPassword`

The BQSH JCL procedure before adding the Java system properties for `IBM_JAVA_OPTIONS` is as follows.
    
    # JVM options
    IJO="-Xms512m -Xmx512m -Xcompressedrefs -Djava.net.preferIPv4Stack=true"
    export IBM_JAVA_OPTIONS="$IJO"
     ```
    
    The BQSH JCL procedure after adding the Java system properties for
    <code>IBM_JAVA_OPTIONS</code> is as follows.
    
    ```none
    # JVM options
    IJO="-Xms512m -Xmx512m -Xcompressedrefs -Djava.net.preferIPv4Stack=true"
    IJO="$IJO -Djavax.net.ssl.trustStore=/path/to/cacerts"
    IJO="$IJO -Djavax.net.ssl.trustStorePassword=notasecret"
    IJO="$IJO -Dhttp.proxyHost=proxy.example.com"
    IJO="$IJO -Dhttp.proxyUser=username"
    IJO="$IJO -Dhttp.proxyPassword=password"
    export IBM_JAVA_OPTIONS="$IJO"
     ```
    

  9. If you are using the default trust store password _changeit_ , then you don't have to set the `trustStorePassword` system property. The proxy capabilities are provided by `Apache HttpComponents HttpClient`.

You must use a certificate trust store format supported by Mainframe Connector. The certificate trust store can be stored in the following formats:

     * **PKCS12 (.p12):** May contain many certificates and requires a password
     * **JKS (.jks):** May contain many certificates and requires a password
     * **PEM (.pem):** May contain many certificates encoded as _base64_
     * **Binary (.der):** Contains one certificate per file

If the `trustStore` system property is the path to a directory, the directory is scanned and all certificates with the _.pem_ and _.der_ format found in the directory are added as trusted certificates. You must manually load PKCS12 or JKS certificates.




If you need to make changes to the BQSH JCL procedure at any time, you can stage a newer version in the lower environment [procedure library (PROCLIB)](https://www.ibm.com/docs/en/zos/3.1.0?topic=libraries-procedure-proclib). This library is added before the system library, _SYSP.PROCLIB_ , so the changes can be vetted against the lower environment before updating the procedure in _SYSP.PROCLIB_. This way, you can avoid updating JCL procedures to point to a new updated procedure during testing.

## Sample BQSH JCL procedure

The following is a sample BQSH JCL procedure. In this procedure, the _ENV_ symbolic is used to point to the Java standard environment statements and is specific to the Google Cloud environment. This way, you don't need multiple BQSH procedures for each environment. If you want to make changes for a particular environment, you just need to update that specific member in the Google Cloud environment in system _PARMLIB_ library. For example, create new JAR file, use a different IBM Java version, or change the JSON key file using environment statements.
    
    
    #BQSH PROC ENV=DEV
    //
    //******************************************************************
    //*
    //* Copyright 2022 Google LLC All Rights Reserved
    //*
    //* Licensed under the Apache License, Version 2.0 (the "License");
    //* you may not use this file except in compliance with the License.
    //* You may obtain a copy of the License at
    //*      http://www.apache.org/licenses/LICENSE-2.0
    //* Unless required by applicable law or agreed to in writing , software
    //* distributed under the License is distributed on as "AS IS" BASIS,
    //* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express of impl.
    //* See the license for the specific language governing permissions and
    //* limitations under the License.
    //*
    //******************************************************************
    //BQSH EXEC PGM=JVMLDM86,REGION=0M,
    //  PARM='/+I com.google.cloud.bqsh.Bqsh'
    //SYSPRINT DD SYSOUT = *
    //SYSOUT   DD SYSOUT = *
    //STDOUT   DD SYSOUT = *
    //STDERR   DD SYSOUT = *
    //CEEDUMP  DD SYSOUT = *
    //ABNLIGNR DD DUMMY
    //STDIN    DD DUMMY
    //QUERY    DD DUMMY
    //INFILE   DD DUMMY
    //COPYBOOK DD DUMMY
    //KEYFILE  DD DUMMY
    //STDENV   DD DISP=SHR,DSN=SYSP.PARMLIB(EDW&ENV)
    //         DD *,SYMBOLS=EXECSYS
    # Do not modify the 3 lines below
    # Collect system symbols from JES
    export JOBNAME=&JOBNAME
    export JOBDATE=&YYMMDD
    export JOBTIME=&HHMMSS
    

The following is an example of the _DEV PARMLIB_ member showing how the JSON key file and the Mainframe Connector software JAR file are referenced.
    
    
    # Service Account Keyfile
    # Edit the line below to specify a unix filesystem path where
    # the service account keyfile is stored.
    # The service account should be granted Storage, BigQuery and Logging pe
    GKPATH= "/opt/google/keyfile"
    GKFILE= "prj-ent-edw-dev-landing-2451-f89d99af31e5.json"
    export GKEYFILE= "$GKPATH/$GKFILE"
    
    # Path  to directory containing google jar file
    # Edit this is set actual path selected for your site
    # its recommended to have a path with a version identifier
    # and create a symlink to the directory of the latert version
    GOOGLE_DIR= "/opt/google/mainframe-connector/5.9.0"
    GOOGLE_CLASSPATH= "$GOOGLE_DIR/*"
    
    #IBM JZOS JDK Location
    JH= "/usr/lpp/java/J8.0_64"
    export JAVA_HOME= "$JH"
    export PATH= "/bin:$JH/bin"
    
    # Log Level
    export BQSH_ROOT_LOGGER=DEBUG
    

## What's next

  * [Move locally transcoded mainframe data to Google Cloud](https://docs.cloud.google.com/mainframe-connector/docs/local-transcoding)
  * [Transcode mainframe data remotely on Google Cloud](https://docs.cloud.google.com/mainframe-connector/docs/remote-transcoding)
  * [Transcode mainframe data moved to Google Cloud using a virtual tape library](https://docs.cloud.google.com/mainframe-connector/docs/vtl-transcoding)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
