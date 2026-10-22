---
url: https://docs.cloud.google.com/appengine/docs/flexible/java/configuring-the-web-xml-deployment-descriptor/
title: Configuring the web.xml deployment descriptor \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:30.853513+00:00
---

# Configuring the web.xml deployment descriptor  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/java/configuring-the-web-xml-deployment-descriptor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Configuring the web.xml deployment descriptor Stay organized with collections  Save and categorize content based on your preferences. 

The `web.xml` file is only used when deploying a Java app to a runtime that includes the Eclipse Jetty 9/ servlet 3 server. For more details, see [the Eclipse Jetty 9.3 Runtime](https://docs.cloud.google.com/appengine/docs/flexible/java/runtime).

Java web applications use a deployment descriptor file to determine how URLs map to servlets, which URLs require authentication, and other information. This file is named `web.xml`, and resides in the app's WAR under the `WEB-INF/` directory. `web.xml` is part of the servlet standard for web applications.

For more information about the `web.xml` standard, see [the Servlet specification](http://jcp.org/aboutJava/communityprocess/final/jsr154/index.html).

## About deployment descriptors

A web application's deployment descriptor describes the classes, resources and configuration of the application and how the web server uses them to serve web requests. When the web server receives a request for the application, it uses the deployment descriptor to map the URL of the request to the code that ought to handle the request.

The deployment descriptor is a file named `web.xml`. It resides in the app's WAR under the `WEB-INF/` directory. The file is an XML file whose root element is `<web-app>`.

Here is a `web.xml` example that maps all URL paths (`/*`) to the servlet class =`mysite.server.ComingSoonServlet`:
    
    
    <web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
             http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
             version="3.1">
        <servlet>
            <servlet-name>comingsoon</servlet-name>
            <servlet-class>mysite.server.ComingSoonServlet</servlet-class>
        </servlet>
        <servlet-mapping>
            <servlet-name>comingsoon</servlet-name>
            <url-pattern>/*</url-pattern>
        </servlet-mapping>
    </web-app>
    

## Servlets and URL paths

`web.xml` defines mappings between URL paths and the servlets that handle requests with those paths. The web server uses this configuration to identify the servlet to handle a given request and call the class method that corresponds to the request method (e.g., the `doGet()` method for HTTP GET requests).

To map a URL to a servlet, you declare the servlet with the `<servlet>` element, then define a mapping from a URL path to a servlet declaration with the `<servlet-mapping>` element.

The `<servlet>` element declares the servlet, including a name used to refer to the servlet by other elements in the file, the class to use for the servlet, and initialization parameters. You can declare multiple servlets using the same class with different initialization parameters. The name for each servlet must be unique across the deployment descriptor.
    
    
        <servlet>
            <servlet-name>redteam</servlet-name>
            <servlet-class>mysite.server.TeamServlet</servlet-class>
            <init-param>
                <param-name>teamColor</param-name>
                <param-value>red</param-value>
            </init-param>
            <init-param>
                <param-name>bgColor</param-name>
                <param-value>#CC0000</param-value>
            </init-param>
        </servlet>
    
        <servlet>
            <servlet-name>blueteam</servlet-name>
            <servlet-class>mysite.server.TeamServlet</servlet-class>
            <init-param>
                <param-name>teamColor</param-name>
                <param-value>blue</param-value>
            </init-param>
            <init-param>
                <param-name>bgColor</param-name>
                <param-value>#0000CC</param-value>
            </init-param>
        </servlet>
    

The `<servlet-mapping>` element specifies a URL pattern and the name of a declared servlet to use for requests whose URL matches the pattern. The URL pattern can use an asterisk (`*`) at the beginning or end of the pattern to indicate zero or more of any character. The standard does not support wildcards in the middle of a string, and does not allow multiple wildcards in one pattern. The pattern matches the full path of the URL, starting with and including the forward slash (`/`) following the domain name.
    
    
    <servlet-mapping>
        <servlet-name>redteam</servlet-name>
        <url-pattern>/red/*</url-pattern>
    </servlet-mapping>
    
    <servlet-mapping>
        <servlet-name>blueteam</servlet-name>
        <url-pattern>/blue/*</url-pattern>
    </servlet-mapping>
    

With this example, a request for the URL `http://www.example.com/blue/teamProfile` is handled by the TeamServlet class, with the `teamColor` parameter equal to `blue` and the `bgColor` parameter equal to `#0000CC`. The servlet can get the portion of the URL path matched by the wildcard using the ServletRequest object's `getPathInfo()` method.

The servlet can access its initialization parameters by getting its servlet configuration using its own `getServletConfig()` method, then calling the `getInitParameter()` method on the configuration object using the name of the parameter as an argument.
    
    
            String teamColor = getServletConfig().getInitParameter("teamColor");

## JSPs

An app can use JavaServer Pages (JSPs) to implement web pages. JSPs are servlets defined using static content (such as HTML) mixed with Java code.

App Engine supports automatic compilation and URL mapping for JSPs. A JSP file in the application's WAR (outside of `WEB-INF/`) whose filename ends in `.jsp` is compiled into a servlet class automatically, and mapped to the URL path equivalent to the path to the JSP file from the WAR root. For example, if an app has a JSP file named `start.jsp` in a subdirectory named `register/` in its WAR, App Engine compiles it and maps it to the URL path `/register/start.jsp`.

If you want more control over how the JSP is mapped to a URL, you can specify the mapping explicitly by declaring it with a `<servlet>` element in the deployment descriptor. Instead of a `<servlet-class>` element, you specify a `<jsp-file>` element with the path to the JSP file from the WAR root. The `<servlet>` element for the JSP can contain initialization parameters.
    
    
    <servlet>
        <servlet-name>register</servlet-name>
        <jsp-file>/register/start.jsp</jsp-file>
    </servlet>
    
    <servlet-mapping>
        <servlet-name>register</servlet-name>
        <url-pattern>/register/*</url-pattern>
    </servlet-mapping>
    

**Note:** The `<jsp-file>` must start with a forward slash (`/`) if the JSP is in the application's root directory.

You can install JSP tag libraries with the `<taglib>` element. A tag library has a path to the JSP Tag Library Descriptor (TLD) file (`<taglib-location>`) and a URI that JSPs use to select the library for loading (`<taglib-uri>`). Note that App Engine provides the [JavaServer Pages Standard Tag Library (JSTL)](http://java.sun.com/products/jsp/jstl/), and you do not need to install it.
    
    
    <taglib>
        <taglib-uri>/escape</taglib-uri>
        <taglib-location>/WEB-INF/escape-tags.tld</taglib-location>
    </taglib>
    

## The welcome file list

When the URLs for your site represent paths to static files or JSPs in your WAR, it is often a good idea for paths to directories to do something useful as well. A user visiting the URL path `/help/accounts/password.jsp` for information on account passwords may try to visit `/help/accounts/` to find a page introducing the account system documentation. The deployment descriptor can specify a list of filenames that the server should try when the user accesses a path that represents a WAR subdirectory (that is not already explicitly mapped to a servlet). The servlet standard calls this the "welcome file list."

For example, if the user accesses the URL path `/help/accounts/`, the following `<welcome-file-list>` element in the deployment descriptor tells the server to check for `help/accounts/index.jsp` and `help/accounts/index.html` before reporting that the URL does not exist:
    
    
    <welcome-file-list>
        <welcome-file>index.jsp</welcome-file>
        <welcome-file>index.html</welcome-file>
    </welcome-file-list>
    

## Filters

A _filter_ is a class that acts on a request like a servlet, but may allow the handling of the request to continue with other filters or servlets. A filter may perform an auxiliary task such as logging, performing specialized authentication checks, or annotating the request or response objects before calling the servlet. Filters allow you to compose request processing tasks from the deployment descriptor.

A filter class implements the `javax.servlet.Filter` interface, including the `doFilter()` method. Here is a simple filter implementation that logs a message, and passes control down the chain, which may include other filters or a servlet, as described by the deployment descriptor:
    
    
    package mysite.server;
    
    import java.io.IOException;
    import java.util.logging.Logger;
    import javax.servlet.Filter;
    import javax.servlet.FilterChain;
    import javax.servlet.FilterConfig;
    import javax.servlet.ServletException;
    import javax.servlet.ServletRequest;
    import javax.servlet.ServletResponse;
    
    public class LogFilterImpl implements Filter {
    
        private FilterConfig filterConfig;
        private static final Logger log = Logger.getLogger(LogFilterImpl.class.getName());
    
        public void doFilter(ServletRequest request, ServletResponse response, FilterChain filterChain)
            throws IOException, ServletException {
            log.warning("Log filter processed a " + getFilterConfig().getInitParameter("logType")
                + " request");
    
            filterChain.doFilter(request, response);
        }
    
        public FilterConfig getFilterConfig() {
            return filterConfig;
        }
    
        public void init(FilterConfig filterConfig) {
            this.filterConfig = filterConfig;
        }
    
        public void destroy() {}
    
    }
    

Similar to servlets, you configure a filter in the deployment descriptor by declaring the filter with the `<filter>` element, then mapping it to a URL pattern with the `<filter-mapping>` element. You can also map filters directly to other servlets.

The `<filter>` element contains a `<filter-name>`, `<filter-class>`, and optional `<init-param>` elements.
    
    
    <filter>
        <filter-name>logSpecial</filter-name>
        <filter-class>mysite.server.LogFilterImpl</filter-class>
        <init-param>
            <param-name>logType</param-name>
            <param-value>special</param-value>
        </init-param>
    </filter>
    

The `<filter-mapping>` element contains a `<filter-name>` that matches the name of a declared filter, and either a `<url-pattern>` element for applying the filter to URLs, or a `<servlet-name>` element that matches the name of a declared servlet for applying the filter whenever the servlet is called.
    
    
    <!-- Log for all URLs ending in ".special" -->
    <filter-mapping>
        <filter-name>logSpecial</filter-name>
        <url-pattern>*.special</url-pattern>
    </filter-mapping>
    
    <!-- Log for all URLs that use the "comingsoon" servlet -->
    <filter-mapping>
        <filter-name>logSpecial</filter-name>
        <servlet-name>comingsoon</servlet-name>
    </filter-mapping>
    

**Note:** Filters are not invoked on static assets, even if the path matches a `filter-mapping` pattern. Static files are served directly to the browser.

## Error Handlers

You can customize what the server sends to the user when an error occurs, using the deployment descriptor. The server can display an alternate page location when it's about to send a particular HTTP status code, or when a servlet raises a particular Java exception.

The `<error-page>` element contains either an `<error-code>` element with an HTTP error code value (such as `500`), or an `<exception-type>` element with the class name of the expected exception (such as `java.io.IOException`). It also contains a `<location>` element containing the URL path of the resource to show when the error occurs.
    
    
    <error-page>
        <error-code>500</error-code>
        <location>/errors/servererror.jsp</location>
    </error-page>
    

**Note:** You can't configure custom error handlers for some error conditions. Specifically, you cannot customize the `404` response page when no servlet mapping is defined for a URL, the `403` quota error page, or the `500` server error page that appears after an App Engine internal error.

## web.xml features not supported

The following `web.xml` features are not supported by App Engine:

  * App Engine supports the `<load-on-startup>` element for servlet declarations. However, the load actually occurs during the first request handled by the web server instance, not prior to it.
  * Some deployment descriptor elements can take a human readable display name, description and icon for use in IDEs. App Engine doesn't use these, and ignores them.
  * App Engine doesn't support JNDI environment variables (`<env-entry>`).
  * App Engine doesn't support EJB resources (`<resource-ref>`).
  * Notification of the destruction of servlets, servlet context, or filters is not supported.
  * The `<distributable>` element is ignored.
  * Servlet scheduling with `<run-at>` is not supported.
  * Security Constraints are not supported: for equivalent functionality, see [Authenticate to Cloud services using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).
  * CONFIDENTIAL is not supported in `web.xml`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
