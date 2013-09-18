HTTP API
========

GET /
-----

.. code-block:: json

    {
      "_last_updated": "2013-09-18 11:31:22.709266",
      "rivers": [
        {
          "name": "Godstow",
          "status": "green"
        },
        {
          "name": "Isis",
          "status": "green"
        }
    ]
    }

The ``status`` value is one of:

 * ``green``: Green: No restrictions
 * ``blue``: Blue: No novice coxes
 * ``yellow``: Yellow: Senior crews only
 * ``red``: Red: No crews allowed out
 * ``grey``: Grey: Flag not currently being maintained
