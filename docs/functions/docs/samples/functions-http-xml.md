---
url: https://docs.cloud.google.com/functions/docs/samples/functions-http-xml/
title: HTTP XML \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:46.514049+00:00
---

# HTTP XML  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-http-xml/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  HTTP XML Stay organized with collections  Save and categorize content based on your preferences. 

Parses an HTTP request that contains "application/xml" content.

## Code sample

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package http provides a set of HTTP Cloud Functions samples.
    package http
    
    import (
    	"encoding/xml"
    	"fmt"
    	"html"
    	"io"
    	"net/http"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    )
    
    func init() {
    	functions.HTTP("ParseXML", ParseXML)
    }
    
    // ParseXML is an example of parsing a text/xml request.
    func ParseXML(w http.ResponseWriter, r *http.Request) {
    	var d struct {
    		Name string
    	}
    	b, err := io.ReadAll(r.Body)
    	if err != nil {
    		http.Error(w, "Could not read request", http.StatusBadRequest)
    	}
    	if err := xml.Unmarshal(b, &d); err != nil {
    		http.Error(w, "Could not parse request", http.StatusBadRequest)
    	}
    	if d.Name == "" {
    		d.Name = "World"
    	}
    	fmt.Fprintf(w, "Hello, %v!", html.EscapeString(d.Name))
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import java.io.ByteArrayInputStream;
    import java.io.IOException;
    import java.io.InputStream;
    import java.io.PrintWriter;
    import java.net.HttpURLConnection;
    import javax.xml.parsers.DocumentBuilder;
    import javax.xml.parsers.DocumentBuilderFactory;
    import javax.xml.parsers.ParserConfigurationException;
    import org.w3c.dom.Document;
    import org.xml.sax.SAXException;
    
    public class ParseXml implements HttpFunction {
      private static final DocumentBuilderFactory dbFactory;
    
      static {
        dbFactory = DocumentBuilderFactory.newInstance();
        try {
          // Prevent XXE attacks (see https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
          dbFactory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
          dbFactory.setFeature("http://xml.org/sax/features/external-general-entities", false);
          dbFactory.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
          dbFactory.setFeature("http://apache.org/xml/features/nonvalidating/load-external-dtd", false);
          dbFactory.setXIncludeAware(false);
          dbFactory.setExpandEntityReferences(false);
        } catch (ParserConfigurationException e) {
          throw new RuntimeException(e);
        }
      }
    
      // Parses a HTTP request in XML format
      // (Responds with a 400 error if the HTTP request isn't valid XML.)
      @Override
      public void service(HttpRequest request, HttpResponse response)
          throws IOException, ParserConfigurationException {
    
        try {
          DocumentBuilder docBuilder = dbFactory.newDocumentBuilder();
          var writer = new PrintWriter(response.getWriter());
    
          // Get request body
          InputStream bodyStream = new ByteArrayInputStream(
              request.getInputStream().readAllBytes());
    
          // Parse + process XML
          Document doc = docBuilder.parse(bodyStream);
          writer.printf("Root element: %s", doc.getDocumentElement().getNodeName());
        } catch (SAXException e) {
          response.setStatusCode(HttpURLConnection.HTTP_BAD_REQUEST);
          return;
        }
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    /**
     * Parses a document of type 'text/xml'
     *
     * @param {Object} req Cloud Function request context.
     * @param {Object} res Cloud Function response context.
     */
    functions.http('parseXML', (req, res) => {
      // Convert the request to a Buffer and a string
      // Use whichever one is accepted by your XML parser
      const data = req.rawBody;
      const xmlData = data.toString();
    
      const {parseString} = require('xml2js');
    
      parseString(xmlData, (err, result) => {
        if (err) {
          console.error(err);
          res.status(500).end();
          return;
        }
        res.send(result);
      });
    });

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import json
    
    import functions_framework
    
    import xmltodict
    
    @functions_framework.http
    def parse_xml(request):
        """Parses a document of type 'text/xml'
        Args:
            request (flask.Request): The request object.
        Returns:
            The response text, or any set of values that can be turned into a
             Response object using `make_response`
            <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
        """
        data = xmltodict.parse(request.data)
        return json.dumps(data, indent=2)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
