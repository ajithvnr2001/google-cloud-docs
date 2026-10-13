---
url: https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/integrate-applications-data-agent/
title: Integrate QueryData with an application \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:53:02.729145+00:00
---

# Integrate QueryData with an application  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/integrate-applications-data-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Integrate QueryData with an application Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This tutorial describes how to set up and use QueryData in Firestore with MongoDB compatibility using the Google Cloud console and integrate it with your application. Learn how to build the [context set](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/context-sets-overview) file, create a context set that uses the context set file, use [MCP Toolbox](https://github.com/googleapis/mcp-toolbox) to call the [QueryData method in the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-databases) to generate MongoDB-compatible query language (MQL) queries for natural language questions, and integrate it with your application.

For more information, see [QueryData overview](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/data-agent-overview). 

## Objectives

  * Create databases and populate them with data.
  * Build a context set file with the context engineering agent.
  * Create a context set and upload a context set file.
  * Test QueryData and generate MQL queries in Firestore with MongoDB compatibility Studio.
  * Integrate QueryData with your application using [Gemini Data Analytics QueryData](https://mcp-toolbox.dev/integrations/cloudgda/tools/cloud-gda-query/) tool in MCP Toolbox.
  * Add grounding to LLM responses using value search queries.



## Costs

In this document, you use the following billable components of Google Cloud:

  * [ Firestore with MongoDB compatibility](https://cloud.google.com/firestore/enterprise/pricing#firestore-enterprise-edition-pricing)
  * [ Gemini for Google Cloud API](https://docs.cloud.google.com/gemini/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free).

To avoid continued billing, delete the resources you created when you finish the tasks in this document. For more information, see Clean up.

## Before you begin

Complete the following prerequisites before creating a context set.

### Enable required services

Enable the following services for your project: 

  * [Data Analytics API with Gemini](https://console.cloud.google.com/apis/library/geminidataanalytics.googleapis.com)
  * [Gemini for Google Cloud API](https://console.cloud.google.com/apis/library/cloudaicompanion.googleapis.com)
  * [Knowledge Catalog API](https://console.cloud.google.com/apis/library/dataplex.googleapis.com)



### Prepare a Firestore database

Make sure that you have a Firestore Enterprise edition database with MongoDB compatibility.

If you're trying the examples on this page, we recommend that you create a new database for this purpose. For more information, see [Create and manage databases](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/create-databases).

### Required roles and permissions

  * Grant the `roles/datastore.viewer` and `roles/geminidataanalytics.queryDataUser` roles to the IAM user at the project level. For more information, see [Add IAM policy binding for a project](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding). 



## Populate the `flights` and `airports` collections

In this section, you populate the `flights` and `airports` collections using the provided MQL scripts.

  1. In the Google Cloud console, go to the Firestore page.

[Go to Firestore](https://console.cloud.google.com/firestore)

  2. Select a database from the list. For example, if you created a new database earlier, select it. The database must be an Enterprise edition database with MongoDB compatibility.

  3. In the navigation menu, click **Firestore Studio**.

  4. Click **New MQL editor tab** or **New tab** to open a new tab.

  5. Populate the `airports` collection by running the following script. Make sure the **Read-only** option isn't selected.

#### See MQL script
         
         db.airports.insertMany([
         { iata: "BOS", name: "General Edward Lawrence Logan International Airport", city: "Boston", country: "United States" },
         { iata: "OGG", name: "Kahului Airport", city: "Kahului", country: "United States" },
         { iata: "MCI", name: "Kansas City International Airport", city: "Kansas City", country: "United States" },
         { iata: "PHX", name: "Phoenix Sky Harbor International Airport", city: "Phoenix", country: "United States" },
         { iata: "SFO", name: "San Francisco International Airport", city: "San Francisco", country: "United States" },
         { iata: "LAX", name: "Los Angeles International Airport", city: "Los Angeles", country: "United States" },
         { iata: "CLE", name: "Cleveland Hopkins International Airport", city: "Cleveland", country: "United States" },
         { iata: "EWR", name: "Newark Liberty International Airport", city: "Newark", country: "United States" },
         { iata: "BOI", name: "Boise Air Terminal/Gowen Field", city: "Boise", country: "United States" },
         { iata: "DAL", name: "Dallas Love Field", city: "Dallas", country: "United States" },
         { iata: "KOA", name: "Ellison Onizuka Kona International At Keahole Airport", city: "Kona", country: "United States" },
         { iata: "DCA", name: "Ronald Reagan Washington National Airport", city: "Washington", country: "United States" },
         { iata: "SLC", name: "Salt Lake City International Airport", city: "Salt Lake City", country: "United States" },
         { iata: "IAH", name: "George Bush Intercontinental Houston Airport", city: "Houston", country: "United States" },
         { iata: "PIT", name: "Pittsburgh International Airport", city: "Pittsburgh", country: "United States" },
         { iata: "MIA", name: "Miami International Airport", city: "Miami", country: "United States" },
         { iata: "SEA", name: "Seattle Tacoma International Airport", city: "Seattle", country: "United States" },
         { iata: "LGB", name: "Long Beach /Daugherty Field/ Airport", city: "Long Beach", country: "United States" },
         { iata: "IND", name: "Indianapolis International Airport", city: "Indianapolis", country: "United States" },
         { iata: "LIH", name: "Lihue Airport", city: "Lihue", country: "United States" },
         { iata: "SAT", name: "San Antonio International Airport", city: "San Antonio", country: "United States" },
         { iata: "RDU", name: "Raleigh Durham International Airport", city: "Raleigh-durham", country: "United States" },
         { iata: "TUS", name: "Tucson International Airport", city: "Tucson", country: "United States" },
         { iata: "BUR", name: "Bob Hope Airport", city: "Burbank", country: "United States" },
         { iata: "DTW", name: "Detroit Metropolitan Wayne County Airport", city: "Detroit", country: "United States" },
         { iata: "DFW", name: "Dallas Fort Worth International Airport", city: "Dallas-Fort Worth", country: "United States" },
         { iata: "AUS", name: "Austin Bergstrom International Airport", city: "Austin", country: "United States" },
         { iata: "STL", name: "St Louis Lambert International Airport", city: "St. Louis", country: "United States" },
         { iata: "ATL", name: "Hartsfield Jackson Atlanta International Airport", city: "Atlanta", country: "United States" },
         { iata: "FAT", name: "Fresno Yosemite International Airport", city: "Fresno", country: "United States" },
         { iata: "IAD", name: "Washington Dulles International Airport", city: "Washington", country: "United States" },
         { iata: "MKE", name: "General Mitchell International Airport", city: "Milwaukee", country: "United States" },
         { iata: "PDX", name: "Portland International Airport", city: "Portland", country: "United States" },
         { iata: "HNL", name: "Daniel K Inouye International Airport", city: "Honolulu", country: "United States" },
         { iata: "SAN", name: "San Diego International Airport", city: "San Diego", country: "United States" },
         { iata: "ONT", name: "Ontario International Airport", city: "Ontario", country: "United States" },
         { iata: "MDW", name: "Chicago Midway International Airport", city: "Chicago", country: "United States" },
         { iata: "DEN", name: "Denver International Airport", city: "Denver", country: "United States" },
         { iata: "PHL", name: "Philadelphia International Airport", city: "Philadelphia", country: "United States" },
         { iata: "JFK", name: "John F Kennedy International Airport", city: "New York", country: "United States" },
         { iata: "RNO", name: "Reno Tahoe International Airport", city: "Reno", country: "United States" },
         { iata: "SMF", name: "Sacramento International Airport", city: "Sacramento", country: "United States" },
         { iata: "COS", name: "City of Colorado Springs Municipal Airport", city: "Colorado Springs", country: "United States" },
         { iata: "PSP", name: "Palm Springs International Airport", city: "Palm Springs", country: "United States" },
         { iata: "BWI", name: "Baltimore/Washington International Thurgood Marshall Airport", city: "Baltimore", country: "United States" },
         { iata: "MSP", name: "Minneapolis-St Paul International/Wold-Chamberlain Airport", city: "Minneapolis", country: "United States" },
         { iata: "MSY", name: "Louis Armstrong New Orleans International Airport", city: "New Orleans", country: "United States" },
         { iata: "SNA", name: "John Wayne Airport-Orange County Airport", city: "Santa Ana", country: "United States" },
         { iata: "CLT", name: "Charlotte Douglas International Airport", city: "Charlotte", country: "United States" },
         { iata: "LAS", name: "McCarran International Airport", city: "Las Vegas", country: "United States" },
         { iata: "MCO", name: "Orlando International Airport", city: "Orlando", country: "United States" },
         { iata: "MRY", name: "Monterey Peninsula Airport", city: "Monterey", country: "United States" },
         { iata: "SBA", name: "Santa Barbara Municipal Airport", city: "Santa Barbara", country: "United States" },
         { iata: "RDD", name: "Redding Municipal Airport", city: "Redding", country: "United States" },
         { iata: "EUG", name: "Mahlon Sweet Field", city: "Eugene", country: "United States" },
         { iata: "MFR", name: "Rogue Valley International Medford Airport", city: "Medford", country: "United States" },
         { iata: "RDM", name: "Roberts Field", city: "Redmond-Bend", country: "United States" },
         { iata: "ACV", name: "California Redwood Coast-Humboldt County Airport", city: "Arcata CA", country: "United States" },
         { iata: "CEC", name: "Jack Mc Namara Field Airport", city: "Crescent City", country: "United States" },
         { iata: "SBP", name: "San Luis County Regional Airport", city: "San Luis Obispo", country: "United States" },
         { iata: "PSC", name: "Tri Cities Airport", city: "Pasco", country: "United States" },
         { iata: "SUN", name: "Friedman Memorial Airport", city: "Hailey", country: "United States" },
         { iata: "ASE", name: "Aspen-Pitkin Co/Sardy Field", city: "Aspen", country: "United States" },
         { iata: "MMH", name: "Mammoth Yosemite Airport", city: "Mammoth Lakes", country: "United States" }
         ])

  6. Populate the `flights` collection by running the following script. Make sure the **Read-only** option isn't selected.

#### See MQL script
         
         db.flights.insertMany([
         { "airline": "UA", "flight_number": "1532", "departure_airport": "SFO", "arrival_airport": "DEN", "departure_time": ISODate("2025-01-01T05:50:00Z"), "arrival_time": ISODate("2025-01-01T09:23:00Z"), "departure_gate": "E49", "arrival_gate": "D6" },
         { "airline": "UA", "flight_number": "1158", "departure_airport": "SFO", "arrival_airport": "ORD", "departure_time": ISODate("2025-01-01T05:57:00Z"), "arrival_time": ISODate("2025-01-01T12:13:00Z"), "departure_gate": "C38", "arrival_gate": "D30" },
         { "airline": "F9", "flight_number": "1057", "departure_airport": "IAH", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T05:52:00Z"), "arrival_time": ISODate("2025-01-01T08:14:00Z"), "departure_gate": "E33", "arrival_gate": "E43" },
         { "airline": "OO", "flight_number": "6403", "departure_airport": "MFR", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T05:57:00Z"), "arrival_time": ISODate("2025-01-01T07:23:00Z"), "departure_gate": "A6", "arrival_gate": "E50" },
         { "airline": "OO", "flight_number": "5628", "departure_airport": "RNO", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T06:19:00Z"), "arrival_time": ISODate("2025-01-01T07:37:00Z"), "departure_gate": "A37", "arrival_gate": "B29" },
         { "airline": "CY", "flight_number": "922", "departure_airport": "SFO", "arrival_airport": "LAX", "departure_time": ISODate("2025-01-01T06:38:00Z"), "arrival_time": ISODate("2025-01-01T07:49:00Z"), "departure_gate": "D20", "arrival_gate": "E45" },
         { "airline": "AA", "flight_number": "338", "departure_airport": "LAX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T06:44:00Z"), "arrival_time": ISODate("2025-01-01T08:03:00Z"), "departure_gate": "E20", "arrival_gate": "A45" },
         { "airline": "UA", "flight_number": "1195", "departure_airport": "MCO", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T12:28:00Z"), "arrival_time": ISODate("2025-01-01T15:06:00Z"), "departure_gate": "D22", "arrival_gate": "B36" },
         { "airline": "OO", "flight_number": "5632", "departure_airport": "SBA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T06:56:00Z"), "arrival_time": ISODate("2025-01-01T08:39:00Z"), "departure_gate": "E19", "arrival_gate": "A49" },
         { "airline": "UA", "flight_number": "300", "departure_airport": "CLE", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T07:15:00Z"), "arrival_time": ISODate("2025-01-01T09:22:00Z"), "departure_gate": "E8", "arrival_gate": "C28" },
         { "airline": "UA", "flight_number": "706", "departure_airport": "SEA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T07:14:00Z"), "arrival_time": ISODate("2025-01-01T09:07:00Z"), "departure_gate": "A32", "arrival_gate": "B26" },
         { "airline": "AA", "flight_number": "167", "departure_airport": "MIA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T07:47:00Z"), "arrival_time": ISODate("2025-01-01T10:51:00Z"), "departure_gate": "A23", "arrival_gate": "E4" },
         { "airline": "OO", "flight_number": "5441", "departure_airport": "SFO", "arrival_airport": "SBP", "departure_time": ISODate("2025-01-01T07:08:00Z"), "arrival_time": ISODate("2025-01-01T08:12:00Z"), "departure_gate": "E21", "arrival_gate": "D24" },
         { "airline": "UA", "flight_number": "616", "departure_airport": "SFO", "arrival_airport": "ORD", "departure_time": ISODate("2025-01-01T07:14:00Z"), "arrival_time": ISODate("2025-01-01T13:24:00Z"), "departure_gate": "A11", "arrival_gate": "D8" },
         { "airline": "AA", "flight_number": "24", "departure_airport": "SFO", "arrival_airport": "JFK", "departure_time": ISODate("2025-01-01T07:14:00Z"), "arrival_time": ISODate("2025-01-01T15:46:00Z"), "departure_gate": "D4", "arrival_gate": "C15" },
         { "airline": "UA", "flight_number": "72", "departure_airport": "HNL", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T07:28:00Z"), "arrival_time": ISODate("2025-01-01T14:22:00Z"), "departure_gate": "B33", "arrival_gate": "D49" },
         { "airline": "AS", "flight_number": "244", "departure_airport": "PDX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T07:24:00Z"), "arrival_time": ISODate("2025-01-01T09:04:00Z"), "departure_gate": "E46", "arrival_gate": "B8" },
         { "airline": "OO", "flight_number": "6307", "departure_airport": "MSP", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T07:29:00Z"), "arrival_time": ISODate("2025-01-01T09:32:00Z"), "departure_gate": "C49", "arrival_gate": "C36" },
         { "airline": "OO", "flight_number": "4975", "departure_airport": "STL", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T07:31:00Z"), "arrival_time": ISODate("2025-01-01T09:58:00Z"), "departure_gate": "C43", "arrival_gate": "E16" },
         { "airline": "AA", "flight_number": "23", "departure_airport": "DFW", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T08:41:00Z"), "arrival_time": ISODate("2025-01-01T10:34:00Z"), "departure_gate": "E13", "arrival_gate": "E19" },
         { "airline": "B6", "flight_number": "434", "departure_airport": "SFO", "arrival_airport": "BOS", "departure_time": ISODate("2025-01-01T08:00:00Z"), "arrival_time": ISODate("2025-01-01T16:23:00Z"), "departure_gate": "D16", "arrival_gate": "E46" },
         { "airline": "F9", "flight_number": "657", "departure_airport": "DEN", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T07:58:00Z"), "arrival_time": ISODate("2025-01-01T09:13:00Z"), "departure_gate": "E41", "arrival_gate": "E28" },
         { "airline": "OO", "flight_number": "6464", "departure_airport": "COS", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T07:56:00Z"), "arrival_time": ISODate("2025-01-01T09:45:00Z"), "departure_gate": "D49", "arrival_gate": "E17" },
         { "airline": "UA", "flight_number": "1235", "departure_airport": "IAD", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T08:28:00Z"), "arrival_time": ISODate("2025-01-01T11:15:00Z"), "departure_gate": "A22", "arrival_gate": "D19" },
         { "airline": "OO", "flight_number": "6527", "departure_airport": "EUG", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T07:54:00Z"), "arrival_time": ISODate("2025-01-01T09:36:00Z"), "departure_gate": "D9", "arrival_gate": "B26" },
         { "airline": "AA", "flight_number": "242", "departure_airport": "SFO", "arrival_airport": "ORD", "departure_time": ISODate("2025-01-01T08:18:00Z"), "arrival_time": ISODate("2025-01-01T14:26:00Z"), "departure_gate": "E30", "arrival_gate": "C1" },
         { "airline": "UA", "flight_number": "1739", "departure_airport": "SFO", "arrival_airport": "EWR", "departure_time": ISODate("2025-01-01T08:22:00Z"), "arrival_time": ISODate("2025-01-01T16:42:00Z"), "departure_gate": "C13", "arrival_gate": "D45" },
         { "airline": "B6", "flight_number": "133", "departure_airport": "BOS", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T08:34:00Z"), "arrival_time": ISODate("2025-01-01T12:30:00Z"), "departure_gate": "D49", "arrival_gate": "C16" },
         { "airline": "OO", "flight_number": "6336", "departure_airport": "SFO", "arrival_airport": "RNO", "departure_time": ISODate("2025-01-01T08:32:00Z"), "arrival_time": ISODate("2025-01-01T09:29:00Z"), "departure_gate": "B45", "arrival_gate": "A2" },
         { "airline": "UA", "flight_number": "567", "departure_airport": "IAD", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T10:47:00Z"), "arrival_time": ISODate("2025-01-01T13:39:00Z"), "departure_gate": "C27", "arrival_gate": "B24" },
         { "airline": "OO", "flight_number": "5223", "departure_airport": "SLC", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T08:50:00Z"), "arrival_time": ISODate("2025-01-01T09:55:00Z"), "departure_gate": "C38", "arrival_gate": "C11" },
         { "airline": "US", "flight_number": "1784", "departure_airport": "SFO", "arrival_airport": "CLT", "departure_time": ISODate("2025-01-01T08:47:00Z"), "arrival_time": ISODate("2025-01-01T16:32:00Z"), "departure_gate": "C42", "arrival_gate": "C31" },
         { "airline": "WN", "flight_number": "1579", "departure_airport": "ATL", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T08:48:00Z"), "arrival_time": ISODate("2025-01-01T10:55:00Z"), "departure_gate": "C47", "arrival_gate": "B5" },
         { "airline": "OO", "flight_number": "6396", "departure_airport": "BOI", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T08:56:00Z"), "arrival_time": ISODate("2025-01-01T09:43:00Z"), "departure_gate": "E20", "arrival_gate": "A6" },
         { "airline": "AA", "flight_number": "2293", "departure_airport": "DFW", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T08:57:00Z"), "arrival_time": ISODate("2025-01-01T11:08:00Z"), "departure_gate": "D41", "arrival_gate": "C37" },
         { "airline": "DL", "flight_number": "1106", "departure_airport": "SFO", "arrival_airport": "MSP", "departure_time": ISODate("2025-01-01T09:06:00Z"), "arrival_time": ISODate("2025-01-01T14:56:00Z"), "departure_gate": "E38", "arrival_gate": "B30" },
         { "airline": "DL", "flight_number": "1631", "departure_airport": "SFO", "arrival_airport": "ATL", "departure_time": ISODate("2025-01-01T09:00:00Z"), "arrival_time": ISODate("2025-01-01T16:26:00Z"), "departure_gate": "B13", "arrival_gate": "B45" },
         { "airline": "OO", "flight_number": "5427", "departure_airport": "SFO", "arrival_airport": "SMF", "departure_time": ISODate("2025-01-01T09:06:00Z"), "arrival_time": ISODate("2025-01-01T10:00:00Z"), "departure_gate": "C34", "arrival_gate": "C25" },
         { "airline": "CY", "flight_number": "352", "departure_airport": "SFO", "arrival_airport": "BOS", "departure_time": ISODate("2025-01-01T09:25:00Z"), "arrival_time": ISODate("2025-01-01T17:51:00Z"), "departure_gate": "A46", "arrival_gate": "E42" },
         { "airline": "UA", "flight_number": "1239", "departure_airport": "LAX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T09:59:00Z"), "arrival_time": ISODate("2025-01-01T11:19:00Z"), "departure_gate": "A35", "arrival_gate": "C2" },
         { "airline": "UA", "flight_number": "1285", "departure_airport": "SFO", "arrival_airport": "IAH", "departure_time": ISODate("2025-01-01T09:41:00Z"), "arrival_time": ISODate("2025-01-01T15:20:00Z"), "departure_gate": "A39", "arrival_gate": "E10" },
         { "airline": "CY", "flight_number": "753", "departure_airport": "SEA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T09:58:00Z"), "arrival_time": ISODate("2025-01-01T11:53:00Z"), "departure_gate": "C40", "arrival_gate": "E35" },
         { "airline": "CY", "flight_number": "956", "departure_airport": "SFO", "arrival_airport": "SAN", "departure_time": ISODate("2025-01-01T09:57:00Z"), "arrival_time": ISODate("2025-01-01T11:30:00Z"), "departure_gate": "B10", "arrival_gate": "E44" },
         { "airline": "OO", "flight_number": "5196", "departure_airport": "PDX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T09:53:00Z"), "arrival_time": ISODate("2025-01-01T11:39:00Z"), "departure_gate": "D13", "arrival_gate": "C34" },
         { "airline": "WN", "flight_number": "2346", "departure_airport": "SFO", "arrival_airport": "LAX", "departure_time": ISODate("2025-01-01T09:59:00Z"), "arrival_time": ISODate("2025-01-01T11:17:00Z"), "departure_gate": "C24", "arrival_gate": "E45" },
         { "airline": "OO", "flight_number": "6400", "departure_airport": "EUG", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T10:06:00Z"), "arrival_time": ISODate("2025-01-01T11:27:00Z"), "departure_gate": "E46", "arrival_gate": "D20" },
         { "airline": "CY", "flight_number": "23", "departure_airport": "JFK", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T10:21:00Z"), "arrival_time": ISODate("2025-01-01T14:09:00Z"), "departure_gate": "D2", "arrival_gate": "B21" },
         { "airline": "B6", "flight_number": "534", "departure_airport": "SFO", "arrival_airport": "BOS", "departure_time": ISODate("2025-01-01T10:33:00Z"), "arrival_time": ISODate("2025-01-01T18:55:00Z"), "departure_gate": "A49", "arrival_gate": "A5" },
         { "airline": "UA", "flight_number": "1727", "departure_airport": "BOS", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T10:34:00Z"), "arrival_time": ISODate("2025-01-01T13:57:00Z"), "departure_gate": "D43", "arrival_gate": "A31" },
         { "airline": "WN", "flight_number": "4391", "departure_airport": "LAS", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T10:49:00Z"), "arrival_time": ISODate("2025-01-01T12:17:00Z"), "departure_gate": "A40", "arrival_gate": "C49" },
         { "airline": "OO", "flight_number": "5335", "departure_airport": "CEC", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T10:25:00Z"), "arrival_time": ISODate("2025-01-01T12:04:00Z"), "departure_gate": "C8", "arrival_gate": "C6" },
         { "airline": "DL", "flight_number": "1680", "departure_airport": "ATL", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T10:43:00Z"), "arrival_time": ISODate("2025-01-01T12:45:00Z"), "departure_gate": "E49", "arrival_gate": "E24" },
         { "airline": "OO", "flight_number": "6283", "departure_airport": "SFO", "arrival_airport": "MCI", "departure_time": ISODate("2025-01-01T10:38:00Z"), "arrival_time": ISODate("2025-01-01T17:01:00Z"), "departure_gate": "C32", "arrival_gate": "B12" },
         { "airline": "OO", "flight_number": "5260", "departure_airport": "SFO", "arrival_airport": "FAT", "departure_time": ISODate("2025-01-01T10:37:00Z"), "arrival_time": ISODate("2025-01-01T11:39:00Z"), "departure_gate": "B46", "arrival_gate": "B43" },
         { "airline": "OO", "flight_number": "6249", "departure_airport": "LAS", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T10:48:00Z"), "arrival_time": ISODate("2025-01-01T12:19:00Z"), "departure_gate": "D11", "arrival_gate": "A49" },
         { "airline": "AA", "flight_number": "23", "departure_airport": "SFO", "arrival_airport": "DFW", "departure_time": ISODate("2025-01-01T11:23:00Z"), "arrival_time": ISODate("2025-01-01T17:00:00Z"), "departure_gate": "B31", "arrival_gate": "A11" },
         { "airline": "UA", "flight_number": "753", "departure_airport": "SFO", "arrival_airport": "AUS", "departure_time": ISODate("2025-01-01T10:59:00Z"), "arrival_time": ISODate("2025-01-01T16:44:00Z"), "departure_gate": "B18", "arrival_gate": "D6" },
         { "airline": "WN", "flight_number": "4855", "departure_airport": "SFO", "arrival_airport": "MKE", "departure_time": ISODate("2025-01-01T11:08:00Z"), "arrival_time": ISODate("2025-01-01T17:33:00Z"), "departure_gate": "D3", "arrival_gate": "D40" },
         { "airline": "DL", "flight_number": "1845", "departure_airport": "SLC", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T11:29:00Z"), "arrival_time": ISODate("2025-01-01T12:06:00Z"), "departure_gate": "A22", "arrival_gate": "D2" },
         { "airline": "UA", "flight_number": "720", "departure_airport": "SFO", "arrival_airport": "DEN", "departure_time": ISODate("2025-01-01T12:46:00Z"), "arrival_time": ISODate("2025-01-01T16:19:00Z"), "departure_gate": "C41", "arrival_gate": "E39" },
         { "airline": "UA", "flight_number": "1257", "departure_airport": "IAH", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T11:30:00Z"), "arrival_time": ISODate("2025-01-01T13:19:00Z"), "departure_gate": "A26", "arrival_gate": "D2" },
         { "airline": "WN", "flight_number": "2509", "departure_airport": "SFO", "arrival_airport": "LAX", "departure_time": ISODate("2025-01-01T11:34:00Z"), "arrival_time": ISODate("2025-01-01T13:03:00Z"), "departure_gate": "C42", "arrival_gate": "D35" },
         { "airline": "UA", "flight_number": "73", "departure_airport": "EWR", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T12:11:00Z"), "arrival_time": ISODate("2025-01-01T15:24:00Z"), "departure_gate": "C5", "arrival_gate": "E10" },
         { "airline": "UA", "flight_number": "364", "departure_airport": "PHX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T11:56:00Z"), "arrival_time": ISODate("2025-01-01T13:11:00Z"), "departure_gate": "A39", "arrival_gate": "D26" },
         { "airline": "AA", "flight_number": "221", "departure_airport": "DFW", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T11:55:00Z"), "arrival_time": ISODate("2025-01-01T13:30:00Z"), "departure_gate": "A47", "arrival_gate": "B22" },
         { "airline": "AA", "flight_number": "2293", "departure_airport": "SFO", "arrival_airport": "DFW", "departure_time": ISODate("2025-01-01T12:04:00Z"), "arrival_time": ISODate("2025-01-01T17:36:00Z"), "departure_gate": "C43", "arrival_gate": "E30" },
         { "airline": "OO", "flight_number": "5199", "departure_airport": "SFO", "arrival_airport": "SLC", "departure_time": ISODate("2025-01-01T12:09:00Z"), "arrival_time": ISODate("2025-01-01T14:58:00Z"), "departure_gate": "A40", "arrival_gate": "E42" },
         { "airline": "OO", "flight_number": "6280", "departure_airport": "SLC", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T12:13:00Z"), "arrival_time": ISODate("2025-01-01T13:09:00Z"), "departure_gate": "E16", "arrival_gate": "E36" },
         { "airline": "OO", "flight_number": "6317", "departure_airport": "RNO", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T12:05:00Z"), "arrival_time": ISODate("2025-01-01T13:09:00Z"), "departure_gate": "C23", "arrival_gate": "A31" },
         { "airline": "UA", "flight_number": "864", "departure_airport": "SFO", "arrival_airport": "EWR", "departure_time": ISODate("2025-01-01T12:14:00Z"), "arrival_time": ISODate("2025-01-01T20:38:00Z"), "departure_gate": "C30", "arrival_gate": "E37" },
         { "airline": "OO", "flight_number": "5400", "departure_airport": "ONT", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T12:25:00Z"), "arrival_time": ISODate("2025-01-01T13:40:00Z"), "departure_gate": "A48", "arrival_gate": "E19" },
         { "airline": "UA", "flight_number": "236", "departure_airport": "HNL", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T12:40:00Z"), "arrival_time": ISODate("2025-01-01T19:36:00Z"), "departure_gate": "A34", "arrival_gate": "C12" },
         { "airline": "OO", "flight_number": "6343", "departure_airport": "SNA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T12:37:00Z"), "arrival_time": ISODate("2025-01-01T13:57:00Z"), "departure_gate": "A15", "arrival_gate": "D26" },
         { "airline": "UA", "flight_number": "1148", "departure_airport": "SFO", "arrival_airport": "IAD", "departure_time": ISODate("2025-01-01T13:10:00Z"), "arrival_time": ISODate("2025-01-01T21:02:00Z"), "departure_gate": "D24", "arrival_gate": "A23" },
         { "airline": "DL", "flight_number": "432", "departure_airport": "JFK", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T13:00:00Z"), "arrival_time": ISODate("2025-01-01T16:28:00Z"), "departure_gate": "E3", "arrival_gate": "A35" },
         { "airline": "B6", "flight_number": "1435", "departure_airport": "SFO", "arrival_airport": "LGB", "departure_time": ISODate("2025-01-01T13:33:00Z"), "arrival_time": ISODate("2025-01-01T14:47:00Z"), "departure_gate": "B24", "arrival_gate": "C12" },
         { "airline": "OO", "flight_number": "6408", "departure_airport": "SFO", "arrival_airport": "EUG", "departure_time": ISODate("2025-01-01T13:43:00Z"), "arrival_time": ISODate("2025-01-01T15:10:00Z"), "departure_gate": "B47", "arrival_gate": "A35" },
         { "airline": "UA", "flight_number": "645", "departure_airport": "PDX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T13:27:00Z"), "arrival_time": ISODate("2025-01-01T15:02:00Z"), "departure_gate": "D7", "arrival_gate": "E4" },
         { "airline": "WN", "flight_number": "1812", "departure_airport": "SFO", "arrival_airport": "SAN", "departure_time": ISODate("2025-01-01T14:32:00Z"), "arrival_time": ISODate("2025-01-01T15:51:00Z"), "departure_gate": "B35", "arrival_gate": "D48" },
         { "airline": "OO", "flight_number": "6409", "departure_airport": "SFO", "arrival_airport": "PDX", "departure_time": ISODate("2025-01-01T13:42:00Z"), "arrival_time": ISODate("2025-01-01T15:27:00Z"), "departure_gate": "C10", "arrival_gate": "B17" },
         { "airline": "UA", "flight_number": "358", "departure_airport": "AUS", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T14:31:00Z"), "arrival_time": ISODate("2025-01-01T15:48:00Z"), "departure_gate": "E33", "arrival_gate": "D21" },
         { "airline": "UA", "flight_number": "1728", "departure_airport": "OGG", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T14:02:00Z"), "arrival_time": ISODate("2025-01-01T20:38:00Z"), "departure_gate": "A30", "arrival_gate": "C29" },
         { "airline": "UA", "flight_number": "816", "departure_airport": "SEA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T13:44:00Z"), "arrival_time": ISODate("2025-01-01T15:38:00Z"), "departure_gate": "A36", "arrival_gate": "A9" },
         { "airline": "UA", "flight_number": "724", "departure_airport": "HNL", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T13:59:00Z"), "arrival_time": ISODate("2025-01-01T20:44:00Z"), "departure_gate": "A14", "arrival_gate": "C9" },
         { "airline": "UA", "flight_number": "1733", "departure_airport": "SFO", "arrival_airport": "DEN", "departure_time": ISODate("2025-01-01T14:38:00Z"), "arrival_time": ISODate("2025-01-01T18:35:00Z"), "departure_gate": "B27", "arrival_gate": "E32" },
         { "airline": "OO", "flight_number": "5543", "departure_airport": "SFO", "arrival_airport": "BOI", "departure_time": ISODate("2025-01-01T14:27:00Z"), "arrival_time": ISODate("2025-01-01T17:10:00Z"), "departure_gate": "E10", "arrival_gate": "B16" },
         { "airline": "UA", "flight_number": "1761", "departure_airport": "IAH", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T14:55:00Z"), "arrival_time": ISODate("2025-01-01T16:45:00Z"), "departure_gate": "B2", "arrival_gate": "E20" },
         { "airline": "UA", "flight_number": "277", "departure_airport": "DEN", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T14:44:00Z"), "arrival_time": ISODate("2025-01-01T16:04:00Z"), "departure_gate": "B47", "arrival_gate": "B13" },
         { "airline": "AA", "flight_number": "1213", "departure_airport": "DFW", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T15:14:00Z"), "arrival_time": ISODate("2025-01-01T16:45:00Z"), "departure_gate": "D11", "arrival_gate": "C31" },
         { "airline": "US", "flight_number": "407", "departure_airport": "PHX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T15:03:00Z"), "arrival_time": ISODate("2025-01-01T16:00:00Z"), "departure_gate": "C7", "arrival_gate": "D19" },
         { "airline": "OO", "flight_number": "5367", "departure_airport": "SFO", "arrival_airport": "RDM", "departure_time": ISODate("2025-01-01T14:52:00Z"), "arrival_time": ISODate("2025-01-01T16:23:00Z"), "departure_gate": "A5", "arrival_gate": "E40" },
         { "airline": "OO", "flight_number": "5454", "departure_airport": "SMF", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T15:46:00Z"), "arrival_time": ISODate("2025-01-01T16:33:00Z"), "departure_gate": "A20", "arrival_gate": "A40" },
         { "airline": "WN", "flight_number": "2687", "departure_airport": "SFO", "arrival_airport": "LAX", "departure_time": ISODate("2025-01-01T15:15:00Z"), "arrival_time": ISODate("2025-01-01T16:35:00Z"), "departure_gate": "D41", "arrival_gate": "B37" },
         { "airline": "CY", "flight_number": "932", "departure_airport": "SFO", "arrival_airport": "LAX", "departure_time": ISODate("2025-01-01T15:31:00Z"), "arrival_time": ISODate("2025-01-01T16:51:00Z"), "departure_gate": "A19", "arrival_gate": "E46" },
         { "airline": "WN", "flight_number": "3236", "departure_airport": "SFO", "arrival_airport": "SAN", "departure_time": ISODate("2025-01-01T15:56:00Z"), "arrival_time": ISODate("2025-01-01T17:23:00Z"), "departure_gate": "B29", "arrival_gate": "B32" },
         { "airline": "UA", "flight_number": "404", "departure_airport": "IAH", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T15:56:00Z"), "arrival_time": ISODate("2025-01-01T17:52:00Z"), "departure_gate": "B15", "arrival_gate": "B42" },
         { "airline": "CY", "flight_number": "933", "departure_airport": "LAX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T15:42:00Z"), "arrival_time": ISODate("2025-01-01T16:51:00Z"), "departure_gate": "E16", "arrival_gate": "E7" },
         { "airline": "US", "flight_number": "596", "departure_airport": "SFO", "arrival_airport": "PHX", "departure_time": ISODate("2025-01-01T15:51:00Z"), "arrival_time": ISODate("2025-01-01T18:52:00Z"), "departure_gate": "B25", "arrival_gate": "E38" },
         { "airline": "AA", "flight_number": "379", "departure_airport": "SFO", "arrival_airport": "DFW", "departure_time": ISODate("2025-01-01T16:04:00Z"), "arrival_time": ISODate("2025-01-01T21:55:00Z"), "departure_gate": "A30", "arrival_gate": "D49" },
         { "airline": "OO", "flight_number": "6280", "departure_airport": "SFO", "arrival_airport": "SNA", "departure_time": ISODate("2025-01-01T16:52:00Z"), "arrival_time": ISODate("2025-01-01T18:19:00Z"), "departure_gate": "B5", "arrival_gate": "C40" },
         { "airline": "UA", "flight_number": "735", "departure_airport": "DEN", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T17:34:00Z"), "arrival_time": ISODate("2025-01-01T19:09:00Z"), "departure_gate": "C31", "arrival_gate": "B15" },
         { "airline": "OO", "flight_number": "5553", "departure_airport": "PDX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T16:00:00Z"), "arrival_time": ISODate("2025-01-01T17:36:00Z"), "departure_gate": "E9", "arrival_gate": "D27" },
         { "airline": "UA", "flight_number": "73", "departure_airport": "SFO", "arrival_airport": "HNL", "departure_time": ISODate("2025-01-01T16:13:00Z"), "arrival_time": ISODate("2025-01-01T19:52:00Z"), "departure_gate": "C37", "arrival_gate": "B37" },
         { "airline": "UA", "flight_number": "587", "departure_airport": "SEA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T16:25:00Z"), "arrival_time": ISODate("2025-01-01T18:27:00Z"), "departure_gate": "B7", "arrival_gate": "B23" },
         { "airline": "OO", "flight_number": "5363", "departure_airport": "SFO", "arrival_airport": "ONT", "departure_time": ISODate("2025-01-01T16:09:00Z"), "arrival_time": ISODate("2025-01-01T17:28:00Z"), "departure_gate": "D21", "arrival_gate": "E29" },
         { "airline": "OO", "flight_number": "6386", "departure_airport": "SFO", "arrival_airport": "BOI", "departure_time": ISODate("2025-01-01T16:12:00Z"), "arrival_time": ISODate("2025-01-01T18:58:00Z"), "departure_gate": "D48", "arrival_gate": "E33" },
         { "airline": "CY", "flight_number": "27", "departure_airport": "JFK", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T16:28:00Z"), "arrival_time": ISODate("2025-01-01T20:19:00Z"), "departure_gate": "C6", "arrival_gate": "E14" },
         { "airline": "OO", "flight_number": "5190", "departure_airport": "SFO", "arrival_airport": "ASE", "departure_time": ISODate("2025-01-01T16:24:00Z"), "arrival_time": ISODate("2025-01-01T19:42:00Z"), "departure_gate": "C50", "arrival_gate": "B44" },
         { "airline": "CY", "flight_number": "746", "departure_airport": "SFO", "arrival_airport": "SEA", "departure_time": ISODate("2025-01-01T16:40:00Z"), "arrival_time": ISODate("2025-01-01T18:32:00Z"), "departure_gate": "D35", "arrival_gate": "C24" },
         { "airline": "UA", "flight_number": "1640", "departure_airport": "SFO", "arrival_airport": "ORD", "departure_time": ISODate("2025-01-01T17:01:00Z"), "arrival_time": ISODate("2025-01-01T23:02:00Z"), "departure_gate": "E27", "arrival_gate": "C24" },
         { "airline": "OO", "flight_number": "6221", "departure_airport": "MCI", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T17:28:00Z"), "arrival_time": ISODate("2025-01-01T19:08:00Z"), "departure_gate": "E2", "arrival_gate": "C36" },
         { "airline": "UA", "flight_number": "486", "departure_airport": "SFO", "arrival_airport": "LAS", "departure_time": ISODate("2025-01-01T16:47:00Z"), "arrival_time": ISODate("2025-01-01T18:16:00Z"), "departure_gate": "C42", "arrival_gate": "B47" },
         { "airline": "CY", "flight_number": "2", "departure_airport": "DCA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T17:01:00Z"), "arrival_time": ISODate("2025-01-01T20:07:00Z"), "departure_gate": "E43", "arrival_gate": "A33" },
         { "airline": "B6", "flight_number": "1436", "departure_airport": "LGB", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T16:59:00Z"), "arrival_time": ISODate("2025-01-01T18:35:00Z"), "departure_gate": "B12", "arrival_gate": "B22" },
         { "airline": "WN", "flight_number": "694", "departure_airport": "PHX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T17:11:00Z"), "arrival_time": ISODate("2025-01-01T18:05:00Z"), "departure_gate": "B44", "arrival_gate": "B18" },
         { "airline": "OO", "flight_number": "5635", "departure_airport": "MMH", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T17:00:00Z"), "arrival_time": ISODate("2025-01-01T18:01:00Z"), "departure_gate": "A25", "arrival_gate": "D7" },
         { "airline": "AS", "flight_number": "341", "departure_airport": "PSP", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T18:25:00Z"), "arrival_time": ISODate("2025-01-01T19:46:00Z"), "departure_gate": "A11", "arrival_gate": "E18" },
         { "airline": "OO", "flight_number": "6364", "departure_airport": "PSP", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T18:01:00Z"), "arrival_time": ISODate("2025-01-01T19:31:00Z"), "departure_gate": "A14", "arrival_gate": "B47" },
         { "airline": "OO", "flight_number": "5418", "departure_airport": "SBP", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T17:17:00Z"), "arrival_time": ISODate("2025-01-01T18:15:00Z"), "departure_gate": "B24", "arrival_gate": "D17" },
         { "airline": "AA", "flight_number": "197", "departure_airport": "SFO", "arrival_airport": "ORD", "departure_time": ISODate("2025-01-01T17:21:00Z"), "arrival_time": ISODate("2025-01-01T23:33:00Z"), "departure_gate": "D25", "arrival_gate": "E49" },
         { "airline": "CY", "flight_number": "720", "departure_airport": "SFO", "arrival_airport": "DAL", "departure_time": ISODate("2025-01-01T18:25:00Z"), "arrival_time": ISODate("2025-01-01T23:43:00Z"), "departure_gate": "B24", "arrival_gate": "A2" },
         { "airline": "OO", "flight_number": "6268", "departure_airport": "FAT", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T17:33:00Z"), "arrival_time": ISODate("2025-01-01T18:39:00Z"), "departure_gate": "E35", "arrival_gate": "D25" },
         { "airline": "OO", "flight_number": "5615", "departure_airport": "SFO", "arrival_airport": "EUG", "departure_time": ISODate("2025-01-01T17:45:00Z"), "arrival_time": ISODate("2025-01-01T19:18:00Z"), "departure_gate": "B11", "arrival_gate": "A34" },
         { "airline": "CY", "flight_number": "960", "departure_airport": "SFO", "arrival_airport": "SAN", "departure_time": ISODate("2025-01-01T17:55:00Z"), "arrival_time": ISODate("2025-01-01T19:23:00Z"), "departure_gate": "D23", "arrival_gate": "E44" },
         { "airline": "AA", "flight_number": "1393", "departure_airport": "DFW", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T17:51:00Z"), "arrival_time": ISODate("2025-01-01T19:25:00Z"), "departure_gate": "E11", "arrival_gate": "A41" },
         { "airline": "OO", "flight_number": "6352", "departure_airport": "BOI", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T17:58:00Z"), "arrival_time": ISODate("2025-01-01T18:46:00Z"), "departure_gate": "B31", "arrival_gate": "D23" },
         { "airline": "DL", "flight_number": "1151", "departure_airport": "SFO", "arrival_airport": "HNL", "departure_time": ISODate("2025-01-01T17:53:00Z"), "arrival_time": ISODate("2025-01-01T21:34:00Z"), "departure_gate": "E29", "arrival_gate": "B45" },
         { "airline": "OO", "flight_number": "5227", "departure_airport": "SFO", "arrival_airport": "SAN", "departure_time": ISODate("2025-01-01T19:07:00Z"), "arrival_time": ISODate("2025-01-01T20:31:00Z"), "departure_gate": "A35", "arrival_gate": "B38" },
         { "airline": "CY", "flight_number": "941", "departure_airport": "LAX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T18:19:00Z"), "arrival_time": ISODate("2025-01-01T19:34:00Z"), "departure_gate": "C33", "arrival_gate": "B44" },
         { "airline": "UA", "flight_number": "1044", "departure_airport": "EWR", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T19:19:00Z"), "arrival_time": ISODate("2025-01-01T22:53:00Z"), "departure_gate": "D50", "arrival_gate": "D26" },
         { "airline": "CY", "flight_number": "211", "departure_airport": "ORD", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T18:41:00Z"), "arrival_time": ISODate("2025-01-01T21:14:00Z"), "departure_gate": "D13", "arrival_gate": "E45" },
         { "airline": "UA", "flight_number": "685", "departure_airport": "ORD", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T18:51:00Z"), "arrival_time": ISODate("2025-01-01T21:04:00Z"), "departure_gate": "D26", "arrival_gate": "D45" },
         { "airline": "UA", "flight_number": "370", "departure_airport": "SFO", "arrival_airport": "SEA", "departure_time": ISODate("2025-01-01T18:49:00Z"), "arrival_time": ISODate("2025-01-01T20:41:00Z"), "departure_gate": "B6", "arrival_gate": "E20" },
         { "airline": "UA", "flight_number": "1433", "departure_airport": "IAH", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T19:45:00Z"), "arrival_time": ISODate("2025-01-01T21:39:00Z"), "departure_gate": "C42", "arrival_gate": "C48" },
         { "airline": "UA", "flight_number": "1172", "departure_airport": "DEN", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T20:19:00Z"), "arrival_time": ISODate("2025-01-01T22:37:00Z"), "departure_gate": "E31", "arrival_gate": "D43" },
         { "airline": "CY", "flight_number": "593", "departure_airport": "PSP", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T19:09:00Z"), "arrival_time": ISODate("2025-01-01T20:26:00Z"), "departure_gate": "C23", "arrival_gate": "C43" },
         { "airline": "UA", "flight_number": "1564", "departure_airport": "SFO", "arrival_airport": "ORD", "departure_time": ISODate("2025-01-01T19:14:00Z"), "arrival_time": ISODate("2025-01-02T01:14:00Z"), "departure_gate": "E3", "arrival_gate": "C48" },
         { "airline": "UA", "flight_number": "741", "departure_airport": "ORD", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T19:18:00Z"), "arrival_time": ISODate("2025-01-01T21:58:00Z"), "departure_gate": "A25", "arrival_gate": "B38" },
         { "airline": "WN", "flight_number": "600", "departure_airport": "SFO", "arrival_airport": "SNA", "departure_time": ISODate("2025-01-01T19:36:00Z"), "arrival_time": ISODate("2025-01-01T20:53:00Z"), "departure_gate": "D21", "arrival_gate": "D11" },
         { "airline": "F9", "flight_number": "664", "departure_airport": "SFO", "arrival_airport": "DEN", "departure_time": ISODate("2025-01-01T19:31:00Z"), "arrival_time": ISODate("2025-01-01T23:13:00Z"), "departure_gate": "E11", "arrival_gate": "E12" },
         { "airline": "OO", "flight_number": "4995", "departure_airport": "LAS", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T19:18:00Z"), "arrival_time": ISODate("2025-01-01T20:58:00Z"), "departure_gate": "B42", "arrival_gate": "B49" },
         { "airline": "CY", "flight_number": "717", "departure_airport": "DAL", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T19:31:00Z"), "arrival_time": ISODate("2025-01-01T21:02:00Z"), "departure_gate": "A42", "arrival_gate": "D32" },
         { "airline": "UA", "flight_number": "1243", "departure_airport": "SFO", "arrival_airport": "DEN", "departure_time": ISODate("2025-01-01T19:38:00Z"), "arrival_time": ISODate("2025-01-01T23:15:00Z"), "departure_gate": "B34", "arrival_gate": "A3" },
         { "airline": "UA", "flight_number": "560", "departure_airport": "IAD", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T19:41:00Z"), "arrival_time": ISODate("2025-01-01T22:29:00Z"), "departure_gate": "D9", "arrival_gate": "D33" },
         { "airline": "WN", "flight_number": "2791", "departure_airport": "LAX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T19:45:00Z"), "arrival_time": ISODate("2025-01-01T20:57:00Z"), "departure_gate": "C49", "arrival_gate": "C22" },
         { "airline": "WN", "flight_number": "2079", "departure_airport": "SAN", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T21:03:00Z"), "arrival_time": ISODate("2025-01-01T22:33:00Z"), "departure_gate": "A25", "arrival_gate": "E24" },
         { "airline": "OO", "flight_number": "6356", "departure_airport": "SFO", "arrival_airport": "SLC", "departure_time": ISODate("2025-01-01T19:57:00Z"), "arrival_time": ISODate("2025-01-01T22:49:00Z"), "departure_gate": "A28", "arrival_gate": "C45" },
         { "airline": "OO", "flight_number": "6290", "departure_airport": "PSP", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T19:48:00Z"), "arrival_time": ISODate("2025-01-01T21:12:00Z"), "departure_gate": "A33", "arrival_gate": "E27" },
         { "airline": "OO", "flight_number": "5363", "departure_airport": "ONT", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T20:27:00Z"), "arrival_time": ISODate("2025-01-01T21:54:00Z"), "departure_gate": "A14", "arrival_gate": "E17" },
         { "airline": "OO", "flight_number": "5206", "departure_airport": "SFO", "arrival_airport": "PHX", "departure_time": ISODate("2025-01-01T20:12:00Z"), "arrival_time": ISODate("2025-01-01T23:05:00Z"), "departure_gate": "D22", "arrival_gate": "E31" },
         { "airline": "B6", "flight_number": "1136", "departure_airport": "LGB", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T20:41:00Z"), "arrival_time": ISODate("2025-01-01T21:56:00Z"), "departure_gate": "B7", "arrival_gate": "E45" },
         { "airline": "US", "flight_number": "736", "departure_airport": "PHX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T21:12:00Z"), "arrival_time": ISODate("2025-01-01T22:11:00Z"), "departure_gate": "B22", "arrival_gate": "E33" },
         { "airline": "AA", "flight_number": "1611", "departure_airport": "DFW", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T21:42:00Z"), "arrival_time": ISODate("2025-01-01T23:37:00Z"), "departure_gate": "A13", "arrival_gate": "B44" },
         { "airline": "UA", "flight_number": "1241", "departure_airport": "SFO", "arrival_airport": "EWR", "departure_time": ISODate("2025-01-01T21:44:00Z"), "arrival_time": ISODate("2025-01-02T05:55:00Z"), "departure_gate": "D3", "arrival_gate": "A17" },
         { "airline": "UA", "flight_number": "1726", "departure_airport": "OGG", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T22:19:00Z"), "arrival_time": ISODate("2025-01-02T04:56:00Z"), "departure_gate": "C35", "arrival_gate": "B23" },
         { "airline": "US", "flight_number": "898", "departure_airport": "SFO", "arrival_airport": "CLT", "departure_time": ISODate("2025-01-01T22:29:00Z"), "arrival_time": ISODate("2025-01-02T06:18:00Z"), "departure_gate": "D7", "arrival_gate": "D15" },
         { "airline": "UA", "flight_number": "1669", "departure_airport": "SFO", "arrival_airport": "PHL", "departure_time": ISODate("2025-01-01T22:26:00Z"), "arrival_time": ISODate("2025-01-02T06:30:00Z"), "departure_gate": "B13", "arrival_gate": "A12" },
         { "airline": "UA", "flight_number": "362", "departure_airport": "SFO", "arrival_airport": "BWI", "departure_time": ISODate("2025-01-01T22:31:00Z"), "arrival_time": ISODate("2025-01-02T06:36:00Z"), "departure_gate": "E32", "arrival_gate": "A36" },
         { "airline": "OO", "flight_number": "6220", "departure_airport": "SFO", "arrival_airport": "RNO", "departure_time": ISODate("2025-01-01T22:25:00Z"), "arrival_time": ISODate("2025-01-01T23:23:00Z"), "departure_gate": "D18", "arrival_gate": "A31" },
         { "airline": "OO", "flight_number": "6376", "departure_airport": "SFO", "arrival_airport": "MRY", "departure_time": ISODate("2025-01-01T22:35:00Z"), "arrival_time": ISODate("2025-01-01T23:19:00Z"), "departure_gate": "C24", "arrival_gate": "E48" },
         { "airline": "UA", "flight_number": "522", "departure_airport": "SFO", "arrival_airport": "PDX", "departure_time": ISODate("2025-01-01T22:36:00Z"), "arrival_time": ISODate("2025-01-02T00:31:00Z"), "departure_gate": "B17", "arrival_gate": "A40" },
         { "airline": "UA", "flight_number": "1728", "departure_airport": "SFO", "arrival_airport": "BOS", "departure_time": ISODate("2025-01-01T22:46:00Z"), "arrival_time": ISODate("2025-01-02T07:20:00Z"), "departure_gate": "C40", "arrival_gate": "E43" },
         { "airline": "UA", "flight_number": "724", "departure_airport": "SFO", "arrival_airport": "LAX", "departure_time": ISODate("2025-01-01T22:45:00Z"), "arrival_time": ISODate("2025-01-02T00:29:00Z"), "departure_gate": "E43", "arrival_gate": "B23" },
         { "airline": "UA", "flight_number": "1681", "departure_airport": "SFO", "arrival_airport": "CLE", "departure_time": ISODate("2025-01-01T23:03:00Z"), "arrival_time": ISODate("2025-01-02T06:45:00Z"), "departure_gate": "D26", "arrival_gate": "E19" },
         { "airline": "UA", "flight_number": "1580", "departure_airport": "OGG", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-01T23:24:00Z"), "arrival_time": ISODate("2025-01-02T06:07:00Z"), "departure_gate": "E38", "arrival_gate": "A35" },
         { "airline": "DL", "flight_number": "806", "departure_airport": "SFO", "arrival_airport": "MSP", "departure_time": ISODate("2025-01-02T00:22:00Z"), "arrival_time": ISODate("2025-01-02T05:57:00Z"), "departure_gate": "B27", "arrival_gate": "A3" },
         { "airline": "OO", "flight_number": "5467", "departure_airport": "ONT", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T05:02:00Z"), "arrival_time": ISODate("2025-01-02T06:18:00Z"), "departure_gate": "E8", "arrival_gate": "C32" },
         { "airline": "WN", "flight_number": "1989", "departure_airport": "SFO", "arrival_airport": "LAS", "departure_time": ISODate("2025-01-02T05:35:00Z"), "arrival_time": ISODate("2025-01-02T06:46:00Z"), "departure_gate": "A21", "arrival_gate": "D15" },
         { "airline": "UA", "flight_number": "1619", "departure_airport": "BOS", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T05:56:00Z"), "arrival_time": ISODate("2025-01-02T09:56:00Z"), "departure_gate": "C46", "arrival_gate": "E11" },
         { "airline": "UA", "flight_number": "1076", "departure_airport": "SFO", "arrival_airport": "ORD", "departure_time": ISODate("2025-01-02T05:58:00Z"), "arrival_time": ISODate("2025-01-02T12:00:00Z"), "departure_gate": "E27", "arrival_gate": "A31" },
         { "airline": "F9", "flight_number": "1056", "departure_airport": "SFO", "arrival_airport": "IAH", "departure_time": ISODate("2025-01-02T05:59:00Z"), "arrival_time": ISODate("2025-01-02T12:09:00Z"), "departure_gate": "A29", "arrival_gate": "B13" },
         { "airline": "WN", "flight_number": "2242", "departure_airport": "LAX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T06:22:00Z"), "arrival_time": ISODate("2025-01-02T07:36:00Z"), "departure_gate": "C12", "arrival_gate": "D43" },
         { "airline": "B6", "flight_number": "735", "departure_airport": "SFO", "arrival_airport": "LGB", "departure_time": ISODate("2025-01-02T06:01:00Z"), "arrival_time": ISODate("2025-01-02T07:20:00Z"), "departure_gate": "C2", "arrival_gate": "C37" },
         { "airline": "WN", "flight_number": "3859", "departure_airport": "SFO", "arrival_airport": "MDW", "departure_time": ISODate("2025-01-02T06:27:00Z"), "arrival_time": ISODate("2025-01-02T12:26:00Z"), "departure_gate": "A28", "arrival_gate": "E38" },
         { "airline": "UA", "flight_number": "1285", "departure_airport": "SFO", "arrival_airport": "ORD", "departure_time": ISODate("2025-01-02T06:43:00Z"), "arrival_time": ISODate("2025-01-02T12:47:00Z"), "departure_gate": "B43", "arrival_gate": "A35" },
         { "airline": "WN", "flight_number": "1726", "departure_airport": "SFO", "arrival_airport": "PHX", "departure_time": ISODate("2025-01-02T06:32:00Z"), "arrival_time": ISODate("2025-01-02T09:20:00Z"), "departure_gate": "C16", "arrival_gate": "B2" },
         { "airline": "OO", "flight_number": "5186", "departure_airport": "SFO", "arrival_airport": "SAN", "departure_time": ISODate("2025-01-02T06:25:00Z"), "arrival_time": ISODate("2025-01-02T07:59:00Z"), "departure_gate": "C47", "arrival_gate": "C1" },
         { "airline": "UA", "flight_number": "566", "departure_airport": "PIT", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T07:15:00Z"), "arrival_time": ISODate("2025-01-02T09:46:00Z"), "departure_gate": "C39", "arrival_gate": "E39" },
         { "airline": "UA", "flight_number": "1195", "departure_airport": "MCO", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T07:18:00Z"), "arrival_time": ISODate("2025-01-02T10:05:00Z"), "departure_gate": "A47", "arrival_gate": "C43" },
         { "airline": "CY", "flight_number": "925", "departure_airport": "LAX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T06:57:00Z"), "arrival_time": ISODate("2025-01-02T08:07:00Z"), "departure_gate": "E29", "arrival_gate": "C19" },
         { "airline": "UA", "flight_number": "761", "departure_airport": "ORD", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T07:07:00Z"), "arrival_time": ISODate("2025-01-02T09:34:00Z"), "departure_gate": "B22", "arrival_gate": "A3" },
         { "airline": "UA", "flight_number": "758", "departure_airport": "SFO", "arrival_airport": "JFK", "departure_time": ISODate("2025-01-02T07:07:00Z"), "arrival_time": ISODate("2025-01-02T15:53:00Z"), "departure_gate": "B15", "arrival_gate": "B39" },
         { "airline": "CY", "flight_number": "67", "departure_airport": "IAD", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T07:07:00Z"), "arrival_time": ISODate("2025-01-02T10:00:00Z"), "departure_gate": "D24", "arrival_gate": "E33" },
         { "airline": "UA", "flight_number": "706", "departure_airport": "SEA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T07:05:00Z"), "arrival_time": ISODate("2025-01-02T08:59:00Z"), "departure_gate": "D9", "arrival_gate": "C28" },
         { "airline": "OO", "flight_number": "5441", "departure_airport": "SFO", "arrival_airport": "SBP", "departure_time": ISODate("2025-01-02T07:06:00Z"), "arrival_time": ISODate("2025-01-02T08:11:00Z"), "departure_gate": "B3", "arrival_gate": "B29" },
         { "airline": "CY", "flight_number": "202", "departure_airport": "SFO", "arrival_airport": "ORD", "departure_time": ISODate("2025-01-02T07:18:00Z"), "arrival_time": ISODate("2025-01-02T13:23:00Z"), "departure_gate": "C16", "arrival_gate": "D10" },
         { "airline": "CY", "flight_number": "710", "departure_airport": "SFO", "arrival_airport": "DAL", "departure_time": ISODate("2025-01-02T07:16:00Z"), "arrival_time": ISODate("2025-01-02T12:43:00Z"), "departure_gate": "D1", "arrival_gate": "E13" },
         { "airline": "AA", "flight_number": "24", "departure_airport": "SFO", "arrival_airport": "JFK", "departure_time": ISODate("2025-01-02T07:06:00Z"), "arrival_time": ISODate("2025-01-02T15:29:00Z"), "departure_gate": "C38", "arrival_gate": "D2" },
         { "airline": "UA", "flight_number": "72", "departure_airport": "HNL", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T07:28:00Z"), "arrival_time": ISODate("2025-01-02T14:20:00Z"), "departure_gate": "C8", "arrival_gate": "E18" },
         { "airline": "UA", "flight_number": "1278", "departure_airport": "ATL", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T07:30:00Z"), "arrival_time": ISODate("2025-01-02T09:41:00Z"), "departure_gate": "C16", "arrival_gate": "B21" },
         { "airline": "UA", "flight_number": "498", "departure_airport": "SFO", "arrival_airport": "SAN", "departure_time": ISODate("2025-01-02T07:20:00Z"), "arrival_time": ISODate("2025-01-02T08:38:00Z"), "departure_gate": "B42", "arrival_gate": "E44" },
         { "airline": "CY", "flight_number": "183", "departure_airport": "EWR", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T07:26:00Z"), "arrival_time": ISODate("2025-01-02T10:51:00Z"), "departure_gate": "B33", "arrival_gate": "A12" },
         { "airline": "AA", "flight_number": "76", "departure_airport": "SFO", "arrival_airport": "LAX", "departure_time": ISODate("2025-01-02T07:22:00Z"), "arrival_time": ISODate("2025-01-02T08:44:00Z"), "departure_gate": "E28", "arrival_gate": "B18" },
         { "airline": "WN", "flight_number": "2325", "departure_airport": "DEN", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T07:40:00Z"), "arrival_time": ISODate("2025-01-02T09:03:00Z"), "departure_gate": "A5", "arrival_gate": "A17" },
         { "airline": "WN", "flight_number": "1545", "departure_airport": "LAX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T07:48:00Z"), "arrival_time": ISODate("2025-01-02T09:02:00Z"), "departure_gate": "D42", "arrival_gate": "A25" },
         { "airline": "OO", "flight_number": "5196", "departure_airport": "SFO", "arrival_airport": "PDX", "departure_time": ISODate("2025-01-02T07:46:00Z"), "arrival_time": ISODate("2025-01-02T09:32:00Z"), "departure_gate": "B12", "arrival_gate": "B11" },
         { "airline": "UA", "flight_number": "1053", "departure_airport": "DEN", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T08:06:00Z"), "arrival_time": ISODate("2025-01-02T09:41:00Z"), "departure_gate": "C37", "arrival_gate": "E7" },
         { "airline": "AA", "flight_number": "23", "departure_airport": "DFW", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T07:53:00Z"), "arrival_time": ISODate("2025-01-02T09:26:00Z"), "departure_gate": "D24", "arrival_gate": "C34" },
         { "airline": "UA", "flight_number": "322", "departure_airport": "SNA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T07:53:00Z"), "arrival_time": ISODate("2025-01-02T09:17:00Z"), "departure_gate": "E22", "arrival_gate": "D32" },
         { "airline": "UA", "flight_number": "500", "departure_airport": "IND", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T08:02:00Z"), "arrival_time": ISODate("2025-01-02T09:46:00Z"), "departure_gate": "D47", "arrival_gate": "B25" },
         { "airline": "UA", "flight_number": "662", "departure_airport": "SAN", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T08:51:00Z"), "arrival_time": ISODate("2025-01-02T10:38:00Z"), "departure_gate": "C36", "arrival_gate": "B37" },
         { "airline": "UA", "flight_number": "834", "departure_airport": "LAS", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T07:51:00Z"), "arrival_time": ISODate("2025-01-02T09:17:00Z"), "departure_gate": "B24", "arrival_gate": "E14" },
         { "airline": "CY", "flight_number": "1930", "departure_airport": "SFO", "arrival_airport": "LAX", "departure_time": ISODate("2025-01-02T07:58:00Z"), "arrival_time": ISODate("2025-01-02T09:29:00Z"), "departure_gate": "D1", "arrival_gate": "E49" },
         { "airline": "UA", "flight_number": "1454", "departure_airport": "ORD", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T08:09:00Z"), "arrival_time": ISODate("2025-01-02T10:54:00Z"), "departure_gate": "C45", "arrival_gate": "D18" },
         { "airline": "AA", "flight_number": "1368", "departure_airport": "SFO", "arrival_airport": "DFW", "departure_time": ISODate("2025-01-02T08:11:00Z"), "arrival_time": ISODate("2025-01-02T13:35:00Z"), "departure_gate": "A24", "arrival_gate": "D28" },
         { "airline": "UA", "flight_number": "460", "departure_airport": "LAX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T08:22:00Z"), "arrival_time": ISODate("2025-01-02T09:53:00Z"), "departure_gate": "E4", "arrival_gate": "D14" },
         { "airline": "UA", "flight_number": "1547", "departure_airport": "SFO", "arrival_airport": "BOS", "departure_time": ISODate("2025-01-02T08:30:00Z"), "arrival_time": ISODate("2025-01-02T16:52:00Z"), "departure_gate": "B24", "arrival_gate": "D37" },
         { "airline": "AA", "flight_number": "242", "departure_airport": "SFO", "arrival_airport": "ORD", "departure_time": ISODate("2025-01-02T08:28:00Z"), "arrival_time": ISODate("2025-01-02T14:41:00Z"), "departure_gate": "D10", "arrival_gate": "B31" },
         { "airline": "OO", "flight_number": "5538", "departure_airport": "MFR", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T08:15:00Z"), "arrival_time": ISODate("2025-01-02T09:44:00Z"), "departure_gate": "D3", "arrival_gate": "B43" },
         { "airline": "UA", "flight_number": "1739", "departure_airport": "SFO", "arrival_airport": "EWR", "departure_time": ISODate("2025-01-02T08:56:00Z"), "arrival_time": ISODate("2025-01-02T17:03:00Z"), "departure_gate": "B18", "arrival_gate": "A15" },
         { "airline": "DL", "flight_number": "745", "departure_airport": "DTW", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T08:36:00Z"), "arrival_time": ISODate("2025-01-02T10:43:00Z"), "departure_gate": "B2", "arrival_gate": "D29" },
         { "airline": "OO", "flight_number": "5445", "departure_airport": "SFO", "arrival_airport": "SBP", "departure_time": ISODate("2025-01-02T10:35:00Z"), "arrival_time": ISODate("2025-01-02T11:50:00Z"), "departure_gate": "D39", "arrival_gate": "A1" },
         { "airline": "OO", "flight_number": "5223", "departure_airport": "SLC", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T08:52:00Z"), "arrival_time": ISODate("2025-01-02T09:50:00Z"), "departure_gate": "C17", "arrival_gate": "C19" },
         { "airline": "UA", "flight_number": "1615", "departure_airport": "SFO", "arrival_airport": "IAD", "departure_time": ISODate("2025-01-02T08:44:00Z"), "arrival_time": ISODate("2025-01-02T16:41:00Z"), "departure_gate": "A19", "arrival_gate": "C46" },
         { "airline": "AA", "flight_number": "1435", "departure_airport": "ORD", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T08:43:00Z"), "arrival_time": ISODate("2025-01-02T11:08:00Z"), "departure_gate": "B49", "arrival_gate": "B11" },
         { "airline": "HA", "flight_number": "11", "departure_airport": "SFO", "arrival_airport": "HNL", "departure_time": ISODate("2025-01-02T09:28:00Z"), "arrival_time": ISODate("2025-01-02T13:38:00Z"), "departure_gate": "E28", "arrival_gate": "B21" },
         { "airline": "OO", "flight_number": "6373", "departure_airport": "SFO", "arrival_airport": "DFW", "departure_time": ISODate("2025-01-02T08:51:00Z"), "arrival_time": ISODate("2025-01-02T14:40:00Z"), "departure_gate": "B42", "arrival_gate": "D13" },
         { "airline": "UA", "flight_number": "479", "departure_airport": "SFO", "arrival_airport": "LAX", "departure_time": ISODate("2025-01-02T11:15:00Z"), "arrival_time": ISODate("2025-01-02T12:47:00Z"), "departure_gate": "E32", "arrival_gate": "B7" },
         { "airline": "UA", "flight_number": "361", "departure_airport": "SFO", "arrival_airport": "LIH", "departure_time": ISODate("2025-01-02T09:33:00Z"), "arrival_time": ISODate("2025-01-02T13:10:00Z"), "departure_gate": "A45", "arrival_gate": "C26" },
         { "airline": "WN", "flight_number": "2074", "departure_airport": "SFO", "arrival_airport": "SNA", "departure_time": ISODate("2025-01-02T09:08:00Z"), "arrival_time": ISODate("2025-01-02T10:18:00Z"), "departure_gate": "A6", "arrival_gate": "A49" },
         { "airline": "CY", "flight_number": "84", "departure_airport": "SFO", "arrival_airport": "IAD", "departure_time": ISODate("2025-01-02T09:20:00Z"), "arrival_time": ISODate("2025-01-02T17:25:00Z"), "departure_gate": "A37", "arrival_gate": "B4" },
         { "airline": "WN", "flight_number": "2969", "departure_airport": "SAN", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T09:35:00Z"), "arrival_time": ISODate("2025-01-02T10:59:00Z"), "departure_gate": "B50", "arrival_gate": "A43" },
         { "airline": "UA", "flight_number": "1249", "departure_airport": "SFO", "arrival_airport": "MCO", "departure_time": ISODate("2025-01-02T10:10:00Z"), "arrival_time": ISODate("2025-01-02T18:15:00Z"), "departure_gate": "D13", "arrival_gate": "E20" },
         { "airline": "WN", "flight_number": "1820", "departure_airport": "SFO", "arrival_airport": "LAS", "departure_time": ISODate("2025-01-02T09:52:00Z"), "arrival_time": ISODate("2025-01-02T11:19:00Z"), "departure_gate": "B19", "arrival_gate": "D16" },
         { "airline": "WN", "flight_number": "2414", "departure_airport": "SFO", "arrival_airport": "PHX", "departure_time": ISODate("2025-01-02T09:57:00Z"), "arrival_time": ISODate("2025-01-02T12:52:00Z"), "departure_gate": "E1", "arrival_gate": "C5" },
         { "airline": "UA", "flight_number": "698", "departure_airport": "SEA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T09:54:00Z"), "arrival_time": ISODate("2025-01-02T11:59:00Z"), "departure_gate": "E37", "arrival_gate": "D34" },
         { "airline": "AS", "flight_number": "303", "departure_airport": "SFO", "arrival_airport": "SEA", "departure_time": ISODate("2025-01-02T10:06:00Z"), "arrival_time": ISODate("2025-01-02T12:11:00Z"), "departure_gate": "D36", "arrival_gate": "C9" },
         { "airline": "WN", "flight_number": "3323", "departure_airport": "SFO", "arrival_airport": "DEN", "departure_time": ISODate("2025-01-02T10:40:00Z"), "arrival_time": ISODate("2025-01-02T13:59:00Z"), "departure_gate": "A4", "arrival_gate": "E35" },
         { "airline": "OO", "flight_number": "6286", "departure_airport": "SBA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T10:23:00Z"), "arrival_time": ISODate("2025-01-02T11:47:00Z"), "departure_gate": "B46", "arrival_gate": "A8" },
         { "airline": "OO", "flight_number": "5603", "departure_airport": "PHX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T10:29:00Z"), "arrival_time": ISODate("2025-01-02T11:41:00Z"), "departure_gate": "A2", "arrival_gate": "C22" },
         { "airline": "CY", "flight_number": "218", "departure_airport": "SFO", "arrival_airport": "AUS", "departure_time": ISODate("2025-01-02T10:28:00Z"), "arrival_time": ISODate("2025-01-02T15:56:00Z"), "departure_gate": "E49", "arrival_gate": "C21" },
         { "airline": "OO", "flight_number": "5335", "departure_airport": "CEC", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T10:32:00Z"), "arrival_time": ISODate("2025-01-02T12:09:00Z"), "departure_gate": "D29", "arrival_gate": "D17" },
         { "airline": "OO", "flight_number": "5646", "departure_airport": "SFO", "arrival_airport": "SBA", "departure_time": ISODate("2025-01-02T10:33:00Z"), "arrival_time": ISODate("2025-01-02T11:54:00Z"), "departure_gate": "A50", "arrival_gate": "E40" },
         { "airline": "OO", "flight_number": "5635", "departure_airport": "SFO", "arrival_airport": "SNA", "departure_time": ISODate("2025-01-02T11:22:00Z"), "arrival_time": ISODate("2025-01-02T12:55:00Z"), "departure_gate": "C17", "arrival_gate": "D47" },
         { "airline": "OO", "flight_number": "6380", "departure_airport": "SFO", "arrival_airport": "BOI", "departure_time": ISODate("2025-01-02T10:41:00Z"), "arrival_time": ISODate("2025-01-02T13:18:00Z"), "departure_gate": "B18", "arrival_gate": "C15" },
         { "airline": "UA", "flight_number": "662", "departure_airport": "SFO", "arrival_airport": "MSP", "departure_time": ISODate("2025-01-02T10:52:00Z"), "arrival_time": ISODate("2025-01-02T16:39:00Z"), "departure_gate": "B6", "arrival_gate": "E11" },
         { "airline": "OO", "flight_number": "6270", "departure_airport": "SFO", "arrival_airport": "RNO", "departure_time": ISODate("2025-01-02T10:43:00Z"), "arrival_time": ISODate("2025-01-02T11:52:00Z"), "departure_gate": "C15", "arrival_gate": "E10" },
         { "airline": "OO", "flight_number": "4975", "departure_airport": "SFO", "arrival_airport": "TUS", "departure_time": ISODate("2025-01-02T12:23:00Z"), "arrival_time": ISODate("2025-01-02T15:18:00Z"), "departure_gate": "D5", "arrival_gate": "C12" },
         { "airline": "UA", "flight_number": "322", "departure_airport": "SFO", "arrival_airport": "SEA", "departure_time": ISODate("2025-01-02T10:49:00Z"), "arrival_time": ISODate("2025-01-02T12:54:00Z"), "departure_gate": "E29", "arrival_gate": "D3" },
         { "airline": "WN", "flight_number": "1009", "departure_airport": "LAX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T11:33:00Z"), "arrival_time": ISODate("2025-01-02T12:45:00Z"), "departure_gate": "E12", "arrival_gate": "C30" },
         { "airline": "OO", "flight_number": "4966", "departure_airport": "SFO", "arrival_airport": "SUN", "departure_time": ISODate("2025-01-02T11:11:00Z"), "arrival_time": ISODate("2025-01-02T14:15:00Z"), "departure_gate": "D39", "arrival_gate": "D21" },
         { "airline": "UA", "flight_number": "753", "departure_airport": "SFO", "arrival_airport": "AUS", "departure_time": ISODate("2025-01-02T11:40:00Z"), "arrival_time": ISODate("2025-01-02T17:33:00Z"), "departure_gate": "B30", "arrival_gate": "D47" },
         { "airline": "UA", "flight_number": "242", "departure_airport": "SFO", "arrival_airport": "SAN", "departure_time": ISODate("2025-01-02T12:00:00Z"), "arrival_time": ISODate("2025-01-02T13:24:00Z"), "departure_gate": "B27", "arrival_gate": "E27" },
         { "airline": "UA", "flight_number": "390", "departure_airport": "SEA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T11:10:00Z"), "arrival_time": ISODate("2025-01-02T13:08:00Z"), "departure_gate": "A17", "arrival_gate": "A23" },
         { "airline": "OO", "flight_number": "6336", "departure_airport": "RNO", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T11:17:00Z"), "arrival_time": ISODate("2025-01-02T12:17:00Z"), "departure_gate": "A45", "arrival_gate": "E39" },
         { "airline": "OO", "flight_number": "5250", "departure_airport": "MRY", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T11:12:00Z"), "arrival_time": ISODate("2025-01-02T12:28:00Z"), "departure_gate": "B33", "arrival_gate": "E11" },
         { "airline": "UA", "flight_number": "317", "departure_airport": "SAN", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T12:10:00Z"), "arrival_time": ISODate("2025-01-02T13:40:00Z"), "departure_gate": "A14", "arrival_gate": "A42" },
         { "airline": "OO", "flight_number": "5652", "departure_airport": "SFO", "arrival_airport": "PSP", "departure_time": ISODate("2025-01-02T12:14:00Z"), "arrival_time": ISODate("2025-01-02T13:50:00Z"), "departure_gate": "E17", "arrival_gate": "B17" },
         { "airline": "UA", "flight_number": "1195", "departure_airport": "SFO", "arrival_airport": "ORD", "departure_time": ISODate("2025-01-02T11:56:00Z"), "arrival_time": ISODate("2025-01-02T18:12:00Z"), "departure_gate": "B39", "arrival_gate": "B19" },
         { "airline": "CY", "flight_number": "714", "departure_airport": "SFO", "arrival_airport": "DAL", "departure_time": ISODate("2025-01-02T11:40:00Z"), "arrival_time": ISODate("2025-01-02T17:22:00Z"), "departure_gate": "C50", "arrival_gate": "A19" },
         { "airline": "WN", "flight_number": "2779", "departure_airport": "LAX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T11:58:00Z"), "arrival_time": ISODate("2025-01-02T13:09:00Z"), "departure_gate": "B19", "arrival_gate": "C27" },
         { "airline": "UA", "flight_number": "1722", "departure_airport": "SFO", "arrival_airport": "IAH", "departure_time": ISODate("2025-01-02T11:58:00Z"), "arrival_time": ISODate("2025-01-02T18:29:00Z"), "departure_gate": "E12", "arrival_gate": "D6" },
         { "airline": "UA", "flight_number": "766", "departure_airport": "JFK", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T11:55:00Z"), "arrival_time": ISODate("2025-01-02T15:21:00Z"), "departure_gate": "A16", "arrival_gate": "C18" },
         { "airline": "UA", "flight_number": "1437", "departure_airport": "ORD", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T12:36:00Z"), "arrival_time": ISODate("2025-01-02T15:09:00Z"), "departure_gate": "A33", "arrival_gate": "E19" },
         { "airline": "UA", "flight_number": "1294", "departure_airport": "LAS", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T12:20:00Z"), "arrival_time": ISODate("2025-01-02T13:45:00Z"), "departure_gate": "E7", "arrival_gate": "A10" },
         { "airline": "UA", "flight_number": "1266", "departure_airport": "SEA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T12:13:00Z"), "arrival_time": ISODate("2025-01-02T14:11:00Z"), "departure_gate": "B32", "arrival_gate": "C18" },
         { "airline": "UA", "flight_number": "1668", "departure_airport": "SFO", "arrival_airport": "EWR", "departure_time": ISODate("2025-01-02T12:24:00Z"), "arrival_time": ISODate("2025-01-02T20:34:00Z"), "departure_gate": "D37", "arrival_gate": "A30" },
         { "airline": "OO", "flight_number": "6304", "departure_airport": "BUR", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T12:31:00Z"), "arrival_time": ISODate("2025-01-02T14:01:00Z"), "departure_gate": "C7", "arrival_gate": "C4" },
         { "airline": "WN", "flight_number": "4391", "departure_airport": "SFO", "arrival_airport": "STL", "departure_time": ISODate("2025-01-02T12:55:00Z"), "arrival_time": ISODate("2025-01-02T18:36:00Z"), "departure_gate": "A12", "arrival_gate": "D39" },
         { "airline": "UA", "flight_number": "236", "departure_airport": "HNL", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T13:19:00Z"), "arrival_time": ISODate("2025-01-02T20:12:00Z"), "departure_gate": "B25", "arrival_gate": "D26" },
         { "airline": "UA", "flight_number": "1705", "departure_airport": "SFO", "arrival_airport": "IAH", "departure_time": ISODate("2025-01-02T12:51:00Z"), "arrival_time": ISODate("2025-01-02T18:50:00Z"), "departure_gate": "E11", "arrival_gate": "E32" },
         { "airline": "OO", "flight_number": "6490", "departure_airport": "EUG", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T13:00:00Z"), "arrival_time": ISODate("2025-01-02T14:21:00Z"), "departure_gate": "D34", "arrival_gate": "D29" },
         { "airline": "UA", "flight_number": "820", "departure_airport": "SFO", "arrival_airport": "ORD", "departure_time": ISODate("2025-01-02T13:02:00Z"), "arrival_time": ISODate("2025-01-02T19:11:00Z"), "departure_gate": "B45", "arrival_gate": "E24" },
         { "airline": "AS", "flight_number": "381", "departure_airport": "SFO", "arrival_airport": "PDX", "departure_time": ISODate("2025-01-02T12:52:00Z"), "arrival_time": ISODate("2025-01-02T14:34:00Z"), "departure_gate": "E11", "arrival_gate": "B3" },
         { "airline": "AS", "flight_number": "305", "departure_airport": "SFO", "arrival_airport": "SEA", "departure_time": ISODate("2025-01-02T12:59:00Z"), "arrival_time": ISODate("2025-01-02T15:10:00Z"), "departure_gate": "C34", "arrival_gate": "C41" },
         { "airline": "OO", "flight_number": "6273", "departure_airport": "SFO", "arrival_airport": "SLC", "departure_time": ISODate("2025-01-02T12:57:00Z"), "arrival_time": ISODate("2025-01-02T15:50:00Z"), "departure_gate": "C3", "arrival_gate": "D36" },
         { "airline": "DL", "flight_number": "2254", "departure_airport": "SFO", "arrival_airport": "DTW", "departure_time": ISODate("2025-01-02T13:05:00Z"), "arrival_time": ISODate("2025-01-02T20:29:00Z"), "departure_gate": "E10", "arrival_gate": "D30" },
         { "airline": "B6", "flight_number": "1435", "departure_airport": "SFO", "arrival_airport": "LGB", "departure_time": ISODate("2025-01-02T13:34:00Z"), "arrival_time": ISODate("2025-01-02T15:02:00Z"), "departure_gate": "B31", "arrival_gate": "D48" },
         { "airline": "F9", "flight_number": "661", "departure_airport": "DEN", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T13:11:00Z"), "arrival_time": ISODate("2025-01-02T14:35:00Z"), "departure_gate": "C3", "arrival_gate": "E38" },
         { "airline": "UA", "flight_number": "1092", "departure_airport": "EWR", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T13:44:00Z"), "arrival_time": ISODate("2025-01-02T17:05:00Z"), "departure_gate": "D13", "arrival_gate": "A41" },
         { "airline": "US", "flight_number": "1812", "departure_airport": "SFO", "arrival_airport": "CLT", "departure_time": ISODate("2025-01-02T13:32:00Z"), "arrival_time": ISODate("2025-01-02T21:36:00Z"), "departure_gate": "A50", "arrival_gate": "A5" },
         { "airline": "WN", "flight_number": "2598", "departure_airport": "LAX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T13:48:00Z"), "arrival_time": ISODate("2025-01-02T14:54:00Z"), "departure_gate": "E23", "arrival_gate": "C38" },
         { "airline": "UA", "flight_number": "216", "departure_airport": "SFO", "arrival_airport": "SNA", "departure_time": ISODate("2025-01-02T15:23:00Z"), "arrival_time": ISODate("2025-01-02T16:41:00Z"), "departure_gate": "C23", "arrival_gate": "E6" },
         { "airline": "UA", "flight_number": "1060", "departure_airport": "SFO", "arrival_airport": "DCA", "departure_time": ISODate("2025-01-02T15:19:00Z"), "arrival_time": ISODate("2025-01-02T23:18:00Z"), "departure_gate": "D14", "arrival_gate": "B18" },
         { "airline": "OO", "flight_number": "6326", "departure_airport": "BOI", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T13:51:00Z"), "arrival_time": ISODate("2025-01-02T14:24:00Z"), "departure_gate": "D49", "arrival_gate": "A43" },
         { "airline": "UA", "flight_number": "724", "departure_airport": "HNL", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T14:43:00Z"), "arrival_time": ISODate("2025-01-02T21:33:00Z"), "departure_gate": "B26", "arrival_gate": "A50" },
         { "airline": "OO", "flight_number": "5463", "departure_airport": "SFO", "arrival_airport": "SMF", "departure_time": ISODate("2025-01-02T13:50:00Z"), "arrival_time": ISODate("2025-01-02T14:32:00Z"), "departure_gate": "A13", "arrival_gate": "D23" },
         { "airline": "UA", "flight_number": "698", "departure_airport": "SFO", "arrival_airport": "MCO", "departure_time": ISODate("2025-01-02T14:24:00Z"), "arrival_time": ISODate("2025-01-02T22:33:00Z"), "departure_gate": "D49", "arrival_gate": "B2" },
         { "airline": "CY", "flight_number": "1178", "departure_airport": "SFO", "arrival_airport": "EWR", "departure_time": ISODate("2025-01-02T13:58:00Z"), "arrival_time": ISODate("2025-01-02T22:06:00Z"), "departure_gate": "C27", "arrival_gate": "D9" },
         { "airline": "OO", "flight_number": "6425", "departure_airport": "TUS", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T14:50:00Z"), "arrival_time": ISODate("2025-01-02T15:54:00Z"), "departure_gate": "E29", "arrival_gate": "D17" },
         { "airline": "OO", "flight_number": "5615", "departure_airport": "MFR", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T13:55:00Z"), "arrival_time": ISODate("2025-01-02T15:15:00Z"), "departure_gate": "B44", "arrival_gate": "E27" },
         { "airline": "WN", "flight_number": "3450", "departure_airport": "SFO", "arrival_airport": "MDW", "departure_time": ISODate("2025-01-02T14:50:00Z"), "arrival_time": ISODate("2025-01-02T20:46:00Z"), "departure_gate": "D39", "arrival_gate": "B44" },
         { "airline": "UA", "flight_number": "1733", "departure_airport": "SFO", "arrival_airport": "DEN", "departure_time": ISODate("2025-01-02T15:11:00Z"), "arrival_time": ISODate("2025-01-02T18:47:00Z"), "departure_gate": "D8", "arrival_gate": "D2" },
         { "airline": "UA", "flight_number": "1263", "departure_airport": "KOA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T14:59:00Z"), "arrival_time": ISODate("2025-01-02T21:49:00Z"), "departure_gate": "C39", "arrival_gate": "E3" },
         { "airline": "UA", "flight_number": "1568", "departure_airport": "SFO", "arrival_airport": "RDU", "departure_time": ISODate("2025-01-02T14:55:00Z"), "arrival_time": ISODate("2025-01-02T23:03:00Z"), "departure_gate": "A30", "arrival_gate": "A26" },
         { "airline": "UA", "flight_number": "1159", "departure_airport": "SFO", "arrival_airport": "BOS", "departure_time": ISODate("2025-01-02T14:57:00Z"), "arrival_time": ISODate("2025-01-02T23:23:00Z"), "departure_gate": "C19", "arrival_gate": "A30" },
         { "airline": "OO", "flight_number": "5652", "departure_airport": "PSP", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T14:52:00Z"), "arrival_time": ISODate("2025-01-02T16:46:00Z"), "departure_gate": "D37", "arrival_gate": "A5" },
         { "airline": "US", "flight_number": "749", "departure_airport": "CLT", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T15:28:00Z"), "arrival_time": ISODate("2025-01-02T17:47:00Z"), "departure_gate": "D17", "arrival_gate": "D38" },
         { "airline": "UA", "flight_number": "1491", "departure_airport": "SFO", "arrival_airport": "DEN", "departure_time": ISODate("2025-01-02T15:09:00Z"), "arrival_time": ISODate("2025-01-02T18:45:00Z"), "departure_gate": "E31", "arrival_gate": "E36" },
         { "airline": "WN", "flight_number": "2687", "departure_airport": "SFO", "arrival_airport": "LAX", "departure_time": ISODate("2025-01-02T15:27:00Z"), "arrival_time": ISODate("2025-01-02T16:31:00Z"), "departure_gate": "E42", "arrival_gate": "B13" },
         { "airline": "DL", "flight_number": "2040", "departure_airport": "SFO", "arrival_airport": "JFK", "departure_time": ISODate("2025-01-02T15:09:00Z"), "arrival_time": ISODate("2025-01-02T23:20:00Z"), "departure_gate": "E2", "arrival_gate": "D33" },
         { "airline": "OO", "flight_number": "5549", "departure_airport": "SFO", "arrival_airport": "AUS", "departure_time": ISODate("2025-01-02T15:24:00Z"), "arrival_time": ISODate("2025-01-02T21:11:00Z"), "departure_gate": "B42", "arrival_gate": "C1" },
         { "airline": "AS", "flight_number": "308", "departure_airport": "SEA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T15:22:00Z"), "arrival_time": ISODate("2025-01-02T17:18:00Z"), "departure_gate": "C39", "arrival_gate": "A46" },
         { "airline": "F9", "flight_number": "662", "departure_airport": "SFO", "arrival_airport": "DEN", "departure_time": ISODate("2025-01-02T15:16:00Z"), "arrival_time": ISODate("2025-01-02T18:50:00Z"), "departure_gate": "C5", "arrival_gate": "A8" },
         { "airline": "UA", "flight_number": "735", "departure_airport": "DEN", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T16:00:00Z"), "arrival_time": ISODate("2025-01-02T17:19:00Z"), "departure_gate": "A32", "arrival_gate": "C24" },
         { "airline": "UA", "flight_number": "404", "departure_airport": "IAH", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T17:26:00Z"), "arrival_time": ISODate("2025-01-02T19:32:00Z"), "departure_gate": "C14", "arrival_gate": "A7" },
         { "airline": "CY", "flight_number": "210", "departure_airport": "SFO", "arrival_airport": "ORD", "departure_time": ISODate("2025-01-02T15:42:00Z"), "arrival_time": ISODate("2025-01-02T21:44:00Z"), "departure_gate": "A31", "arrival_gate": "B46" },
         { "airline": "AS", "flight_number": "315", "departure_airport": "SFO", "arrival_airport": "SEA", "departure_time": ISODate("2025-01-02T19:47:00Z"), "arrival_time": ISODate("2025-01-02T22:16:00Z"), "departure_gate": "A8", "arrival_gate": "B49" },
         { "airline": "WN", "flight_number": "1901", "departure_airport": "SAN", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T15:48:00Z"), "arrival_time": ISODate("2025-01-02T17:09:00Z"), "departure_gate": "A23", "arrival_gate": "B38" },
         { "airline": "OO", "flight_number": "5580", "departure_airport": "SFO", "arrival_airport": "SNA", "departure_time": ISODate("2025-01-02T16:35:00Z"), "arrival_time": ISODate("2025-01-02T18:03:00Z"), "departure_gate": "D40", "arrival_gate": "E43" },
         { "airline": "AA", "flight_number": "2265", "departure_airport": "DFW", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T16:07:00Z"), "arrival_time": ISODate("2025-01-02T17:41:00Z"), "departure_gate": "A4", "arrival_gate": "A23" },
         { "airline": "OO", "flight_number": "5363", "departure_airport": "SFO", "arrival_airport": "ONT", "departure_time": ISODate("2025-01-02T16:15:00Z"), "arrival_time": ISODate("2025-01-02T17:32:00Z"), "departure_gate": "A10", "arrival_gate": "A26" },
         { "airline": "OO", "flight_number": "5609", "departure_airport": "SFO", "arrival_airport": "PDX", "departure_time": ISODate("2025-01-02T17:01:00Z"), "arrival_time": ISODate("2025-01-02T18:42:00Z"), "departure_gate": "E49", "arrival_gate": "D4" },
         { "airline": "OO", "flight_number": "5645", "departure_airport": "MFR", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T16:15:00Z"), "arrival_time": ISODate("2025-01-02T17:35:00Z"), "departure_gate": "A25", "arrival_gate": "E49" },
         { "airline": "OO", "flight_number": "4976", "departure_airport": "SFO", "arrival_airport": "STL", "departure_time": ISODate("2025-01-02T16:37:00Z"), "arrival_time": ISODate("2025-01-02T22:27:00Z"), "departure_gate": "C35", "arrival_gate": "A2" },
         { "airline": "OO", "flight_number": "6217", "departure_airport": "BUR", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T16:44:00Z"), "arrival_time": ISODate("2025-01-02T17:55:00Z"), "departure_gate": "D50", "arrival_gate": "A14" },
         { "airline": "WN", "flight_number": "1276", "departure_airport": "SFO", "arrival_airport": "LAX", "departure_time": ISODate("2025-01-02T16:25:00Z"), "arrival_time": ISODate("2025-01-02T17:32:00Z"), "departure_gate": "B8", "arrival_gate": "D22" },
         { "airline": "OO", "flight_number": "6238", "departure_airport": "ACV", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T16:25:00Z"), "arrival_time": ISODate("2025-01-02T17:36:00Z"), "departure_gate": "E24", "arrival_gate": "A39" },
         { "airline": "OO", "flight_number": "5190", "departure_airport": "SFO", "arrival_airport": "ASE", "departure_time": ISODate("2025-01-02T17:08:00Z"), "arrival_time": ISODate("2025-01-02T20:17:00Z"), "departure_gate": "C9", "arrival_gate": "E6" },
         { "airline": "OO", "flight_number": "4627", "departure_airport": "SFO", "arrival_airport": "SLC", "departure_time": ISODate("2025-01-02T16:43:00Z"), "arrival_time": ISODate("2025-01-02T19:41:00Z"), "departure_gate": "C32", "arrival_gate": "C4" },
         { "airline": "OO", "flight_number": "6476", "departure_airport": "SFO", "arrival_airport": "MFR", "departure_time": ISODate("2025-01-02T16:38:00Z"), "arrival_time": ISODate("2025-01-02T18:16:00Z"), "departure_gate": "B26", "arrival_gate": "D33" },
         { "airline": "UA", "flight_number": "486", "departure_airport": "SFO", "arrival_airport": "LAS", "departure_time": ISODate("2025-01-02T16:52:00Z"), "arrival_time": ISODate("2025-01-02T18:24:00Z"), "departure_gate": "D25", "arrival_gate": "E8" },
         { "airline": "DL", "flight_number": "214", "departure_airport": "SFO", "arrival_airport": "DTW", "departure_time": ISODate("2025-01-02T19:09:00Z"), "arrival_time": ISODate("2025-01-03T02:20:00Z"), "departure_gate": "C6", "arrival_gate": "E35" },
         { "airline": "CY", "flight_number": "592", "departure_airport": "SFO", "arrival_airport": "PSP", "departure_time": ISODate("2025-01-02T16:54:00Z"), "arrival_time": ISODate("2025-01-02T18:14:00Z"), "departure_gate": "B40", "arrival_gate": "B9" },
         { "airline": "UA", "flight_number": "529", "departure_airport": "SNA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T17:01:00Z"), "arrival_time": ISODate("2025-01-02T18:15:00Z"), "departure_gate": "D28", "arrival_gate": "B30" },
         { "airline": "UA", "flight_number": "372", "departure_airport": "MSP", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T17:39:00Z"), "arrival_time": ISODate("2025-01-02T19:19:00Z"), "departure_gate": "E28", "arrival_gate": "C18" },
         { "airline": "AA", "flight_number": "1213", "departure_airport": "SFO", "arrival_airport": "DFW", "departure_time": ISODate("2025-01-02T18:20:00Z"), "arrival_time": ISODate("2025-01-03T00:19:00Z"), "departure_gate": "E39", "arrival_gate": "A42" },
         { "airline": "AS", "flight_number": "341", "departure_airport": "PSP", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T17:15:00Z"), "arrival_time": ISODate("2025-01-02T18:37:00Z"), "departure_gate": "D40", "arrival_gate": "D15" },
         { "airline": "OO", "flight_number": "5418", "departure_airport": "SBP", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T18:11:00Z"), "arrival_time": ISODate("2025-01-02T19:09:00Z"), "departure_gate": "C31", "arrival_gate": "D39" },
         { "airline": "CY", "flight_number": "193", "departure_airport": "EWR", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T17:29:00Z"), "arrival_time": ISODate("2025-01-02T20:59:00Z"), "departure_gate": "E20", "arrival_gate": "E40" },
         { "airline": "UA", "flight_number": "1723", "departure_airport": "SFO", "arrival_airport": "KOA", "departure_time": ISODate("2025-01-02T17:26:00Z"), "arrival_time": ISODate("2025-01-02T21:02:00Z"), "departure_gate": "E18", "arrival_gate": "D41" },
         { "airline": "UA", "flight_number": "1762", "departure_airport": "SFO", "arrival_airport": "IAH", "departure_time": ISODate("2025-01-02T17:37:00Z"), "arrival_time": ISODate("2025-01-02T23:11:00Z"), "departure_gate": "C40", "arrival_gate": "C37" },
         { "airline": "CY", "flight_number": "720", "departure_airport": "SFO", "arrival_airport": "DAL", "departure_time": ISODate("2025-01-02T17:23:00Z"), "arrival_time": ISODate("2025-01-02T22:47:00Z"), "departure_gate": "D13", "arrival_gate": "D23" },
         { "airline": "CY", "flight_number": "963", "departure_airport": "SAN", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T17:36:00Z"), "arrival_time": ISODate("2025-01-02T19:05:00Z"), "departure_gate": "B1", "arrival_gate": "E32" },
         { "airline": "OO", "flight_number": "5255", "departure_airport": "SFO", "arrival_airport": "EUG", "departure_time": ISODate("2025-01-02T17:27:00Z"), "arrival_time": ISODate("2025-01-02T19:02:00Z"), "departure_gate": "C7", "arrival_gate": "B2" },
         { "airline": "CY", "flight_number": "960", "departure_airport": "SFO", "arrival_airport": "SAN", "departure_time": ISODate("2025-01-02T17:32:00Z"), "arrival_time": ISODate("2025-01-02T18:50:00Z"), "departure_gate": "C3", "arrival_gate": "C4" },
         { "airline": "UA", "flight_number": "1419", "departure_airport": "MSY", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T17:46:00Z"), "arrival_time": ISODate("2025-01-02T20:07:00Z"), "departure_gate": "C26", "arrival_gate": "E49" },
         { "airline": "WN", "flight_number": "1585", "departure_airport": "SFO", "arrival_airport": "LAX", "departure_time": ISODate("2025-01-02T17:46:00Z"), "arrival_time": ISODate("2025-01-02T19:31:00Z"), "departure_gate": "A12", "arrival_gate": "A12" },
         { "airline": "DL", "flight_number": "1505", "departure_airport": "MSP", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T17:47:00Z"), "arrival_time": ISODate("2025-01-02T19:48:00Z"), "departure_gate": "A33", "arrival_gate": "B37" },
         { "airline": "US", "flight_number": "686", "departure_airport": "PHX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T17:59:00Z"), "arrival_time": ISODate("2025-01-02T19:05:00Z"), "departure_gate": "C28", "arrival_gate": "C11" },
         { "airline": "AS", "flight_number": "302", "departure_airport": "SEA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T18:00:00Z"), "arrival_time": ISODate("2025-01-02T20:04:00Z"), "departure_gate": "B28", "arrival_gate": "E17" },
         { "airline": "UA", "flight_number": "1552", "departure_airport": "RDU", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T18:08:00Z"), "arrival_time": ISODate("2025-01-02T20:51:00Z"), "departure_gate": "B15", "arrival_gate": "D48" },
         { "airline": "UA", "flight_number": "697", "departure_airport": "LAS", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T17:55:00Z"), "arrival_time": ISODate("2025-01-02T19:14:00Z"), "departure_gate": "E37", "arrival_gate": "B31" },
         { "airline": "AA", "flight_number": "219", "departure_airport": "LAX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T17:54:00Z"), "arrival_time": ISODate("2025-01-02T19:05:00Z"), "departure_gate": "C27", "arrival_gate": "E34" },
         { "airline": "OO", "flight_number": "5425", "departure_airport": "ONT", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T18:04:00Z"), "arrival_time": ISODate("2025-01-02T19:23:00Z"), "departure_gate": "C46", "arrival_gate": "A14" },
         { "airline": "WN", "flight_number": "1861", "departure_airport": "SFO", "arrival_airport": "PHX", "departure_time": ISODate("2025-01-02T20:49:00Z"), "arrival_time": ISODate("2025-01-02T23:31:00Z"), "departure_gate": "C31", "arrival_gate": "B42" },
         { "airline": "OO", "flight_number": "5631", "departure_airport": "SFO", "arrival_airport": "BUR", "departure_time": ISODate("2025-01-02T18:10:00Z"), "arrival_time": ISODate("2025-01-02T19:29:00Z"), "departure_gate": "D26", "arrival_gate": "E29" },
         { "airline": "UA", "flight_number": "720", "departure_airport": "SFO", "arrival_airport": "AUS", "departure_time": ISODate("2025-01-02T18:13:00Z"), "arrival_time": ISODate("2025-01-02T23:41:00Z"), "departure_gate": "E10", "arrival_gate": "D1" },
         { "airline": "UA", "flight_number": "1581", "departure_airport": "SFO", "arrival_airport": "OGG", "departure_time": ISODate("2025-01-02T18:15:00Z"), "arrival_time": ISODate("2025-01-02T22:06:00Z"), "departure_gate": "B40", "arrival_gate": "E18" },
         { "airline": "OO", "flight_number": "5227", "departure_airport": "SFO", "arrival_airport": "SAN", "departure_time": ISODate("2025-01-02T18:26:00Z"), "arrival_time": ISODate("2025-01-02T19:59:00Z"), "departure_gate": "E33", "arrival_gate": "E50" },
         { "airline": "CY", "flight_number": "941", "departure_airport": "LAX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T18:24:00Z"), "arrival_time": ISODate("2025-01-02T19:39:00Z"), "departure_gate": "D4", "arrival_gate": "A22" },
         { "airline": "AA", "flight_number": "1459", "departure_airport": "ORD", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T18:21:00Z"), "arrival_time": ISODate("2025-01-02T21:11:00Z"), "departure_gate": "D42", "arrival_gate": "B25" },
         { "airline": "OO", "flight_number": "5442", "departure_airport": "SFO", "arrival_airport": "RDD", "departure_time": ISODate("2025-01-02T18:19:00Z"), "arrival_time": ISODate("2025-01-02T19:35:00Z"), "departure_gate": "E21", "arrival_gate": "B9" },
         { "airline": "AA", "flight_number": "69", "departure_airport": "MIA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T18:31:00Z"), "arrival_time": ISODate("2025-01-02T21:33:00Z"), "departure_gate": "B11", "arrival_gate": "B15" },
         { "airline": "OO", "flight_number": "6220", "departure_airport": "DFW", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T19:01:00Z"), "arrival_time": ISODate("2025-01-02T20:40:00Z"), "departure_gate": "D35", "arrival_gate": "E4" },
         { "airline": "UA", "flight_number": "1670", "departure_airport": "SFO", "arrival_airport": "HNL", "departure_time": ISODate("2025-01-02T18:42:00Z"), "arrival_time": ISODate("2025-01-02T22:52:00Z"), "departure_gate": "A15", "arrival_gate": "C18" },
         { "airline": "DL", "flight_number": "435", "departure_airport": "JFK", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T18:57:00Z"), "arrival_time": ISODate("2025-01-02T22:25:00Z"), "departure_gate": "D35", "arrival_gate": "C33" },
         { "airline": "UA", "flight_number": "508", "departure_airport": "SEA", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T19:01:00Z"), "arrival_time": ISODate("2025-01-02T21:05:00Z"), "departure_gate": "C16", "arrival_gate": "B8" },
         { "airline": "UA", "flight_number": "1523", "departure_airport": "BOS", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T21:19:00Z"), "arrival_time": ISODate("2025-01-03T01:19:00Z"), "departure_gate": "E7", "arrival_gate": "B32" },
         { "airline": "CY", "flight_number": "593", "departure_airport": "PSP", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T19:03:00Z"), "arrival_time": ISODate("2025-01-02T20:21:00Z"), "departure_gate": "C13", "arrival_gate": "A47" },
         { "airline": "UA", "flight_number": "741", "departure_airport": "ORD", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T19:44:00Z"), "arrival_time": ISODate("2025-01-02T22:14:00Z"), "departure_gate": "A16", "arrival_gate": "C32" },
         { "airline": "WN", "flight_number": "3414", "departure_airport": "SFO", "arrival_airport": "SAN", "departure_time": ISODate("2025-01-02T19:43:00Z"), "arrival_time": ISODate("2025-01-02T21:10:00Z"), "departure_gate": "E3", "arrival_gate": "D46" },
         { "airline": "UA", "flight_number": "404", "departure_airport": "SFO", "arrival_airport": "PDX", "departure_time": ISODate("2025-01-02T19:42:00Z"), "arrival_time": ISODate("2025-01-02T21:24:00Z"), "departure_gate": "B48", "arrival_gate": "A30" },
         { "airline": "UA", "flight_number": "637", "departure_airport": "SFO", "arrival_airport": "SNA", "departure_time": ISODate("2025-01-02T19:32:00Z"), "arrival_time": ISODate("2025-01-02T20:49:00Z"), "departure_gate": "D40", "arrival_gate": "A23" },
         { "airline": "OO", "flight_number": "5573", "departure_airport": "SAT", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T21:13:00Z"), "arrival_time": ISODate("2025-01-02T22:57:00Z"), "departure_gate": "D34", "arrival_gate": "E33" },
         { "airline": "AA", "flight_number": "219", "departure_airport": "SFO", "arrival_airport": "LAX", "departure_time": ISODate("2025-01-02T20:03:00Z"), "arrival_time": ISODate("2025-01-02T22:00:00Z"), "departure_gate": "E27", "arrival_gate": "D38" },
         { "airline": "OO", "flight_number": "5600", "departure_airport": "BUR", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T19:55:00Z"), "arrival_time": ISODate("2025-01-02T21:21:00Z"), "departure_gate": "A7", "arrival_gate": "A27" },
         { "airline": "CY", "flight_number": "947", "departure_airport": "LAX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T20:38:00Z"), "arrival_time": ISODate("2025-01-02T22:06:00Z"), "departure_gate": "D28", "arrival_gate": "C15" },
         { "airline": "WN", "flight_number": "138", "departure_airport": "SFO", "arrival_airport": "LAS", "departure_time": ISODate("2025-01-02T20:26:00Z"), "arrival_time": ISODate("2025-01-02T21:49:00Z"), "departure_gate": "B35", "arrival_gate": "E31" },
         { "airline": "OO", "flight_number": "5302", "departure_airport": "SFO", "arrival_airport": "PSC", "departure_time": ISODate("2025-01-02T20:29:00Z"), "arrival_time": ISODate("2025-01-02T22:28:00Z"), "departure_gate": "C9", "arrival_gate": "A15" },
         { "airline": "CY", "flight_number": "748", "departure_airport": "SFO", "arrival_airport": "SEA", "departure_time": ISODate("2025-01-02T20:46:00Z"), "arrival_time": ISODate("2025-01-02T23:17:00Z"), "departure_gate": "D7", "arrival_gate": "E25" },
         { "airline": "UA", "flight_number": "236", "departure_airport": "SFO", "arrival_airport": "EWR", "departure_time": ISODate("2025-01-02T20:41:00Z"), "arrival_time": ISODate("2025-01-03T05:04:00Z"), "departure_gate": "D12", "arrival_gate": "B47" },
         { "airline": "OO", "flight_number": "6503", "departure_airport": "SFO", "arrival_airport": "EUG", "departure_time": ISODate("2025-01-02T20:54:00Z"), "arrival_time": ISODate("2025-01-02T22:27:00Z"), "departure_gate": "A50", "arrival_gate": "E49" },
         { "airline": "WN", "flight_number": "1174", "departure_airport": "LAS", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T20:58:00Z"), "arrival_time": ISODate("2025-01-02T22:19:00Z"), "departure_gate": "C42", "arrival_gate": "D33" },
         { "airline": "AS", "flight_number": "744", "departure_airport": "SFO", "arrival_airport": "SLC", "departure_time": ISODate("2025-01-02T20:52:00Z"), "arrival_time": ISODate("2025-01-02T23:33:00Z"), "departure_gate": "B11", "arrival_gate": "A39" },
         { "airline": "WN", "flight_number": "4992", "departure_airport": "SFO", "arrival_airport": "PHX", "departure_time": ISODate("2025-01-02T21:49:00Z"), "arrival_time": ISODate("2025-01-03T00:32:00Z"), "departure_gate": "D19", "arrival_gate": "E15" },
         { "airline": "UA", "flight_number": "469", "departure_airport": "EWR", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T23:07:00Z"), "arrival_time": ISODate("2025-01-03T02:27:00Z"), "departure_gate": "E3", "arrival_gate": "D19" },
         { "airline": "UA", "flight_number": "1163", "departure_airport": "SFO", "arrival_airport": "EWR", "departure_time": ISODate("2025-01-02T21:44:00Z"), "arrival_time": ISODate("2025-01-03T05:45:00Z"), "departure_gate": "D19", "arrival_gate": "C17" },
         { "airline": "DL", "flight_number": "2337", "departure_airport": "SFO", "arrival_airport": "ATL", "departure_time": ISODate("2025-01-02T21:44:00Z"), "arrival_time": ISODate("2025-01-03T05:23:00Z"), "departure_gate": "B4", "arrival_gate": "A39" },
         { "airline": "OO", "flight_number": "6432", "departure_airport": "SFO", "arrival_airport": "EUG", "departure_time": ISODate("2025-01-02T22:24:00Z"), "arrival_time": ISODate("2025-01-02T23:57:00Z"), "departure_gate": "E11", "arrival_gate": "A4" },
         { "airline": "US", "flight_number": "898", "departure_airport": "SFO", "arrival_airport": "CLT", "departure_time": ISODate("2025-01-02T22:24:00Z"), "arrival_time": ISODate("2025-01-03T06:16:00Z"), "departure_gate": "A45", "arrival_gate": "A24" },
         { "airline": "UA", "flight_number": "292", "departure_airport": "SFO", "arrival_airport": "MCO", "departure_time": ISODate("2025-01-02T22:30:00Z"), "arrival_time": ISODate("2025-01-03T06:37:00Z"), "departure_gate": "C7", "arrival_gate": "C5" },
         { "airline": "OO", "flight_number": "5600", "departure_airport": "SFO", "arrival_airport": "MFR", "departure_time": ISODate("2025-01-02T22:36:00Z"), "arrival_time": ISODate("2025-01-03T00:01:00Z"), "departure_gate": "E42", "arrival_gate": "E38" },
         { "airline": "UA", "flight_number": "263", "departure_airport": "LAX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T22:48:00Z"), "arrival_time": ISODate("2025-01-03T00:04:00Z"), "departure_gate": "B22", "arrival_gate": "E27" },
         { "airline": "OO", "flight_number": "5414", "departure_airport": "SFO", "arrival_airport": "RDM", "departure_time": ISODate("2025-01-02T22:32:00Z"), "arrival_time": ISODate("2025-01-03T00:12:00Z"), "departure_gate": "A46", "arrival_gate": "C18" },
         { "airline": "UA", "flight_number": "1241", "departure_airport": "SFO", "arrival_airport": "EWR", "departure_time": ISODate("2025-01-02T23:22:00Z"), "arrival_time": ISODate("2025-01-03T07:44:00Z"), "departure_gate": "A28", "arrival_gate": "E27" },
         { "airline": "UA", "flight_number": "522", "departure_airport": "SFO", "arrival_airport": "PDX", "departure_time": ISODate("2025-01-02T22:55:00Z"), "arrival_time": ISODate("2025-01-03T00:42:00Z"), "departure_gate": "A10", "arrival_gate": "E39" },
         { "airline": "UA", "flight_number": "724", "departure_airport": "SFO", "arrival_airport": "ORD", "departure_time": ISODate("2025-01-02T23:05:00Z"), "arrival_time": ISODate("2025-01-03T05:20:00Z"), "departure_gate": "B40", "arrival_gate": "D23" },
         { "airline": "UA", "flight_number": "156", "departure_airport": "SFO", "arrival_airport": "MSY", "departure_time": ISODate("2025-01-02T23:22:00Z"), "arrival_time": ISODate("2025-01-03T05:24:00Z"), "departure_gate": "C40", "arrival_gate": "A9" },
         { "airline": "CY", "flight_number": "358", "departure_airport": "SFO", "arrival_airport": "BOS", "departure_time": ISODate("2025-01-02T22:52:00Z"), "arrival_time": ISODate("2025-01-03T07:31:00Z"), "departure_gate": "B23", "arrival_gate": "A44" },
         { "airline": "DL", "flight_number": "1370", "departure_airport": "SFO", "arrival_airport": "JFK", "departure_time": ISODate("2025-01-02T23:04:00Z"), "arrival_time": ISODate("2025-01-03T07:36:00Z"), "departure_gate": "E10", "arrival_gate": "A49" },
         { "airline": "UA", "flight_number": "1729", "departure_airport": "SFO", "arrival_airport": "IAD", "departure_time": ISODate("2025-01-02T23:10:00Z"), "arrival_time": ISODate("2025-01-03T07:35:00Z"), "departure_gate": "D32", "arrival_gate": "E42" },
         { "airline": "CY", "flight_number": "34", "departure_airport": "SFO", "arrival_airport": "JFK", "departure_time": ISODate("2025-01-02T23:15:00Z"), "arrival_time": ISODate("2025-01-03T07:54:00Z"), "departure_gate": "D28", "arrival_gate": "E25" },
         { "airline": "DL", "flight_number": "1880", "departure_airport": "SFO", "arrival_airport": "ATL", "departure_time": ISODate("2025-01-02T00:53:00Z"), "arrival_time": ISODate("2025-01-02T08:27:00Z"), "departure_gate": "E2", "arrival_gate": "A29" },
         { "airline": "UA", "flight_number": "1523", "departure_airport": "SFO", "arrival_airport": "EWR", "departure_time": ISODate("2025-01-02T23:39:00Z"), "arrival_time": ISODate("2025-01-03T07:43:00Z"), "departure_gate": "B9", "arrival_gate": "D15" },
         { "airline": "US", "flight_number": "426", "departure_airport": "PHX", "arrival_airport": "SFO", "departure_time": ISODate("2025-01-02T00:18:00Z"), "arrival_time": ISODate("2025-01-02T01:16:00Z"), "departure_gate": "D47", "arrival_gate": "C42" }
         ])




## Create a context set in Firestore Studio

In this section, create a context set named `flights-assistant`. This context set doesn't include any context set file uploaded to it.

  1. In the Google Cloud console, go to the Firestore page.

[Go to Firestore](https://console.cloud.google.com/firestore)

  2. Select a database from the list. The database must be an Enterprise edition database in MongoDB compatibility mode.

  3. In the navigation menu, click **Firestore Studio**. 

  4. In the **Explorer pane** , next to **Context sets** , click **More actions ( more_vert)**.

  5. Click **Create context set**.

  6. In **Context set name** , enter `flights-assistant`.

  7. Click **Create**.




## Test QueryData in Studio

In this section, use the `flights-assistant` context set by asking natural language questions to generate a MQL query. Since the context set doesn't have any context set file uploaded to it, even after asking a question with context such as `nighttime traffic`, QueryData generates a sub-optimal query.

  1. In the **Explorer pane** , next to your context set, click **More actions ( more_vert)**.
  2. Click **Test context set**.
  3. In the query editor, click **Generate MQL using QueryData with: flights-assistant**.
  4. Enter the following natural language question to generate a MQL query, and click **Generate**.
         
         Find flights from SFO to JFK.
         

Review the MQL query. Notice that QueryData generates the correct MQL for this unambiguous question.
         
         db.flights.find({"departure_airport": "SFO", "arrival_airport": "JFK"})
         

  5. In the **Generate MQL using QueryData with: flights-assistant** window, click **Edit**.

  6. Enter the following natural language question to generate a MQL query, and click **Update**.
         
         Tell me flights that can help me beat nighttime traffic if traveling from New York
         

The database fails to understand the term `nighttime` traffic. This might prevent it from generating a MQL query or cause it to generate a query that ignores the term, as the following query shows.

**Note:** GenAI models are nondeterministic, meaning the same prompt may yield different responses across separate calls due to the probabilistic nature of the output generation.
         
         // The database schema does not contain information about traffic.
         // Returning all flights departing from New York airports.
         db.flights.find({
           $and: [
             {
               "departure_airport": {"$regex": "New York", "$options": "i"}
             },
             {
               "$or": [
                 {"departure_time": {"$exists": true}},
                 {"arrival_time": {"$exists": true}}
               ]
             }
           ]
         })
         




## Generate context for the context set

In this section, you prepare the environment and create a context file that helps improve the context set's querying capabilities.

### Set up your environment

Before you can start generating context, you must prepare your environment.

To set up your environment, perform the following steps:

  1. Install Antigravity CLI. For more information, see [Get Started with Antigravity CLI](https://antigravity.google/docs/cli/getting-started/).
  2. [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  3. [Set up Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). Run the following commands in your terminal to authenticate and select your project:
         
         gcloud auth application-default login

  4. [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/), a Python package and project manager that is a prerequisite for the context engineering agent. If you don't already have Python on your system, `uv` can install it for you.

  5. [Install the context engineering agent](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/build-context-sets#install-agent):
         
         agy plugin install https://github.com/GoogleCloudPlatform/db-context-enrichment/tree/main/plugin

  6. In your terminal, start the Antigravity CLI.
         
         agy

  7. Set up a database connection for context generation using [MCP Toolbox](https://mcp-toolbox.dev/documentation/introduction/). The connection is defined in the `tools.yaml` configuration file.

To create the `tools.yaml` configuration file in your current directory, enter a prompt such as: 
         
         Help me set up context generation for a Firestore database with MongoDB compatibility.
         

Follow the instructions provided by the skill. For more information about the `tools.yaml` file, see [MCP Toolbox documentation](https://mcp-toolbox.dev/documentation/configuration/).

**Note:** If this connection is not established, the extension returns error messages, such as `Error Discovering tools from mcp_toolbox`, and context generation fails to work.
  8. To reload the configuration after the `tools.yaml` file is created, run the following command in the Antigravity CLI and follow the instruction to reload the toolbox MCP server:
         
         /mcp

     1. Select `db-context-engineering_toolbox`.

     2. Select `Restart`.

  9. Verify that the MCP toolbox and the context engineering agent plugin are connected and ready to use.
         
         /mcp




### Generate template context

In this section, to address the issue from the previous section where QueryData didn't recognize the term `nighttime traffic`, define the term in the context set file as traffic occurring between `5:00 PM` and `7:00 PM`. 

To generate template context, perform the following steps:

  1. Enter the following prompt into the Antigravity CLI:
         
         Generate a template for the question: "Tell me flights that can help me beat nighttime traffic if traveling from New York" with the following MQL query:
         
         db.flights.aggregate([
           {
             "$lookup": {
               "from": "airports",
               "localField": "departure_airport",
               "foreignField": "iata",
               "as": "departure_airport_info",
               "pipeline": [{ "$project": { "_id": 0, "name": 1, "city": 1 } }]
             }
           },
           { "$unwind": { "path": "$departure_airport_info" } },
           {
             "$match": {
               "$expr": {
                 "$and": [
                   { "$eq": ["$departure_airport_info.city", "New York"] },
                   {
                     "$or": [
                       { "$lte": [{ "$hour": "$departure_time" }, 17] },
                       { "$gte": [{ "$hour": "$departure_time" }, 19] }
                     ]
                   }
                 ]
               }
             }
           },
         ])
         

  2. The agent converts your input into a specific format that refines the context set's performance across a wide range of user queries. For more information, see [Context sets overview](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/context-sets-overview#context-sets).

  3. Review the generated query template. You can either save the query template as a new agent context file or append it to an existing agent context file.

  4. Prompt the agent to save the template:
         
         Save it to context_set.json.
         

The agent creates the file in the same directory, with the following content:
         
         {
           "templates": [
             {
               "nl_query": "Tell me flights that can help me beat nighttime traffic if traveling from New York",
               "sql": "db.flights.aggregate([\n  {\n    \"$lookup\": {\n      \"from\": \"airports\",\n      \"localField\": \"departure_airport\",\n      \"foreignField\": \"iata\",\n      \"as\": \"departure_airport_info\",\n      \"pipeline\": [{ \"$project\": { \"_id\": 0, \"name\": 1, \"city\": 1 } }]\n    }\n  },\n  { \"$unwind\": { \"path\": \"$departure_airport_info\" } },\n  {\n    \"$match\": {\n      \"$expr\": {\n        \"$and\": [\n          { \"$eq\": [\"$departure_airport_info.city\", \"New York\"] },\n          {\n            \"$or\": [\n              { \"$lte\": [{ \"$hour\": \"$departure_time\" }, 17] },\n              { \"$gte\": [{ \"$hour\": \"$departure_time\" }, 19] }\n            ]\n          }\n        ]\n      }\n    }\n  }\n])",
               "intent": "Tell me flights that can help me beat nighttime traffic if traveling from New York",
               "manifest": "Tell me flights that can help me beat nighttime traffic if traveling from a given city",
               "parameterized": {
                 "parameterized_sql": "db.flights.aggregate([\n  {\n    \"$lookup\": {\n      \"from\": \"airports\",\n      \"localField\": \"departure_airport\",\n      \"foreignField\": \"iata\",\n      \"as\": \"departure_airport_info\",\n      \"pipeline\": [{ \"$project\": { \"_id\": 0, \"name\": 1, \"city\": 1 } }]\n    }\n  },\n  { \"$unwind\": { \"path\": \"$departure_airport_info\" } },\n  {\n    \"$match\": {\n      \"$expr\": {\n        \"$and\": [\n          { \"$eq\": [\"$departure_airport_info.city\", \"$1\"] },\n          {\n            \"$or\": [\n              { \"$lte\": [{ \"$hour\": \"$departure_time\" }, 17] },\n              { \"$gte\": [{ \"$hour\": \"$departure_time\" }, 19] }\n            ]\n          }\n        ]\n      }\n    }\n  }\n])",
                 "parameterized_intent": "Tell me flights that can help me beat nighttime traffic if traveling from $1"
               }
             }
           ]
         }
         




## Upload the context set file to the QueryData

In this section, you upload the context set file to QueryData, so that it improves the QueryData's MQL generation capabilities on your database.

To upload the context, perform the following steps:

  1. In the Google Cloud console, go to the Firestore page.

[Go to Firestore](https://console.cloud.google.com/firestore)

  2. Select a database from the list. The database must be an Enterprise edition database in MongoDB compatibility mode.

  3. In the navigation menu, click **Firestore Studio**. 

  4. In the **Explorer pane** , next to **Context sets** , click the **Actions** (more_vert) icon.

  5. Click **Edit context set**.

  6. Click **Browse** in the **Upload context set file** section, and select the context set file generated earlier.

  7. Click **Save**.




## Generate MQL query using QueryData

In this section, you use the context set file you uploaded to ask natural language questions. This lets you verify that QueryData correctly understands and applies definitions for terms like `nighttime traffic` and other related phrases.

**Note:** GenAI models are nondeterministic, meaning the same prompt may yield different responses across separate calls due to the probabilistic nature of the output generation.

To generate MQL queries, perform the following steps:

  1. In the **Explorer** pane, next to your context set, click **More actions ( more_vert)**.
  2. Click **Test context set**.
  3. In the query editor, click **Generate MQL using QueryData with: flights-assistant**.
  4. Enter the following natural language question to generate a MQL query, and click **Generate**.
         
         Tell me flights that can help me beat nighttime traffic if traveling from New York
         

The generated MQL query looks similar to the following:
         
         // Tell me flights that can help me beat nighttime traffic if traveling from New York
         db.flights.aggregate([
           {
             "$lookup": {
               "from": "airports",
               "localField": "departure_airport",
               "foreignField": "iata",
               "as": "departure_airport_info",
               "pipeline": [{ "$project": { "_id": 0, "name": 1, "city": 1 } }]
             }
           },
           { "$unwind": { "path": "$departure_airport_info" } },
           {
             "$match": {
               "$expr": {
                 "$and": [
                   { "$eq": ["$departure_airport_info.city", "New York"] },
                   {
                     "$or": [
                       { "$lte": [{ "$hour": "$departure_time" }, 17] },
                       { "$gte": [{ "$hour": "$departure_time" }, 19] }
                     ]
                   }
                 ]
               }
             }
           }
         ])
         

This is the same question you added to QueryData's context. Observe that QueryData can now accurately interpret the term `nighttime traffic`.

Although the context originates from one particular question, QueryData uses it to enhance MQL generation for a wide range of similar questions.

  5. In the **Generate MQL using QueryData with: flights-assistant** window, click **Edit**.

  6. Enter the following similar question to generate a MQL query, and click **Update**.
         
         What are the flights that can help me avoid evening traffic if departing from Boston
         

Since the question replaces the term `nighttime traffic` with a similar term, `evening traffic`, QueryData provides a consistent answer to this question by applying the same interpretation.

The generated MQL query looks similar to the following:
         
         // What are the flights that can help me avoid evening traffic if departing from Boston
         db.flights.aggregate([
           {
             "$lookup": {
               "from": "airports",
               "localField": "departure_airport",
               "foreignField": "iata",
               "as": "departure_airport_info",
               "pipeline": [{ "$project": { "_id": 0, "name": 1, "city": 1 } }]
             }
           },
           { "$unwind": { "path": "$departure_airport_info" } },
           {
             "$match": {
               "$expr": {
                 "$and": [
                   { "$eq": ["$departure_airport_info.city", "Boston"] },
                   {
                     "$or": [
                       { "$lte": [{ "$hour": "$departure_time" }, 17] },
                       { "$gte": [{ "$hour": "$departure_time" }, 19] }
                     ]
                   }
                 ]
               }
             }
           }
         ])
         




## Integrate QueryData with your application

In this section, you create a data agent for a flight-finding application. This data agent provides a conversational interface to the `flights` and `airports` tables you created earlier. It also explains how to create and integrate this data agent into your application using [Agent Development Kit (ADK)](https://github.com/google/adk-python), the Gemini Data Analytics QueryData MCP tool, and a context set to improve quality of the responses.

**Note:** GenAI models are nondeterministic, meaning the same prompt may yield different responses across separate calls due to the probabilistic nature of the output generation.

  1. Download [MCP Toolbox](https://mcp-toolbox.dev/documentation/introduction/#install-toolbox) version 1.14.0 or later. MCP Toolbox exposes the data agent as a tool for applications to connect with. The MCP Toolbox differs from the context engineering agent you installed earlier, which generates context.

  2. Set up [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
         
         gcloud auth application-default login

  3. Find the ID of the context set you created earlier. For more information about how to find the context set ID, see [Find the context set ID](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/inspect-data-agent#find-context-id).

  4. Append the following to the `tools.yaml` configuration to connect to the data agent using the MCP Toolbox. For more information, see [Gemini Data Analytics Source](https://mcp-toolbox.dev/integrations/cloudgda/source/) and [Gemini Data Analytics QueryData tool](https://mcp-toolbox.dev/integrations/cloudgda/tools/cloud-gda-query/).
         
         kind: source
         name: gda-api-source
         type: cloud-gemini-data-analytics
         projectId: "PROJECT_ID"
         ---
         kind: tool
         name: cloud_gda_query_tool
         type: cloud-gemini-data-analytics-query
         source: gda-api-source
         description: Use this tool to send natural language queries to the Gemini Data Analytics API and receive MongoDB-compatible query language (MQL), natural language answers, and explanations.
         location: "REGION_ID"
         context:
           datasourceReferences:
             firestoreReference:
               databaseReference:
                 projectId: "PROJECT_ID"
                 databaseId: "DATABASE_ID"
               agentContextReference:
                 contextSetId: "CONTEXT_SET_ID"
         generationOptions:
           generateQueryResult: true
           generateNaturalLanguageAnswer: true
           generateExplanation: true
           generateDisambiguationQuestion: true
         

Replace the following:

     * `PROJECT_ID`: Your Google Cloud project ID.
     * `DATABASE_ID`: The name of the database to connect to.
     * `REGION_ID`: The region of your database (for example `us-central1`).
     * `CONTEXT_SET_ID`: The context set ID. For more information about how to find the context set ID, see [Find the context set ID](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/inspect-data-agent#find-context-id).
  5. Run the MCP Toolbox server with the `tools.yaml` file.
         
         ./toolbox --config autoctx/tools.yaml

**Note:** Don't close the terminal window where the MCP Toolbox server is running.
  6. Create an ADK application that invokes [Gemini Data Analytics QueryData tool](https://mcp-toolbox.dev/integrations/cloudgda/tools/cloud-gda-query/) using the MCP Toolbox's Python SDK. For more information about how to use the MCP Toolbox's Python SDK, see the [quickstart for Toolbox](https://mcp-toolbox.dev/documentation/getting-started/local_quickstart/) and for Python ADK, see the [quickstart for ADK](https://google.github.io/adk-docs/get-started/python/).

     1. Create a directory to store the application, for example `flight-assistant-app`.
     2. Change directory to the `flight-assistant-app` directory.
            
            mkdir flight-assistant-app
            cd flight-assistant-app

     3. Run the following commands under the `flight-assistant-app` directory to create a virtual environment and install required components.
            
            uv init
            uv add google-adk toolbox-core google-genai

     4. Set up an ADK agent.

        1. Create an ADK agent.
               
               uv run adk create my_agent

        2. Select the `gemini-3.8-flash` model, or newer.

        3. Select **Google AI** , and enter your Gemini API key. For more information about how to find your API key, see [Using Gemini API keys](https://ai.google.dev/gemini-api/docs/api-key). (Alternatively, if you don't need a free trial, you can select **Vertex AI** and specify a Google Cloud project with billing enabled).

     5. Replace the contents of the `agent.py` file with the following Flight Data Assistant sample application code.
            
            from typing import cast
            
            from google.adk.agents.llm_agent import Agent
            from google.adk.agents.llm_agent import ToolUnion
            
            from toolbox_core import ToolboxSyncClient
            
            TOOLBOX_URL = "http://127.0.0.1:5000"
            
            INSTRUCTION = """
            # ROLE
            You are a friendly and factual flight data assistant. Your goal is to help users find the best flights for their needs by providing accurate information with a helpful, professional tone.
            - use the Query Data Tool to answer the user's question, if the tool fails to generate a valid query, ask the user to clarify their question.
            
            # OPERATIONAL CONSTRAINTS
            - TOOL LIMITATION: You only have access to the Query Data Tool. Do not claim to have capabilities beyond what this tool provides.
            - TRANSPARENCY POLICY: Maintain a seamless user experience. Never mention that you are using a tool, querying a database, or generating MQL. Frame all responses as your own direct assistance.
            - SCOPE MANAGEMENT: If a user asks for something beyond your capabilities, politely state that you cannot perform that specific task. Guide the user towards what you can help with.
            
            # COMMUNICATION STYLE
            - Be concise and scannable when listing answers.
            - Maintain a helpful, professional persona.
            
            =====
            
            # QUERY DATA TOOL
            
            Inputs:
            1. query: A natural language formulation of a database query.
            
            Outputs: (all optional)
            1. disambiguation_question: Clarification questions or comments where the tool needs the users' input.
            2. generated_query: The generated query for the user query.
            3. intent_explanation: An explanation for why the tool produced `generated_query`.
            4. query_result: The result of executing `generated_query`.
            5. natural_language_answer: The natural language answer that summarizes the `query` and `query_result`.
            
            Usage guidance:
            1. If `disambiguation_question` is produced, then solicit the needed inputs from the user and try the tool with a new `query` that has the needed clarification.
            2. If `natural_language_answer` is produced, use `intent_explanation` and `generated_query` to see if you need to clarify any assumptions for the user.
            3. If the tool output indicates failure or empty results, explain that clearly using the provided reasoning.
            """
            
            client = ToolboxSyncClient(TOOLBOX_URL)
            
            mcp_tool = client.load_tool("cloud_gda_query_tool")
            
            root_agent = Agent(
                model="gemini-3.8-flash",  # Or newer.
                name="root_agent",
                instruction=INSTRUCTION,
                tools=cast(list[ToolUnion], [mcp_tool]),
            )
            

**Note:** The instruction contains a system prompt that sets up a `flight assistant` data agent. It also instructs the agent how to use the Gemini Data Analytics QueryData tool you set up in the `tools.yaml` file you created earlier in step 5.
  7. Run the following commands under the `flight-assistant-app` directory to start the application and access the ADK web server at `http://127.0.0.1:8000`.
         
         uv run adk web --port 8000

  8. Enter any text, such as `hello`, to start interacting with the agent.

The ADK agent answers general questions and calls the required MCP tools.

  9. Enter the following flight-related question.
         
         How many flights depart from the west side?
         

The MCP tool is called to answer this question. However, since the term `the west` is ambiguous and doesn't specify any airports, the MCP tool returns a disambiguation question which the agent uses to construct a response.
         
         I cannot determine how many flights depart from the 'west side' as the database does not contain information about which airports are considered to be on the 'west side'. However, I can help you with questions like:
         
         1. How many flights depart from a specific airport?
         
         2. What are the departure airports for all flights?
         
         3. How many flights depart from each airport? Would you like to rephrase your question based on these options?
         

  10. Enter a question similar to that in the query template generated for the agent.
         
         Help me find flights from San Francisco that avoid the evening rush hour.
         

Based on the QueryData context added earlier, the MCP tool understands that `evening traffic` occurs between 5 PM and 7 PM. The MCP tool returns the associated data for the agent to use in constructing its response.
         
         Here are the flights departing from San Francisco that avoid the evening rush hour (defined as 5 PM to 7 PM):
         
         * UA 1532 departing at 05:50:00
         * UA 1158 departing at 05:57:00
         * CY 922 departing at 06:38:00
         * OO 5441 departing at 07:08:00
         * UA 616 departing at 07:14:00
         * AA 24 departing at 07:14:00
         * B6 434 departing at 08:00:00
         * AA 242 departing at 08:18:00
         * UA 1739 departing at 08:22:00
         * OO 6336 departing at 08:32:00
         * US 1784 departing at 08:47:00
         * DL 1631 departing at 09:00:00
         * DL 1106 departing at 09:06:00
         * OO 5427 departing at 09:06:00
         * CY 352 departing at 09:25:00
         




## Iterate agent performance

The ADK web UI lets you inspect the request and response from the Gemini Data Analytics QueryData MCP tool. You can use this response to observe the tool responses such as generated MQL query, result set, intent explanation, disambiguation question, and natural language answer, to help you confirm the correctness of your agent's responses.

For example, for the input text `How many flights depart from the west side?` you entered earlier, click the agent bubble. In the **Event** tab in the left navigation, expand the `functionResponse` to see the following response.
    
    
    "{"disambiguationQuestion": ["[NOT_ENOUGH_INFO] The database schema does not
    contain information about which airports are on the 'west side'. Therefore, I
    cannot determine how many flights depart from the west side.Possible alternative
    questions: 1. How many flights depart from a specific airport? 2. What are the
    departure airports for all flights? 3. How many flights depart from each
    airport?"]}"
    

### Refine response accuracy

You can continuously refine the accuracy of responses from the Gemini Data Analytics QueryData tool by adding additional context. Use the context engineering agent to generate context, and then upload the updated context set file to the existing `flights-assistant` data agent. For more information, see [Manage context sets in Firestore Studio](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/manage-data-agents). The console immediately ingests new context after you upload it, enabling you to enhance the agent's accuracy without any application downtime.

### Multiple agents

In your development environment, you can perform A/B testing on multiple data agent contexts by assigning distinct names to tools in your `tools.yaml` file. For example, you can create unique `tools.yaml` configurations by defining two `cloud-gemini-data-analytics-query` tools with different names, such as `cloud_gda_query_tool_v1` and `cloud_gda_query_tool_v2`. This setup lets you implement application logic that programmatically selects the required context version by choosing the corresponding tool name.

The following example `tools.yaml` shows how to set up multiple data agents for a database source:
    
    
    kind: source
    name: gda-api-source
    type: cloud-gemini-data-analytics
    projectId: PROJECT_ID
    ---
    kind: tool
    name: cloud_gda_query_tool_v1
    type: cloud-gemini-data-analytics-query
    source: gda-api-source
    context:
      datasourceReferences:
        DB_SOURCE:
          databaseReference: ...
          agentContextReference:
            contextSetId: "V1_YOUR_CONTEXT_SET_ID"
    generationOptions: ...
    ---
    kind: tool
    name: cloud_gda_query_tool_v2
    type: cloud-gemini-data-analytics-query
    source: gda-api-source
    context:
      datasourceReferences:
        DB_SOURCE:
          databaseReference: ...
          agentContextReference:
            contextSetId: "V2_YOUR_CONTEXT_SET_ID"
    generationOptions: ...
    

Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `V1_YOUR_CONTEXT_SET_ID`: The context set ID for version 1.
  * `V2_YOUR_CONTEXT_SET_ID`: The context set ID for version 2.



### Access control and security considerations

In the preview launch, QueryData for Firestore with MongoDB compatibility doesn't support fine-grained access controls. When integrating QueryData with your application, consider how data access is controlled:

  * **Database-level granularity** : Access granularity can be controlled using IAM conditions at the database level. However, there is no granular access control at the collection, document, or field level.
  * **Full database read access** : The data agent has read access to the entire database. Any query generated by the agent can read from all collections, documents, and fields within that database. The data agent isn't restricted by Firebase security rules.
  * **Application user scoping** : Because fine-grained access controls are not supported, you cannot restrict data access to specific collections, documents, or fields based on application user identities. Queries generated by QueryData execute with the full read permissions of the database user or service account used by your application.



## Clean up

After you have finished following this tutorial, you should delete the resources that you created to avoid incurring ongoing costs. The following sections describe how to delete these resources.

### Delete the context set

Before you delete the database, delete the context set that you created.

  1. In the Google Cloud console, go to the Firestore page.

[Go to Firestore](https://console.cloud.google.com/firestore)

  2. Select a database from the list. The database must be an Enterprise edition database in MongoDB compatibility mode.

  3. In the navigation menu, click **Firestore Studio**. 

  4. In the **Explorer pane** , next to your context set, click **More actions ( more_vert)**.

  5. In the **Delete context set** window, enter `flight-assistant` in the confirmation box.

  6. Click **Confirm**.




### Delete the database

When you delete the database that you created in the before you begin section, you also delete all of the objects you created.

  1. In the Google Cloud console, go to the Firestore page.

[Go to Firestore](https://console.cloud.google.com/firestore)

  2. Find the row for the name of the database that you want to delete.

  3. Click the **Actions** (more_vert) icon, then click **Delete**.

  4. Confirm that you want to delete the database by entering the database name and clicking **Delete**.




## What's next

  * Learn more about [context sets](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/context-sets-overview).
  * Learn how to [define authored context for database data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-databases).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
