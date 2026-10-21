---
url: https://docs.cloud.google.com/error-reporting/docs/setup/java/
title: Instrument Java apps for Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:15.361374+00:00
---

# Instrument Java apps for Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/docs/setup/java/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Guides ](https://docs.cloud.google.com/error-reporting/docs/grouping-errors)



Send feedback 

#  Instrument Java apps for Error Reporting Stay organized with collections  Save and categorize content based on your preferences. 

The [Error Reporting package for Java](https://cloud.google.com/java/docs/reference/google-cloud-errorreporting/latest/overview.html) lets you send error events directly from your Java applications to Error Reporting so that you can diagnose and monitor runtime crashes. Instrumenting your application with the library lets you report custom error events and capture errors even when your log buckets use [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

For applications running on integrated Google Cloud services—including Cloud Run functions, [App Engine](https://docs.cloud.google.com/appengine/docs), [Compute Engine](https://docs.cloud.google.com/compute/docs), and [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs)—Error Reporting can also infer error events automatically from Cloud Logging without the Error Reporting package for Java. For Error Reporting to infer error events from logs, your log entries must follow the [error formatting requirements](https://docs.cloud.google.com/error-reporting/docs/formatting-error-messages) and be stored in a non-CMEK log bucket owned by the originating project or by the destination project to which the logs were routed.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Error Reporting API , if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=clouderrorreporting.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Error Reporting API , if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=clouderrorreporting.googleapis.com)




## Install the client library

The Error Reporting package for Java lets you monitor and view error events reported by Java applications running nearly anywhere.

If you are using [Maven](https://maven.apache.org/), add the following to your `pom.xml` file. For more information about BOMs, see [The Google Cloud Platform Libraries BOM](https://cloud.google.com/java/docs/bom).
    
    <dependencyManagement>
      <dependencies>
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>libraries-bom</artifactId>
          <version>26.90.0</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
      </dependencies>
    </dependencyManagement>
    
    <dependencies>
      <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-errorreporting</artifactId>
      </dependency>
    </dependencies>

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    implementation platform('com.google.cloud:libraries-bom:26.90.0')
    
    implementation 'com.google.cloud:google-cloud-errorreporting'

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    libraryDependencies += "com.google.cloud" % "google-cloud-errorreporting" % "0.220.0-beta"

If you're using Visual Studio Code or IntelliJ, you can add client libraries to your project using the following IDE plugins:

     * [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/client-libraries)
     * [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/client-libraries)

The plugins provide additional functionality, such as key management for service accounts. Refer to each plugin's documentation for details.




For more information on installation, read the [documentation](https://cloud.google.com/java/docs/reference/google-cloud-errorreporting/latest/overview) for the Error Reporting package for Java. You can also report issues using the [issue tracker](https://github.com/googleapis/google-cloud-java/issues).

### Configure the client library

You can customize the behavior of the Error Reporting package for Java. See the [Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-errorreporting/latest/overview). 

## Run apps on Google Cloud

To create error groups by using [`projects.events.report`](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report), your service account requires the [Error Reporting Writer role](https://docs.cloud.google.com/error-reporting/docs/iam#errorreporting.writer) (`roles/errorreporting.writer`).

Some Google Cloud services automatically grant the Error Reporting Writer role (`roles/errorreporting.writer`) to the appropriate service account. However, you must grant this role to the appropriate service account for some services.

### Cloud Run and Cloud Run functions

The default service account used by [Cloud Run](https://docs.cloud.google.com/run/docs) has the permissions of [Error Reporting Writer role](https://docs.cloud.google.com/error-reporting/docs/iam#errorreporting.writer) (`roles/errorreporting.writer`).

The Error Reporting package for Java can be used without needing to explicitly provide credentials.

Cloud Run is configured to use Error Reporting automatically. Unhandled JavaScript exceptions will appear in Logging and be processed by Error Reporting without needing to use the Error Reporting package for Java.

**Note:** Error Reporting automatically creates an error event when a log entry contains a stack trace and the severity level of the log entry isn't set or is set to at least `ERROR`.

### App Engine flexible environment

[App Engine](https://docs.cloud.google.com/appengine/docs) grants the [Error Reporting Writer role](https://docs.cloud.google.com/error-reporting/docs/iam#errorreporting.writer) (`roles/errorreporting.writer`) to your default service account automatically.

The Error Reporting package for Java can be used without needing to explicitly provide credentials.

Error Reporting is automatically enabled for App Engine flexible environment applications. No additional setup is required. **Note:** Error log entries written to `stderr` are processed automatically by Error Reporting, without needing to use the Error Reporting package for Java directly.
    
    
    @WebServlet(name = "Error reporting", value = "/error")
    public class ErrorReportingExample extends HttpServlet {
    
      private Logger logger = Logger.getLogger(ErrorReportingExample.class.getName());
    
      @Override
      public void doGet(HttpServletRequest req, HttpServletResponse resp)
          throws IOException, ServletException {
    
        // errors logged to stderr / Cloud logging with exceptions are automatically reported.
        logger.log(Level.SEVERE, "exception using log framework", new IllegalArgumentException());
    
        // use the error-reporting client library only if you require logging custom error events.
        logCustomErrorEvent();
    
        // runtime exceptions are also automatically reported.
        throw new RuntimeException("this is a runtime exception");
      }
    
      private void logCustomErrorEvent() {
        try (ReportErrorsServiceClient reportErrorsServiceClient = ReportErrorsServiceClient.create()) {
          // Custom error events require an error reporting location as well.
          ErrorContext errorContext =
              ErrorContext.newBuilder()
                  .setReportLocation(
                      SourceLocation.newBuilder()
                          .setFilePath("Test.java")
                          .setLineNumber(10)
                          .setFunctionName("myMethod")
                          .build())
                  .build();
          // Report a custom error event
          ReportedErrorEvent customErrorEvent =
              ReportedErrorEvent.getDefaultInstance()
                  .toBuilder()
                  .setMessage("custom error event")
                  .setContext(errorContext)
                  .build();
    
          // default project id
          ProjectName projectName = ProjectName.of(ServiceOptions.getDefaultProjectId());
          reportErrorsServiceClient.reportErrorEvent(projectName, customErrorEvent);
        } catch (Exception e) {
          logger.log(Level.SEVERE, "Exception encountered logging custom event", e);
        }
      }
    }

### Google Kubernetes Engine

To use Error Reporting with Google Kubernetes Engine, do the following:

  1. Ensure that the service account to be used by your container has been granted the [Error Reporting Writer role](https://docs.cloud.google.com/error-reporting/docs/iam#errorreporting.writer) (`roles/errorreporting.writer`).

You can use either the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) or a custom service account.

For information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  2. Create your cluster and grant the cluster the `cloud-platform` [access scope](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam).

For example, the following create command specifies the `cloud-platform` access scope and a service account:
         
         gcloud container clusters create CLUSTER_NAME --service-account  SERVICE_ACCT_NAME --scopes=cloud-platform
         


**Note:** After you create a cluster, you can't change its service account.

### Compute Engine

To use Error Reporting with Compute Engine VM instances, do the following:

  1. Ensure that the service account to be used by your VM instance has been granted the [Error Reporting Writer role](https://docs.cloud.google.com/error-reporting/docs/iam#errorreporting.writer) (`roles/errorreporting.writer`).

You can use either the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) or a custom service account.

For information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  2. In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  3. Select the VM instance that you want to receive the `cloud-platform` [access scope](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam).

  4. Click **Stop** , and then click **Edit**.

  5. In the **Identity and API access** section, select a service account that has the Error Reporting Writer role (`roles/errorreporting.writer`).

  6. In the **Access scopes** section, select **Allow full access to all Cloud APIs** , and then save your changes.

  7. Click **Start/Resume**.




## Example

Exceptions logged using the [Cloud Logging Logback Appender](https://github.com/googleapis/java-logging-logback) or [java.util.logging Handler](https://cloud.google.com/logging/docs/setup/java#jul_handler) are automatically reported to the Error Reporting console.

The following sample demonstrates using the Java client library to report a custom error event:
    
    
    import com.google.cloud.[ServiceOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceOptions.html);
    import com.google.devtools.clouderrorreporting.v1beta1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.ProjectName.html);
    import com.google.devtools.clouderrorreporting.v1beta1.ReportErrorsServiceClient;
    import com.google.devtools.clouderrorreporting.v1beta1.ReportedErrorEvent;
    import java.io.IOException;
    import java.io.PrintWriter;
    import java.io.StringWriter;
    
    /**
     * Snippet demonstrates using the Error Reporting API to report an exception.
     * <p>
     * When the workload runs on App Engine, GKE, Cloud Functions or another managed environment,
     * printing the exception's stack trace to stderr will automatically report the error
     * to Error Reporting.
     */
    public class QuickStart {
    
      static [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId;
    
      public static void main([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html)[] args) throws Exception {
        // Set your Google Cloud Platform project ID via environment or explicitly
        projectId = [ServiceOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceOptions.html).getDefaultProjectId();
        if (args.length > 0) {
          projectId = args[0];
        } else {
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) value = System.getenv("GOOGLE_CLOUD_PROJECT");
          if (value != null && value.isEmpty()) {
            projectId = value;
          }
        }
    
        try {
          throw new Exception("Something went wrong");
        } catch (Exception ex) {
          reportError(ex);
        }
      }
    
      /**
       * Sends formatted error report to Google Cloud including the error context.
       *
       * @param ex Exception containing the error and the context.
       * @throws IOException if fails to communicate with Google Cloud
       */
      private static void reportError(Exception ex) throws IOException {
        try (ReportErrorsServiceClient serviceClient = ReportErrorsServiceClient.create()) {
          StringWriter sw = new StringWriter();
          PrintWriter pw = new PrintWriter(sw);
          ex.printStackTrace(pw);
    
          ReportedErrorEvent errorEvent = ReportedErrorEvent.getDefaultInstance()
              .toBuilder()
              .setMessage(sw.toString())
              .build();
          // If you need to report an error asynchronously, use reportErrorEventCallable()
          // method
          serviceClient.reportErrorEvent([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.ProjectName.html).of(projectId), errorEvent);
        }
      }
    }

See the [Java API Reference Documentation](https://cloud.google.com/java/docs/reference/google-cloud-errorreporting/latest/overview) on how to retrieve and manage error statistics as well as data for individual events. 

## Run apps in a local development environment

To use the Error Reporting package for Java in a local development environment, such as running the library on your own workstation, you must provide your Error Reporting package for Java with the local application default credentials. For more information, see [Authenticate to Error Reporting](https://docs.cloud.google.com/error-reporting/docs/reference/authentication#client-libs).

To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

**Note:** If the gcloud CLI prints a warning that your account doesn't have the `serviceusage.services.use` permission, then some gcloud CLI commands and client libraries might not work. Ask an administrator to grant you the Service Usage Consumer IAM role (`roles/serviceusage.serviceUsageConsumer`), then run the following command: 
         
         gcloud auth application-default set-quota-project PROJECT_ID

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/error-reporting/docs/reference/authentication#local-development). 

The [`projects.events.report` method](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report) also supports API keys. If you want to use API keys for authentication, you do not need to set up a local Application Default Credentials file. For more information, see [Create an API key](https://docs.cloud.google.com/docs/authentication/api-keys#create) in the Google Cloud authentication documentation. 

## View error groups

In the Google Cloud console, go to the **Error Reporting** page: 

[Go to **Error Reporting**](https://console.cloud.google.com/errors)

You can also find this page by using the search bar.

For more information, see [View and filter error groups](https://docs.cloud.google.com/error-reporting/docs/viewing-errors).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
