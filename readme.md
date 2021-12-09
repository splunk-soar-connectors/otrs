[comment]: # "Auto-generated SOAR connector documentation"
# OTRS

Publisher: Tokyo Electron Device  
Connector Version: 1\.0\.4  
Product Vendor: OTRS  
Product Name: OTRS  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 1\.2\.283  

This app allows OTRS ticket management system by implementing actions such as 'create ticket', 'get ticket' etc\. You have to create and set up Web Services on an OTRS services in advance\. Network Transport must be 'HTTP\:\:REST'

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a OTRS asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**device\_url** |  required  | string | Device URL including the port, e\.g\. http\://otrs\.mydomain\:8080
**verify\_server\_cert** |  required  | boolean | Verify server certificate if you uses https
**username** |  required  | string | Username
**password** |  required  | password | Password
**service\_name** |  required  | string | OTRS web service name
**mapping\_create\_ticket** |  optional  | string | Route mapping for creating a ticket \(default \: '/TicketCreate'\)
**mapping\_update\_ticket** |  optional  | string | Route mapping for updating a ticket \(default \: '/TicketUpdate'\)
**mapping\_get\_ticket** |  optional  | string | Route mapping for getting a ticket \(default \: '/TicketGet'\)
**mapping\_search\_ticket** |  optional  | string | Route mapping for searching a ticket \(default \: '/TicketSearch'\)

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied credentials\.  
[create ticket](#action-create-ticket) - Create ticket  
[update ticket](#action-update-ticket) - Update a ticket  
[get ticket](#action-get-ticket) - Get ticket  
[run query](#action-run-query) - Run query for searching ticket  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied credentials\.

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'create ticket'
Create ticket

Type: **generic**  
Read only: **False**

This action requires some parameters for will create ticket

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**Ticket\:Title** |  required  | Ticket title | string | 
**Ticket\:CustomerUser** |  required  | Customer user name | string | 
**Ticket\:Priority** |  required  | Ticket priority | string | 
**Ticket\:State** |  required  | Ticket state | string | 
**Ticket\:Queue** |  required  | Ticket queue | string | 
**Article\:Subject** |  required  | Ticket article subject | string | 
**Article\:Body** |  required  | Ticket article body | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.summary | string | 
action\_result\.status | string | 
action\_result\.parameter\.Ticket\:Queue | string | 
action\_result\.parameter\.Ticket\:Title | string | 
action\_result\.parameter\.Ticket\:State | string | 
action\_result\.parameter\.Ticket\:Priority | string | 
action\_result\.parameter\.Article\:Subject | string | 
action\_result\.parameter\.Article\:Body | string | 
action\_result\.parameter\.Ticket\:CustomerUser | string | 
action\_result\.data\.\*\.TicketNumber | string | 
action\_result\.data\.\*\.TicketID | string | 
action\_result\.data\.\*\.ArticleID | string |   

## action: 'update ticket'
Update a ticket

Type: **generic**  
Read only: **False**

This action requires ticket id and some parameters for will update ticket

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**Ticket\:TicketID** |  required  | Ticket id of updating ticket | string | 
**Ticket\:Title** |  optional  | Ticket title | string | 
**Ticket\:CustomerUser** |  optional  | Customer user | string | 
**Ticket\:Priority** |  optional  | Ticket priority | string | 
**Ticket\:State** |  optional  | Ticket state | string | 
**Ticket\:Queue** |  optional  | Ticket queue | string | 
**Article\:Subject** |  optional  | Ticket article subject | string | 
**Article\:Body** |  optional  | Ticket article body | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.summary | string | 
action\_result\.status | string | 
action\_result\.parameter\.Ticket\:Queue | string | 
action\_result\.parameter\.Ticket\:TicketID | string | 
action\_result\.parameter\.Ticket\:Title | string | 
action\_result\.parameter\.Ticket\:State | string | 
action\_result\.parameter\.Ticket\:Priority | string | 
action\_result\.parameter\.Article\:Subject | string | 
action\_result\.parameter\.Article\:Body | string | 
action\_result\.parameter\.Ticket\:CustomerUser | string | 
action\_result\.data\.\*\.TicketNumber | string | 
action\_result\.data\.\*\.TicketID | string |   

## action: 'get ticket'
Get ticket

Type: **generic**  
Read only: **True**

This action requires ticket id for will get ticket

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**Ticket\:TicketID** |  required  | Ticket id of retreaving ticket | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.summary | string | 
action\_result\.status | string | 
action\_result\.parameter\.Ticket\:TicketID | string | 
action\_result\.data\.\*\.CustomerUserID | string | 
action\_result\.data\.\*\.SLAID | string | 
action\_result\.data\.\*\.Lock | string | 
action\_result\.data\.\*\.CreateTimeUnix | string | 
action\_result\.data\.\*\.ArchiveFlag | string | 
action\_result\.data\.\*\.TypeID | string | 
action\_result\.data\.\*\.CustomerID | string | 
action\_result\.data\.\*\.Owner | string | 
action\_result\.data\.\*\.GroupID | string | 
action\_result\.data\.\*\.RealTillTimeNotUsed | string | 
action\_result\.data\.\*\.Changed | string | 
action\_result\.data\.\*\.OwnerID | string | 
action\_result\.data\.\*\.EscalationTime | string | 
action\_result\.data\.\*\.Age | string | 
action\_result\.data\.\*\.PriorityID | string | 
action\_result\.data\.\*\.ServiceID | string | 
action\_result\.data\.\*\.Type | string | 
action\_result\.data\.\*\.Responsible | string | 
action\_result\.data\.\*\.StateID | string | 
action\_result\.data\.\*\.Title | string | 
action\_result\.data\.\*\.ResponsibleID | string | 
action\_result\.data\.\*\.ChangeBy | string | 
action\_result\.data\.\*\.Created | string | 
action\_result\.data\.\*\.Priority | string | 
action\_result\.data\.\*\.UntilTime | string | 
action\_result\.data\.\*\.EscalationUpdateTime | string | 
action\_result\.data\.\*\.Queue | string | 
action\_result\.data\.\*\.QueueID | string | 
action\_result\.data\.\*\.State | string | 
action\_result\.data\.\*\.Title | string | 
action\_result\.data\.\*\.CreateBy | string | 
action\_result\.data\.\*\.TicketID | string | 
action\_result\.data\.\*\.StateType | string | 
action\_result\.data\.\*\.UnlockTimeout | string | 
action\_result\.data\.\*\.EscalationResponseTime | string | 
action\_result\.data\.\*\.EscalationSolutionTime | string | 
action\_result\.data\.\*\.LockID | string | 
action\_result\.data\.\*\.TicketNumber | string |   

## action: 'run query'
Run query for searching ticket

Type: **investigate**  
Read only: **True**

This action requires search query in json format that consists of key names and list of values\. e\.g\. \{"Queues"\: \["Raw", "Junk"\]\}\. The result is list of ticket ids\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**query** |  required  | Search query in json format for searching ticket | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.summary | string | 
action\_result\.status | string | 
action\_result\.parameter\.query | string | 
action\_result\.data\.\*\.TicketID | string | 