# ENGR 301: Architectural Design and Proof-of-Concept

## Proof-of-Concept

The aim of an architectural proof-of-concept (spike or walking skeleton) is to demonstrate the technical feasibility of your chosen architecture, to mitigate technical and project risks, and to plan and validate your technical and team processes (e.g., build systems, story breakdown, Kanban boards, acceptance testing, deployment).

A walking skeleton is an initial technical attempt that will form the architectural foundation of your product. Since a walking skeleton is expected to be carried into your product, it must be completed to the quality standards expected for your final product. A walking skeleton should demonstrate all the technologies your program will rely on "end-to-end" &mdash; from the user interface down to the hardware.

In the context of ENGR 301, a walking skeleton does not need to deliver any business value to your project: the aim is technical validation and risk mitigation.


## Document

The aim of the architectural design document is to describe the architecture and high-level design of the system your group is to build, to identify any critical technical issues with your design, and to explain how you have addressed the highest rated technical and architectural risks. The architecture document should also demonstrate your understanding of architectural techniques and architectural quality, using tools and associated notations as necessary to communicate the architecture precisely, unambiguously and clearly in a written technical document.

Page specifications below are *limits not targets* and refer to the pages in the PDF generated from the markdown. Because the size of your document is necessarily limited, you should ensure that you focus your efforts on those architectural concerns that are most important to completing a successful system: if sections are at their page limit, indicate how many items would be expected in a complete specification.

The ENGR 301 project architecture design document should be based on the standard ISO/IEC/IEEE 42010:2011(E) _Systems and software engineering &mdash; Architecture description_, plus appropriate sections from ISO/IEC/IEEE 29148:2018(E) _Systems and software engineering &mdash; Life cycle processes &mdash; Requirements engineering_; ISO/IEC/IEEE 15289:2017 _Systems and software engineering &mdash; Content of life-cycle information items (documentation)_; ISO/IEC/IEEE 15288:2015 _Systems and software engineering &mdash; System life-cycle processes_; ISO/IEC/IEEE 12207:2017 _Systems and software engineering &mdash; Software life cycle processes_ and ISO 25010 SQuaRE; with notations from ISO/ISE 19501 (UML). In particular, Annex F of ISO/IEC/IEEE 15288 and Annex F of ISO/IEC/IEEE 12207. These standards are available through the Victoria University Library subscription to the [IEEE Xplore Digital Library](https://ieeexplore.ieee.org/) (e.g., by visiting IEEE Xplore from a computer connected to the University network).

The document should contain the sections listed below, and conform to the formatting rules listed at the end of this brief.

All team members are expected to contribute equally to the document and list their contributions in the last section of the document (please make sure that your continued contribution to this document can be traced in GitLab). You should work on your document in your team's GitLab repository in a directory called "M2_Architecture". If more than one team member has contributed to a particular commit, all those team member IDs should be included in the first line of the git commit message. ``git blame``, ``git diff``, file histories, etc. will be tools used to assess individual contributions, so everyone is encouraged to contribute individually (your contribution should be made to many sections of the document, rather than focusing on just a single section), commit early and commit often.

---

# ENGR 301 Project *14* Architectural Design and Proof-of-Concept

#### Isabella Tomaz Ketley, Jaya Narayan, Timothy McDermott, Dylan Simpson, Damien Tamasese, Nathan Wong, James Houlihan

## 1. Introduction

Web applications are accessed and used by everyone everywhere. Therefore, ensuring web application security is extremely important, yet it is becoming increasingly difficult. There are many vulnerabilities web applications are susceptible to. The number of potential vulnerabilities makes safeguarding against any exploitation of vulnerabilities very difficult. The exploitation of a single vulnerability may result in an entire website, or user account being compromised.   

XSS is one of the most common vulnerabilities which occurs whenever a web application trusts, or does not validate untrusted data. [1]. An XSS vulnerability can allow an attacker to execute scripts in an end user’s browser, access a user’s cookies, and could even result in an attacker compromising a user’s account [1]. Furthermore, an XSS attack can have huge consequences which are why implementing appropriate security measures are vital.

One way to mitigate the XSS attacks is to use CSP [2]. CSP is an added layer of security that can help protect against different attacks. CSP nonce tags are used to prevent XSS [3]. A nonce is a pseudo-random value intended for one-time use, meaning the nonce changes with each HTTP request [4]. This is to ensure an attacker cannot obtain the value of it. If an application contains script tags in the HTTP response, the nonce value is added as a tag to any trusted script tags within the application. Once the application is run, only script tags that have the correct nonce tag and value will be executed [4]. This ensures that only trusted script tags are allowed to be executed within an application. 

This project will use CSP headers and nonce tags to determine whether or not script tags should be run on a web application, to mitigate XSS attacks.   

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

The purpose of this project is to create a working prototype of a proxy plugin program. This program will be capable of reading, interpreting, and analyzing HTTP source code, with the intended purpose of preventing XSS from using CSP nonce tags.

### 1.2 Scope

The scope of this project is to create a proxy plugin capable of reading and interpreting HTTP responses to determine what script tags are safe and unsafe. This program will implement script fingerprinting for non-variable, and non-inline script tags, to prevent XSS attacks. Python unit tests will be used to ensure the validity of the program we create.

### 1.3 Changes to requirements

After meeting with the client, Redshield, and having them read the project requirements some minor changes have been noted. These changes are based more around clarification of functionality, rather than changing the required functionality of the project. These changes will have little to no effect on the project moving forward.<br>

The most substantial change is clarification of the stages of the program’s functionality. Initially the project team had stated that there were two stages: a collections stage and an operational stage. In the initial report the collection stage was responsible for collecting HTML responses from the website owners’ server and analysing these responses for script tags. <br>

This stage has been split into two distinct phases: collection and analysis. The collection stage in this scenario, is still responsible for the collection and storage of the HTML responses. However, the analysis stage will be responsible for parsing, analysing, and updating the percentages relative to the perceived safety of the script tags, within the HTML. <br>

The operational stage will operate as described in the project requirements documents. This operation being parsing the HTML responses, checking percentages of found script tags, and applying nonce to those scripts deemed safe. <br>

This distinction does not change how the proxy plugin operates, but rather gives a clear distinction between collection and analysis. As noted by the client, the ideal outcome of the proxy plugin would be to have all three stages operating simultaneously. Meaning the plugin will continue to update the relative percentages during operational mode. <br>

By having these three stages all operating as an independent process, the plugin could function in this manner. This has no effect on the website user or the website owner, as the plugin will still operate in the same manner. The website user will still have no interaction with the plugin, unless trying to enter an invalid script tag. The client will still implement the plugin in the same manner by first initiating the proxy in collection mode, where it will collect HTML responses and analyse said responses to get a baseline percentage of included scripts. Then switching to operational mode where the program will continue to analyse HTML responses and in addition, apply nonce to ‘safe’ script tags. Essentially, this distinction allows for greater functionality of the plugin. <br>

Another change is to the extension of the program to include a different definition regarding what is considered a ‘safe’ script tag. <br>

In the initial project requirements, it was stated that:
* For the MVP, any script tag found in the collection phase would be to be deemed as safe.
* For the extended functionality, a script tag having a low occurrence would be deemed as unsafe. 

However, after a discussion with the client, it has been decided that a more optimal way to carry out the extension of the project, is to determine whether the occurrence of a script is greater than a precalculated amount. This will also mean that if an unsafe script tag has been entered into a website during the collection phase, we can account for this and still prevent the script tag from being executed. <br>

Another change is clarification on what is considered a ‘safe’ script tag. In the initial project requirements, a script was deemed safe by having a high percentage (occurrence/Total HTML responses per page). However, a script with a low occurrence could be deemed ‘safe’ using this logic creating a possible security exploit. Because of this the plugin will also need to account for scripts total occurrence to mitigate the possibility of ‘unsafe’ scripts being inserted using this exploit. <br>

The last change is the implementation of a ‘whitelist’ of ‘safe’ scripts regardless of context, such as google analytics as these can be regarded as safe regardless of occurrence. By utilising this approach, the plugin can process HTML responses with more efficiency. <br>


## 2. References

[1]F. Inc., "CSP Nonce ⟶ Examples and Guide", Content-security-policy.com, 2021. [Online]. Available: https://content-security-policy.com/nonce/. [Accessed: 05- Apr- 2021].

[2]M. West and J. Medley, "Content Security Policy  |  Web Fundamentals  |  Google Developers", Google Developers, 2021. [Online]. Available: https://developers.google.com/web/fundamentals/security/csp/#if_you_absolutely_must_use_it_. [Accessed: 05- Apr- 2021].

[3]J. Keith and J. Sambells, DOM Scripting, 2nd ed. O'Reilly, 2010.

[4]"Products - Content Security Policy", Report URI, 2021. [Online]. Available: https://report-uri.com/products/content_security_policy. [Accessed: 05- Apr- 2021].

[5]S. Larsen, "Csper: Content Security Policy made easy", Csper, 2020. [Online]. Available: https://csper.io/blog/an-introduction-to-report-uri. [Accessed: 05- Apr- 2021].

[6]"mitmproxy - an interactive HTTPS proxy", Mitmproxy.org, 2021. [Online]. Available: https://mitmproxy.org/. [Accessed: 05- Apr- 2021].

[7]V. Pattanshetti, "How the MITM Proxy works", Medium, 2020. [Online]. Available: https://vinodpattanshetti49.medium.com/how-the-mitm-proxy-works-8a329cc53fb. [Accessed: 05- Apr- 2021].

[8]"Content Security Policy - OWASP Cheat Sheet Series", Cheatsheetseries.owasp.org, 2021. [Online]. Available: https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html. [Accessed: 05- Apr- 2021].

[9]D. Hauscknecht, J. Magazinius, A. Sabelfeld, May I? Content Security Policy Endorsement for Browser Extension, Springer Link, 2015

[10]"OWASP Top Ten Web Application Security Risks | OWASP", Owasp.org, 2021. [Online]. Available: https://owasp.org/www-project-top-ten/. [Accessed: 06- Apr- 2021].

[11]"Cross Site Scripting Prevention - OWASP Cheat Sheet Series", Cheatsheetseries.owasp.org, 2021. [Online]. Available: https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html. [Accessed: 06- Apr- 2021].

[12]"Content Security Policy (CSP) - HTTP | MDN", Developer.mozilla.org, 2021. [Online]. Available: https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP. [Accessed: 06- Apr- 2021].

[13]T. Hunt, "Locking Down Your Website Scripts with CSP, Hashes, Nonces, and Report URI", Troy Hunt, 2017. [Online]. Available: https://www.troyhunt.com/locking-down-your-website-scripts-with-csp-hashes-nonces-and-report-uri/. [Accessed: 06- Apr- 2021].

References to other documents or standards. Follow the IEEE Citation Reference scheme, available from the [IEEE website](https://ieee-dataport.org/sites/default/files/analysis/27/IEEE%20Citation%20Guidelines.pdf) (PDF; 20 KB). (1 page, longer if required)

## 3. Architecture

Describe your system's architecture according to ISO/IEC/IEEE 42010:2011(E), ISO/IEC/IEEE 12207, ISO/IEC/IEEE 15289 and ISO/IEC/IEEE 15288.

Note in particular the note to clause 5 of 42010:

_"The verb include when used in Clause 5 indicates that either the information is present in the architecture description or reference to that information is provided therein."_

This means that you should refer to information (e.g. risks, requirements, models) in this or other documents rather than repeat information.

### 3.1 Stakeholders

See ISO/IEC/IEEE 42010 clause 5.3 and ISO/IEC/IEEE 12207 clause 6.4.4.3(2).

For most systems this will be about 2 pages, including a table mapping concerns to stakeholder.

### 3.2 Architectural Viewpoints
(1 page, 42010 5.4) 

Identify the architectural viewpoints you will use to present your system's architecture. Write one sentence to outline each viewpoint. Show which viewpoint frames which architectural concern.

**Logical:** The logical viewpoint involves the functionality that system provides to the end user. 

**Development:** The development viewpoint illustrates the system from a developers perspective and involves the software mananagement of the project.   

**Process:** The process viewpoint involves the system processes and how they communicate and run. This view addresses the concurrency, distribution, integrator, performance and scalability of the project.

**Physical:** The physical viewpoint involves the topology of software components on the physical layer and the physical connections between these components. 

**Scenarios:** The scenarios viewpoint describes the architecture of the system through use cases. 

**Circuit Architecture:** The circuit architecture viewpoint involve any circuitry involved with the project. Since this is a software project, there will be no circuitry involved.  

**Hardware Architecture:** The hardware architecture viewpoint involve any circuitry involved with the project. Since this is a software project, there will be no hardware involved. 

### 4. Architectural Views

(5 sub-sections of 2 pages each sub-section, per 42010, 5.5, 5.6, with reference to Annex F of both 12207 and 15288) 

Describe your system's architecture in a series of architectural views, each view corresponding to one viewpoint.

You should include views from the following viewpoints (from Kruchten's 4+1 model):

 * Logical
 * Development
 * Process
 * Physical 
 * Scenarios - present scenarios illustrating how two of your most important use cases are supported by your architecture

As appropriate you should include the following viewpoints:

 * Circuit Architecture
 * Hardware Architecture

Each architectural view should include at least one architectural model. If architectural models are shared across views, refer back to the first occurrence of that model in your document, rather than including a separate section for the architectural models.

### 4.1 Logical
The proxy will be designed and function independently without any interaction or input from the website user. The website owner will also have limited interactions with the proxy. If the project is made open source the website owners only interactions with the proxy plugin will be switching between modes. If the program is not made open source, then the client Redshield will be handling this implementation. <br>
![](./architecture-design/Logical_View_Project_Group_14.png)


### 4.2 Development
...

### 4.3 Process
...

### 4.4 Physical 
This project is solely software-based and therefore this means that there are no physical requirements. The only requirement this project has is that there must be access to a computer to run the program. Furthermore, the computer must have Python installed on it. The computer must be able to run Python version 3.0 or higher.  Section 4.4 discusses how software deals with the hardware availability, reliability, performance and scalability of the system. Therefore, as previously stated above due to the fact that project is completely software based the physical concerns that do not need to be considered. 
 
However this project is part of a larger system that does include hardware components. For this software project there may be hardware concerns when dealing with the larger system. For this project there will interaction with a disk. During the collection phase data will be both sent and extracted from the disk. This is a hardware concern that might be considered when the software integrates with hardware. This is not a concern that directly concerns  this software project, however it may need to be considered when working with larger systems.  


### 4.5 Scenarios

The two most important scenarios for our MVP are:

* The website is able to run in the collection phase, with no disruptions to the user of the website, and collect the HTML of the website.

* The website is able to run in the operation phase, with no disruptions unless an unsafe script tag has been entered into the site.

In both of these use cases, each time the website is accessed, information about each script tag within the page is stored and updated. As such, the analysis phase will be utilised to do this.

## 5. Development Schedule

_For each subsection, make clear what (if anything) has changed from the requirements document._ If unchanged, these sections should be copied over from the requirements document, not simply cross-referenced.

Schedules must be justified and supported by evidences; they must be either direct client requirements or direct consequences of client requirements. If the requirements document did not contain justifications or supporting evidences, then both must be provided here.

### 5.1 Schedule

Identify dates for key project deliverables:

|  Project Deliverables  | Date     |
| ---------------------- |  ------  |
| Architectural Prototype|   Friday 7th May |
| Minimum Viable Product |   Monday 16th August |
| Further Releases       |   Friday 8th October |
| Final Project          |   Saturday 6th November |

Dates are subject to change as the project continues


### 5.2 Budget and Procurement

#### 5.2.1 Budget

| Item     | Amount |
| -------- |  ----- |
| Software |  nil   |
| Hardware |  nil   |
| Travel   |  nil   |

This project does not require a budget as it makes use of open-source programs such as MITM. Accessing this can be done using personal computers or the computers available at Victoria University of Wellington.<br>

The client is local and has indicated they can travel to Victoria University of Wellington for meetings.<br>

#### 5.2.2 Procurement

As Stated in Section 5.2.1, as of writing this document, there is no budget requirements for this project. Therefore, there are no procurement requirements. <br> 

### 5.3 Risks 

Identify the ten most important project risks: their type, likelihood, impact, and mitigation strategies (3 pages).

| Risks    | Type     |  Likelihood  |  Impact  | Mitigation |
| ---------|  ------  | ------------ | -------- | ---------- |
|Code being deleted |Technical |  Likely | Moderate-Significant (depending on amount/importance of code)| Use Gitlab to ensure code is backed up and restore it|
|Code being overwritten | Technical |  Very Likely | Moderate| Use Mattermost to notify others of commits and if code is overwritten, use Gitlab to ensure it can be restored |
|Team member unable to contribute for unforeseen reasons |Teamwork |  Possible | Moderate-Significant(depending on project stage)| Keep good documentation of what has been done and what needs to be done so others can pick up tasks without too much hassle |
|Team member has other commitments which cause them to not be available  |Teamwork |  Very Likely  |Minor| Keep good documentation of what is done and what needs to be done so others can pick up tasks without too much hassle and ensure no one is out of the loop. Ensure the team has good communication so if someone is unavailable the rest of the team knows. |
|Team member has not done their specified work| Teamwork |Possible| Significant | Regularly meet up and contact team members to ensure everyone is on track. Refer back to the team contract to ensure everyone is doing their part and what happens if someone isn't.  |
|COVID Lockdown|  |Very Likely| Significant | Ensure everyone can connect online and that all work is online |
|Misunderstanding about the project requirements| Requirements |Likely| Moderate | Ensure constant communication with the client and clear up any uncertainties promptly. |
|Changes to project requirements| Requirements | Possible | Significant | Ensure there is a clear understanding of what is required from the team from the beginning and ensure constant communication with the client. |
|Bugs within code go undetected| Technical |Very Likely| Significant | Create tests for the program to test different aspects of it and minimize the number of errors that go undetected. |
|Team members burning out| Teamwork |Likely| Significant | Ensure everyone is communicating with each other so the team knows if someone is doing too much work and ensure all work is evenly divided. |


### 5.4 Health and Safety

**Occupational Overuse**
Occupational Overuse is a type of overuse injury that may result in Muscle pains, hot or cold flushes, numbness or a restricted range of movement. To prevent this from happening team members will be encouraged to take regular breaks away from their work and personal devices. Furthermore realistic deadlines and workloads will be set to discourage overworking, alongside getting the team to practice good time management to prevent overuse to meet deadlines.
Additionally, team members will have ergonomic workspaces so that any required equipment will be nearby and easily accessible. This will also encompass ensuring desks are at the correct height to encourage correct posture and reduce straining. Correct postures will be promoted and ensured for all team members and the team will use comfortable chairs which if possible, will have back support. This will reduce straining and incorrect postures in a work environment, mitigating occupational overuse and its potential symptoms.
https://www.southerncross.co.nz/group/medical-library/occupational-overuse-syndrome-oos

**Eye Strain**
Eye strain occurs when a person has been staring at a computer for large periods without having any breaks away from technology. Insufficient lighting and screen flickering can also contribute to eye strain. As with the Occupational Overuse, the team will be encouraged to take regular breaks away from their work and personal devices. The team will also be encouraged to work in environments that have a sufficient level of lighting, for example not working in the dark with the screen as your only light. The team will also make sure that text displayed in any of the work produced is easily readable to avoid eye strain from having to read small text.

**Electrical Saftey**
Since we are dealing with technology there is the risk of receiving electrical shocks from any appliances that are used in the process of working on this project. This could pose a small risk to the health of team members when they are dealing with electrical appliances such as laptops, desktop computers, monitors, electrical jugs, and the associated cables for these appliances.  As per the AS/NZS 3760 Standard, to minimise the risk of any electrical shocks the team should be encouraged to only use appliances which have been through the Test and Tag process in the last 12 months.

**Cable Management**
Unmanaged cables are a safety risk as team members or nearby people can get caught on them and/or trip on them. To manage this risk, all team members will ensure that any cables they use will be kept underneath their desk, mitigating the possibility of someone getting caught on them. Furthermore, all cables which are not being used will be stored away in a cupboard or bag to further mitigate the risk unmanaged cables pose.

**COVID-19 Outbreak and/or Lockdown**
To manage the safety risk of another Covid-19 outbreak or lockdown, team members will ensure all work is saved online using Gitlab so access to the University labs is not mandatory. Furthermore, everyone involved in the project will ensure they have a way to contact each other online. This will ensure all members of the team can work from home. This will mitigate this safety risk as it ensures that if there was a Covid-19 outbreak or lockdown, members do not need to expose themselves to any additional Covid-19 risks to do this project.

**Natural Disaster**
To manage the safety risk of earthquakes, cyclones, or tsunamis team members will ensure that they each have an understanding of the basic Natural Disaster responses that should be carried out in the event of any of the above mentioned natural disasters so that our team maximises their chances of getting through the disasters without injury. This basic knowledge should include what to do in the initial stage of a natural disaster as well as where to go and what to do after a natural disaster has occurred.

**Health and Safety at External Workplaces**
The project does not require any work or testing to be held off-campus. However, there is a possibility that some meetings will be held at Red Shield’s office. To receive a Health and Safety induction for this external workplace, team members will get in contact with the client to arrange this, before any work being done at the clients' office.

**Human or Animal Test Subjects**

This project does not include any human or animal subjects. This is because all testing can and will be done by the team, using different web applications.

#### 5.4.1 Safety Plans

Project requirements do not involve risk of death, serious harm, harm or injury.


## 6. Appendices

### 6.1 Assumptions and dependencies 

One page on assumptions and dependencies (9.5.7) 
Below is a list of assumptions and dependencies for this project:<br>

* It is assumed that during the collection phase, the websites scanned (HTML being parsed) will be clean. <br>
* It is assumed that if the scripts are hosted on a different domain, they have not been modified after the original application developer determining they are safe to include in their application. <br>
* It is assumed that users of this program will have access to either of the following browsers: Edge, Chrome or Firefox.<br>
* It is assumed that users have access to a technological device (i.e. computer, cellular phone, tablet).<br>
* It is assumed that users have internet access to run this program.<br>
* A dependency is that the browsers used must either be Edge, Chrome or Firefox to gain the full benefits of security from CSP being inforced client-side. <br>

### 6.2 Acronyms and abbreviations

CSP - Content Security Policy

MITM  - Man In The Middle

DOM - Document Object Model

HTML - Hyper-Text Markup Language

HTTP - Hyper-Text Transfer Protocol

XSS - Cross Site Scripting

## 7. Contributions

An one page statement of contributions, including a list of each member of the group and what they contributed to this document.

| Contributors  | Sections    |
| ------        |  ---------- |
|    Dylan      |             |
|    Isabella   |             |
|    Damien     |     1, 1.1, 1.2, 1.3, 4.1        |
|    James      |             |
|    Jaya       |             |
|    Nathan     |             |
|    Timothy    |             |

---

## Formatting Rules 

 * Write your document using [Markdown](https://gitlab.ecs.vuw.ac.nz/help/user/markdown#gitlab-flavored-markdown-gfm) in your team's GitLab repository.
 * Major sections should be separated by a horizontal rule.


## Assessment 

This document will be weighted at 20% on the architectural proof-of-concept(s), and 80% on the architecture design.

The proof-of-concept will be assessed for coverage (does it demonstrate all the technologies needed to build your project?) and quality (with an emphasis on simplicity, modularity, and modifiability).

The document will be assessed by considering both presentation and content. Group and individual group members will be assessed by identical criteria, the group mark for the finished PDF and the individual mark on the contributions visible through `git blame`, `git diff`, file histories, etc. 

The presentation will be based on how easy it is to read, correct spelling, grammar, punctuation, clear diagrams, and so on.

The content will be assessed according to its clarity, consistency, relevance, critical engagement and a demonstrated understanding of the material in the course. We look for evidence these traits are represented and assess the level of performance against these traits. Inspection of the GitLab Group is the essential form of assessing this document. While being comprehensive and easy to understand, this document must be reasonably concise too. You will be affected negatively by writing a report with too many pages (far more than what has been suggested for each section above).

---
