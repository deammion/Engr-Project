# Final Project Report

**Project _Name_:** Shield all the things<br>
**Client:** Kirk Jackson<br>
**Date:** 18 October 2021<br>

## Project Objective(s)

The objective of this project is to create a working prototype of a proxy plugin program that will prevent cross-site scripting (XSS) on websites. This plugin is an add-on for MITMproxy. Which will collect, process, analyse and categorise scripts on a webpage to allow for the filtering of unsafe scripts. Filtering will be achieved through the use of Content Security Policy (CSP) headers and Nonce Tags. Filtered/Blocked scripts should be blocked from execution and reported through report-URI.

## Summary of Project Results

Full functionality was achieved as per the objective stated above. The plugin is capable of monitoring traffic and collecting HTTP flows and analysing scripts as they pass through the proxy. This process will allow the plugin to learn which scripts are common and/or safe. The program will use this information to apply CSP headers and assign nonces to safe script tags. This will result in unsafe script tags being blocked from executing, hence preventing XSS. Blocked scripts are also reported as per the objective.

## Original and Delivered Scope

The proxy delivers on all areas of our original scope. The project consists of the 3 phases outlined in the scope: Collection, Analysis and Operation. 

Each phase has all the functionality outlined in our original scope. The Collection phase can gather the HTTP intercepted by MITM and can write that to a file. The naming and storing are based on the time the response was gathered and the domain of the website. The Analysis phase can extract the script data from the latest collected files, calculate the frequency and probability related to those scripts and present the data in two database files. One that can be easily read by other phases and the other that can be readable by the client for debugging purposes. Finally, the operation phase can compare extracted scripts from HTTP responses to the data in the database files to determine the safe scripts. If all the scrips are safe, it applies the nonce tags and CSP headers. If it detects an unsafe script, it will alert the user and send a report to ReportURI. 

In summary, our original project scope was to use Content Security Policy (CSP) headers and nonce tags to prevent XSS on websites through the use of MITM Proxy. We have achieved that goal.

## Original and Actual Schedule

### Original Scope
|  Project Deliverables  | Date     |
| ---------------------- |  ------  |
| Architectural Prototype|   14th May|
| Collection Phase Implementation|   20th July |
| Analysis Phase Implementation |   3rd August |
| Operational Phase Implementation |   17th August |
| Application - Minimum Viable Product |   17th August  |
| Documentation - Minimum Viable Product |  13th August |
| Further Releases       |   8th October |
| Final Project          |   6th November |

### Delivered Scope
There were some deviations from the original plan in respect to implementing each phase. This then resulted in the timeline of the minimum viable product to also be delayed. Furthermore, the minimum viable product, the further releases and the final project all resulted in the same outcome. 

The following table depicts the deviations from the original timeline plan.

|  Project Deliverables  | Date     |
| ---------------------- |  ------  |
| Collection Phase Implementation|   3rd August |
| Analysis Phase Implementation |   17th August |
| Operational Phase Implementation |   28th September |
| Application - Minimum Viable Product |   7th October  |
| Documentation - Minimum Viable Product |  7th October  |
| Further Releases       |   7th October |
| Final Project          |   8th October |

## Delivered Expenditure

No expenditure

## Project Self-Assessment

The team was able to achieve all the objectives set by the client. The plugin can monitor traffic, capture and store HTTP flows (Collection class). From these flows, the plugin can read these HTTP files, analyse the scripts within these files and produce a database of safe scripts (Analysis class). The plugin can then use this database to apply the CSP to the HTTP response (Operational class).<br>

The Analysis class is designed in a way that it can be called each time a HTTP response is captured, or independently. Meaning the class will function correctly whether it is analysing one HTTP file or thousands of files. It does this by, first reading from the Database file (if it exists), then reading and analysing the new HTTP files.<br>

## Lessons Learned
Throughout this project, as a group, we learnt how to use Python. Only one member of the group had experience using Python, so the rest of us
had to learn. This was a challenge at the start because, despite Python being similar to Java (a language we are all familiar with) i.e., it is an object-oriented language, with different syntax, it was still a hurdle to get around.<br>
Furthermore, we learnt how to use the Man-in-the-Middle proxy. This was an entirely new piece of software that we were directed to use by the client, Kirk at RedShield.
It was originally very difficult to get it working on all members of the groups' laptops. We found that the documentation was somewhat confusing
however we managed to get it done in the end.<br>
We also learnt how to use deadlines/scheduling and produce deliverables for a client. It was beneficial that we were ahead of the class schedule, which allowed for refactoring and polishing the program. <br>


## Procurement Summary

No procurements

