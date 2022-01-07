secrank-api
--------------

Installation
~~~~~~~~~~~~~~~~~

::

   pip3 install secrank


API Token
~~~~~~~~~~~~~~~~~~~

::

   ~/.secrank.lic


Usage
~~~~~~~~~~~~~~~~~~~

::

  secrank <api_type> [options]
  
  Example: secrank pdns -d www.google.com


PassiveDNS
~~~~~~~~~~~~~~~~~~~

::

   $ secrank pdns -h
   usage: secrank [-h] [-d DOMAIN] [-a ANSWER] [-l LIMIT] [-rtype RTYPE]

   secrank-pdns command line tool

   optional arguments:
   -h, --help            show this help message and exit
   -d DOMAIN, --domain DOMAIN
                           query domain
   -a ANSWER, --answer ANSWER
                           response rrdata
   -l LIMIT, --limit LIMIT
                           limit
   -rtype RTYPE, --rtype RTYPE
                           request type

::

   Examples:
   secrank pdns -d www.baidu.com
   secrank pdns -d www.baidu.com -top 10
   secrank pdns -d www.baidu.com -l 100 -top 100 -s count
   secrank pdns -d www.baidu.com -l 100 -top 100 -s count -st asc
   secrank pdns -d www.baidu.com -l 100 -top 100 -s count -st desc


Whois
~~~~~~~~~~~~~~~~~~~

::

   $ secrank whois -h
   usage: secrank [-h] [-fc FINDCOLUMN] [-f FIND] [-d DOMAIN] [-l LIMIT] [-c COLUMNS]

   secrank-whois command line tool

   optional arguments:
   -h, --help            show this help message and exit
   -fc FINDCOLUMN, --find-column FINDCOLUMN
                           column: org | email | phone | nameserver | name
   -f FIND, --find FIND  find value
   -d DOMAIN, --domain DOMAIN
                           query domain
   -l LIMIT, --limit LIMIT
                           limit
   -c COLUMNS, --columns COLUMNS
                           columns: domainName, domainNames, createdDate, expiresDate, updatedDate, nameServers, whoisServerList, status, adminAddress, adminCity, adminCountry, adminEmail,
                           adminFax, adminName, adminOrganization, adminPostalCode, adminState, adminTelephone, registrantAddress, registrantCity, registrantCountry, registrantEmail,
                           registrantFax, registrantName, registrantOrganization, registrantPostalCode, registrantState, registrantTelephone, techAddress, techCity, techCountry, techEmail,
                           techFax, techName, techOrganization, techPostalCode, techState, techTelephone

::

   Examples:
   secrank whois -d baidu.com
   secrank whois -f zhangsan
   secrank whois -f zhangsan
   secrank whois +86.13511629585 -c phone


Trends
~~~~~~~~~~~~~~~~~~~

::

   $ secrank trends -h                      
   usage: secrank [-h] [-v] [-d DOMAIN] [-b BEGIN] [-e END] [-l LAST] [-sld] [-c COLUMNS]

   secrank-trends command line tool

   optional arguments:
   -h, --help            show this help message and exit
   -v, --verbose         Verbose
   -d DOMAIN, --domain DOMAIN
                           query domain
   -b BEGIN, --begin BEGIN
                           date begin
   -e END, --end END     date end
   -l LAST, --last LAST  last days
   -sld, --sld           sld
   -c COLUMNS, --columns COLUMNS
                           columns: noError,totalCount,aCount,aaaaCount,nsCount,cnameCount,soaCount,mxCount,txtCount,srvCount,dnameCount,dsCount,rrsigCount,nsecCount,nsec3Count,nullCount,clien
                           tipCount,subdomainCount,pointIPaCount,pointIPaaaaCount,pointIPcnameCount,pointIPdnameCount,pointIPdsCount,pointIPmxCount,pointIPnsCount,pointIPnsec3Count,pointIPnsec
                           Count,pointIPnullCount,pointIPrrsigCount,pointIPsoaCount,pointIPsrvCount,pointIPtotalCount,pointIPtxtCount

::

   Examples:
   secrank trends -d www.baidu.com -l 20
   secrank trends -d baidu.com -l 20 -sld
   secrank trends -d www.baidu.com -l 20 -v
