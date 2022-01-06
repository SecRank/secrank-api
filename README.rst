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
  usage: secrank [-h] [-d DOMAIN] [-a ANSWER] [-s SORT] [-l LIMIT] [-st SORT_TYPE] [-rtype RTYPE] [-top TOP] [-tail TAIL]
  secrank-pdns command line tool
  optional arguments:
    -h, --help            show this help message and exit
    -d DOMAIN, --domain DOMAIN
                          query domain
    -a ANSWER, --answer ANSWER
                          response rrdata
    -s SORT, --sort SORT  sort by
    -l LIMIT, --limit LIMIT
                          limit
    -st SORT_TYPE, --sort-type SORT_TYPE
                          sort by
    -rtype RTYPE, --rtype RTYPE
                          request type
    -top TOP, --top TOP   top rows
    -tail TAIL, --tail TAIL
                          last rows

::

   Examples:
   secrank pdns -d www.baidu.com
   secrank pdns -d www.baidu.com -top 10
   secrank pdns -d www.baidu.com -l 100 -top 100 -s count
