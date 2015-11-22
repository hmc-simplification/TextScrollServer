API version 1
=============

.. http:get:: /users
   :synopsis: List of all users.

   A list of all users - requires admin or researcher authorization.

   **Example request**:

   .. sourcecode:: http

      GET /users HTTP/1.1
      Host: textscroll.cs.hmc.edu
      Authorization: Credential=alsdkfjqeprt798sdhvzxkfnioq34ruaps98dfyaskjcan

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
          "users": [
              "user1",
              "user2",
              "user3"
          ]
      }

   :reqheader Authorization:
      encrypted token for authentication, or a username/password combo

   :statuscode 200: no error
   :statuscode 401: not an authenticated administrator or researcher

.. http:post:: /users/create_user
   :synopsis: Create a new user.

   Creates a new user `user_id` with the application, logs them in, and
   returns a token to be used for future authentication.

   **Example request**:

   .. sourcecode:: http

      POST /users/create_user
      Host: textscroll.cs.hmc.edu
      Content-Type: application/x-www-form-urlencoded

      username=MyNewUserName&password=SuPeRH@x0rPa$$w()rD

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 201 Created
      Vary: Accept
      Content-Type: application/json
      Location: https://textscroll.cs.hmc.edu/api/v1/users/MyNewUserName

      token=alsdkfjqeprt798sdhvzxkfnioq34ruaps98dfyaskjcan

   :statuscode 201: The user was successfully created
   :statuscode 400: The username is malformed (i.e. invalid)
   :statuscode 409: The given username exists

.. http:get:: /users/(string:user_id)
   :synopsis: Get a user

   Gets information about `user_id`.

   **Example request**:

   .. sourcecode:: http

      GET /users/MyUserName
      Host: textscroll.cs.hmc.edu

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
         "username": "MyUserName",
         "trials": [
            1,
            3,
            11
         ],
         "library": [
            "The Once and Future King",
            "A Brief History of Time"
         ],
         "settings": {
            "FontSize": "Large",
            "FontColor": "Black",
            "Theme": "Light"
         }
      }

   :statuscode 200: The user could be found
   :statuscode 400: The username is malformed
   :statuscode 404: The user does not exist

.. http:post:: /users/(string:user_id)/authenticate
   :synopsis: Authenticate user

   Authenticates `user_id`.

   **Example request:**

   .. sourcecode:: http

      POST /users/MyUserName/authenticate
      Host: textscroll.cs.hmc.edu
      Authorization: Credential=SuPeRH@x0rPa$$w()rD

   **Example response:**

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json 

      {
         "authenticated": true
      }

   :reqheader Authorization:
      Authorization for the request in the form of the user's password.

   :statuscode 200: User was authenticated correctly
   :statuscode 400: The username is malformed
   :statuscode 404: User does not exist

.. http:post:: /users/(string:user_id)/change_password
   :synopsis: Change the password

   Changes `user_id`'s password, invalidates all existing sessions, and
   returns a new valid session token.

   **Example request:**

   .. sourcecode:: http

      POST /users/MyUserName/change_password
      Host: textscroll.cs.hmc.edu
      Authorization: Credential=SuPeRH@x0rPa$$w()rD

      new_password=XxXtr4SuPeRH@x0rPa$$w()rD

   **Example Response:**

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
         "password_changed": true,
         "new_token": oqwe879fasokdljfqnl3o4fi7asicvqjwek
      }

   :reqheader Authorization:
      Authorization for the request - a token or password

   :statuscode 200: Password was successfully changed
   :statuscode 400: The username is malformed
   :statuscode 400: The password was invalid
   :statuscode 400: The new password is invalid
   :statuscode 404: User does not exist

.. http:get:: /users/(string:user_id)/trials
   :synopsis: The user's trials

   Returns a list of the trial-ids that `user_id` had participated in.

   Requires administrator or researcher credentials.

   **Example Request:**

   .. sourcecode:: http

      GET /users/MyUserName/trials
      Host: textscroll.cs.hmc.edu
      Authorizaton: Credential=s0upersecrett0ken

   **Example Response:**

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
         "trials": [
            1,
            3,
            11
         ],
      }

   :reqheader Authorization:
      Authorizes the user for this request - must be an administrator or
      researcher credential

   :statuscode 200: The trials were returned
   :statuscode 400: The username was malformed
   :statuscode 401: Not an administrator or researcher
   :statuscode 404: User does not exist

.. http:get:: /users/(string:user_id)/trials/(int:trial_id)
   :synopsis: A specific trial.

   Returns the trial for user `user_id` and trial `trial_id`

   Requires administrator or researcher credentials.

   **Example Request:**

   .. sourcecode:: http

      GET /users/MyUserName/trials/1
      Host: textscroll.cs.hmc.edu
      Authorizaton: Credential=s0upersecrett0ken

   **Example Response:**

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
         1: {
            "trial_data": "stuff",
            "other_data": "other_stuff"
         }
      }

   :reqheader Authorization:
      Authorizes the user for this request - must be an administrator or
      researcher credential.

   :statuscode 200: The trial was returned
   :statuscode 400: The username was malformed
   :statuscode 400: The trial doesn't exist for this user
   :statuscode 401: Not an administrator or researcher
   :statuscode 404: User does not exist
   :statuscode 404: Trial does not exist

.. http:get:: /users/(string:user_id)/settings
   :synopsis: User settings

   Returns the settings for `user_id`.

   **Example Request:**

   .. sourcecode:: http

      GET /users/MyUserName/settings
      Host: textscroll.cs.hmc.edu
      Authorizaton: Credential=s0upersecrett0ken

   **Example Response:**

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
         "settings": {
            "FontSize": "Large",
            "FontColor": "Black",
            "Theme": "Light"
         }
      }

   :reqheader Authorization:
      Authorizes the user for this request - can be a token or a password.

   :statuscode 200: The settings could be found
   :statuscode 400: The username was malformed
   :statuscode 401: User is not authenticated
   :statuscode 404: User does not exist

.. http:get:: /users/(string:user_id)/settings/(string:setting_id)
   :synopsis: Specific setting value

   Returns the setting value of `setting_id` for `user_id`.

   **Example Request:**

   .. sourcecode:: http

      GET /users/MyUserName/settings/FontSize
      Host: textscroll.cs.hmc.edu
      Authorizaton: Credential=s0upersecrett0ken

   **Example Response:**

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
         "FontSize": "Large"
      }

   :reqheader Authorization:
      Authorizes the user for this request - can be a token or a password.

   :statuscode 200: The setting was valid and had a value
   :statuscode 400: The username was malformed
   :statuscode 400: The setting does not exist
   :statuscode 401: User is not authenticated
   :statuscode 404: User does not exist

.. http:post:: /users/(string:user_id)/settings/(string:setting_id)
   :synopsis: Set setting value

   Sets the value of `setting_id` for `user_id`.

   **Example Request:**

   .. sourcecode:: http

      POST /users/MyUserName/settings/FontSize
      Host: textscroll.cs.hmc.edu
      Authorizaton: Credential=s0upersecrett0ken

      FontSize=Small

   **Example Response:**

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
         "FontSize": "Small"
      }

   :reqheader Authorization:
      Authorizes the user for this request - can be a token or a password.

   :statuscode 200: The setting could be updated
   :statuscode 400: The username was malformed
   :statuscode 400: The setting does not exist
   :statuscode 401: User is not authenticated
   :statuscode 404: User does not exist

.. http:get:: /users/(string:user_id)/library
   :synopsis: Get user library

   Get `user_id`'s text library.

   **Example Request:**

   .. sourcecode:: http

      GET /users/MyUserName/library
      Host: textscroll.cs.hmc.edu
      Authorizaton: Credential=s0upersecrett0ken

   **Example Response:**

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
         "library": [
            "The Once and Future King",
            "A Brief History of Time"
         ]
      }

   :reqheader Authorization:
      Authorizes the user for this request - can be a token or a password.

   :statuscode 200: The library was returned.
   :statuscode 400: The username was malformed
   :statuscode 401: User is not authenticated
   :statuscode 404: User does not exist

.. http:get:: /users/(string:user_id)/library/(string:text_id)
   :synopsis: Get text from user library

   Get the text associated with `text_id` from `user_id`'s text library.

   **Example Request:**

   .. sourcecode:: http

      GET /users/MyUserName/library/The%20Once%20and%20Future%20King
      Host: textscroll.cs.hmc.edu
      Authorizaton: Credential=s0upersecrett0ken

   **Example Response:**

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
         "bookmarks": [30, 80, 117],
         "title": "The Once and Future King",
         "pages": "lots",
         "last page read": 3,
         "preview": "...excerpt...",
         "contents": Object(compressed_contents)
      }

   :reqheader Authorization:
      Authorizes the user for this request - can be a token or a password.

   :statuscode 200: The text was returned
   :statuscode 400: The username was malformed
   :statuscode 401: User is not authenticated
   :statuscode 404: User does not exist
   :statuscode 404: The text does not exist

.. http:post:: /users/(string:user_id)/library/(string:text_id)
   :synopsis: Add text to user library

   Add a text to `user_id`'s library with `text_id` name.

   **Example Request:**

   .. sourcecode:: http

      POST /users/MyUserName/library/The%20Once%20and%20Future%20King
      Host: textscroll.cs.hmc.edu
      Authorizaton: Credential=s0upersecrett0ken

      title=The%20Once%20and%20Future%20King&bookmarks=30,80,117

   **Example Response:**

   .. sourcecode:: http

      HTTP/1.1 201 Created
      Content-Type: application/json
      Location: https://textscroll.cs.hmc.edu/api/v1/users/MyUserName/library/The%20Once%20and%20Future%20King

   :reqheader Authorization:
      Authorizes the user for this request - can be a token or a password.

   :statuscode 201: The text was created
   :statuscode 400: The username was malformed
   :statuscode 400: The text was malformed
   :statuscode 401: User is not authenticated
   :statuscode 404: User does not exist

.. http:get:: /users/(string:user_id)/library/(string:text_id)/(string:text_attr)
   :synopsis: Get an attribute of the text

   Get the attribute named by `text_attr` of the text `text_id` in `user_id`'s library.

   **Example Request:**

   .. sourcecode:: http

      GET /users/MyUserName/library/The%20Once%20and%20Future%20King/title
      Host: textscroll.cs.hmc.edu
      Authorizaton: Credential=s0upersecrett0ken

   **Example Response:**

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
         "title": "The Once and Future King"
      }

   :reqheader Authorization:
      Authorizes the user for this request - can be a token or a password.

   :statuscode 200: The attribute was found
   :statuscode 400: The username was malformed
   :statuscode 400: The text name was malformed
   :statuscode 400: The attribute is invalid
   :statuscode 401: User is not authenticated
   :statuscode 404: User does not exist
   :statuscode 404: Text does not exist

.. http:post:: /users/(string:user_id)/library/(string:text_id)/(string:text_attr)
   :synopsis: Set an attribute of the text

   Set the attribute named by `text_attr` of the text `text_id` in `user_id`'s library.

   **Example Request:**

   .. sourcecode:: http

      POST /users/MyUserName/library/The%20Once%20and%20Future%20King/title
      Host: textscroll.cs.hmc.edu
      Authorizaton: Credential=s0upersecrett0ken

      title=The%20once%20and%20Future%20King

   **Example Response:**

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
         "original": "The Once and Future King",
         "updated": "The once and Future King"
      }

   :reqheader Authorization:
      Authorizes the user for this request - can be a token or a password.

   :statuscode 200: The attribute was found
   :statuscode 400: The username was malformed
   :statuscode 400: The text name was malformed
   :statuscode 400: The attribute is invalid
   :statuscode 400: The value was invalid
   :statuscode 401: User is not authenticated
   :statuscode 404: User does not exist
   :statuscode 404: Text does not exist

.. http:get:: /trials
   :synopsis: Get all of the trials

   Get all trials that have been conducted, and the user who performed them.

   Requires administrator or researcher credentials.

   **Example Request:**

   .. sourcecode:: http

      GET /trials
      Host: textscroll.cs.hmc.edu
      Authorizaton: Credential=s0upersecrett0ken

   **Example Response:**

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
         1: "MyUserName",
         2: "SomeOtherUserName",
         ...
      }

   :reqheader Authorization:
      Authorizes the user for this request - can be a token or a password.

   :statuscode 200: The trials were returned
   :statuscode 401: User is not authenticated

.. http:get:: /trials/(int:trial_id)
   :synopsis: Get a specific trial

   Get the trial with an id of `trial_id`.

   Requires administrator or researcher credentials.

   **Example Request:**

   .. sourcecode:: http

      GET /trials/13
      Host: textscroll.cs.hmc.edu
      Authorizaton: Credential=s0upersecrett0ken

   **Example Response:**

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
         "trial_data": "stuff",
         "other_data": "other_stuff",
         "user_id": "MyUserName"
      }

   :reqheader Authorization:
      Authorizes the user for this request - can be a token or a password.

   :statuscode 200: The trials were returned
   :statuscode 401: User is not authenticated
   :statuscode 404: The trial doesn't exist

.. http:post:: /trials/(int:trial_id)
   :synopsis: Set a specific trial

   Set the trial with an id of `trial_id`.

   Requires administrator or researcher credentials.

   **Example Request:**

   .. sourcecode:: http

      POST /trials/13
      Host: textscroll.cs.hmc.edu
      Authorizaton: Credential=s0upersecrett0ken

      trial_data=stuff&other_data=other_stuff&user_id=MyUserName

   **Example Response:**

   .. sourcecode:: http

      HTTP/1.1 201 Created
      Content-Type: application/json
      Location: https://textscroll.cs.hmc.edu/api/v1/trials/13

   :reqheader Authorization:
      Authorizes the user for this request - can be a token or a password.

   :statuscode 201: The trial was created
   :statuscode 400: No username indicated, or invalid username
   :statuscode 401: User is not authenticated

