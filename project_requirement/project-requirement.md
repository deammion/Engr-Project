# ENGR 301: Project Requirements Document

The aim of this document is to specify the requirements of the system your group is to build. The focus of a requirements document is the problem you are attempting to solve:  not a first attempt at a solution to that problem. This document should communicate clearly to the supervisor, client and course coordinator what the system you build is going to do, and what constraints it must meet while doing so.

The document should also demonstrate your understanding of the main analysis principles and quality guidelines, and applicable standards, using tools and notations as necessary to communicate the requirements precisely, unambiguously and clearly in a written technical document. Page specifications below are *limits not targets* and refer to the pages in the PDF generated from the markdown. Because the size of your document is necessarily limited, you should ensure that you focus your efforts on those requirements that are most important to completing a successful system: if sections are at their page limit, indicate how many items would be expected in a complete specification. 

The ENGR 301 project proposal and requirements document should be based on the standard ISO/IEC/IEEE 29148:2011(E), primarily sections 8.4 and 9.5, plus section 9.4 for projects involving hardware and ISO 25010 SQuaRE for systemic requirements. While excerpts from the standard have been quoted within the template, to understand what is required it will be necessary to read earlier sections of the standards themselves. A supplementary treatment of requirements gathering in engineering projects may be found in [Requirements in Engineering Projects](https://victoria.rl.talis.com/items/F166DA94-DAD8-FBDB-0785-7A63C9BA3603.html?referrer=%2Flists%2F5886F297-2506-1F17-45D9-7F04CEE284EE.html%23item-F166DA94-DAD8-FBDB-0785-7A63C9BA3603) (Talis). The requirements document should contain the sections listed below, and conform to the formatting rules listed at the end of this brief. 

All team members are expected to contribute equally to the document and list their contributions in section 6 of the document. You should work on your document in your team's GitLab repository. While collective contributions are expected to be the exception rather than the rule, if more than one team member has contributed to a particular commit then all those team member IDs should be included in the first line of the git commit message. `git blame`, `git diff`, file histories, etc. will be tools used to assess individual contributions, so everyone is encouraged to contribute individually, commit early and commit often. Any team wishing to separate individually contributed sections into a single file before collation into the single proposal document for submission is welcome to do so.

---

<div style="page-break-after: always;"></div>

# ENGR 301 Project *NN* Project Proposal and Requirements Document
#### Author list, a comma-separated list of the names of each member of the team.

## 1. Introduction

One page overall introduction including sections 1.1 and 1.2.

### Client
Company: RedShield

Contact: Kirk Jackson <br>
Email: 	kirk@redshield.co <br>
Address: <br>
    RedShield <br>
    Level 12 <br>
    RedShield House <br>
    79 Boulcott St <br>

### 1.1 Purpose

The Purpose of this project is to create a working prototype of a stand alone program capable of a reading, interpepting, and analyising HTTP source code with the intended purpose of preventing XSS, using nonce tags.

### 1.2 Scope

The scope of this project is to create a MITM proxy capable of reading and interperting HTTP responses to determine what script tags are safe and unsafe. This program will implement script fingerprinting using nonce for non-variable, and non-inline script tags, to prevent XSS attacks. Python unit test will be used to ensure the validity of the program we create. 

### 1.3 Product overview 
#### 1.3.1 Product perspective

One page defining the system's relationship to other related products
(9.5.3. but not the subsections in the standard.)

> **9.5.3 Product perspective** <br>

The project will produce a proxy program that will be demonstrated to Red Shield which will assist with the development of a similar solution to CPS (Content Security Policy), their Red Core Shielding technology. The project does not need to directly access or use any of the components of the Red Core Shielding technology, nor does it need to written in elixir, which is the native coding language used by Red Core Shielding technology. Red Shield will handle the conversion from python to elixir, once the project is completed.

The project will produce a system which will relate to any host server implementing the proxy program. This relation will not interfere with the host server or its standard functionality. The project team will ensure that the produced program does not interfere in any way with the host server’s functionality, with exception of an unsafe XSS tag being tagged, notified and added.

> Define the system's relationship to other related products. 
> 
> If the product is an element of a larger system, then relate the requirements of that larger system to the functionality of the product covered by the software requirements specification.
> 
> If the product is an element of a larger system, then identify the interfaces between the product covered by the software requirements specification and the larger system of which the product is an element. 
>
> A block diagram showing the major elements of the larger system, interconnections, and external interfaces can be helpful.
> 
> Describe how the software operates within the following constraints:  
a) System interfaces;  
b) User interfaces;  
c) Hardware interfaces;  
d) Software interfaces;  
e) Communications interfaces;  
f) Memory;  
g) Operations;  
h) Site adaptation requirements.

#### 1.3.2 Product functions

One page summary of the main functions of the product (9.5.4), briefly characterising the minimum viable product.

#### 1.3.3 User characteristics   

One page identifying the main classes of users and their characteristics (9.5.5) 

#### 1.3.4 Limitations

One page on the limitations on the product (9.5.6)<br>
A limitation for our program is that during the collection phase, it will be assumed that websites are already clean. So that any scripts on that page which are often present will be deemed as safe. However, this means if a page isn’t initially clea we could be incorrectly deeming a script tag as safe.

Another limitation is that this will only be able to run on certain browsers such as Edge, Chrome and Firefox because strict CSP is not enabled for other web browsers. 


## 2. References

References to other documents or standards. Follow the IEEE Citation  Reference scheme, available from the [IEEE website](https://www.ieee.org/) (please use the search box). (1 page, longer if required)

## 3. Specific requirements  

20 pages outlining the requirements of the system. You should apportion these pages across the following subsections to focus on the most important parts of your product.

### 3.1 External interfaces

See 9.5.10. for most systems this will be around one page. 

### 3.2 Functions

This is typically the longest subsection in the document. List up to fifty use cases (in order of priority for development), and for at least top ten focal use cases, write a short goal statement and use case body (up to seven pages).  Identify the use cases that comprise a minimum viable product.

| Phases    | Explanation     |
| --------- |  -------------  |
|Collection |                 |
|Real       |                 |

| 1         |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |   * Parses the HTML of the site  |
|           |   * New script tags are found  |
|Goal       |   * Program notes new script  |
|           |   * Calculates initial percentage |

| 2         |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |   * Parses the HTML of the site  |
|           |   * Previously found script tags are found again |
|Goal       |   * Script tags percentages increase |

| 3         |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |   * Parses the HTML of the site  |
|           |   * Previously found script tags does not appear |
|Goal       |   * Script tags percentages decreases |

| 4         |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |   * Parses the HTML of the site  |
|           |   * No script tags are found |
|Goal       |   * Nothing happens  |

| 5         |                 |
| --------- |  -------------  |
|Phase      |   Real    |
|System     |   * Parses the HTML of the site  |
|           |   * No script tags are found |
|Goal       |   * No nonces are added  |

| 6         |                 |
| --------- |  -------------  |
|Phase      |   Real    |
|System     |   * Parses the HTML of the site  |
|           |   * Script tag with high percentages are found |
|Goal       |   * Nonces added to these script tags  |

| 7         |                 |
| --------- |  -------------  |
|Phase      |   Real    |
|System     |   * Parses the HTML of the site  |
|           |   * Script tag with low percentages are found |
|Goal       |   * Nonces added to these script tags  |

| 8         |                 |
| --------- |  -------------  |
|Phase      |   Real    |
|System     |   * Parses the HTML of the site  |
|           |   * Script tag which hasn’t been registered before |
|Goal       |   * Nonces not added to these script tags  |
|           |   * Reported on report-uri.com |

| 9         |                 |
| --------- |  -------------  |
|Phase      |   Real    |
|System     |   * Parses the HTML of the site  |
|           |   * Found script tag which has a high percentage and script tag which hasn’t been registered before |
|Goal       |   * Nonces added to these script tags with high percentages   |
|           |   * Nonces not added to script tags which aren’t registered |
|           |   * Report non registered script tags on report-uri.com |

| 10        |                 |
| --------- |  -------------  |
|Phase      |   Real    |
|System     |   * Parses the HTML of the site  |
|           |   * Found inline script tag |
|Goal       |   * Nonce is added and script is ignored  |

| 11        |                 |
| --------- |  -------------  |
|Phase      |   Collection    |
|System     |   * Parses the HTML of the site  |
|           |   * Found inline script tag |
|Goal       |   * Script tags percentage increases  |

### 3.3 Usability Requirements

See 9.5.12. for most systems this will be around one page.

> **9.5.12 Usability requirements**<br>
> Define usability (quality in use) requirements. Usability requirements and objectives for the software system include measurable effectiveness, efficiency, and satisfaction criteria in specific contexts of use.

The goal is to design a proxy program which adheres to appreciate expectations and specifications to create additional security features for web applications. Fulfilling the usability requirements ensures that certain XSS inserted to the website is prevented from executing and safe script tags are applied to prevent websites from breaking due to the security. 

### 3.4 Performance requirements

See 9.5.13. for most systems this will be around one page. Hardware projects also see section 9.4.6.

> **9.5.13 Performance requirements** <br>
> Specify both the static and the dynamic numerical requirements placed on the software or on human interaction with the software as a whole. 
> 
> Static numerical requirements may include the following:
> 
> a) The number of terminals to be supported;  
> b) The number of simultaneous users to be supported;  
> c) Amount and type of information to be handled.
> 
> Static numerical requirements are sometimes identified under a separate section entitled Capacity.
> 
> Dynamic numerical requirements may include, for example, the numbers of transactions and tasks and the amount of data to be processed within certain time periods for both normal and peak workload conditions. The performance requirements should be stated in measurable terms.
> 
>  For example, "_95 % of the transactions shall be processed in less than 1 second._" rather than, "An operator shall not have to wait for the transaction to complete."
> 
> NOTE Numerical limits applied to one specific function are normally specified as part of the processing subparagraph description of that function.


### 3.5 Logical database requirements

See 9.5.14. for most systems, a focus on d) and e) is appropriate, such as an object-oriented domain analysis. You should provide an overview domain model (e.g.  a UML class diagram of approximately ten classes) and write a brief description of the responsibilities of each class in the model (3 pages).

You should use right tools, preferabley PlantUML, to draw your URL diagrams which can be easily embedded into a Mardown file (PlantUML is also supported by GitLab and Foswiki).

### 3.6 Design constraints

see 9.5.15 and 9.5.16. for most systems, this will be around one page.

> 9.5.15 Design constraints<br>
> Specify constraints on the system design imposed by external standards, regulatory requirements, or project limitations.
> 
> 9.5.16 Standards compliance<br>
> Specify the requirements derived from existing standards or regulations, including:
> 
> a) Report format;<br>
> b) Data naming;<br>
> c) Accounting procedures;<br>
> d) Audit tracing.
> 
> For example, this could specify the requirement for software to trace processing activity. Such traces are needed for some applications to meet minimum regulatory or financial standards. An audit trace requirement may, for example, state that all changes to a payroll database shall be recorded in a trace file with before and after values.

### 3.7 Nonfunctional system attributes

Present the systemic (aka nonfunctional) requirements of the product (see ISO/IEC 25010).
List up to twenty systemic requirements / attributes.
Write a short natural language description of the top nonfunctional requirements (approx. five pages).

The nonfunctional requirements of this project are as follows (in descending order of priority): Security, Reliability, Performance, Scalability, Maintainability, and Usability.<br>

Security: <br>
The main purpose of this project is to increase internet browser security by implementing CSP on all outgoing HTTP requests sent by the host server; security is the top priority.  As such the project will need to produce a program that can perform such implementation without compromising security of both the end user and the host server.<br>
The program/proxy must also be able to operate without exposing itself to attack. Since the program has a read functionality used to train the system on what to apply the CSP too. The program needs security measures to prevent the possibility of this being exploited. Since exploiting this part of the program would result in ineffective application of the CSP.<br>

Reliability:<br>
The project needs to produce a program capable of running independently as it is implemented by use of a proxy server. Since the proxy is remote to the host and end user reliability is also a top priority as neither the end user or host server have access to the program. Meaning if problems arise due to the use of said program external intervention is required to initiate recover. <br>
Since external intervention or termination of the proxy is required if the program malfunctions then the project becomes null and void. So the program needs to be as robust as possible as failure can cause the host server to lose business, traffic etc, depending on the host site. Failure could potentially result in a security risk depending on the severity of the failure and if the program is the only CSP the host server is operating.<br>

Performance and Scalability:<br>
The program needs to be able to operate in such a way that it can handle a single request at once with limited interference/lag between the host server and the end user. If the program is unable to handle a single request without hindering normal use of the host website, the host server may see the program as more of a nuisance than a necessary security measure. Further on from this the program potentially needs to be able to handle multiple requests at once, with the same amount of limited interference. If the program is unable to handle such requests this will lead to downgraded performance.<br>
Downgraded performance or limited scalability could result in loss of business, traffic to the host server. If this were to occur it could become a case of functionality over security resulting in the program being abandoned. <br>

Maintainability:<br>
As the program is to be designed in such a manner that it operates on a proxy server it can be considered to be an independent system. Meaning the end user and host server cannot and do not interact with the program. The program operates between the two independently of the others. As such maintainability of the program by the end user of the HTTP request and the host server is a null issue.<br>
However, the program may still require maintenance as HTTP continues to change and become increasingly complex. The program needs to be built in a way that will allow for updates and regular patching if it is deemed necessary. <br>

Usability:



### 3.8 Physical and Environmental Requirements 

For systems with hardware components, identify the physical characteristics of that hardware (9.4.10) and environment conditions in which it must operate (9.4.11).  Depending on the project, this section may be from one page up to 5 pages.<br>

This project is a software-based project therefore this means that there will be no physical requirements. However, in order to complete this project, we will need access to a computer. This computer must not only have python installed but also be able to run python 3 or higher.    

### 3.9 Supporting information

see 9.5.19. 

## 4. Verification

3 pages outlining how you will verify that the product meets the most important specific requirements. The format of this section should parallel section 3 of your document (see 9.5.18). Wherever possible (especially systemic requirements) you should indicate testable acceptance criteria.

## 5. Development schedule.

### 5.1 Schedule

Identify dates for key project deliverables: 

|  Project Deliverables  | Date     |
| ---------------------- |  ------  |
| Architectural Prototype|          |
| Minimum Viable Product |          |
| Further Releases       |          |
| Final Project          |          |

(1 page).

### 5.2 Budget

| Item     | Amount |
| -------- |  ----- |
| Software |  nil   |
| Hardware |  nil   |
| Travel   |  nil   |

This project does not require a budget as it makes use of open source programs such as MITM. Accessing this can be done using personal computers or the computers available at Victoria University of Wellington.<br>

The Client is local, and has indicated they can travel to Victoria University of Wellington for meetings.<br>


### 5.3 Risks 

Identify the ten most important project risks to achieving project goals: their type, likelihood, impact, and mitigation strategies (3 pages).

If the project will involve any work outside the ECS laboratories, i.e. off-campus activities, these should be included in the following section.<br>

| Risks    | Type     |  Likelihood  |  Impact  | Mitigation |
| ---------|  ------  | ------------ | -------- | ---------- |
|          |          |              |          |            |
|Code being deleted |Technical |  Likely | Moderate-Significant (depending on amount/importance)| Use Gitlab |
|Code being overwritten | Technical |  Very Likely | Moderate| Mattermost to notify others of commitments and if code is overwritten, use gitlab to restore it |
|Team member unable to contribute for unforeseen reasons |Teamwork |  Possible | Moderate-Significant(depending on project stage)| Keep good documentation of what is done so others can pick up tasks without too much hassle |
|Team member has other commitments which cause them to not be available  |Teamwork |  Very Likely  |Minor| Keep good documentation of what is done so others can pick up tasks without too much hassle and ensure no one is out of the loop |
|Team member has not done their specified work| Teamwork |Possible| Significant | Regularly meet up and contact team members to ensure everyone is on track  |
|COVID Lockdown|  |Very Likely| Significant | Ensure everyone is able to connect online and all work is online |
|Misunderstanding about the project requirements| Requirements |Likely| Moderate | Ensure constant communication with the client and clear up any uncertainties promptly |
|Changes to project requirements| Requirements | Possible | Significant | Ensure there is a clear understanding of what is required from the team from the beginning and ensure constant communication with client |
|Bugs within code go undetected| Technical |Very Likely| Significant | Create tests for the program, to test different aspects of it and minimize the number of errors that go undectected |
|Team members burning out| eamwork |Likely| Significant | Ensure everyone is communicating with each other so the team knows if someone is doing too much work and ensure all work is evenly divided |


### 5.4 Health and Safety

Document here project requirements for Health and Safety. All teams must state in this section:

1. How teams will manage computer-related risks such as Occupational Over Use, Cable management, etc.  

2. Whether project work requires work or testing at any external (off-campus) workplaces/sites. If so, state the team's plans for receiving a Health and Safety induction for the external workplaces/sites. If the team has already received such an induction, state the date it was received. 

3. Whether project work requires the team test with human or animal subjects? If so, explain why there is no option but for the team to perform this testing, and state the team's plans for receiving Ethics Approval _prior_ to testing.

Also document in this section any additional discussions with the School Safety Officer regarding Health and Safety risks. Give any further information on relevant health and safety regulations, risks, and mitigations, etc.


#### 5.4.1 Safety Plans

Safety Plans may be required for some projects, depending on project requirements. Safety Plan templates are available on the course Health & Safety page. Two questions all teams must answer are:

Do project requirements involve anything that can cause serious harm or death?
Our project requirements does not involve anything that can cause us serious harm or death. 

Examples: building/modifying devices using voltages > 60 V, chemicals, large moving machinery, flying devices, bodies of water.

If so, you will have to write a separate Safety Plan as part of project requirements, and the Safety Plan must be referenced in this section. For health and safety risks involving serious harm or death, you must first contact the School Safety Officer and Course Coordinator first to discuss the Safety Plan and project requirements.

**Do project requirements involve anything that can cause harm or injury?**  
- tripping over cables
- not having enough breaks
- eye strain 
Examples: building/modifying things with voltages <= 60V, small moving machinery, wearable devices.

If so, you will have to write a separate Safety Plan as part of project requirements, and the Safety Plan must be referenced in this section. For health and safety risks involving harm or injury, you should write a draft of the Safety Plan before contacting the School Safety Officer and Course Coordinator to discuss the Safety Plan and project requirements.

If a safety plan is required, list in this section the date the School Safety officer accepted your Health and Safety plan (if accepted by submission date).

_If the project is purely software and requires no contact risks involving physical harm, then state "Project requirements do not involve risk of death, serious harm, harm or injury." in this section._

Project requirements do not involve risk of death, serious harm, harm, or injury.


## 6. Appendices
### 6.1 Assumptions and dependencies 

One page on assumptions and dependencies (9.5.7).<br>
We are assuming that during the collection phase, the websites scanned will be clean. 
We are assuming that anyone using our program is using either Edge, Chrome or FireFox.
A dependency is that the browsers used must be either Edge, Chrome or FireFox.


### 6.2 Acronyms and abbreviations

One page glossary _as required_.

## 7. Contributions

| Contributors  | Sections     |
| ------        |  ----------  |
|    Dylan      |              |
|    Isabella   | 1.1, 1.2, 1.3.1, 5.4.1, 5.2, 3.2, 3.3, 5.3  |
|    Damien     | 1.1, 1.2,1.3.1, 3.7, 5.4    |
|    James      |              |
|    Jaya       |1.3.4, 3.8, 5.3, 6.1 |
|    Nathan     |              |
|    Timothy    |              |

---

## Formatting Rules 

 * Write your document using [Markdown](https://gitlab.ecs.vuw.ac.nz/help/user/markdown#gitlab-flavored-markdown-gfm) and ensure you commit your work to your team's GitLab repository.
 * Major sections should be separated by a horizontal rule.


## Assessment  

The goal of a requirements document is the problem you are attempting to solve:  not a first attempt at a solution to that problem. The most important factor in the assessmernt of the document is how will it meet that goal. The document will be assessed for both presentation and content. 

The presentation will be based on how easy it is to read, correct spelling, grammar, punctuation, clear diagrams, and so on.

The content will be assessed according to its clarity, consistency, relevance, critical engagement and a demonstrated understanding of the material in the course. We look for evidence these traits are represented and assess the level of performance against these traits. While being comprehensive and easy to understand, this document must be reasonably concise too. You will be affected negatively by writing a report with too many pages (far more than what has been suggested for each section above).

We aim to evaluate ENGR301 documents and projects as if they were real projects rather than academic exercises &mdash; especially as they are real projects with real clients. The best way to get a good mark in a document is to do the right thing for your project, your client, and your team. We encourage you to raise questions with your tutor or course staff, as soon as possible, so you can incorporate their feedback into your work.

---
