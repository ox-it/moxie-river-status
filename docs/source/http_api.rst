========
HTTP API
========

GET /
=====

.. code-block:: json

    {
      "_last_updated": "2013-09-18 14:20:18.257317",
      "_links": {
        "self": {
          "href": "/rivers/"
        }
      },
      "rivers": [
        {
          "name": "Godstow",
          "status": "green",
          "status_description": "No restrictions"
        },
        {
          "name": "Isis",
          "status": "green",
          "status_description": "No restrictions"
        }
      ]
    }

Status values
-------------

The property ``status`` and ``status_description`` can have the following values.

================================    =======================================================================
Status                              Description
================================    =======================================================================
green                               No restrictions
blue                                No novice coxes
yellow                              Senior crews only
red                                 No crews allowed out
grey                                Flag not currently being maintained
black                               No rowing for any crews. Isis on Environment Agency flood watch.
================================    =======================================================================

Eventually, a different value for ``status`` might be displayed, the ``status_description`` will then be "Undefined".
