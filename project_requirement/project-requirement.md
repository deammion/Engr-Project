# ENGR 301: Project Requirements Document

The aim of this document is to specify the requirements of the system your group is to build. The focus of a requirements document is the problem you are attempting to solve:  not a first attempt at a solution to that problem. This document should communicate clearly to the supervisor, client and course coordinator what the system you build is going to do, and what constraints it must meet while doing so.

The document should also demonstrate your understanding of the main analysis principles and quality guidelines, and applicable standards, using tools and notations as necessary to communicate the requirements precisely, unambiguously and clearly in a written technical document. Page specifications below are *limits not targets* and refer to the pages in the PDF generated from the markdown. Because the size of your document is necessarily limited, you should ensure that you focus your efforts on those requirements that are most important to completing a successful system: if sections are at their page limit, indicate how many items would be expected in a complete specification. 

The ENGR 301 project proposal and requirements document should be based on the standard ISO/IEC/IEEE 29148:2011(E), primarily sections 8.4 and 9.5, plus section 9.4 for projects involving hardware and ISO 25010 SQuaRE for systemic requirements. While excerpts from the standard have been quoted within the template, to understand what is required it will be necessary to read earlier sections of the standards themselves. A supplementary treatment of requirements gathering in engineering projects may be found in [Requirements in Engineering Projects](https://victoria.rl.talis.com/items/F166DA94-DAD8-FBDB-0785-7A63C9BA3603.html?referrer=%2Flists%2F5886F297-2506-1F17-45D9-7F04CEE284EE.html%23item-F166DA94-DAD8-FBDB-0785-7A63C9BA3603) (Talis). The requirements document should contain the sections listed below, and conform to the formatting rules listed at the end of this brief. 

All team members are expected to contribute equally to the document and list their contributions in section 6 of the document. You should work on your document in your team's GitLab repository. While collective contributions are expected to be the exception rather than the rule, if more than one team member has contributed to a particular commit then all those team member IDs should be included in the first line of the git commit message. `git blame`, `git diff`, file histories, etc. will be tools used to assess individual contributions, so everyone is encouraged to contribute individually, commit early and commit often. Any team wishing to separate individually contributed sections into a single file before collation into the single proposal document for submission is welcome to do so.

---

<div style="page-break-after: always;"></div>

# ENGR 301 Project *14* Project Proposal and Requirements Document
#### Isabella Tomaz Ketley, Jaya Narayan, Timothy McDermott, Dylan Simpson, Damien Tamasese, Nathan Wong, James Houlihan

## 1. Introduction

Web applications are accessed and used everywhere thus keeping web applications secure is getting increasingly difficult. There are many vulnerabilities web applications can have and ensuring all of these are patched can be very difficult. These days, all it takes is for an attacker to exploit a single vulnerability and a whole website or user account could be compromised.  

XSS is one of the most common web application vulnerabilities that occurs whenever an application does not validate or escape untrusted data [1]. An XSS vulnerability can cause an attacker to be able to execute scripts in a user’s browser, access a user’s cookies, and could even result in an attacker compromising a user’s account [1]. Furthermore an XSS attack can have huge consequences which is why it is important to defend against this.

One way to mitigate the XSS attacks is to use CSP [2]. CSP is an added layer of security which can help protect against different attacks. CSP nonce tags are used to prevent XSS [3]. A nonce is a pseudo-random value intended for one time use hence the nonce changes at every request to ensure an attacker cannot guess the value of it [4]. If an application contains script tags in the HTTP, the nonce value is added as a tag to any trusted script tags within the application. Once the application is run, only script tags which have the nonce tag, with the correct nonce value will be executed and run [4]. This ensures that only trusted script tags are allowed to be executed within an application. 

This project will use CSP nonce tags to determine whether or not script tags should be run on a web application, in order to mitigate XSS attacks. 


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

As discussed above the project will produce a program that will be responsible for blocking XSS attacks by adding CSP protection to web applications. This will be done in the form of adding nonce tags to scripts that are deemed safe to run.  
 
To be able to do this the project will implement a MITM proxy. This proxy will be responsible for tracking all outgoing HTTP requests from a device and all incoming HTTP responses from the web application. The HTTP responses will get stored in a secure location where the program will scan through the HTML located in the HTTP responses. As of our initial planning, the HTTP requests will not be required in our project.  
 
For the program to be able to differentiate which HTTP responses are safe to add nonce tags to it will operate in two phases. The first phase of the program is the collection stage. When operating in this phase the program will be busy identifying which script tags are safe to add nonce tags to, and which scripts are not safe not have nonce tags to. This phase will be where the program is using the collected HTTP responses to calculate the chance that content inside an HTML script tag is safe to run. Safe script tags will be defined as tags that appear on the clean page, in the collection phase over a certain threshold. For example, a script tag that appears 80 / 100 times the page is loaded will likely be safe to run. The exact point at which a program is deemed safe to run will be determined at a later stage through testing. The program assumes that web applications will be clean (not containing malicious scripts or modifications)   
 
DOM parsing will be the parsing method that will be used on the HTML inside of the collected HTTP responses, and from this determine which script tags are present and how often they are present. Since we will be able to extract each HTML script by itself, the program will be able to store any scripts that appear in a secure location, and then keep a running count of how often that script appears.  
 
So the overall process in the collections stage will look as below;  
Collect HTTP response from web application 
Store the HTTP response.  
Parse the HTTP response using DOM. 
Track all HTML scripts present from that request.  
Adjust weighting of safe scripts.  
Repeat.  
 
The second phase of our program is the real phase. In this, the program will check the scripts that are appearing on web applications, against the scripts that have appeared when running the collections phase. If a safe script is found then the program will insert a nonce tag into the HTML of the page where that script appears. This nonce tag will validate that the script tag is safe to execute. Any script tags which the program deems are not safe to run, will be collected and reported in ‘report-uri.com’.  
 
Both phases of this program will only check for non-variable and non-inline script tags.  
 
Lastly, the project will also produce a set of documentation detailing the process for setting up the MITM proxy as well as how to run our program on different devices.

#### 1.3.3 User characteristics   

One page identifying the main classes of users and their characteristics (9.5.5)

**Website Owner**<br>
This class of users include the owners of any website that enabled our proxy and program. With our proxy and program enabled, these users would experience no change in how people use their website, and their data will be protected from attacks that involve XSS. 

**Average Web Page Surfer**<br>
This class of users include anyone who accesses a webpage that has our proxy and program enabled. With our proxy and program enabled, these users would experience no changes in how they are able to use the webpage unless they are inputting script tags (which would class them as a hacker user).   

**A Red Shield Tester**<br>
This class of users include anyone from Red Shield who has access to our software. These users would have full access to the code from this project and would be able to test the performance of our software or add features to the code that are not within the scope of this project before implementing the code into their Red Core Shielding technology to be released to Red Shield’s clients. 

**A Hacker trying to attack the webpage with XSS**<br>
This class of users include anyone trying to attack a webpage with XSS that has our proxy and program enabled. With our proxy and program enabled, these users will be unable to attack the webpage through XSS as any script tags that the user implements will not have the nonce tag for the webpage and any script the user has inputted will not run.  



#### 1.3.4 Limitations

One page on the limitations on the product (9.5.6)<br>

* **Browsers**:
   * The number of browsers the program can successfully run on is limited. This program is limited to Edge, Chrome and FireFox because strict CPS is not enabled for other web browsers.<br>

<br>

* **Collection Phase**:
  * During the collection phase the program is limited as it will be assumed that websites are already clean. Therefore, any scripts on that page which are often present will be deemed to be safe. However, if a page is not initially clean the program could be incorrectly considering a script tag as being safe. 

 


## 2. References

References to other documents or standards. Follow the IEEE Citation  Reference scheme, available from the [IEEE website](https://www.ieee.org/) (please use the search box). (1 page, longer if required)

## 3. Specific requirements  

20 pages outlining the requirements of the system. You should apportion these pages across the following subsections to focus on the most important parts of your product.

### 3.1 External interfaces

See 9.5.10. for most systems this will be around one page. 

### 3.2 Functions

This is typically the longest subsection in the document. List up to fifty use cases (in order of priority for development), and for at least top ten focal use cases, write a short goal statement and use case body (up to seven pages).  Identify the use cases that comprise a minimum viable product.

#### Use Cases for the Minimum Viable Product:

| Phases    | Explanation     |
| --------- |  -------------  |
|Collection |  This is the phase where the program receives multiple versions of a web application HTTP response and parses the HTTP using DOM. Each time the program parses the HTML, it will search for script tags and store any it finds, along with its probability of occurring. If the script tag has been stored previously, the program will increase the probability that the tag has appeared. |
|Real       | This is the phase where the program takes a HTTP response, gets the HTML code. The program then searches through the code to add nonce tags to the trusted script tags. To determine which script tags are trusted, the program uses the probability that the script tag occurs which is calculated in the collection phase. |

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

#### Use Cases for Extensions of the Product:

| 1         |                 |
| --------- |  -------------  |
|Phase      |   Real          |
|System     |   * Parses the HTML of the site  |
|           |   * Untrusted script tag found within a trusted script tag |
|Goal       |   * Add a nonce tag to the outside script tag and ensure the untrusted script tag does not run  |

| 2         |                 |
| --------- |  -------------  |
|Phase      |   Real          |
|System     |   * Parses the HTML of the site  |
|           |   * Untrusted script tag found within a untrusted script tag |
|Goal       |   * Ensure no nonce tags and added and neither tags are executed  |

| 3         |                 |
| --------- |  -------------  |
|Phase      |   Real          |
|System     |   * Parses the HTML of the site  |
|           |   * Found inline script tag |
|Goal       |   * Determine whether the script tag is trusted or not and if it is trusted, add a nonce tag  |

### 3.3 Usability Requirements

See 9.5.12. for most systems this will be around one page.

> **9.5.12 Usability requirements**<br>
> Define usability (quality in use) requirements. Usability requirements and objectives for the software system include measurable effectiveness, efficiency, and satisfaction criteria in specific contexts of use.

The goal is to design a proxy program which adheres to appreciate expectations and specifications to create additional security features for web applications. Fulfilling the usability requirements ensures that certain XSS inserted to the website is prevented from executing and safe script tags are applied to prevent websites from breaking due to the security. 

### 3.4 Performance requirements

See 9.5.13. for most systems this will be around one page. Hardware projects also see section 9.4.6.

 **9.5.13 Performance requirements** <br>

The performance requirements section will discuss how a system will perform once it is in use. In order for the performance of a system to be deemed successful, the system must adhere to a set of specific requirements. Furthermore, this section will comprehensively outline what a user should expect when interacting with the system. <br>
 
* The number of simultaneous users that the system can support during the collection phase is 1. However, during the real phase the system is able to support >1 (multiple) users.<br>

* The system should load 98% of the HTML in less than 1 second. <br> 

* If delays are experienced 87% of the HTML should load in 2 seconds.<br>

* The system should not affect the user end of the website. Therefore, this means that if users use any website with our proxy and program enabled, they should not experience any changes in how they are able to utilize the websites. However, if a script tag is considered unsafe the system will affect users as the unsafe script tag will not run hence changing what the website should do. <br>

* The program should have 100% functionality if users use Edge, Chrome or FireFox as browsers.<br>

* During the collection phase the program should be able to identify which script tags contained within the HTML are safe. This will be achieved by the program scanning through websites that are clean. <br>

* The program should insert nonce tags in script tags during the real phase to indicate which script tags are deemed safe.<br>

* The program should be able to notify if script tags in a webpage are not safe. This will be achieved by collecting and reporting unsafe script tags in ‘report-uri.com’.<br> 

* The program should be able to support data encryption when handling HTTP requests to maintain data integrity.<br> 

* The program should be able to manage a single request at once without there being significant disruption in between the host server and the users. <br>

* As the nonce is a pseudo-random value intended for one time use. The program should ensure that at every request the nonce changes.<br>


### 3.5 Logical database requirements

#### Class Diagram ####
![alternative text](http://www.plantuml.com/plantuml/svg/bLLFR_is3BtxKn0vROS4sFM78cZNjLY0kWrY7mCKYiKaQcp94-MkHj7lFih_LRSebeDXa-BZ8_d4N9CJrbL57aMbo2xYXB3OMlDMBzwZ2FY7sYbNGxn9u-TDl7suY-yUqvjqy_GO-3SwCuNIf-STKcaqOUkzpGKHa7Z5tluUGVTBdEK0i9qZnJSt-4fXQGZvxVV1xf5ISw_otlWnpLCOgOxrc6a8CuSNp1mSS_Flok8_5P9RKNR60liZeQyqTkHoTgvS_PscsnvuLOWBZk1T0I6Zhne6otcRu1TiYZ9d9je9fum6aJCJskkZiN0q_iDtIMJUIGtq70GMVomOdPz1hndSVnBWAzeQzjfNaGo4lm5hi5gmiA4CrnWKqe31H44YqvUSweXxVQZXfYnpbJNLHD77H5X-Reap5XTmTIM54mT1k5v3ABLfgnEc_nSV30vGPbNfKd4AlK7bNC1NE5o2VoLm1exC1gWcXyLU1pmd1N30BGy1i-PZUsR2YqzyaxF2NB9nElxC2pAKyQZyfrQElrg_77K-X-0gueV42TSeP7PvgFSC3bPrTacQ3YNYwB1crD4dz0d_DBBU2kis-gMoADa_IygztIcwm9XFQTTR7wlYWFPd9eIkYvXGGAa-MJ_yy-jXBSC6SiDo8sIxJoJiHWaABTkZ18vlDQmzPiztl1npvJ3asXFrPy7wmwndO_sJcOPcduIyUa7nvVGP-j4lmoanw5NlEg4Z3bPQgbSbAv7pnz0g2a2MFM6Elo5I9qtDn3BiU8DZDef0-YbQKn5qXKQpbTdN70jTBsRiOg6ud8d8zxhRVDH94lpjxD6_lnex57buAJe1UKTRr_-HaA_ov_-0kLmbEhI5qjWg7ju_BtvdAxmNEM6CH5p7HADQThP0ZYF_RvPsme44glC4ApK8dd7pWjioQUoYP-6pYELy3NVf_SRrojJ6jUz5MmgicxrxpOUg8lyF)
#### State Diagram ####
![alternative text](http://www.plantuml.com/plantuml/svg/hLN1QXin4BtxAqIWq1O2FGV793I75Xh7h1Tw27iGwx6pH5vj9JcD2VttQfyiUTPoQWpD8MZUl3Sp6hriRgoJnctMQZJo9qTYPlJhzhPspGk9jz58-9_7pvMul9o8dx9nJRiAO61VxB2Ftyfozkb2I1jPOZos2sMe9bzfCe662mkodMujCMM4XhHV6x9km08Y-1Xzjjnsv9lMJxgfVKEaup0OFvAGY04oiR6u4ey0hnDKvUmu02S3gGQR-RvgjI6C78uyEPSlT2UTH3e6XolZWdkzeAklMYcgNQDRwFPXnYn8Ad3wGrXLd19tO1E58tzWm741ICG9KIX5IEs7w1VIDnUMNAbZeiebc6b01XJMnmlkEYTVZFv4b-v9AFAs7smmzvH-nnWC09mmayOcIURHGHRh722dB7wl3SrhqtJEbXfArCXXBhhJBVMWVmUmMJoml0clQGjQowRrsSpxACrlcsl0or1myodx9ulbVj3IYOduKhrVWK-UIQ-Z5ByuixUKLFL6IKT5OvyVbgLSMT2EuD6Td0hkaV6FFZVNefmloB-1oNAmA3CRujrMfSgCTW06uhbkC__3RkOylvbt3LUST9p9BPUhmCpXm3xBTKV8-PR_rUsaGuFwm9xr4zNFS1hRZfLBUZ1JxVXI-9wJ2bjEqQb7dVkwdWVHxipJKzroHWhZqwK-k70Q4haK8HTqs8C_EjgAGk9VvqIyVgXo0UkLQyRGG1GvNd7RTMhhPNMynH0HsTyUFlWtr2usQ_KN)

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

**Use of Python**<br>
The software for this project will be written in python code which is an unfamiliar programming language to most team members as previous courses have focused on Java. This will be a major constraint as team members will have to learn python during this project which will likely slow development progress.  

**Skill levels**<br>
Team members will have different experiences and specialties in software development and cybersecurity. This will be a constraint on the development process as many team members have limited knowledge about nonce tags, XSS and HTML parsing.   

**Timeframe and deadlines**<br>
Timeframes and deadlines will be a major constraint on this project as unexpected events are bound to occur that will affect deadlines such as bugs and code deletion. Other courses that team members take can be an issue if there are overlapping deadlines. There is also the chance that team members cannot access campus resources (labs, meeting rooms etc.) due to the COVID-19 pandemic.

**Performance Expectations**<br>
Performance expectations can be a hindrance as the expectations set by team members before the development process begins may not be met at the conclusion of the project.
This relates to each member of the team as other commitments that team members have will hinder the development process as members will be unable to give 100% of their time/effort to the project.  


### 3.7 Nonfunctional system attributes

Present the systemic (aka nonfunctional) requirements of the product (see ISO/IEC 25010).
List up to twenty systemic requirements / attributes.
Write a short natural language description of the top nonfunctional requirements (approx. five pages).

The nonfunctional requirements of this project are as follows (in descending order of priority): Security, Data integrity, Reliability, Performance, Scalability, Maintainability, and Usability.<br>
<br>
**Security:**<br>
<br>
The main purpose of this project is to increase internet browser security by implementing CSP on all outgoing HTTP requests sent by the host server; security is the top priority.  As such the project will need to produce a program that can perform such implementation without compromising security of both the end user and the host server.<br>
<br>
The program/proxy must also be able to operate without exposing itself to attack. Since the program has a read functionality used to train the system on what to apply the CSP too. The program needs security measures to prevent the possibility of this being exploited. Since exploiting this part of the program would result in ineffective application of the CSP.<br>
<br>
During the reading stage of the programs lifecycle it will need to operate in a way that is secure. If the reading stage can be exploited it could be possible for an attacker to intercept the incoming HTTP requests and train the system to ignore malicious code or input any code the attacker deems fit. If unsecure the attacker could gain the ability to edit more than the script tags. If the program can be exploited in such a way it could lead to an increased possibility of attacks occurring, instead of preventing them.<br>
<br>
During the reading stage the system stores and reads outgoing HTTPS, if not stored properly, or accessible to any outside user this could lead to attackers being able to access this data. The program needs to ensure these files are not accessible. If accessible this could also result in further attacks or privacy breaches.<br>
<br>
Since the program operates as a proxy during each stage of its life cycle the program must also prevent the possibility of exploitation during the encoding stage. If an exploit is discovered there could be potential for an attack to add malicious code to every request processed by the program. Such exploits would once again lead to an increased possibility of attacks affecting any end user of the website.<br>
<br>
**Data integrity:**<br>
<br>
The purpose of the program is to read and encrypt HTTP responses from the host websites server. Since it operates on a proxy the program and the project team need to ensure that the data is encrypted correctly. Ensuring the data sent from the host server is preserved to prevent incorrect or unreadable HTTP responses being sent is essential. If the system can not ensure this then it could result in unreadable HTTP responses sent to the end user.<br> 
<br>
This is one of the highest priorities with this program, failure to ensure data integrity will result in the host website becoming essentially inaccessible to the end user. If the program cannot maintain data integrity then it is deemed a failure.<br>
<br>
**Reliability:**<br>
<br>
The project needs to produce a program capable of running independently as it is implemented by use of a proxy server. Since the proxy is remote to the host and end user reliability is also a top priority as neither the end user or host server have access to the program. Meaning if problems arise due to the use of said program external intervention is required to initiate recover.<br>
<br>
Since external intervention or termination of the proxy is required if the program malfunctions then the project becomes null and void. So the program needs to be as robust as possible as failure can cause the host server to lose business, traffic etc, depending on the host site. Failure could potentially result in a security risk depending on the severity of the failure, if the program is the only CSP or security protocol the host server is operating.<br>
<br>
Reliability will be determined by the programs ability to not only encode the correct script tags sent in the HTTP response from the host server, but also maintain data integrity. By correctly identifying which script tags to encode the program can be as reliable.<br>
<br>
**Performance:**<br>
<br>
The program needs to be able to operate in such a way that it can handle a single request at once with limited interference/lag between the host server and the end user. If the program is unable to handle a single request without hindering normal use of the host website, the owner of the host server may see the program as more of a nuisance than a necessary security measure, especially when the program will need to handle multiple requests at once.<br>
<br>
If the program is unable to adhere to the performance requirements stated above this could result in loss of business/traffic to the host server. If this were to occur it could become a case of functionality over security resulting in the program being abandoned. If the program is unable to meet these performance requirements then the project has failed.<br>
<br>
**Scalability:**<br>
<br>
This program will potentially need to be able to handle multiple requests at once, with the same amount of limited interference. Scalability is supplemental to performance since if the program is unable to handle a single HTTP request with acceptable latency, then scalability will also be affected. So by meeting the above performance requirements, scalability will be the next non-functional requirement the project team can address.<br> 
<br>
Ensuring the program can operate at the same efficiency whilst handling multiple requests is paramount to ensuring performance capabilities are maintained.  If the program is unable to handle such requests this will lead to downgraded performance. As Stated above, this could lead to the proxy being abandoned in favour of performance over security.<br> 
<br>
**Maintainability:**<br>
<br>
As the program is to be designed in such a manner that it operates on a proxy server it can be considered to be an independent system. Meaning the end user and the owner of the host server cannot and do not interact with the program. The program operates between the two independently of the others. As such maintainability of the program by the end user and host server of the HTTP requests are a null issue.<br>

However, the program may still require maintenance as HTTP continues to change and become increasingly complex. The program needs to be built in a way that will allow for updates and regular patching if it is deemed necessary. Or the program needs to be designed in such a way that it can account for the increasing complexity.<br>

Handling some of these changes may be outside the scope of this project, as the scope pertains only to the script tags of an HTTP request. Thus, this level of maintainability is not a priority of this project. However, the program needs to be designed to be not only functional but also easy to understand, modify and patch if Redshield sees the need.<br>

**Usability:**<br>

Due to the nature of the program being run in as a proxy, Usability by the end user and the  host server owner is null. However, the program still needs to be easy to use by the client Redshield. As such the program needs to be easy to set up, initiate, and switch between modes. Usability is ranked low as if all other criteria are met then usability will be met as well. Following this logic, if the program can maintain performance, ensure security and data integrity then the program, since it operates independently, would meet usability requirements.<br>

### 3.8 Physical and Environmental Requirements 

For systems with hardware components, identify the physical characteristics of that hardware (9.4.10) and environment conditions in which it must operate (9.4.11).  Depending on the project, this section may be from one page up to 5 pages.<br>

Due to the fact that this project is a solely software-based project there are no physical or environmental requirements involved. The only requirement this project has is that there must be access to a computer to run the program. Furthermore, the computer must have python installed on it. It is vital that the computer is able to run python version 3.0 or higher. <br>  

### 3.9 Supporting information

see 9.5.19. 

## 4. Verification

3 pages outlining how you will verify that the product meets the most important specific requirements. The format of this section should parallel section 3 of your document (see 9.5.18). Wherever possible (especially systemic requirements) you should indicate testable acceptance criteria.


### 3.2 Functions

To verify that the project satisfies it’s required functions in a reliable and complete way, a combination of continuous integration testing, automated testing and manual testing will be done. Each case specified in section 3.2 will be manually tested to ensure that when the specified system input has happened, the outcome will be what the specified goal states. This will allow any case to be tested, to ensure there are no issues and validate that the product meets its specifications laid out in section 3.2. Any unexpected behaviour of the program will be logged as an issue to be fixed. Furthermore, automated tests will be added to test for a range of different inputs, including invalid and no input.

For the minimum viable product, only the cases outlined in section 3.2 relating to this will be tested against. Once the minimum viable product has been attained, then the cases outlined in the extension section of 3.2 will be tested against to verify the programs extended behaviour.

### 4.6 Design constraints

**Use of Python**<br>
To verify that this project remains in python, team members will go learn what they need to about the language in context to the project, will use an IDE that supports Python, and will make sure their code follows Python coding standards.   

**Skill levels**<br>
To verify that each team member has the required skill level, they will learn what they need to about the concepts involved in this project and will make an effort to ask for assistance when needed.   

**Timeframe and deadlines**<br>
To verify that project deadlines are met, weekly meetings will be held to review and assess progress made by team members. During the development progress, scope will be evaluated. 

**Performance Expectations**<br>
To verify that team members are contributing equally to this project, each member must commit at least 8 hours per week to the project. Contributions of each team member will primarily be tracked by their commits to the project’s Gitlab with communications on the project’s Mattermost also being assessed. 

### 4.7 Nonfunctional system attributes

**Security:**<br>

Verification of the read stage, can be obtained by asserting the HTML responses are coming from the correct IP.<br>

During the read stage the program will store collected HTML responses from the host website. To ensure security is maintained, these collected files will need to be inaccessible to external users of the program.<br>

During the operational stage the program needs to ensure nonce tags are applied to the correct script tags (those deemed safe by the program), and report correctly those deemed unsafe by the program. This will be verified during the testing phase of the project, ensuring the program can identify the correct script tags.<br>

**Data integrity:**<br>

As stated above, data integrity can be verified by use of hashing. Ensuring the outgoing and incoming data matches.<br>

**Reliability:**<br>

Reliability will be verified by the programs ability to ensure data integrity, security and performance.<br>

**Performance:**<br>

Performance will be verified relative to the guidelines set in section 3.4<br>

**Scalability:**<br>

Scalability will be verified relative to the guidelines set in section 3.4<br>

**Maintainability:**<br>

Maintainability will be verified by use of standard coding practice (use of java docs, commenting, appropriate classes and methods) to ensure the program is able to be used and maintained by the client.<br>

**Usability:**<br>

Usability can be verified, by how well the program meets the above requirements. <br>


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
|Code being deleted |Technical |  Likely | Moderate-Significant (depending on amount/importance)| Use Gitlab |
|Code being overwritten | Technical |  Very Likely | Moderate| Mattermost to notify others of commitments and if code is overwritten, use gitlab to restore it |
|Team member unable to contribute for unforeseen reasons |Teamwork |  Possible | Moderate-Significant(depending on project stage)| Keep good documentation of what is done so others can pick up tasks without too much hassle |
|Team member has other commitments which cause them to not be available  |Teamwork |  Very Likely  |Minor| Keep good documentation of what is done so others can pick up tasks without too much hassle and ensure no one is out of the loop |
|Team member has not done their specified work| Teamwork |Possible| Significant | Regularly meet up and contact team members to ensure everyone is on track  |
|COVID Lockdown|  |Very Likely| Significant | Ensure everyone is able to connect online and all work is online |
|Misunderstanding about the project requirements| Requirements |Likely| Moderate | Ensure constant communication with the client and clear up any uncertainties promptly |
|Changes to project requirements| Requirements | Possible | Significant | Ensure there is a clear understanding of what is required from the team from the beginning and ensure constant communication with client |
|Bugs within code go undetected| Technical |Very Likely| Significant | Create tests for the program, to test different aspects of it and minimize the number of errors that go undectected |
|Team members burning out| Teamwork |Likely| Significant | Ensure everyone is communicating with each other so the team knows if someone is doing too much work and ensure all work is evenly divided |


### 5.4 Health and Safety

Document here project requirements for Health and Safety. All teams must state in this section:

1. How teams will manage computer-related risks such as Occupational Over Use, Cable management, etc.  

2. Whether project work requires work or testing at any external (off-campus) workplaces/sites. If so, state the team's plans for receiving a Health and Safety induction for the external workplaces/sites. If the team has already received such an induction, state the date it was received. 

3. Whether project work requires the team test with human or animal subjects? If so, explain why there is no option but for the team to perform this testing, and state the team's plans for receiving Ethics Approval _prior_ to testing.

Also document in this section any additional discussions with the School Safety Officer regarding Health and Safety risks. Give any further information on relevant health and safety regulations, risks, and mitigations, etc.

#### Occupational Overuse

To manage occupational overuse, team members will ensure that they take regular breaks away from their devices to ensure they are doing different tasks. Furthermore, realistic deadlines will be set for tasks and the team will practice good time management to prevent overuse in order to meet deadlines. 

Additionally, team members will have ergonomic workspaces so that any required equipment will be nearby and easily accessible. This will also encompass ensuring desks are at the correct height to encourage correct posture and reduce straining. Correct postures will be promoted and ensured for all team members and the team will use comfortable chairs which if possible, will have back support. This will reduce straining and incorrect postures in a work environment, mitigating occupational overuse and its potential symptoms. 

https://www.southerncross.co.nz/group/medical-library/occupational-overuse-syndrome-oos

#### Cable Management

Unmanaged cables are a safety risk as team members or nearby people can get caught on them or trip on them. In order to manage this risk, all team members will ensure that any cables they use will be kept underneath their desk, mitigating the possibility of someone getting caught on it. Furthermore, all cables which are not being used will be stored away in a cupboard or bag to further mitigate the risk unmanaged cables pose. 

#### Health and Safety at External Workplaces

The project does not require any work or testing to be held off-campus. However, there is a possibility that some meetings will be held at Red Shield’s office. In order to receive a Health and Safety induction for this external workplace, team members will get in contact with the client to arrange this, prior to any work being done at the clients' office. 

#### Human or Animal Test Subjects

This project does not include any human or animal subjects. This is because all testing can and will be done by the team, using different web applications. 


#### 5.4.1 Safety Plans

Project requirements do not involve risk of death, serious harm, harm or injury.

## 6. Appendices
### 6.1 Assumptions and dependencies 

One page on assumptions and dependencies (9.5.7).<br>
We are assuming that during the collection phase, the websites scanned will be clean. 
We are assuming that anyone using our program is using either Edge, Chrome or FireFox.
A dependency is that the browsers used must be either Edge, Chrome or FireFox.


### 6.2 Acronyms and abbreviations

CSP - Content Security Policy
MITM  - Man In The Middle
DOM - Document Object Model
HTML - Hyper-Text Markup Language
HTTP - Hyper-Text Transfer Protocol
XSS - Cross Site Scripting

## 7. Contributions

| Contributors  | Sections     |
| ------        |  ----------  |
|    Dylan      |              |
|    Isabella   | 1, 1.1, 1.2, 1.3.1, 5.4.1, 5.2, 3.2, 3.3, 5.3, 5.4, 5.4.1  |
|    Damien     | 1.1, 1.2,1.3.1, 3.7, 4.7, 5.2    |
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
