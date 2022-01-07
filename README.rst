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


pdns
~~~~~~~~~~~~~~~~~~~

::

   $ secrank pdns -h                                  
   usage: cli.py [-h] [-d DOMAIN] [-a ANSWER] [-l LIMIT] [-rtype RTYPE]

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


whois
~~~~~~~~~~~~~~~~~~~

::

   $ secrank whois -h          
   usage: cli.py [-h] [-c COLUMN] [-f FIND] [-d DOMAIN] [-l LIMIT]

   secrank-whois command line tool

   optional arguments:
   -h, --help            show this help message and exit
   -c COLUMN, --column COLUMN
                           column: org | email | phone | nameserver | name
   -f FIND, --find FIND  find value
   -d DOMAIN, --domain DOMAIN
                           query domain
   -l LIMIT, --limit LIMIT
                           limit

::

   Examples:
   secrank whois -d baidu.com
   secrank whois -f zhangsan
   secrank whois -f zhangsan
   secrank whois +86.13511629585 -c phone
