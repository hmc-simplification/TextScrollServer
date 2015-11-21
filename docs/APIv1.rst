TextScrollServer API version 1
==============================


.. http:get:: /users
   :synopsis: List of all users.

   A list of all users - requires admin or researcher authorization.

   **Example request**:

   .. sourcecode:: http

      GET /users HTTP/1.1
      Host: textscroll.cs.hmc.edu

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/json

      [
        ["user1", "user2", "user3"]
      ]

   :reqheader Authorization: optional OAuth token to authenticate
   :resheader Content-Type: text/json

   :statuscode 200: no error
   :statuscode 401: not an authenticated administrator or researcher

.. http:post:: /users/create_user
   :synopsis: Create a new user.

   **Example request**:

   .. sourcecode:: http

      POST /users/create_user
      Host: textscroll.cs.hmc.edu

.. http:get:: /users/(string:user_id)
.. http:post:: /users/(string:user_id)/authenticate
.. http:post:: /users/(string:user_id)/change_password
.. http:get:: /users/(string:user_id)/trials
.. http:get:: /users/(string:user_id)/trials/(int:trial_id)
.. http:post:: /users/(string:user_id)/trials/(int:trial_id)
.. http:get:: /users/(string:user_id)/settings
.. http:get:: /users/(string:user_id)/settings/(string:setting_id)
.. http:post:: /users/(string:user_id)/settings/(string:setting_id)
.. http:get:: /users/(string:user_id)/library
.. http:get:: /users/(string:user_id)/library/(string:text_id)
.. http:post:: /users/(string:user_id)/library/(string:text_id)
.. http:get:: /users/(string:user_id)/library/(string:text_id)/(string:text_attr)
.. http:post:: /users/(string:user_id)/library/(string:text_id)/(string:text_attr)
.. http:get:: /trials
.. http:get:: /trials/(int:trial_id)
