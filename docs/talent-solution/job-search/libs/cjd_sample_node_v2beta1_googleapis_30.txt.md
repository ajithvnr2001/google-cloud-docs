---
url: https://docs.cloud.google.com/talent-solution/job-search/libs/cjd_sample_node_v2beta1_googleapis_30.txt
title: https://docs.cloud.google.com/talent-solution/job-search/libs/cjd_sample_node_v2beta1_googleapis_30.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:19:29.799418+00:00
---

# https://docs.cloud.google.com/talent-solution/job-search/libs/cjd_sample_node_v2beta1_googleapis_30.txt

> Source: https://docs.cloud.google.com/talent-solution/job-search/libs/cjd_sample_node_v2beta1_googleapis_30.txt

const {google} = require('googleapis'); const discoveryDoc = '/path/to/your/discovery.json'; const key = require('/path/to/your/key.json'); const jwtClient = new google.auth.JWT(key.client_email, null, key.private_key, ["https://www.googleapis.com/auth/jobs"], null); var jobServicePromise = google.discoverAPI(discoveryDoc); jobServicePromise.then(function(jobService){ jwtClient.authorize(function(err, tokens) { if (err) { console.log(err); return; } var searchJobsRequest = { "filters": { "query": "software" }, "offset": 5, "pageSize": 5 } jobService.jobs.search({ auth: jwtClient, resource: searchJobsRequest }, function (err, result) { if (err) { console.error('Failed to search jobs! ' + err); throw err; } console.log("############# POST sample #############"); console.log('result:', result.data); }); }); jwtClient.authorize(function(err, tokens) { if (err) { console.log(err); return; } jobService.companies.list({ auth: jwtClient }, function (err, result) { if (err) { console.error('Failed to retrieve companies! ' + err); throw err; } console.log("############# GET sample #############"); console.log('Companies:', result.data); }); }); }); 
