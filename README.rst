netmon
======

Command line network monitor for linux. Written in python.

|asciicast|

Install
-------

::

   pip install git+https://github.com/TheDen/netmon

Run
---

``$ netmon``

By default ``netmon`` will try to detect your network device. If it
fails, you can specify the network device, e.g., ``netmon wlan1``

Development
-----------

-  PRs are more than welcome
-  Building—``make build``
-  Publishing—``make publish``
-  Converting the markdown readme to ``rst``—``make convert``
-  ``make clean``—a simple ``git clean -fdx``

.. |asciicast| image:: https://asciinema.org/a/178907.png
   :target: https://asciinema.org/a/178907
